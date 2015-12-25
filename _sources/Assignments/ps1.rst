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


Activities through 9/20
=======================

* Before Thursday's discussion section, 1/7 (preferably before first lecture on Wednesday 1/6):

  * Fill in a little `info about you </runestone/default/bio>`_ and, optionally, upload a picture that looks like how you look in class, so we can start to learn your names.
  * Sign up for the `Facebook group <https://www.facebook.com/groups/1752935254934382/>`_
  * Read :ref:`General Intro <the_way_of_the_program>`, and do the exercises in that chapter.

* Participation in Thursday discussion section, 1/7

* By Sunday night, 1/10,

  * read the intro and chapter 1 of The Most Human Human book.
  * Answer `Reading Response 1 <https://umich.instructure.com/courses/48961/assignments/57676>`_ .

* Before Monday's class, 1/11:

  * Read :ref:`Simple Python Data <simple_python_data>`, and do the exercises in that chapter.

* By Tuesday night, 1/12:

  * Read from the beginning through the middle of page 7 of `Minds, Brains, and Programs <https://umich.instructure.com/files/321962/download?download_frd=1>`_, by Richard Searle. It's in the Canvas Files folder, if that link doesn't work.
  * Answer `Reading Response 2 <https://umich.instructure.com/courses/48961/assignments/57677>`_ .

* Before Wednesday's class, 1/13:

  * Read :ref:`Debugging tips<debugging_chap>`, and do the exercises in that chapter
  * Read :ref:`Object Instances and Turtle graphics<turtles_chap>`, and do the exercises in that chapter

* Participation in Thursday discussion section, 1/14

* By Sunday 1/17 at 5PM: 

  * Save answers to the exercises in :ref:`Problem Set 1 <problem_set_1>`
  * Submit your **Demonstrate Understanding exercise** to your section site on Canvas. Instructions can be found `here <https://umich.instructure.com/courses/48961/assignments/57690>`_ . This should demonstrate your understanding of some of the material in this course up to this point.

* By Sunday night, 1/17:

  * Read chapter 2 of The Most Human Human.
  * Answer `Reading Response 3 <https://umich.instructure.com/courses/48961/assignments/57678>`_ .


.. _problem_set_1:

Problem Set
-----------

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. The variable ``tpa`` currently has the value ``0``. Assign the variable ``tpa`` the value ``6`` .

.. activecode:: ps_1_1

   tpa = 0
   
   ====

   import test
   print "\n\n---tests---\n"
   if type(tpa) != type(6):
      print "tpa should be an integer; check it's type with print type(tpa)"
   test.testEqual(tpa, 6)


2. Write code to assign the variable ``yb`` to have the same value that variable ``cw`` has. Do not change the first line of code (``cw = "Hello"``), but write code that would work no matter what the current value of ``cw`` is.

.. activecode:: ps_1_2

   cw = "Hello"
   yb = 0

   ====

   import test
   print "\n\n---tests---\n"
   try:
      test.testEqual(cw, yb)
   except:
      print "yb may not be defined yet..."
   print "Checking to make sure you didn't change cw"
   test.testEqual(cw, "Hello")


3. Write code to print out the type of the variable ``apples_and_oranges``, the type of the variable ``abc``, and the type of the variable ``new_var``.

.. activecode:: ps_1_3
   
   apples_and_oranges = """hello, everybody
                             how're you?"""

   abc = 6.75483

   new_var = 824

   ====

   print "\n\n---\n(There are no tests for this problem.)"


4. There is a function we are giving you called ``square``. It takes one integer and returns the square of that integer value. Write code to assign a variable callex ``xyz`` the value ``5*5`` (five squared). Use the square function, rather than just multiplying with ``*``.

.. activecode:: ps_1_4
    :include: addl_functions

    # Want to make sure there really is a function called square? Uncomment the following line and press run.

    #print type(square)
   
    xyz = ""
    
    ====

    import test
    print "\n\n---tests---\n"
    try:
       test.testEqual(type(xyz), type(3))
       test.testEqual(xyz,25)
    except:
       print "variable xyz doesn't have a value at all!"


5. Write code to assign the return value of the function call ``square(3)`` to the variable ``new_number``.

.. activecode:: ps_1_5
    :include: addl_functions

    # write your code here; include a blank line

    ====

    import test
    print "\n\n---\n"
    import test
    try:
       test.testEqual(new_number, 9)
    except:
       print "Test failed: the variable new_number does not exist yet"


6. Write in a comment what each line of this code does. 

.. activecode:: ps_1_6
    :include: addl_functions

    # Here's an example.
    xyz = 12 # The variable xyz is being assigned the value 12, which is an integer

    # Now do the same for these!
    a = 6

    b = a

    # make sure to be very clear and detailed about the following line of code
    orange = square(b)

    print a

    print b

    print orange

    pear = square

    print pear


7. There are a couple more functions we're giving you in this problem set. One is a function called ``greeting``, which takes any string and adds ``"Hello, "`` in front of it. (You can see examples in the code.) Another one is a function called ``random_digit``, which returns a value of any random integer between 0 and 9 (inclusive). (You can also see examples in the code.)

Write code that assigns to the variable ``func_var`` the **function** ``greeting`` (without executing the function). 

Then, write code that assigns to the variable ``new_digit`` the **return value** from executing the function ``random_digit``.

Then, write code that assigns to the variable ``digit_func`` the **function** ``random_digit`` (without executing the function).

.. activecode:: ps_1_7
   :include: addl_functions

   # For example
   print greeting("Jackie")
   print greeting("everybody")
   print greeting("sdgadgsal")
   
   # Try running all this code more than once, so you can see how calling the function
   # random_digit works.
   print random_digit()
   print random_digit()

   # Write code that assigns the variables as mentioned in the instructions.

   ====

   import test
   print "\n\n---\n"
   # wrap these in try/excepts if variables not defined #
   try:
      test.testEqual(type(func_var), type(greeting))
   except:
      print "Test failed: func_var is undefined"
   try:
      test.testEqual(type(new_digit), type(1))
   except:
      print "Test failed: new_digit is undefined"
   try:
      test.testEqual(type(digit_func), type(random_digit))
   except:
      print "Test failed: digit_func is undefined"



8. Now write code that assigns the variable ``newval`` to hold the **return value** of ``greeting("everyone in class")``.

.. activecode:: ps_1_8
   :include: addl_functions

   ====

   import test
   print "\n\n---\n"
   try:
      test.testEqual(newval, greeting("everyone in class"))
   except:
      print "Test failed: newval is not defined"
    

9. This code causes an error. Why? Write a comment explaining.

.. activecode:: ps_1_9

   another_variable = "?!"
   b = another_variable()


10. Here's another complicated expression, using the Turtle framework we talked about. Arrange these expressions in the order they are executed, like you did in an exercise in Chapter 2 of the textbook.

.. sourcecode:: python

   import turtle

   ella = turtle.Turtle()
   x = "hello class".find("o") - 1
   ella.speed = 3


   ella.move(square(x*ella.speed))

.. parsonsprob:: ps_1_10

   Order the code fragments in the order in which the Python interpreter would evaluate them, when evaluating that last line of code, ``ella.move(square(x*ella.speed))`` (It may help to think about what specifically is happening in the first four lines of code as well.)
   -----
   Look up the variable ella and find that it is an instance of a Turtle object
   =====
   Look up the attribute move of the Turtle ella and find that it's a method object
   =====
   Look up the function square
   =====
   Look up the value of the variable x and find that it is an integer
   =====
   Look up the value of the attribute speed of the instance ella and find that it is an integer
   =====
   Evaluate the expression x * ella.speed to one integer
   =====
   Call the function square on an integer value
   =====
   Call the method .move of the Turtle ella on its input integer

11. Write a program that uses the turtle module to draw something interesting. It doesn't have to be complicated, but draw something different than we did in the textbook or in class. (Optional but encouraged: post a screenshot of the artistic outcome to the Facebook group, or a short video of the drawing as it is created.)

.. activecode:: ps_1_11

   import turtle



.. activecode:: addl_functions
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

