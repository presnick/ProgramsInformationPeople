..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

String Methods
--------------

The "dot notation" is the way we connect an object to one of its attributes or
to invoke a method on that object. There are a wide variety of methods for string objects.  
Try the following program.

.. activecode:: chp08_upper

    ss = "Hello, World"
    print(ss.upper())

    tt = ss.lower()
    print(tt)


In this example, ``upper`` is a method that can be invoked on any string object 
to create a new string in which all the 
characters are in uppercase.  ``lower`` works in a similar fashion changing all characters in the string
to lowercase.  (The original string ``ss`` remains unchanged.  A new string ``tt`` is created.)

.. _string_methods:

In addition to ``upper`` and ``lower``, the following table provides a summary of some other useful string methods.  There are a few activecode examples that follow so that you can try them out.

==========  ==============      ==================================================================
Method      Parameters          Description
==========  ==============      ==================================================================
upper       none                Returns a string in all uppercase
lower       none                Returns a string in all lowercase

strip       none                Returns a string with the leading and trailing whitespace removed
count       item                Returns the number of occurrences of item
replace     old, new            Replaces all occurrences of old substring with new

find        item                Returns the leftmost index where the substring item is found
rfind       item                Returns the rightmost index where the substring item is found
index       item                Like find except causes a runtime error if item is not found
rindex      item                Like rfind except causes a runtime error if item is not found
split       item                Splits a string into a list based on specified character where it will split string at
==========  ==============      ==================================================================

You should experiment with these
methods so that you understand what they do.  Note once again that the methods that return strings do not
change the original.  You can also consult the `Python documentation for strings <http://docs.python.org/3/library/stdtypes.html#string-methods>`_.

.. activecode:: ch08_methods1

    ss = "    Hello, World    "

    els = ss.count("l")
    print(els)

    print("***"+ss.strip()+"***")

    news = ss.replace("o", "***")
    print(news)


.. activecode:: ch08_methods2


    food = "banana bread"
    print(food.upper())

    print(food.find("e"))
    print(food.find("na"))
    print(food.find("b"))

    print(food.rfind("e"))
    print(food.rfind("na"))
    print(food.rfind("b"))

    print(food.index("e"))


**Check your understanding**

.. mchoice:: test_question8_3_1
   :answer_a: 0
   :answer_b: 2
   :answer_c: 3
   :feedback_a: There are definitely o and p characters.
   :feedback_b: There are 2 o characters but what about p?
   :feedback_c: Yes, add the number of o characters and the number of p characters.
   :correct: c

   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s.count("o") + s.count("p"))

.. mchoice:: test_question8_3_2
   :answer_a: yyyyy
   :answer_b: 55555
   :answer_c: n
   :answer_d: Error, you cannot combine all those things together.
   :feedback_a: Yes, s[1] is y and the index of n is 5, so 5 y characters.  It is important to realize that the index method has precedence over the repetition operator.  Repetition is done last.
   :feedback_b: Close.  5 is not repeated, it is the number of times to repeat.
   :feedback_c: This expression uses the index of n
   :feedback_d: This is fine, the repetition operator used the result of indexing and the index method.
   :correct: a

   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s[1]*s.index("n"))


.. index::
    single: len function
    single: function; len
    single: runtime error
    single: negative index
    single: index; negative
