
:orphan:

..  Copyright (C) Paul Resnick, Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500

Lecture 11: Waiver Challenge Exercises
======================================

.. _lecture_11_waiver:

If you have submitted the :ref:`Unix Exercises for Problem Set 5 <problem_set_5_unix>` before this course, you may skip lecture. Please write in this box that you have done so to confirm that you have!

.. activecode:: lec11_1

    Write that you assert you have submitted the Unix Exercises on Canvas.
    ~~~~
    # In a comment. 

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertIn(" ",self.getEditorText())

    
    

However, we *strongly* suggest you attend lecture this time. It will be extremely important for the rest of the semester.