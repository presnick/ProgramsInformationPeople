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


Activities through 1/24
=======================

You have the following graded activities:

* **Before Tuesday 1/19 at midnight:** (Changed for clarity in retrospect: amnesty granted for W16 until 1/21 midnight)

  * Answer `Reading Response 3 <https://umich.instructure.com/courses/48961/assignments/57678>`_ .

* **Before Wednesday's class 1/20** (no class Monday for MLK Day):

  * Read :ref:`Sequences <sequences_chap>`, and do the exercises in that chapter.
  * Read :ref:`unix cat and less<less_chap>` section of the Unix chapter

  * Read chapter 2 of The Most Human Human.

.. usageassignment:: prep_04
    :chapters: Sequences
    :subchapters: Unix/lessCommand
    :assignment_name: Prep 04
    :deadline: 2016-01-20 19:40:00
    :pct_required: 80
    :points: 50

* By **Sunday 1/24 at 5PM**, save answers to the exercises in **Problem Set 2**:

  * Do the Unix Problems part of the problem set: :ref:`Unix Problems (2) <unix_pset2>` and upload the screenshots in Canvas, Assignments > Unix problems 2.
  * Save answers to each of the exercises in :ref:`Problem Set 2 <problem_set_2>`

* By **Sunday 1/24 at 6PM**, save your **Demonstrate Understanding** assignment for this week in Canvas.


.. _unix_pset2:

Unix Problems
-------------

The following problems include instructions for you to follow in your Terminal application, if you have a Mac, or in Git Bash, if you have Windows (:ref:`instructions for installing git bash <install_git_bash>`). Each one requires you to take a screenshot of the result and upload all these screenshots to **PS3 Unix Problems** on Canvas  > Assignments PS3 Unix Problems.

1. Create a folder ``ps2`` in your 106 directory. Download the file ``sample.txt`` from the Canvas Code directory and save it in your ``ps2`` directory.

2. Connect to the ``ps2`` directory. Run the command ``less sample.txt``. Take a screenshot to show that the command worked for displaying the contents. Upload it to the Canvas assignment for **Unix problems 2**.


.. _problem_set_2:

Problem Set
-----------
**Due:** **Sunday, January 24 at 5 pm**

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. Assign the variable ``fl`` the value of the first element of the string value in ``original_str``. Use string indexing to assign the variable ``last_l`` the value of the last element of the string value in ``original_str``. Write code so that will work no matter how long ``original_str``'s value is.

.. activecode:: ps_2_1
 
   original_str = "The quick brown rhino jumped over the extremely lazy fox."
   
   # assign variables as specified below this line!
   
   ====
   
   import test
   print "\n\n---\n"
   try:
      test.testEqual(fl,original_str[0])
   except:
      print "The variable fl has not been defined yet"
   try:
      test.testEqual(last_l, original_str[-1])
   except:
      print "The variable last_l has not been defined yet"

2. See comments for instructions.

.. activecode:: ps_2_2

   sent = """
   He took his vorpal sword in hand:
   Long time the manxome foe he sought
   So rested he by the Tumtum tree,
   And stood awhile in thought.
   - Jabberwocky, Lewis Carroll (1832-1898)"""

   short_sent = """
   So much depends
   on
   """

   # How long (how many characters) is the string in the variable sent?
   # Write code to assign the length of the string to a variable called len_of_sent.


   # How long is the string in the variable short_sent?
   # Write code to assign the length of that string to a variable called short_len.


   # Write code to print out the value of short_len (and the value of len_of_sent, if you want!) so you can see it. 


   # Consider (ungraded but important): Why is the length of short_sent longer than 15 characters?


   # Assign the index of the first 'v' in the value of the variable sent TO a variable called index_of_v. (Hint: we saw a method of the string class that can help with this)

   ====
   
   import test
   print "\n\n---\n"
   try:
      test.testEqual(len_of_sent,len(sent))
   except:
      print "The variable len_of_sent has not been defined yet"
   try:
      test.testEqual(short_len,len(short_sent))
   except:
      print "The variable short_len has not been defined yet"
   try:
      test.testEqual(index_of_v, sent.find('v'))
   except:
      print "The variable index_of_v has not been defined yet"


3. See comments for instructions again. (Keep in mind: All ordinal numbers in *instructions*, like "third" or "fifth" refer to the way HUMANS count. How do you write code to find the right things?)

.. activecode:: ps_2_3

   num_lst = [4,16,25,9,100,12,13]
   mixed_bag = ["hi", 4,6,8, 92.4, "see ya", "23", 23]

   # Assign the value of the third element of num_lst to a variable called third_elem

   # Assign the value of the sixth element of num_lst to a variable called elem_sixth

   # Assign the length of num_lst to a variable called num_lst_len

   # Write a comment explaining the difference between mixed_bag[-1] and mixed_bag[-2]
   # (you may want to print out those values so you can make sure you know what they are!)

   # Write code to print out the type of the third element of mixed_bag

   # Write code to assign the **type of the fifth element of mixed_bag** to a variable called fifth_type

   # Write code to assign the **type of the first element of mixed_bag** to a variable called another_type

   ====

   import test
   print "\n\n---\n"
   try:
      test.testEqual(third_elem, num_lst[2])
   except:
      print "The variable third_elem has not been defined"
   try:
      test.testEqual(elem_sixth, num_lst[5])
   except:
      print "The variable elem_sixth has not been defined"
   try:
      test.testEqual(num_lst_len,len(num_lst))
   except:
      print "The variable num_lst_len has not been defined"
   try:
      test.testEqual(fifth_type,type(mixed_bag[4]))
   except:
      print "The variable fifth_type has not been defined"
   try:
      test.testEqual(another_type, type(mixed_bag[0]))
   except:
      print "The variable another_type has not been defined"


4. There is a function we are giving you for this problem set that takes two strings as inputs, and returns the length of both of those strings added together, called ``add_lengths``. We are also including the functions from Problem Set 1 called ``random_digit`` and ``square`` in this problem set. 

Now, take a look at the following code and related questions, in this code window.

.. activecode:: ps_2_4
   :include: addl_functions_2
   
   new_str = "'Twas brillig"
   
   y = add_lengths("receipt","receive")
   
   x = random_digit()
   
   z = new_str.find('b')
   
   l = new_str.find("'")
   
   # notice that this line of code is made up of a lot of different expressions
   fin_value = square(len(new_str)) + (z - l) + (x * random_digit())
   
   # DO NOT CHANGE ANY CODE ABOVE THIS LINE
   # But below here, putting print statements and running the code may help you!
   
   # The following questions are based on that code. All refer to the types of the 
   #variables and/or expressions after the above code is run.
   
   #####################   
   
   # Write a comment explaining each of the following, after each question.
   # Don't forget to save!
   
   # What is square? 
   
   # What type of object does the expression square(len(new_str)) evaluate to?
   
   # What type is z?
   
   # What type is l?
   
   # What type is the expression z-l?
   
   # What type is x?
   
   # What is random_digit? How many inputs does it take?
   
   # What type does the expression x * random_digit() evaluate to?
   
   # Given all this information, what type will fin_value hold once all this code is run?

   ====

   print "\n\nThere are no tests for this problem"


5. Write code to assign the number of characters in the string ``rv`` to a variable ``num_chars``. Then write code to assign the number of words in the string ``rv`` to the variable ``num_words``. (Hint: remember how to split strings?)

.. activecode:: ps_2_5

    rv = """Once upon a midnight dreary, while I pondered, weak and weary,
      Over many a quaint and curious volume of forgotten lore,
      While I nodded, nearly napping, suddenly there came a tapping,
      As of some one gently rapping, rapping at my chamber door.
      'Tis some visitor, I muttered, tapping at my chamber door;
      Only this and nothing more."""

    # Write your code here!

    ====

    import test
    print "\n\n---\n"
    try:
        test.testEqual(num_chars,len(rv))
    except:
        print "The variable num_chars has not been defined"
    try:
        test.testEqual(num_words,len(rv.split()))
    except:
        print "The variable num_words has not been defined"


.. activecode:: addl_functions_2
   :nopre:
   :hidecode:

   def square(num):
      return num**2

   def greeting(st):
      #st = str(st) # just in case
      return "Hello, " + st

   def random_digit():
     import random
     return random.choice([0,1,2,3,4,5,6,7,8,9])
      
   def add_lengths(str1, str2):
      return len(str1) + len(str2)
