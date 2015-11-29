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


Activities through 10/11
========================


You have the following graded activities:


* Before Monday's class:
    * Read :ref:`Accumulating results in dictionaries<dictionary_accum_chap>`, and do the exercises in that chapter
    * Read :ref:`Strategy for building programs <build_program_chap>`

.. usageassignment:: prep_8
    :chapters: DictionaryAccumulation
    :subchapters: BuildingAProgram/TheStrategy
    :assignment_name: Prep 8
    :deadline: 2015-10-05 21:30:00
    :pct_required: 80
    :points: 50

* Before Wednesday's class:
    * Read :ref:`Defining Functions<functions_chap>`, and do the exercises in that chapter

.. usageassignment:: prep_9
    :chapters: Functions
    :assignment_name: Prep 9
    :deadline: 2015-10-07 21:30:00
    :pct_required: 80
    :points: 50

* By Sunday 10/11 at 5PM.
    * Save answers to the exercises in :ref:`Problem Set 4 <problem_set_4>`.

* By Sunday midnight 10/11:
    * Read *The Most Human Human*, Chapter 10, p.219-237 only (you'll read the rest of the chapter next week). Note: we are skipping some of the other chapters.
    * Answer :ref:`Reading Response 6 <reading_response_6>`.


Reading Response
----------------

.. _reading_response_6:

1. Compare a conversation that "stays in book" to one that doesn't. Which has more surprisal? Which would be easier to compress?
2. Give an example of compression other than the ones Christian addresses. Explain. Why? In what situations does this occur?

.. activecode:: rr_6_1

   # Fill in your response in between the triple quotes
   s = """

   """
   print s



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


1. Old McDonald had a farm. He records the animals on his farm in a dictionary called 'animals'. See comments for instructions...

.. activecode:: ps_4_1

   animals = {'cows': 2, 'chickens': 8, 'pigs': 4, 'mice': 72, 'cats': 9,'dogs': 1}

	# Write code to look up the number of chickens
   # Old McDonald recorded and assign it to the 
   # variable num_chickens. 
   # (Do not hard-code values! num_chickens = 8 will not earn points.)

   # Write code to add the key-value pair "yak":3
   # to the dictionary stored in the variable called animals.

   # Write code to increase the value for the key 
   # "dogs" in the animals dictionary we've provided) by 1.

   ====
   
   import test
   try: 
      test.testEqual(num_chickens, animals['chickens'])
   except:
      print "either num_chickens or animal['chickens'] is undefined"

   try:
      test.testEqual(animals['yak'], 3)
   except:
      print "key 'yak' is not set in dictionary num_chickens"
      
   test.testEqual(animals['dogs'], 2)



2. Here's another dictionary. Write code to print out each key-value pair in it. Then follow the rest of the instructions in the comments.

.. activecode:: ps_4_2

   nd = {"autumn":"spring", "well":"spring", "4":"seasons","23":345}
   
   # Use a for looop to print out each key-value pair. 
   # Remember that printing things with a comma, e.g.
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
   # value of key "23" by 5
   
   # Now, write code to print the 
   # value of the key "well".
   
   ====
   
   import test
   print "\n---\n\n"
   try:
      test.testEqual(nd["23"],350)
   except:
      print "nd doesn't exist or doesn't have the key '23'"


3. We've included the same file in this problem set that we included in the last problem set -- ``about_programming.txt``. Write code to open the file and print out each line in the file that has a "program"-based word (any of the words ``program``, ``programs``, ``programming``, ``programmer``, or ``programmers``...) in it.

.. activecode:: ps_4_3
    :available_files: about_programming.txt

  	 # Write your code here!

    ====

    print "\n---\n\n"
    print "There are no tests for this problem"

4. Define a function called add_three, which takes one integer as input and returns that integer + 3.

.. activecode:: ps_4_4

    # Write your code here.
    # (The tests for this problem are going to try to CALL the function that you write!)

    ====

    import test
    try:
      print "testing if add_three(2) equals 5"
      test.testEqual(add_three(2),5)
      print "testing if add_three(33) equals 36"
      test.testEqual(add_three(33),36)
    except:
      print "The function add_three has not been defined yet, OR it hasn't been defined properly"

5. Take a look at the code below. The function subtract_five is supposed to take one integer as input and return that integer - 5. You'll get an error if you run it as is. Change it so it works!

.. activecode:: ps_4_5

   def subtract_five(inp)
   	print inp - 5
	return None

   y = subtract_five(9) - 6

   ====

   print "\n---\n\n"
   import test
   try:
    print "testing if y is -2"
    test.testEqual(y, -2)
   except:
    print "The variable y was deleted or is not defined"

6. Here's another bit of code with a problem. Also, add comments about what's going on with the current code that causes a problem. Then, fix it so it calls change_amounts on some input and prints out the results.

.. activecode:: ps_4_6

    def change_amounts(yp):
	n = yp - 4
	return n * 7

    print yp

    ====

    print "\n---\n\n"
    print "There are no tests for this problem"


7. Define a function called change_amounts that takes one integer as input. If the input is larger than 10, it should return the input + 5. If the input is smaller than or equal to 10, it should return the input + 2.

.. activecode:: ps_4_7

    # We've started you off with the first line...
    def change_amounts(num_here):
       pass # delete this line and put in your own code for the body of the function.

    ====

    print "\n---\n\n"
    import test
    try:
      print "testing if change_amounts(9) equals 11"
      test.testEqual(change_amounts(9),11)
      print "testing if change_amounts(12) equals 17"
      test.testEqual(change_amounts(12),17)
    except:
      print "The function change_amounts has not been defined properly"
