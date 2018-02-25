..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Extra Exercises
---------------


.. activecode:: interpolation_6
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: StringFormatting/Interpolation
   :tags: StringFormatting/Interpolation.rst

   **1.** Fill in the variable t so that it prints out: ``You have $4.99 in your pocket``

   ~~~~

   pocketmoney = 4.99
   t = # fill in something here
   newstring = t.format(pocketmoney)
   print(newstring)

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(newstring, "You have $4.99 in your pocket", "Testing that newstring is assigned to correct value.")

   myTests().main()


.. activecode:: interpolation_8
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: StringFormatting/Interpolation
   :tags: StringFormatting/Interpolation.rst

   **2.** Fill in the missing code after the ``vals =`` on the first line, so that it prints out: ``v1, v2 are the 2 items in the list``

   ~~~~

   vals =                            
   templ = "{}, {} are the {} items in the list"
   print(templ.format(vals[0], vals[1], len(vals)))

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(templ.format(vals[0], vals[1], len(vals)), "v1, v2 are the 2 items in the list", "Testing that the string displayed is assigned to correct value.")

   myTests().main()


.. activecode:: interpolation_9
   :language: python
   :autograde: unittest
   :chatcodes:
   :hidecode:
   :practice: T
   :topics: StringFormatting/Interpolation
   :tags: StringFormatting/Interpolation.rst

   **3.** Fill in the missing code after the ``val =`` on the first line, so that it prints out: ``Hey, you, you there!``

   ~~~~

   val = 
   temp = "Hey, {0}, {0} there!".format(val)
   print(temp)

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(temp, "Hey, you, you there!", "Testing that temp is assigned to correct value.")

   myTests().main()
