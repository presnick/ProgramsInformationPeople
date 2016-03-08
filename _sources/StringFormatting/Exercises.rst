..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Exercises
---------
  
1. Fill in the variable t so that it it prints out: ``You have $4.99 in your pocket``

.. activecode:: interpolation_6

   pocketmoney = 4.99
   t =
   newstring = t.format(pocketmoney)
   print newstring
   
   
2. Fill in the missing code after the vals = on the first line, so that it prints out: ``v1, v2 are the 2 items in the list``

.. activecode:: interpolation_8

   vals =                            
   templ = "{}, {} are the {} items in the list"
   print templ.format(vals[0], vals[1], len(vals))


3. Fill in the missing code after the ``val =`` on the first line, so that it prints out: ``Hey, you, you there!``

.. activecode:: interpolation_9

   val = 
   temp = "Hey, {0}, {0} there!".format(val)
   print temp
