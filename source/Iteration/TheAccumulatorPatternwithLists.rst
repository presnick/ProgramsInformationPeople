..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _list_accum:

The Accumulator Pattern with Lists
----------------------------------

We can also accumulate values into a list rather than accumulating a single numeric value.
Consider, for example, the following program which transforms a list into a new list by adding one to each of the values.

.. activecode:: iter_accumlist1

   nums = [3, 5, 8]
   accum = []
   for w in nums:
      x = w + 1
      accum = accum.append(x)
   print accum

Here, we **initialize** the accumulator variable to be an empty list, on line 2.
We **iterate** through the sequence (line 3). On each iteration we transform the item by adding 1 to it (line 4).
The **update** step appends the new item to the list which is stored in the accumulator variable (line 5).
At the end, we have accumulated a new list of the same length as the original, but with each item transformed into a new item. This is called a mapping operation, and we will revisit it in a :ref:`later chapter <map_chap>`.


**Check your understanding**

.. mchoicemf:: test_question9_16_1
   :answer_a: [4,2,8,6,5]
   :answer_b: [4,2,8,6,5,5]
   :answer_c: [9,7,13,11,10]
   :answer_d: Error, you cannot concatenate inside an append.
   :correct: c
   :feedback_a: 5 is added to each item before the append is peformed.
   :feedback_b: There are too many items in this list.  Only 5 append operations are performed.
   :feedback_c: Yes, the for loop processes each item of the list.  5 is added before it is appended to blist.
   :feedback_d: 5 is added to each item before the append operation is performed.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4,2,8,6,5]
     blist = [ ]
     for item in alist:
        blist.append(item+5)
     print blist


