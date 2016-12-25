..  Copyright (C)  Sam Carton and Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

The pyglet Window class
-----------------------

Below is just about the most simple Pyglet application you could possibly write.

.. code:: python

    import pyglet
    window = pyglet.window.Window()
    pyglet.app.run()

.. note::

    Throughout this chapter, we will be providing code snippets. They are not provided as ActiveCode windows because the Pyglet module will not run in the browser environment. We strongly encourage you to copy these text snippets into code files on your local machine and run those code files from a terminal window, as you have been doing with recent problem sets.

If you were to run this little program from the console (terminal window), you'd see something like the following:

.. image:: Images/basic_pyglet.png

Application Elements
~~~~~~~~~~~~~~~~~~~~

So let's break this down line-by-line:

.. code:: python

    import pyglet


This line imports the pyglet package that we installed earlier. It gives our program full access to all the functionality contained in the package. Basically that module is a directory named `pyglet` that consists of a set of .py files (or possibly subdirectories that also contain .py files). The python interpreter executes the code in all those .py files. In particular there is a file called ``window.py``. In window.py there is a definition of a class called ``Window``.

.. code:: python

    window = pyglet.window.Window()

This line creates the window that showed up in the screen shot. But, and this is important, **it does not draw the window.** For that, you need the next line.

But first let's pull apart ``pyglet.window.Window()``, to understand how it works to use imported modules and to reinforce how classes work.
    * The python interpreter looks up the word ``pyglet`` and finds that it is bound to a *module* object that was created by the previous ``import pyglet`` line. Think of the module object as being an instance of a class called Module.
    * ``.window`` says to look up the attribute named window in the module instance. That turns out to also be a module object, a submodule of pyglet.
    * ``.Window`` says to look up the Window attribute in that submodule. It's value is the Window class object.
    * ``()`` says to treat the previous object as an executable. If it were a function, it would call the function. Since it's a class, it creates an instance of the class and invokes the constructor on it. It returns the new instance of the Window class. If all that terminology doesn't sound familiar, recheck the textbook section on :ref:`Classes and Constructors <chap_constructor>`.

.. code:: python

    pyglet.app.run()

**This is our get-the-ball rolling line.** It tells Pyglet to look for every object of a type it knows about (such as instances of the Window class), and draw them on the screen. It also starts up what is called the **Pyglet event loop**, which is essentially a loop that runs over and over again, continuously waiting for user interaction, drawing stuff, making things happen, etc. All the stuff that constitutes a visual application, in fact.

Doesn't make sense? That's okay. The loopiness of the event loop will become a little clearer in a bit. Til then, just remember that the second line creates the window, but the third line draws it and keeps it alive until you close it. If you had created more windows, the third line would have drawn it as well.

By default, the loop ends when all windows are closed. What that means is that we are stuck on that third line until all windows get closed. So if you add a print statement to the previous code:

.. code:: python

    import pyglet
    window = pyglet.window.Window()
    pyglet.app.run()
    print 'I made a window and ran the Pyglet event loop!'

...you'll find that you **do** see that print statement in the console, but not until you close the Pyglet window.

Fancier Windows
~~~~~~~~~~~~~~~

You can give your window a different title with the ``caption`` keyword argument, and different starting dimensions with the ``height`` and ``width`` arguments. You can also create multiple windows. The call to ``pyglet.app.run()`` will initialize them all.

.. code:: python

    import pyglet
    window = pyglet.window.Window(caption='This is my first window')
    window = pyglet.window.Window(caption="This is my second window. It's  a biggun.", width = 800, height = 700)
    pyglet.app.run()

Run this code, and you'll see something like the following:

.. image:: Images/basic_pyglet_2.png
