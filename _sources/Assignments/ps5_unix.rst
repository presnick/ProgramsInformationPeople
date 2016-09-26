
:orphan:

..  Copyright (C) Paul Resnick, Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500

Problem Set 5: Unix Exercises (Problem Set Part 1)
==================================================

.. _problem_set_5_unix:

The following is a set of exercises for you to practice the Unix commands you learned about this week. At the end of this part of the problem set, you will run a Python program on your computer for the first time in this course. The other Unix commands you have learned will be very useful when you start programming entirely on your own computer, writing programs in a text editor, rather than programming in the browser, on our textbook, and are closely connected to the processes you use when you run a Python program on your computer. They will help you be able to not just run Python programs, but deal comfortably with your computer's file system while you do that.

This is part of your :ref:`Problem Set 5 <problem_set_5>`. It is graded. The other part is writing Python code, as you have seen.

For each step of this assignment, please take a screenshot (HOWTO DO THAT HERE) that shows us the command(s) you typed and the results. Save the screenshots as ``step1.jpg`` (or ``.png``), ``step2.jpg``, etc. Upload them all to `the PS 5 Unix Exercises <LINK GOES HERE>`_ assignment on Canvas.

----------

.. external:: problem_set_5_unix_1

    1. Open the text editor you installed: Sublime Text. You will be creating and saving 4 different files to your ``Desktop``. 

    **In the first file,** put the following:

    .. sourcecode:: python

        print "hello world"

    Save the file as ``prog1.py``. You've now saved a Python program on your computer!



    **In the second file,** put the following:

    .. sourcecode:: python

        def greeting(x):
            return "hello " + x

        print greeting("there")

    Save this file as ``prog2.py``.
    


    **In the third file,** put the following:

    :: 

        this is a file
        it has 
        multiple
        lines

    Save this as ``unix_test_text.txt``.


    **In the fourth file,** put the following:

    ::

        here is another file
        what a wonderful
        story this is

    Save this file as ``another_text.txt``.

    No need to take a screenshot of the file saving since you need them for the rest of the exercises, but if it's not working or is confusing, let staff know right away so we can help.

.. external:: problem_set_5_unix_2

    2. Open your Command Prompt program -- Terminal or Git Bash. ``cd`` to your ``Desktop``, as you saw in the chapter. Then type ``ls``. You should see a list of all file names on your Desktop, including the files you just saved in step 1. If you have any directories saved in your Desktop, you'll also see those names, of course. Take a screenshot that shows this worked for you.

.. external:: problem_set_5_unix_3

    3. You now want to make a new directory called ``new_class_programs`` in your ``Desktop``, and copy ``prog1.py`` and ``prog2.py`` into it. (Note that files will NOT disappear from your desktop when you've completed this step. There should be a copy of each file in both places.) 

    Use Unix commands to do this, and take a screenshot of the commands you use + evidence they worked. (Hint: using commands like ``cd`` and ``ls`` and ``pwd`` can help you check what you've done when you're creating directories and copying files around!) 

    There is more than one perfectly reasonable way to complete this exercise, but all ways use a similar set of Unix commands.

.. external:: problem_set_5_unix_4
    
    4. Now, you want to create a new directory *inside* the ``new_class_programs`` directory, called ``text_files``, and copy both ``unix_test_text.txt`` and ``another_text.txt`` into *that* folder. Use Unix commands to do this. 

    When you've completed that, change directories to be inside that folder in your command prompt, and use the ``pwd`` command to show the full path of your location. (It should look *something like* this: ``/Users/Jackie/Desktop/new_class_programs/text_files``)

    Take a screenshot showing that these things worked for you. Your screenshot should show the command you typed + evidence it worked.

.. external:: problem_set_5_unix_5

    5. You want to see what content is inside each of your files. Use a unix command to view the content of ``prog2.py`` before you open it. Take a screenshot to show that this worked.

.. external:: problem_set_5_unix_6

    6. You want to concatenate the 2 text files inside the ``text_files`` folder together, and save the result in a file called ``big_story.txt``, which should also be inside that directory. Use unix commands to do this. (Hint: You'll probably need more than 1 typed in the same line.)

.. external:: problem_set_5_unix_7

    7. You now want to see a list of all the files and/or directories inside your ``new_class_programs`` folder whose names include ``text``. Use Unix commands to do this. (Hint: You'll need pipe (``|``) and ``grep``, and ``ls``.)

.. external:: problem_set_5_unix_8

    8. Now that you have a bunch of practice with the unix command prompt, it's time to run Python natively on your computer. You've saved 2 Python files that are in your ``~/Desktop/new_class_programs`` directory. Go there in your command prompt, and run ``prog2.py`` by typing ``python prog2.py`` at the prompt. Take a screenshot of what happens. 

    (Feel free to also play around -- you know a lot of programming now, and you can run it all on your computer, but it will look a little bit different in the command prompt than it did in the textbook.)

.. note::

    You may discover another way to run your python program directly from Sublime Text. We have found that this will not work for everything you need to do throughout the semester. Therefore, it's very important that you learn how to run your python programs from the unix command prompt, including figuring out how to connect to the right directory with the unix ``cd`` command. You will only get credit for these unix problems if your screenshots show that you ran the programs from the unix command prompt.


**This is very important for the rest of the semester. Starting with Problem Set 7, ALL of your problem set will be turned in via Canvas, and you will be writing code in a text editor and running it on your own computer. If you have any trouble running Python natively (on your computer), let an instructor know *right away*.**


You're done with the Unix part of the problem set. `Here <https://umich.instructure.com/courses/105657/assignments/139051>`_ is the Canvas assignment for submitting your screenshots. 

:ref:`Go back to the other part of problem set 5 <problem_set_5>`.


