from threading import Timer
import types

def set_timeout(f, time=None):
    def _set_timeout(f, time):
        interval = Timer(time, f)
        interval.start()
        return interval

    if time==None:
        #f is actually time
        return lambda g: _set_timeout(g, f)
    else:
        return _set_timeout(f, time)

def set_interval(f, time=None):
    def again(g, t):
        def _again():
            set_timeout(again(g, t), t)
            g()
        return _again

    if time==None:
        return lambda g: set_timeout(again(g, f), f)
    else:
        set_timeout(again(f, time), time)


@set_interval(1.000)
def success():
    print "HUGE SUCCESS"

def note():
    print "I'M MAKING A NOTE HERE:"

set_timeout(note, 0.500)
