:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. assignment for problem set
.. assignment::
  :name: PS1
  :assignment_type: problem_set
  :questions: ps_1_1 100, ps_1_2 100, ps_1_3 100, ps_1_4 100, ps_1_5 50, ps_1_6 200, ps_1_7 100, ps_1_8 100, ps_1_9 100, ps_1_10 0, ps_1_11 50
  :deadline: 2016-09-30 04:00
  :points: 1000
  :autograde: unittest

.. assignments for lecture waivers
.. none for lectures 1 and 2 and 3

.. assignments for end of lecture exercise sets
.. assignment::
  :name: lec2_attendance
  :assignment_type: lecture_attendance
  :questions: lec2_1 10, lec2_2 10, lec2_3 20 
  :deadline: 2016-09-12 21:10
  :points: 50
  :autograde: visited
  :threshold: 1


.. assignment::
  :name: lec3_attendance
  :assignment_type: lecture_attendance
  :questions: lec3_1 25, lec3_2 25
  :deadline: 2016-09-14 21:10
  :points: 50
  :autograde: visited
  :threshold: 1

.. assignments for reading responses
.. assignment::
  :name: response_1
  :assignment_type: reading_response
  :questions: rr_1 100
  :points: 100

.. assignment::
  :name: response_2
  :assignment_type: reading_response
  :questions: rr_2 100
  :points: 100

.. assignment for DYU
.. assignment::
  :name: dyu1
  :assignment_type: dyu
  :questions: ps1_dyu 100
  :points: 100

.. highlight:: python
    :linenothreshold: 500


Activities through 9/16
=======================

* **Before your first discussion section (preferably before first lecture on Wednesday 9/7):**

  * Fill in a little `info about you </runestone/default/bio>`_ and, optionally, upload a picture that looks like how you look in class, so we can start to learn your names.
  * Sign up for/join the `Facebook group <https://www.facebook.com/groups/628933357287543/>`_
  * Read :ref:`General Intro <the_way_of_the_program>`. When reading, run the activecodes and answer the multiple choice questions. If there are exercises at the end of a chapter, try to do at least some of them.

.. usageassignment:: 
  :chapters: GeneralIntro
  :assignment_name: Prep 01
  :deadline: 2016-09-30 04:00
  :pct_required: 80
  :points: 50

* **By Sunday 9/11 at 11:59 pm:**

  * read the intro and chapter 1 of The Most Human Human book.
  * Answer `Reading Response 1 <https://umich.instructure.com/courses/105657/assignments/131308>`_ .


* **Before Monday's class, 9/12:**

  * Read :ref:`Simple Python Data <simple_python_data>`. When reading, run the activecodes and answer the multiple choice questions. If there are exercises at the end of a chapter, try to do at least some of them.

.. usageassignment::
  :chapters: SimplePythonData
  :assignment_name: Prep 02
  :deadline: 2016-09-30 04:00
  :pct_required: 65
  :points: 50

* **By Tuesday night 11:59, 9/13:**

  * Read from the beginning through the middle of page 7 of `Minds, Brains, and Programs <https://umich.instructure.com/courses/105657/files?preview=2142149>`_, by Richard Searle. (It's in the Canvas Files folder, if that link doesn't work.)
  * Answer `Reading Response 2 <https://umich.instructure.com/courses/105657/assignments/131313>`_ .


* **Before Wednesday's class, 9/14:**

  * Read :ref:`Debugging tips<debugging_chap>`
  * Read :ref:`Object Instances and Turtle graphics<turtles_chap>`

.. usageassignment::
    :chapters: Debugging, PythonTurtle
    :assignment_name: Prep 03
    :deadline: 2016-09-30 04:00
    :pct_required: 80
    :points: 50

* Participation in your discussion section this week

* **By Friday 9/16 at 6:30 PM:** 

  * Save answers to the exercises in :ref:`Problem Set 1 <problem_set_1>`, including doing the first `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131293>`_ (DYU).

* **By Sunday 9/18 at 11:59 pm:** (We include this in your assignments for next week)

  * Read chapter 2 of The Most Human Human and answer `Reading Response 3 <https://umich.instructure.com/courses/105657/assignments/131314>`_ .


* Note that there is a grace period for the problem set and DYU assignment until **Sunday 9/18 at 5:00 PM**. You will not lose any points if you submit before then, even if you submit after the Friday deadline. After the grace period, we do not accept late assignments. See syllabus.


This Week's Reading Responses 
-----------------------------
.. _reading_response_1:

.. external:: rr_1

  `Reading Response 1 <https://umich.instructure.com/courses/105657/assignments/131308>`_ on Canvas.

.. _reading_response_2:

.. external:: rr_2

  `Reading Response 2 <https://umich.instructure.com/courses/105657/assignments/131313>`_ on Canvas.


.. _problem_set_1:

Problem Set
-----------

**Instructions:** Write the code you want to save in the provided boxes, and click **Run** for each one. That will  *run* your code, so you can see the output, if any, and the result of the tests, if there are any. It will also *save* your code. You should run your code each time you want to save it. You can then load the history of the code you have run and saved. The *last* code you have saved for each problem by the deadline is what will be graded.



.. activecode:: ps_1_1
    :language: python
    :autograde: unittest

    **1.** The variable ``tpa`` currently has the value ``0``. Assign the variable ``tpa`` the value ``6`` .
    ~~~~
    tpa = 0

     
    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(tpa, 6, "Testing that tpa's value is 6.")

    myTests().main()
   

.. activecode:: ps_1_2
    :language: python
    :autograde: unittest

    **2.** Write code to assign the variable ``yb`` to have the same value that variable ``cw`` has. Do not change the first line of code (``cw = "Hello"``). Also, do not "hard code" the result by setting ``yb = "Hello"``. Instead, write code that would work no matter what the current value of ``cw`` is.
    ~~~~
    cw = "Hello"
    yb = 0

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(cw, yb, "Testing that yb has the same value as cw")
           self.assertEqual(cw, "Hello", "Testing that cw's value is 'Hello'.")           

    myTests().main()


.. activecode:: ps_1_3
    :language: python
    :autograde: unittest

    **3.** Write code to print out the type of the variable ``apples_and_oranges``, the type of the variable ``abc``, and the type of the variable ``new_var``. (Use the print command!)
    ~~~~
    apples_and_oranges = """hello, everybody
                               how're you?"""

    abc = 6.75483

    new_var = 824

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn('print', self.getEditorText(), "Testing that 'print' is in the code. (Don't worry about Actual and Expected Values.)")
            self.assertIn('type', self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")           

    myTests().main()
    
.. activecode:: ps_1_4
    :include: addl_functions
    :language: python
    :autograde: unittest

    **4.** There is a function we are giving you called ``square``. It takes one integer and returns the square of that integer value. Write code to assign a variable callex ``xyz`` the value ``5*5`` (five squared). Use the square function, rather than just multiplying with ``*``.
    ~~~~
    xyz = ""
      
    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(type(xyz), type(3), "Checking type of xyz")
            self.assertEqual(xyz, 25, "Checking if xyz is 25")
            self.assertIn('square', self.getEditorText(), "Testing that 'square' is in your code. (Don't worry about Actual and Expected Values.)")

    myTests().main()


.. activecode:: ps_1_5
    :include: addl_functions
    :language: python
    :autograde: unittest

    **5.** Write code to assign the return value of the function call ``square(3)`` to the variable ``new_number``.
    ~~~~
    # Write your code here: 

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(new_number, 9, "Testing that new_number's value is 9")

    myTests().main()


.. activecode:: ps_1_6
    :include: addl_functions
    :language: python

    **6.** Write in a comment what each line of this code does. (You should be very specific! This exercise will train your brain for when you write more complicated code.)
    ~~~~
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

    =====

    print "\n\nThere are no tests for this problem. We have to read your comments.\n"


.. activecode:: ps_1_7
    :include: addl_functions
    :language: python
    :autograde: unittest

    **7.** There are a couple more functions we're giving you in this problem set. One is a function called ``greeting``, which takes any string and adds ``"Hello, "`` in front of it. (You can see examples in the code.) Another one is a function called ``random_digit``, which returns a value of any random integer between 0 and 9 (inclusive). (You can also see examples in the code.)

    Write code that assigns to the variable ``func_var`` the **function** ``greeting`` (without executing the function). 

    Then, write code that assigns to the variable ``new_digit`` the **return value** from executing the function ``random_digit``.

    Then, write code that assigns to the variable ``digit_func`` the **function** ``random_digit`` (without executing the function).
    ~~~~
    # For example
    print greeting("Jackie")
    print greeting("everybody")
    print greeting("sdgadgsal")
     
    # Try running all this code more than once, so you can see how calling the function
    # random_digit works.
    print random_digit()
    print random_digit()

    # Write code that assigns the variables as mentioned in the instructions.


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self): 
            self.assertEqual(type(func_var), type(greeting), "Testing that func_var is same type as greeting")
        def testTwo(self):
            self.assertEqual(type(new_digit), type(1), "Testing that new_digit's value is an integer")
        def testThree(self):
            self.assertEqual(type(digit_func), type(random_digit), "Testing that digit_func is same type as random_digit")

    myTests().main()


.. activecode:: ps_1_8
    :include: addl_functions
    :language: python
    :autograde: unittest

    **8.** Now write code that assigns the variable ``newval`` to hold the **return value** of ``greeting("everyone in class")``.
    ~~~~

  
     

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(newval, greeting("everyone in class"), "Testing that newval was created correctly.")

    myTests().main()
    

.. activecode:: ps_1_9
    :language: python

    **9.** This code causes an error. Why? Write a comment in the code window to explain.
    ~~~~
    another_variable = "?!"
    b = another_variable()



**10.** Here's another complicated expression, using the Turtle framework we talked about. Arrange these sentences in the order they are executed in the following code, like you did in an exercise in Chapter 2 of the textbook. (It may help to think about what specifically is happening in the first four lines of code as well.)

.. sourcecode:: python

     import turtle

     ella = turtle.Turtle()
     x = "hello class".find("o") - 1
     ella.speed = 3


     ella.move(square(x*ella.speed))
  
.. parsonsprob:: ps_1_10

   Order the code fragments in the order in which the Python interpreter would evaluate them, when evaluating that last line of code.

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


.. activecode:: ps_1_11
    :language: python

    **11.** Write a program that uses the turtle module to draw something interesting. It doesn't have to be complicated, but draw something different than we did in the textbook or in class. (Optional but encouraged: post a screenshot of the artistic outcome to the Facebook group, or a short video of the drawing as it is created.) (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting ``.speed(10)`` for the turtle to draw fast, or ``.speed(0)`` for it to draw super fast with no animation.)
    ~~~~
    import turtle


.. external:: ps1_dyu

    **12.** Complete the `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131293>`_ for this week.
    

That's the end of the problem set. In the hidden code below, you will find the definitions of functions square, random_digit, and greeting that were used elsewhere in the problem set. They're hidden because you don't yet need to understand how function definitions work. But if you want a preview, feel free to click on Show/hide code.

.. activecode:: addl_functions
    :nopre:
    :hidecode:

    def square(num):
        return num**2

    def greeting(st):
        st = str(st) # just in case
        return "Hello, " + st

    def random_digit():
        import random
        return random.choice([0,1,2,3,4,5,6,7,8,9])

