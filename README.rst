hiatus
======

Hiatus is a python library that uses the ``threading`` module's "Timer" to
implement analogues to javascript's ``setTimeout``/``clearTimeout`` and
``setInterval``/``clearInterval``.

These functions may be used as decorators. Also important is
that the python analogues take time arguments in *seconds*, not
*milliseconds*, in order to be consistent with the standard library.

A Caveat:
=========

Much of python does not "play nice" with threading. You have been warned.

(I looked into a signal-based approach, but this is limited. Another approach would be to depend on an event loop, such as ``twisted.reactor``.)

Examples:
=========

::

    >>> from hiatus import set_interval
    >>> @set_interval(1.00)
    ... def dave_grohl():
    ...     print "THE BEST"
    ... 
    >>> THE BEST
    THE BEST
    THE BEST
    THE BEST
    THE BEST

::

    >>> def note():
    ...     print "HUGE SUCCESS"... 
    >>> hiatus.set_timeout(lambda: hiatus.clear_interval(glados), 6.0)
    <hiatus.set_timeout object at 0xb770468c>
    >>> glados = hiatus.set_interval(note, 1.000)
    >>> HUGE SUCCESS
    HUGE SUCCESS
    HUGE SUCCESS
    HUGE SUCCESS


Functions:
==========

``set_timeout(f, time=None)``:
------------------------------

Calls ``f`` after ``time`` seconds pass. If ``time`` is
not specified, the first argument is used as time instead and the resulting
object can then be called with a function. This allows for decorator syntax.

``clear_timeout(timeout_obj)``:
-------------------------------

Clears the timeout returned by set_timeout.

`set_interval(f, time=None)`:
-----------------------------

Calls ``f`` every ``time`` seconds pass. If ``time`` is
not specified, the first argument is used as time instead and the resulting
object can then be called with a function. This allows for decorator syntax.

``clear_timeout(timeout_obj)``:
-------------------------------

Clears the interval returned by set_interval.

Tests:
======

`nose` doesn't seem to "like" multithreading, but other than some violated
expectations, testing works fine::

    nosetests

Developers! Developers! Developers!
===================================

If you're a python fan and like what you see (or don't quite like
what you see), I heartily invite you to dig in, fork it up and `git push it
good <https://twitter.com/#!/maraksquires/status/71911996051824640>`_.

License:
========

MIT.
