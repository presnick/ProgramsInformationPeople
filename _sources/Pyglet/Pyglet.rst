..  Copyright (C)  Sam Carton and Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _pyglet_chap:

Pyglet
======

Pyglet (https://bitbucket.org/pyglet/pyglet/wiki/Home) is a "cross-platform windowing and multimedia library for Python." That means that it can be used to build visual applications with their own windows and elements such as text, moving images, sound, and responsiveness to user events such as key presses and mouse movements. 

This chapter will give a brief introduction to installing Pyglet and making (very) simple visual applications with it. 

As a note, Pyglet is not considered the best Python game library as of November 2015, as it hasn't been maintained consistently in recent years. PyGame (http://www.pygame.org/hifi.html) probably holds that distinction for now (though these things change quickly). 

However, Pyglet is simpler, more "Pythonic", and doesn't depend on any other modules. That makes it a better learning tool. If you can understand Pyglet, you will be well positioned to understand other graphics and visual application modules.

The official Pyglet documentation is located here: https://bitbucket.org/pyglet/pyglet/wiki/Documentation

The Pyglet docs will go into much more detail about concepts that are only briefly discussed in this chapter. Be warned, however, that they are sometimes incomplete.

Installation
------------

Pyglet is an official Python package, meaning that it can be installed by simply running the following **in the terminal**:

.. code::

    pip install pyglet

This will install Pyglet into the Lib/site-packages directory of your Python installation. To see a list of packages you've installed, use the command:

.. code::

    pip freeze -l

If you scroll down, you should see one called 'pyglet==1.2.4'. 

Alternatively, or if you run into problems, you can try following the official installation instructions available here: https://pyglet.readthedocs.org/en/pyglet-1.2-maintenance/programming_guide/installation.html

To confirm that Pyglet installed correctly, try running a little Python code (either by saving it with a text editor and running it from the terminal, or by running it in the interactive Python shell):

.. code:: python

    import pyglet

If you don't get an error when you try to do that import, you can be pretty sure you've installed it correctly.


Basics of  Pyglet
-----------------
To understand Pyglet, you have to understand 4  basic things:

1) Creating windows

2) Running the Pyglet event loop

3) Getting your windows to listen for events

4) Making things happen in your windows

We'll talk about these in that order.



Additional Notes
----------------

The Pyglet documentation available at https://pyglet.readthedocs.org/en/pyglet-1.2-maintenance/index.html goes into much more detail than this introduction. 

However, that documentation, rather than using subclassing uses something called **function decorators**, to achieve the function overwrites that it needs to produce real results. That approach produces identical results to subclassing, but is slightly more compact (though also, in our opinion, harder to understand).

The documentation discusses this design decision and alternatives to it, such as subclassing, here: https://pyglet.readthedocs.org/en/pyglet-1.2-maintenance/programming_guide/windowing.html#subclassing-window

In the following pages, we introduce the Pyglet features using subclassing.

