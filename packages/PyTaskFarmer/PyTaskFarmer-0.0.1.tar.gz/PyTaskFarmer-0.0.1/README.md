# PyTaskFarmer

This is a small project containing a python TaskFarmer for running jobs at NERSC
 n Cori (though it should be flexible to run on other systems). It is very
 loosely based on the concept of [Shane Canon's TaskFarmer](https://github.com/scanon/taskfarmer).

## Usage

The executable script is:

    usage: pytaskfarmer.py [-h] [--proc [Processes]] [--timeout TIMEOUT]
                            [--workdir WORKDIR] [--verbose VERB]
                            [--runner RUNNER] [--tasklist TASKLISTHANDLER]
                            tasklist

The `tasklist` argument is a simple text file with one task per line. The
interpretation of the task is up to the `TASKLISTHANDLER`. By default, the task
is treated as a command to run. It is not important how complex the command is.

The `--verbose` flag adds a bit more output (though not much) telling you what
the script is doing as it runs (default False).

The `--timeout` option allows you to set a timeout for the script, so that after
 some number of seconds the tasks will be automatically killed (default none).

The `--proc` option tells the script how many processes it should be in charge
of (default 8). 

The `--workdir` option tells the script where to store the progress (task
status, log files..) of a single run (default is `tasklist_workdir`).

The `--runner` options indicates which runner to execute the command with. See
the dedicated section on the available runners and how they work.

The `--tasklist` options indicates which tasklist handler to parse the tasklist
with. See the dedicated section on the available runners and how they work.

## What it does (60 second version)

The basic behavior, with the default runner/handler, is as follows:

- The task list is read and a `toprocess` file is created in the work directory
with the tasks remaining to be processed.

- A number of workers (`multiprocessing.Pool`) are constructed to run on the
tasks.

- When some work is done, the command is placed into a `finished` file or
`failed`, depending on the status code.

- Duration and start times of completed tasks (timeline) are saved into a
`timeline.json` file. This can then be opened with [Perfetto](ui.perfetto.dev).

- The tasks are prcoessed by the workers until 1) the work is completed; 2) the
timeout is reached; or 3) a signal is intercepted.

## What it does (10 minute version)

This version includes more details that might help in case you see some
unexpected behavior or want to know what the script is capable of. In a little
more detail:

- The task list is read and the `toprocess` file is made, but only if that file
does not yet exist. If the file does exist, the assumption is that you are
re-starting the task farmer and it should continue from where the last farmer
left off. This also protects against the situation that the farmer is run on
multiple nodes at the same time (or multiple instances are run at the same time)
on the same task list, so that the farmers do not compete with each other but
share the tasks as you'd want them to.

- In the `toprocess` file the jobs are given an ID that should be used by the
worker.

- The tasklist handler is reponsible for formatting the contents of a tasklist
before passing the task to a runner. This adds flexibility to the task
definitions. For example, the tasklist can be treated as a list of files. The 
handler can then be reponsible for wrapping the execution command around each
file.

- Enough workers are constructed to run all jobs in the input file. In the case
that the script is run on multiple nodes, this means more workers are created
than needed. If the job runs out of useful work to do, the remaining processes
all return very quickly.

- The workers process the jobs, as described above. The execution of the command
is handled by a runner class. This allows to automate steps common to all tasks
like environmental setup or running inside Shifter.

- The workers don't know (or care) what command they run. That means, for
example, if your single-line commands use 4 threads at a time, you can ask
pytaskfarmer to run 64/4=16 processes, and it will have 16 four-thread processes
running at a time. If your script can fully utilize a node (64 threads on Cori
Haswell), then you can ask the farmer to run one process at a time. In this
case, it is equivalent to running the commands in your text file in order.

- For each job, a log file is created, named `log_N`, where N is the task ID.
The task ID corresponds to the the order that the command is written in the
original task list file starting at 0, but they may not finish in that order.

- The job's exit code is used to put it into the `finished` or `failed` stack.
Exit code 0 indicates success.

- If the work completes, the job finishes and exits.

- If the job catches either a timeout or a SIGUSR1, then the worker pool is
immediately killed in whatever state it is in, with all workers killed. In these
cases, any tasks that were being executed are added back to the `toprocess`
list.

All the file access uses locks that are written to `SCRATCH`. These locks
prevent multiple workers or farmers from racing and trying to modify any of the
files at the same time, or from accidentally picking up the same task at the
same time. The process lists are put in the directory of the original process
list, but some disk systems at NERSC do not support file locking, such that the
lock file needs to be on the scratch system. In case a system does not define
`SCRATCH`, these files are written to a `lock` file in the work directory.

## Runner Definitions
Runners define the execution environment in which the tasks are execute. They 
can be also used globally across multiple tasklists. This reduces the amount of
clutter in each task definition and makes it portable across multiple
environments.

The `BasicRunner` is always available under the namde default. Custom runners
are defined inside the `~/.pytaskfarmer/runners.d` directory as INI files. All
files ending in `.ini` are loaded. There can be multiple runners defined in a
single file.

The format of a single runner definition is

    [runnername]
    Runner = runner.python.class
    Arg0 = value0
    Arg1 = value1

where `runnername` is the name of the runner and `Runner` is the python class
(along with package and module) of the implementation. The remaining key:value
pairs are passed to the `runner.python.class` constructor as keyword arguments.

The desired runner is selected using the `--runner` option to the main
`pytaskfarmer.py` program.

### Provided Runners

#### taskfarmer.runners.BasicRunner (default)
Executes the command as it is given to it. It uses `subprocess.Popen` to execute
the task in the same environment as the worker.

#### taskfarmer.runners.ShifterRunner
Executes each task inside shifter. This can be preferable over starting
PyTaskFarmer inside shifter as it does not require a recent version of Python
in the image. The shifter itself is started using subprocess module with the
following command.

    shifter --image image -- /bin/bash -c "setup_code && task"

The setup_code is user-configurable set of commands to setup the environment
(ie: source ALRB) in shifter.

Options:
- `image`: Shifter image to use for execution
- `setup`: Command to setup the environment (aka `setup_code` above)
- `volumes`: list of volume bindings separated by space
- `modules`: list of modules separated by space
- `tempdir`: task should be run in own temporary directory (`True`/`False`)

Example (muon collider software framework):

    [mcc]
    Runner = taskfarmer.runners.ShifterRunner
    image = docker:gitlab-registry.cern.ch/berkeleylab/muoncollider/muoncollider-docker/mucoll-ilc-framework:1.5.1-centos8


## TaskList Handler Definitions
TaskList definitions are loaded from `pytaskfarmer/tasklists.d` and the current
working directory. All files ending in `.ini` are loaded and are expected to be
the INI format. The following scheme is expected:

    [tasklisthandlername]
    TaskList = tasklist.python.class
    Arg0 = value0
    Arg1 = value1

The extra arguments are passed to the `TaskList` constructor as keyword
arguments.

### Provided TaskList Handlers

#### taskfarmer.tasks.ListTaskList (default)
A list of tasks is defined using a file containing a task per line, with
supporting status files defined using a suffix. The task ID is defined as the
line number (starting at 0) inside the main task file.

## Tips and Tricks

You can use this script as a part of your top-level batch script for submissions
into the NERSC slurm batch system. There are a variety of examples for running
multi-core or multi-node jobs [available here](https://docs.nersc.gov/jobs/examples/).

### Equalize Task Running Time

The farmer likes to have more work than workers, in order to keep
those workers busy at all times. That means if you have jobs that
might be different lengths (e.g. MC and data, or different size
datasets, etc), it is very important to 1) put the longer jobs
earlier in the list; 2) have a total run time that is longer than
the longest job (preferably by a factor of 2 or more); 3) request
a number of cores that will be kept busy by your jobs. For example,
if you expect to have one 1-hour job and ten 5-minute jobs, you
can requests two threads; one thread will process the 1-hour job
and the other thread will process all the 5-minute jobs. This relies
on your ordering the task list well -- if you make the 1-hour job
last, then the two threads will work through all your 5-minute jobs
in about 25 minutes and then one will process the 1-hour job while
the other sit idle (and wastes CPU). This requires some thought
and care, but can save us significant numbers of hours, so please
do think carefully about what you're running!

### Clean-up In Batch Jobs
The farmer can be used in any queue at NERSC. One of the better
options if some work needs doing but is not urgent is to use
the flex queue on KNL. When submitting into that queue, one must
run for example `--time-min=01:30:00 --time=10:00:00`, where
the first is the minimum time that the farmer should be run, which
may not be longer than 2 hours and should be longer than a typical
command you need to execute (better if it's several times longer).
The second is the total wall time for the job, which must be less
than 12 hours. Jobs in this queue will be started, killed, and can
in principle be restarted. Add to your job script:

    # requeueing the job if reamining time >0 (do not change the following 3 lines )
    . /usr/common/software/variable-time-job/setup.sh
    requeue_job func_trap USR1
    #

in order to have the job automatically re-queued so that it will
continue to run. You should also add to your run script

    #SBATCH --signal=B:USR1@10

To give the job 10 seconds to handle the USR1 signal (it should 
not need that long, but in case there are races and locks this
should be safe). For the check-pointing, please also add these
to your job script:

    # use the following three variables to specify the time limit per job (max_timelimit), 
    # the amount of time (in seconds) needed for checkpointing, 
    # and the command to use to do the checkpointing if any (leave blank if none)
    max_timelimit=12:00:00   # can match the #SBATCH --time option but don't have to
    ckpt_overhead=60         # should match the time in the #SBATCH --signal option
    ckpt_command=

Note that these are in addition to the usual sbatch specifications,
and it is quite important that they match.

### Extra Memory

If you have serious memory issues, then it is possible to enable
swap space when running in a full node queue (e.g. regular; this
is not possible in the shared queue). To do so, make a burst-buffer
config file like:

    $ cat bb_swap.conf
    #DW jobdw capacity=160GB access_mode=striped type=scratch
    #DW swap 150GB

This uses the Cray [DataWarp configuration format](https://pubs.cray.com/content/S-2558/CLE%206.0.UP05/xctm-series-datawarptm-user-guide/datawarp-job-script-command-examples).
The second line is the important one here; it provides 150 GB of
swap space within the burst buffer. The first line describes the 
scratch space reservation that your job needs, and may be 
unnecessary or even problematic depending on where you write your 
inputs and outputs for the job (think about what it's doing before 
sending the command off to the queue). You can then add it to your 
job submission like:

    salloc ... --bbf=bb_swap.conf

This allocates space on the burst buffer (generally pretty fast)
to be used for swap space memory for users. Note that swap is 
quite a bit slower than standard (even main) memory, and so this
option should be used with care. It is not, in principle, clever
enough to guarantee each job space in the main memory, so as long
as swap is being used on a node, all jobs on that node may be 
slowed down, depending on the memory profile and usage of the 
offending job.

## Things that should be improved

- At the moment, if the original process file is significantly
modified (item added and removed) or contains duplicates, in some
cases the process IDs may not be unique. Of course, the output can
be re-directed by the user to a log file with a more appropriate 
name, so the log files created by the farmer may be dummy.
If `PROC_NUMBER` is important to your workflow, then please 
either submit additional farmers for new lists of processes or
add a unique (short as you like) comment to the end of the command
to make the items distinguishable.

- It would be nice to add some monitoring hooks so that we can
watch what users are doing with this script.

- Longer-term, it would be interesting to try to keep all
tasks that need to be finished in an sqlite file, including
a state (to process, running, finished, failed). Adding an
integer identifier would solve the above problem and give us
a free way to add jobs mid-way through a run.

## Example

Included in the package is a small test file that you can use as an example. Try
running:

    pytaskfarmer.py test/task_list.txt

That will give you a sense of how the thing works. Feel free to kill it and
restart it if you wish.

### SLURM example

Example batch jobs for using pytaskfarmer.py can be found in
the examples directory. They demonstrate how to correctly handle
cleanup and difference between array and multi-node setups.

To run using array jobs:

    sbatch test/slurm_test.sh test/task_list.txt

To run by requesting multiple nodes at the same time (srun):

    sbatch test/srun_test.sh test/task_list.txt
