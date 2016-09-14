:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Lecture 3 Exercises
===================

.. activecode:: lec3_1

   The following code has a bunch of errors. Try to fix them, so the code will run! As you do so, examine the error messages carefully: why are they happening? Each time you fix an error in a line of code, think about an explanation: what was wrong with it? How did you fix it? (If you're doing this on paper, you can just make notes about what errors there are and how you could fix them. 

   This is an exercise in thought and debugging. (Note that it may be surprising which errors Python gets caught at first -- when you fix one, you'll find another, which is exactly what happens when you make errors by accident!)
   ~~~~
   x = len("hello")
   print x()

   print len()

   b = y

   f = len
   print f("hi")

   print len("sixteen"

   print len - 6
   m = len("seven") + 4
   n = m + " letters!"

   =====
   print "============="
   print "\n No tests; if the code runs without error messages, you've done the right thing!\n"


.. activecode:: lec3_2

   Try to write code to draw a triangle with the ``turtle`` module. (If you have time/want to try, attempt some more fun shapes: a star? A heart? What about a small square shape inside a larger square shape?)
   ~~~~

   =====
   print "============="
   print "\nNo tests for turtles.\n"