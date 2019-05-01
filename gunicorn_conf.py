import multiprocessing

HOST_NAME = ""
PORT = "9224"
APP_NAME = "arbolbinario"

#Do not modify beyond this point

bind = HOST_NAME + ":" + PORT

workers = multiprocessing.cpu_count() * 2 + 1

daemon = True

#
#backlog: The maximum number of pending connections. Like
#This refers to the number of clients that can be waiting to be served. Exceeding this number results in the client getting an error when attempting to conne$
#
#Must be a positive integer. Generally set in the 64-2048 range.
#

backlog = 64

#http://docs.gunicorn.org/en/stable/settings.html#logging

accesslog = "/var/log/arbolbinario/" + APP_NAME + "-access.log"

errorlog = "/var/log/arbolbinario/" + APP_NAME + "-errors.log"

loglevel = "info"


#
#A base to use with setproctitle for process naming.
#
#This affects things like ps and top. If you’re going to be running more than one instance of Gunicorn you’ll probably want to set a name to tell them apart.$
#
#If not set, the default_proc_name setting will be used.
#

proc_name = "Etec-" + APP_NAME

Worker_class = "eventlet"

#
# Server hooks
#
#   post_fork - Called just after a worker has been forked.
#
#    A callable that takes a server and worker instance
#    as arguments.
#
#   pre_fork - Called just prior to forking the worker subprocess.
#
#    A callable that accepts the same arguments as after_fork
#
#   pre_exec - Called just prior to forking off a secondary
#    master process during things like config reloading.
#
#
# Server hooks
#
#   post_fork - Called just after a worker has been forked.
#
#    A callable that takes a server and worker instance
#    as arguments.
#
#   pre_fork - Called just prior to forking the worker subprocess.
#
#    A callable that accepts the same arguments as after_fork
#
#   pre_exec - Called just prior to forking off a secondary
#    master process during things like config reloading.
#
#    A callable that takes a server instance as the sole argument.
#

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")
    
    ## get traceback info
    import threading, sys, traceback
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
    
