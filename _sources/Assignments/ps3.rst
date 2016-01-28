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


Activities through 1/31
=======================

You have the following graded activities:

* **Before Monday's class, 1/25:**

  * Read :ref:`Iteration<iteration_chap>`, and do the exercises in that chapter
  * Read :ref:`Folders and copying <mkdir_and_cp_sect>` about the Unix commands ``mkdir`` and ``cp``

.. usageassignment:: prep_05
    :chapters: Iteration
    :subchapters: Unix/DirectoriesAndCopying
    :assignment_name: Prep 05
    :deadline: 2016-01-25 19:40:00
    :pct_required: 80
    :points: 50

* **Before Tuesday 1/26 at midnight:**

  * Read Chapter 3 of the Most Human Human
  * Answer `Reading Response 4 <https://umich.instructure.com/courses/48961/assignments/57679>`_ on Canvas.

* **Before Wednesday's class, 1/27:**
  
  * Read :ref:`Conditionals <conditionals_chap>` and do exercises
  * Read :ref:`File Input/Output <files_chap>` (read the Selection/Conditionals chapter first, or you won't be able to do the last exercise...)
  * Read :ref:`Understanding Code <understand_code_chap>` and do exercises

.. usageassignment:: prep_06
    :chapters: Selection, Files
    :subchapters: BuildingAProgram/UnderstandingCode
    :assignment_name: Prep 06
    :deadline: 2016-01-27 19:40:00
    :pct_required: 80
    :points: 50

* **Before Sunday evening, 1/31:**

  * Save answers to each of the exercises in :ref:`Problem Set 3 <problem_set_3>` and the exercises in :ref:`Unix Problems 3 <unix_pset3>` to Canvas by **5PM**
  * Upload your **Demonstrate Understanding** assignment to Canvas by **6PM**


.. _unix_pset3:

Unix Problems
-------------

1. Use the ``mkdir`` command and other Unix commands you've learned to create a folder called ``ps3`` inside your ``106`` folder. Use the ``cp`` command and other Unix commands you've learned as needed to copy ``sample.txt`` from the ``ps2`` folder into the ``ps3`` folder. Then use the ``mkdir`` command to make a sub-directory inside the ``ps3`` folder called ``inside_ps3``. Take a screenshot showing that you typed these commands and that they worked properly (you could use ``ls`` or ``pwd`` to show that they worked!), and upload it to **Unix problems 3** on Canvas.

2. Use the ``cp`` command to copy all of the individual files inside ``106/ps1`` to your ``106/ps3`` directory. (You can't copy sub-directories without a special flag, but you can copy files! See the chapter you read.) 

After this, if you type ``ls`` in the ``ps3`` folder, you should see ``test.txt`` and ``sample.txt`` and the ``inside_ps3`` folder (unless you previously added more files to the ``ps1`` directory, in which case you should see those, too). Take a screenshot to show that you typed these commands and that they were successful. Upload it to **Unix problems 3** on Canvas.


.. _problem_set_3:

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

1. Write code that uses iteration to print out each element of the list ``several_things``. Then, write code to print out the TYPE of each element of the list called ``several_things``.

.. activecode:: ps_3_1

   several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

   ====
   
   import test
   print "\n\n---\n"
   print "(There are no tests for this problem.)"

2. See the comments for directions.

.. activecode:: ps_3_2

    sent = "The magical mystery tour is waiting to take you away."

    # The following code does not iterate over the words in the English sentence we can read that's stored in the variable sent:
    for x in sent:
      print x
    # Why not? Knowing what you know about how computers and programming languages deal with sequences, what do you need to do to make sure you can iterate over the words in the sentence? Write a comment explaining:


    # Write code that assigns a variable word_list to hold a LIST of all the
    # WORDS in the string sent. It's fine if words include punctuation.


    ====

    import test
    print "\n\n---\n"
    print "No tests for the comment, of course -- we can only test stored values!\n"
    try:
        test.testEqual(word_list,sent.split())
    except:
        print "The variable word_list has not been defined"


3. Write code that uses iteration to print out each element of the list stored in ``excited_words``, BUT print out each element **without** its ending punctuation. You should see:

``hello``

``goodbye``

``wonderful``

``I love Python``

(Hint: remember string slicing?)

.. activecode:: ps_3_3

    excited_words = ["hello!", "goodbye!", "wonderful!", "I love Python?"]

    # Write your code here.

    ====

    import test
    print "\n\n---\n"
    print "(There are no tests for this problem.)"


4. Write code to open the file we've included in this problem set, ``about_programming.txt``, and print out each of the first two lines only. (Don't worry about blank lines appearing.) (Hint: use one of the file methods you've learned to make this easy!) Do not print out a list. 

The result should look like this:

   Computer programming (often shortened to programming) is a process that leads from an
  
   original formulation of a computing problem to executable programs. It involves

.. activecode:: ps_3_4
       :available_files: about_programming.txt

       # Write your code here.
       # Don't worry about extra blank lines between each of the lines when you print them
       # (but if you want to get rid of them, you can try out the .strip() method)

       ====

       import test
       print "\n\n---\n"
       print "There are no tests for this problem."


5. Write code to open the file ``about_programming.txt`` and assign the **number of lines** in the file to the variable ``file_lines_num``.

.. activecode:: ps_3_5
       :available_files: about_programming.txt

       # Write your code here.

       ====

       import test
       print "\n\n---\n"

       try:
            test.testEqual(file_lines_num,len(open("about_programming.txt","r").readlines()))
       except:
            print "The variable file_lines_num has not been defined"


6. The program below doesn't always work as intended. Try uncommenting different lines setting the initial value of x. Tests will run at the end of your code, and you will get diagnostic error messages. 

Fix the code so that it passes the test for each different value of x. So when the first line is uncommented, and when the second line, third line, and fourth line are each uncommented, you should always pass the test.
(HINT: you don't have to make a big change.)

.. activecode:: ps_3_6

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
            print "test when x is -10; y should be 'maybe'"
            test.testEqual(y, "maybe")
        else:
            print "No tests when value of x is %s" % (x)
    except:
        print "Failed test. Probably y is not bound to a value."


7. See comments in code for instructions.

.. activecode:: ps_3_7

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
   # list lp only IF the length of the element is
   # an even number. Use iteration (a for loop!).

   ====

   print "\n---\n\n"
   print "There are no tests for this problem."


8. Write code to count the number of strings in list ``items`` that have the character ``w`` in it. Assign that number to the variable ``acc_num``. HINT 1: Use the accumulation pattern! HINT 2: the ``in`` operator checks whether a letter or substring is present in a string.

.. activecode:: ps_3_8

   items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

   ====

   import test
   print "\n---\n\n"
   try:
      test.testEqual(acc_num,3)
   except:
      print "The variable acc_num has not been defined yet"



9. **Challenge problem (OPTIONAL, much harder):** write code to find the average (mean) number of words in each line of the file ``about_programming.txt``.

.. activecode:: ps_3_9
    :available_files: about_programming.txt

    # Write your code here.

    ====

    import test
    print "\n\n---\n"
    print "There are no tests for this problem."
