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

Activities through 2/7
=======================

You have the following graded activities:

* **Before Monday's class, 2/1:**

  * Read `External tutorial on unix <, >, and |  <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_ and `External tutorial on unix grep  <http://www.uccs.edu/~ahitchco/grep/>`_.
  * Note: If you're trying out the commands in the tutorial on your own machine, don't be alarmed by the *who* command that is used in one of the examples. It's not very intuitive what it's doing on a single-user computing system like a Mac, and it's not available all in git bash for Windows users.
    
    * Note: you might also like some of the other pages in the tutorial at that site.

  * Read :ref:`Dictionaries<dictionaries_chap>`, and do the exercises in that chapter

.. usageassignment:: prep_07
    :chapters: Dictionaries
    :assignment_name: Prep 07
    :deadline: 2016-02-01 19:40:00
    :pct_required: 80
    :points: 50


* **By Tuesday midnight, 2/2:**

  * Read chapter 5 of The Most Human Human
  * Answer `Reading Response 5 <https://umich.instructure.com/courses/48961/assignments/57680>`_ on Canvas.

* **Before Wednesday's class, 2/3:**

  * Read :ref:`Accumulating results in dictionaries<dictionary_accum_chap>`, and do the exercises in that chapter
  * Read :ref:`Strategy for building programs <build_program_chap>`

.. usageassignment:: prep_08
    :chapters: DictionaryAccumulation
    :subchapters: BuildingAProgram/TheStrategy
    :assignment_name: Prep 08
    :deadline: 2016-02-03 19:40:00
    :pct_required: 80
    :points: 50

* **By Sunday evening, 2/7:**
  
  * Save answers to each of the exercises in :ref:`Problem Set 4 <problem_set_4>` and the exercises in :ref:`Unix Problems 4 <unix_pset4>` to Canvas by **5PM**
  * Upload your **Demonstrate Understanding** assignment to Canvas by **6PM**

Unix Problems
-------------

.. _unix_pset4:

Turn these in as screenshots showing you've done these things via Canvas > Assignments > Unix problems 4.

1. In the `tutorial on unix <, >, and |  <http://www.ee.surrey.ac.uk/Teaching/Unix/unix3.html>`_,  there are instructions for creating two files called  ``list1`` and ``list2``. Write a single unix command that displays all lines in either file that contain the letter ``p``.

2. Save a file in the ``106`` folder you created a couple weeks ago called ``fun_with_unix.txt``. Now use ``ls``, ``|`` (pipe), and ``grep`` to find all filenames in your folder containing the string ``unix``. (For fun, try this with other substrings and other folders.)

.. _problem_set_4:

Problem Set
-----------

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

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

**Note:** Passing tests for a problem (``Pass``) does not ensure that the problem is 100% correct -- we can only test some things, to provide a bit of feedback as you go.


1. Old McDonald had a farm. He records the animals on his farm in a dictionary called 'animals'. See comments for additional instructions...

.. activecode:: ps_4_1

   animals = {'cows': 2, 'chickens': 8, 'pigs': 4, 'mice': 72, 'cats': 9,'dogs': 1}

   # Write code to look up the number of chickens
   # Old McDonald recorded and assign it to the 
   # variable num_chickens. 
   # (Do not hard-code values! num_chickens = 8 will not earn points.)

   # Write code to add the key-value pair "yak":3
   # to the dictionary stored in the variable called animals.

   # Write code to increase the value for the key 
   # "dogs" (in the animals dictionary we've provided) by 1.

   ====
   
   import test
   try: 
      test.testEqual(num_chickens, animals['chickens'])
   except:
      print "Something is is undefined so this test cannot run. Read the directions again!\n"

   try:
      test.testEqual(animals['yak'], 3)
   except:
      print "key 'yak' is not yet set in dictionary animals"
      
   test.testEqual(animals['dogs'], 2)



2. Here's another dictionary. Write code to print out each key-value pair in it, one key and its value on each line. Then follow the rest of the instructions in the comments.

.. activecode:: ps_4_2

   nd = {"autumn":"spring", "well":"spring", "4":"seasons","23":345}
   
   # Use a for loop to print out each key-value pair. 
   # Hint to make this easier: printing things with a comma, e.g.
   # print "hello", "everyone" 
   # will print out those things on the same 
   # line with a space in between them.
   
   # Your output should look SOMETHING LIKE this 
   # (remember, the pairs could be in any order, 
   # because it's a dictionary):
   # autumn spring
   # 4 seasons
   # 23 345
   # well spring
   
   # Now, write code to increase the 
   # value of key "23" by 5. Your code should work 
   # no matter what the value of the key "23" is,
   # as long as its value is an integer.
   
   # Now, write code to print the 
   # value of the key "well".
   # Your code should work no matter 
   # what the value of the key "well" is.
   
   ====
   
   import test
   print "\n---\n\n"
   try:
      test.testEqual(nd["23"],350)
   except:
      print "nd doesn't exist or doesn't have the key '23'"


3. We've included the same file in this problem set that we included in the last problem set -- ``about_programming.txt``. Write code to open the file and print out each line in the file that has the string ``program`` in it. (Note that each line with the string ``program`` in it should only print out once, even if the string ``program`` occurs in it more than once.) Then, write code (or edit the code that you already wrote!) to accumulate a list of the lines in the file that include the string ``program``. Save that list in a variable ``program_lines``.

.. activecode:: ps_4_3
   :available_files: about_programming.txt
  
   # Write your code here!

   ====

   import test
   print "\n---\n\n"
   tmp = []
   for l in open("about_programming.txt").readlines():
     if "program" in l:
       tmp.append(l)
   try:
     test.testEqual(program_lines,tmp)
   except:
     print "program_lines has not been defined, or you have another error"


4. Below is an empty dictionary saved in the variable ``nums``, and a list saved in the variable ``num_words``. Use iteration and dictionary mechanics to add each element of ``num_words`` as a key in the dictionary ``nums``. Each key should have the value ``0``. The dictionary should end up looking something like this when you print it out (remember, you can't be sure of the order): ``{"two":0,"three":0,"four":0,"eight":0,"seventeen":0,"not_a_number":0}``

.. activecode:: ps_4_4

  nums = {}
  num_words = ["two","three","four","seventeen","eight","not_a_number"]
  # Write your code here.

  ====

  import test
  try:
    test.testEqual(nums["two"],0)
    test.testEqual(type(nums["seventeen"]),type(3))
    test.testEqual(nums,{"two":0,"three":0,"four":0,"eight":0,"seventeen":0,"not_a_number":0})
  except:
    print "You've created an error somewhere or have not completed this problem."

5. Given the string ``s`` in the code below, write code to figure out what the most common word in the string is and assign that to the variable ``abc``. (Do not hard-code the right answer.) Hint: dictionary mechanics will be useful here.

.. activecode:: ps_4_5

   s = "Number of slams in an old screen door depends upon how loud you shut it, the count of slices in a bread depends how thin you cut it, and amount 'o good inside a day depends on how well you live 'em. All depends, all depends, all depends on what's around ya."

   # Write your code here.
    
   ====
    
   print "\n---\n\n"
   import test
   print "testing whether abc is set correctly"
   try:
     test.testEqual(abc, 'depends')
   except:
     print "The variable abc has not been defined and/or there is another error"
