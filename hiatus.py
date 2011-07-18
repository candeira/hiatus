import signal
import types

def note():
    print 'IM MAKING A NOTE HERE'

def set_interval(f, time=None):
    def _set_interval(f, time):
        def handler(signum, frame):
            f()

        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, time/1000.0, time/1000.0)

    if time==None:
        #f is actually time
        return lambda g: _set_interval(g, f)
    else:
        _set_interval(f, time)

set_interval(note, 500)

@set_interval(1000)
def success():
    print "HUGE SUCCESS"

while(True):
    pass
