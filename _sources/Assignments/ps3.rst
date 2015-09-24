:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500


Activities through 10/4
=======================

You have the following graded activities:

* Before Monday's class, 9/28:

  * :ref:`Conditionals <conditionals_chap>`
  * :ref:`File Input/Output <files_chap>` (read the Selection/Conditionals chapter first, or you won't be able to do the last exercise...)
  * :ref:`Understanding Code <understand_code_chap>`
  * Read `External tutorial on unix <, >, and |  <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_

    * Note: If you're trying out the commands in the tutorial on your own machine, don't be alarmed by the *who* command that is used in one of the examples. It's not very intuitive what it's doing on a single-user computing system like a Mac, and it's not available all in git bash for Windows users.
    * Note: you might also like some of the other pages in the tutorial at that site.

* Before Wednesday's class 9/30:
  * Read :ref:`Dictionaries<dictionaries_chap>`, and do the exercises in that chapter
  * Read `External tutorial on unix grep  <http://www.uccs.edu/~ahitchco/grep/>`_

* By Sunday 10/4 at 5PM. Save answers to the exercises in :ref:`Problem Set 3 <problem_set_3>`. including :ref:`Unix Problems (2) <unix_pset3>`

* By Sunday midnight 10/4:
  * Read *The Most Human Human*, Chapter 5, "Getting out of Book"
  * Answer :ref:`Reading Response 5 <reading_response_5>`.

Reading Response
----------------

.. _reading_response_5:

Give an example of when you were interacting with someone where you used "book" responses. What's an example of a time when you or the person you were talking to got "out of book" unusually fast?

.. activecode:: rr_5_1
   :nocanvas:

   # Fill in your answer on the lines between the triple quotes
   s = """
   """
   print s

Quick check-in. How are things going for you in this class so far? Feeling overwhelmed? Inspired? Bored?

.. activecode:: rr_5_2
   :nocanvas:

   # Fill in your answer on the lines between the triple quotes
   s = """
   """
   print s



.. _problem_set_3:

.. _unix_pset3:

Unix Problems
-------------

The following problems include instructions for you to follow in your Terminal application, if you have a Mac, or in Git Bash, if you have Windows (:ref:`instructions for installing git bash <install_git_bash>`). Each one requires you to take a screenshot of the result and upload all these screenshots to **PS3 Unix Problems** on Canvas  > Assignments PS3 Unix Problems.

1. Create a folder ps3 in your 106 directory. Download the file ``sample.txt`` from the cTools Resources>Code directory and save it in your ps3 directory.

2. Connect to the ps4 directory. Run the command ``less sample.txt``. Take a screenshot to show that the command worked for displaying the contents. Upload it.


Problem Set
-----------

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

.. datafile::  about_programming.txt
   :hide:

   Computer programming (often shortened to programming) is a process that leads from an
   original formulation of a computing problem to executable programs. It involves
   activities such as analysis, understanding, and generically solving such problems
   resulting in an algorithm, verification of requirements of the algorithm including its
   correctness and its resource consumption, implementation (or coding) of the algorithm in
   a target programming language, testing, debugging, and maintaining the source code,
   implementation of the build system and management of derived artefacts such as machine
   code of computer programs. The algorithm is often only represented in human-parseable
   form and reasoned about using logic. Source code is written in one or more programming
   languages (such as C++, C#, Java, Python, Smalltalk, JavaScript, etc.). The purpose of
   programming is to find a sequence of instructions that will automate performing a
   specific task or solve a given problem. The process of programming thus often requires
   expertise in many different subjects, including knowledge of the application domain,
   specialized algorithms and formal logic.
   Within software engineering, programming (the implementation) is regarded as one phase in a software development process. There is an on-going debate on the extent to which
   the writing of programs is an art form, a craft, or an engineering discipline. In
   general, good programming is considered to be the measured application of all three,
   with the goal of producing an efficient and evolvable software solution (the criteria
   for "efficient" and "evolvable" vary considerably). The discipline differs from many
   other technical professions in that programmers, in general, do not need to be licensed
   or pass any standardized (or governmentally regulated) certification tests in order to
   call themselves "programmers" or even "software engineers." Because the discipline
   covers many areas, which may or may not include critical applications, it is debatable
   whether licensing is required for the profession as a whole. In most cases, the
   discipline is self-governed by the entities which require the programming, and sometimes
   very strict environments are defined (e.g. United States Air Force use of AdaCore and
   security clearance). However, representing oneself as a "professional software engineer"
   without a license from an accredited institution is illegal in many parts of the world.



3. Write code to open the file we've included in this problem set, ``about_programming.txt``, and print it out, line by line. (Don't worry about the blank lines that will appear.)

The first two lines should look like this:

   Computer programming (often shortened to programming) is a process that leads from an
  
   original formulation of a computing problem to executable programs. It involves

.. activecode:: ps_3_3
       :available_files: about_programming.txt

       # Write your code here.
       # Don't worry about extra blank lines between each of the lines
       # (but if you want to get rid of them, you can try out the .strip() method)

       ====

       import test
       print "\n\n---\n"
       print "There are no tests for this problem."


4. Now write code to open the file ``about_programming.txt`` and assign the **number of lines** in the file to the variable ``file_lines_num``.

.. activecode:: ps_3_4
       :available_files: about_programming.txt

       # Write your code here.

       ====

       import test
       print "\n\n---\n"

       try:
            test.testEqual(file_lines_num,len(open("about_programming.txt","r").readlines()))
       except:
            print "The variable file_lines_num has not been defined"

5. The program below doesn't always work as intended. Try uncommenting different lines setting the initial value of x; tests will run at the end of your code and you will get diagnostic error messages.

.. activecode:: ps_3_5

    #x = 25
    #x = 15
    #x = 5
    #x = -10

    if x > 20:
        y = "yes"
    if x > 10:
        y = "no"
    if x < 0:
        y = "maybe"
    else:
        y = "unknown"

    print "y is " + str(y)

    ====

    import test
    print "\n---\n\n"
    try:
        if x == 25:
            print "test when x is 25: y should be 'yes'"
            test.testEqual(y, "yes")
        elif x == 15:
            print "test when x is 15: y should be 'no'"
            test.testEqual(y, "no")
        elif x == 5:
            print "test when x is 5: y should be 'unknown'"
            test.testEqual(y, "unknown")
        elif x == -10:
            print "test when x is -5; y should be 'maybe'"
            test.testEqual(y, "maybe")
        else:
            print "No tests when value of x is %s" % (x)
    except:
        print "Failed test. Probably y is not bound to a value."


6. See comments in code for instructions.

.. activecode:: ps_3_6

   lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]

   # How many characters are in each element of list lp?
   # Write code to print the length (number of characters)
   # of each element of the list on a separate line.
   ## (Do not write 8+ lines of code to do this. Use a for loop.)

   # The output you get should be:
   # 5
   # 13
   # 11
   # 12
   # 3
   # 12
   # 11
   # 6

   # Now write code to print out each element of
   # list lp IF the length of the element is
   # an even number. Use iteration (a for loop!).

   ====

   print "\n---\n\n"
   print "There are no tests for this problem."


7. Write code to count the number of strings in list ``items`` that have the character ``w`` in it. Assign that number to the variable ``acc_num``. HINT 1: Use the accumulation pattern! HINT 2: the ``in`` operator checks whether a letter or substring is present in a string.

.. activecode:: ps_3_7

   items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

   ====

   import test
   print "\n---\n\n"
   try:
      test.testEqual(acc_num,3)
   except:
      print "The variable acc_num has not been defined yet"



8. **Challenge problem (OPTIONAL, much harder):** write code to find the average (mean) number of words in each line of the file ``about_programming.txt``.

.. activecode:: ps_3_8
    :available_files: about_programming.txt

    # Write your code here.

    ====

    import test
    print "\n\n---\n"
    print "There are no tests for this problem."
