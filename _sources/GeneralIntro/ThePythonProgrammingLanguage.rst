..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

The Python Programming Language
-------------------------------

The programming language you will be learning is Python. Python is an example
of a **high-level language**; other high-level languages you might have heard
of are C++, PHP, and Java.

As you might infer from the name high-level language, there are also
**low-level languages**, sometimes referred to as machine languages or assembly
languages. Loosely speaking, computers can only execute programs written in
low-level languages. Thus, programs written in a high-level language have to be
processed before they can run. This extra processing takes some time, which is
a small disadvantage of high-level languages.
However, the advantages to high-level languages are enormous.

First, it is much easier to program in a
high-level language. Programs written in a high-level language take less time
to write, they are shorter and easier to read, and they are more likely to be
correct. Second, high-level languages are **portable**, meaning that they can
run on different kinds of computers with few or no modifications. Low-level
programs can run on only one kind of computer and have to be rewritten to run
on another.

Due to these advantages, almost all programs are written in high-level
languages. Low-level languages are used only for a few specialized
applications.

Two kinds of programs process high-level languages into low-level languages:
**interpreters** and **compilers**. An interpreter reads a high-level program
and executes it, meaning that it does what the program says. It processes the
program a little at a time, alternately reading lines and performing
computations.

.. image:: Figures/interpret.png
   :alt: Interpret illustration

A compiler reads the program and translates it completely before the program
starts running. In this case, the high-level program is called the **source
code**, and the translated program is called the **object code** or the
**executable**. Once a program is compiled, you can execute it repeatedly
without further translation.

.. image:: Figures/compile.png
   :alt: Compile illustration

Many modern languages use both processes. They are first compiled into a lower
level language, called **byte code**, and then interpreted by a program called
a **virtual machine**. Python uses both processes, but because of the way
programmers interact with it, it is usually considered an interpreted language.

In this book, and for the first half of this course, you will not need to install
or run python natively on your computer. Instead, you'll be writing simple
programs and executing them right in your browser. About midway through
the course, you will install python, and then the next few paragraphs will
apply. Consider them a preview for now. 

There are two ways to use the Python interpreter: *shell mode* and *program
mode*. In shell mode, you type Python expressions into the **Python shell**,
and the interpreter immediately shows the result.  The example below shows the Python shell at work.

::

   $ python
   Python 3.5.2
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 2 + 3
   5
   >>> 

The ``>>>`` is called the **Python prompt**. The interpreter uses the prompt to
indicate that it is ready for instructions. We typed ``2 + 3``.  The
interpreter evaluated our expression and replied ``5``. On the next line
it gave a new prompt indicating that it is ready for more input.

Working directly in the interpreter is convenient for testing short bits of
code because you get immediate feedback. Think of it as scratch paper used to
help you work out problems.

Alternatively, you can write an entire program by placing lines of Python instructions
in a file and then use the interpreter to
execute the contents of the file as a whole. Such a file is often referred to as **source code**.  For
example, we will use a text editor to create a source code file named ``firstprogram.py`` with
the following contents:

.. sourcecode:: python

    print("My first program adds two numbers, 2 and 3:")
    print(2 + 3)


By convention, files that contain Python programs have names that end with
``.py`` .  Following this convention will help your operating system and other
programs identify a file as containing python code.

::

    $ python firstprogram.py
    My first program adds two numbers, 2 and 3:
    5

These examples show Python being run from a Unix command line. In other
development environments, the details of executing programs may differ. Also,
most programs are more interesting than this one.

.. note::

    In this textbook, we will not make use of the interactive python shell. We have found that it is quite confusing to students because the interactive shell shows the value of expressions, which are not normally revealed during a program's execution unless the print function is invoked. This textbook reinforces the notion that there is a difference between the internal state of a program during execution, and visible outputs, which are caused by invocations of the print function.

.. admonition:: Want to learn more about Python?

  If you would like to learn more about installing and using Python, here are some video links.
  `Installing Python for Windows <http://youtu.be/9EfGpN1Pnsg>`__ shows you how to install the Python environment under
  Windows Vista,
  `Installing Python for Mac <http://youtu.be/MEmEJCLLI2k>`__ shows you how to install under Mac OS/X, and
  `Installing Python for Linux <http://youtu.be/RLPYBxfAud4>`__ shows you how to install from the Linux
  command line.
  `Using Python <http://youtu.be/kXbpB5_ywDw>`__ shows you some details about the Python shell and source code.

**Check your understanding**

.. mchoice:: question1_2_1
   :answer_a: the instructions in a program, written in a high-level language.
   :answer_b: the language that you are programming in (e.g., Python).
   :answer_c: the environment/tool in which you are programming.
   :answer_d: the number (or “code”) that you must input at the top of each program to tell the computer how to execute your program.
   :feedback_a: If the instructions are strored in a file, it is called the source code file.
   :feedback_b: This language is simply called the programming language, or simply the language. Programs are writte in this language.
   :feedback_c: The environment may be called the IDE, or integrated development environment, though not always.
   :feedback_d: There is no such number that you must type in at the start of your program.
   :correct: a

   Source code is another name for:

.. mchoice:: question1_2_2
   :answer_a: It is high-level if you are standing and low-level if you are sitting.
   :answer_b: It is high-level if you are programming for a computer and low-level if you are programming for a phone or mobile device.
   :answer_c: It is high-level if the program must be processed before it can run, and low-level if the computer can execute it without additional processing.
   :answer_d: It is high-level if it easy to program in and is very short; it is low-level if it is really hard to program in and the programs are really long.
   :feedback_a: In this case high and low have nothing to do with altitude.
   :feedback_b: High and low have nothing to do with the type of device you are programming for.  Instead, look at what it takes to run the program written in the language.
   :feedback_c: Python is a high level language but must be interpreted into machine code (binary) before it can be executed.
   :feedback_d: While it is true that it is generally easier to program in a high-level language and programs written in a high-level language are usually shorter, this is not always the case.
   :correct: c

   What is the difference between a high-level programming language and a low-level programming language?
