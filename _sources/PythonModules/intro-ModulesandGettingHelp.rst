..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _modules_chap: 

Modules
=======

.. video:: inputvid
    :controls:
    :thumb: ../_static/modules.png

    http://media.interactivepython.org/thinkcsVideos/modules.mov
    http://media.interactivepython.org/thinkcsVideos/modules.webm

A **module** is a file containing Python definitions and statements intended for
use in other Python programs. There are many Python modules that come with
Python as part of the **standard library**. 

The  `Python Documentation <http://docs.python.org/2/>`_ site for Python version
2.7 is an extremely useful reference for all aspects of Python. The site
contains a listing of all the standard modules that are available with Python
(see `Global Module Index <http://docs.python.org/2/py-modindex.html>`_). You
will also see that there is a
`Standard Library Reference <http://docs.python.org/2/library/index.html>`_
(Next week, there will be a chapter explaining how to read the language
reference documentation) and a
`Tutorial <http://docs.python.org/2/tutorial/index.html>`_, as well as
installation instructions, how-tos, and frequently asked questions.  We
encourage you to become familiar with this site and to use it often.

If you have not done so already, take a look at the Global Module Index.  Here
you will see an alphabetical listing of all the modules that are available as
part of the standard library.  Find the turtle module.

Importing Modules
-----------------

In order to use Python modules, you have to **import** them into a Python program. That happens with what's called an ``import`` statement: the word ``import``, and then the *name* of the module. The name is specific and case-sensitive. If you need to import a module, you will either be told the specific name of it (or if you are using a new one, you may have to do a Google search to figure out what the correct name is to import it with).

Usually, any ``import`` command occurs at the very beginning of a Python program. Roughly translated to English, this is like saying "here's this other code another programmer wrote, and I want to be able to use its functionality -- its functions and objects -- anywhere I want in this new program I'm writing." 

It's possible to write an import statement anywhere in your code, so there are some situations where you might put an import statement only right before you are about to use the functionality from the new module. However, this can be confusing -- what if you rewrite your code and try to use the module's functionality above where you import it? Then it won't work, because at that point in the program running, your Python does not know about the external module. For that reason, we recommend always putting import statments at the beginning of your program files.

Modules might be available via the **standard library**, and they might be available online to install into your native Python and ``import`` into a program you are writing, as you'll learn about.

You can also use another code file that you have on your own computer as an external module. 

Roughly translated to English, that's like saying, "I wrote this Python program, and I want to be able to use its functions and objects in this new Python program I'm writing." 

When you import a module that is another file on your computer, its name for importing (``import <name of module>``) is the filename you saved the program as -- but *without* the ``.py`` extension. For example, if you saved a program called ``number_functions.py`` and you wanted to import those functions to use in another program, you would write ``import number_functions`` at the top of your new program file.

It is important that you save that file in the *same directory* as your program file. Python has to be able to 'find' the file to import, so the best way to ensure that will work is to save any file that you plan to import in the *same directory* as you save the program where you want to import it!

<TBA image>

Syntax for Importing Modules and Functionality
----------------------------------------------

When you see imported modules in a Python program, you see them in a couple common ways.

The most common is, at the top of a program, ``import <module-name>``. That imports everything in that module to your new program.

You'll also see, for example, ``import <module-name> as <otherPhraseWithNoSpaces>``. (In the real syntax, there are no ``<`` or ``>``, those are only here to indicate that you can fill in anything that is appropriate in your real code.) With this syntax, you can refer to the module as your new name, ``otherPhraseWithNoSpaces``. Programmers often do this to make code easier to type, for example, ``import test106 as test``. ``test`` is a little easier and faster to type than ``test106`` -- may as well make it harder for humans to make human mistakes!

A third possibility for importing syntax occurs when you only want to import SOME of the functionality from a module. You might do this for many reasons -- maybe it's a lot of data in the module and you're worried about space or speed. Maybe you know that you only want to use one specific function, and you don't want to worry about *namespaces*. 

In that case, you use this syntax: ``from <module-name> import <function-or-object-name-you-want-to-use>``. 

When you do that, you can then use the function or object that you specifically *imported* in your program, but other functions and objects that exist in the external module are not available to you -- because you specifically imported that one thing!


.. admonition:: Note: Python modules and limitations with activecode

   Throughout the chapters of this book, activecode windows allow you to practice the Python that you are learning.
   We mentioned in the first chapter that programming is normally done using some type of development
   environment and that the
   activecode used here was strictly to help us learn.  It is not the way we write production programs.

   To that end, it is necessary to mention that many of the  modules available in standard Python
   will **not** work in the activecode environment.  In fact, only turtle, math, random, and a couple others have been
   ported at this point.  If you wish to explore any
   additional modules, you will need to also explore using a more robust development environment.

**Check your understanding**

.. mchoicemf:: question4_1_1
   :answer_a: A file containing Python definitions and statements intended for use in other Python programs.
   :answer_b: A separate block of code within a program.
   :answer_c: One line of code in a program.
   :answer_d: A file that contains documentation about functions in Python.
   :correct: a
   :feedback_a: A module can be reused in different programs.
   :feedback_b: While a module is separate block of code, it is separate from a program.
   :feedback_c: The call to a feature within a module may be one line of code, but modules are usually multiple lines of code separate from the program
   :feedback_d: Each module has its own documentation, but the module itself is more than just documentation.

   In Python a module is:

.. mchoicemf:: question4_1_2
   :answer_a: Go to the Python Documentation site.
   :answer_b: Look at the import statements of the program you are working with or writing.
   :answer_c: Ask the professor
   :answer_d: Look in this textbook.
   :correct: a
   :feedback_a: The site contains a listing of all the standard modules that are available with Python.
   :feedback_b: The import statements only tell you what modules are currently being used in the program, not how to use them or what they contain.
   :feedback_c: While the professor knows a subset of the modules available in Python, chances are the professor will have to look up the available modules just like you would.
   :feedback_d: This book only explains a portion of the modules available.  For a full listing you should look elsewhere.

   To find out information on the standard modules available with Python you should:

.. mchoicemf:: question4_1_3
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: Only turtle, math, and random have been ported to work in activecode at this time.
   :feedback_b: Only turtle, math, and random have been ported to work in activecode at this time.

   True / False:  All standard Python modules will work in activecode.




