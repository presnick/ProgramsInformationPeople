..  Copyright (C)  Sam Carton and Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Scheduling Periodic Actions
---------------------------

An important pair of functions to know are ``pyglet.clock.schedule_interval()`` and ``pyglet.clock.unschedule()``

``pyglet.clock.schedule_interval(function,interval)`` takes two arguments, ``function`` and ``interval``. The ``interval`` is a float representing some number of seconds. ``schedule_interval()`` causes the Pyglet event loop to "schedule" the function to run on the given interval.

``pyglet.clock.unschedule(function)`` tells Pyglet to pull the given function off the scheduler. Below is an example of the two functions being used in conjunction with one another:

.. note::

    Remember how the ``sorted`` function takes an optional parameter called ``key``, which is itself a function? While sorted is executing, it calls the function that is provided for the key parameter. This works a little bit similarly. You pass in a function to pyglet.clock.schedule_interval(). The function you pass in will get called periodically. The function you provide should always take one parameter; pyglet will pass in a value for that parameter that is the interval of time since the function was last called.

.. code:: python

    import pyglet

    print_count = 0

    def print_1(interval):
        global print_count
        print_count += 1

        if print_count <= 5:
            print 'First printing function. Count: ' + str(print_count)
            print '\tIt has been ' + str(interval) +' seconds since the last time this function was called.'

        else:
            print 'Unscheduling first printing function and scheduling second printing function'
            pyglet.clock.unschedule(print_1)
            pyglet.clock.schedule_interval(print_2,1.0)


    def print_2(interval):
        global print_count
        print_count += 1
        if print_count <= 10:
            print 'Second printing function. Count: ' + str(print_count)
            print '\tIt has been ' + str(interval) +' seconds since the last time this function was called.'

        else:
            print 'Exiting Pyglet event loop'
            pyglet.app.exit()

    print 'Scheduling first printing function'
    pyglet.clock.schedule_interval(print_1,1.0)
    print 'Starting up game loop'
    pyglet.app.run()

If you were to run this code, you'd see some output, printed at a 1-second interval:

.. code::

    Scheduling first printing function
    Starting up game loop
    First printing function. Count: 1
        It has been 1.00017619269 seconds.
    First printing function. Count: 2
        It has been 1.00004148226 seconds.
    First printing function. Count: 3
        It has been 1.00059999598 seconds.
    First printing function. Count: 4
        It has been 1.00077661632 seconds.
    First printing function. Count: 5
        It has been 1.00115594379 seconds.
    Unscheduling first printing function and scheduling second printing function
    Second printing function. Count: 7
        It has been 1.00012017026 seconds.
    Second printing function. Count: 8
        It has been 1.00039814416 seconds.
    Second printing function. Count: 9
        It has been 1.00042337564 seconds.
    Second printing function. Count: 10
        It has been 1.00041952677 seconds.
    Exiting Pyglet event loop

What happened here was that initially we scheduled ``print_1()`` to run on a once-per-second interval. But, when print_count exceeded 5, ``print_1()`` unscheduled itself and scheduled ``print_2()`` to run on the same interval. When print_count exceeded 10, ``print_2()`` exited the game using the ``pyglet.game.exit()`` function.

Note that both of my scheduled functions had an argument called ``interval``. The Pyglet scheduler passes the actual time elapsed as an argument to the scheduled function whenever it runs. This is usually very close to the planned interval, but slightly different due to CPU latency and stuff like that. In this case, we see that on each call it has been *slightly* more than 1 second since the last call.

