..  Copyright (C)  Paul Resnick, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _interpolation_chap:

String Interpolation
====================

Until now, we have created strings with variable content using the + operator to concatenate partial strings together. That works, but it's very hard for people to read or debug a code line that includes variable names and strings and complex expressions. Consider the following: 

.. activecode:: interpolation_1

   name = "Rodney Dangerfield"
   score = -1  # No respect!
   print "Hello " + name + ". Your score is " + str(score)

Or perhaps more realistically:
 
.. activecode:: interpolation_2
 
   scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
   for (name, score) in scores:
       print "Hello " + name + ". Your score is " + str(score)

In this section, you will learn to write that in a more readable way:

.. activecode:: interpolation_3
 
   scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
   for (name, score) in scores:
       print "Hello {}. Your score is {}.".format(name, score)


``.format()`` is a special string method that allows you to *interpolate* values into strings -- basically, insert values into strings and automatically make them work, as you see above.

There are a few ways to use the ``.format`` method.

The first, and most common, way, is to insert ``{}`` curly braces into strings at the location where you want to interpolate (stick in) values into the string. Then call the ``.format`` method on the string, and pass to the ``format`` method the items you want to put into the string, separated by commas. 

It is important to pass arguments to the ``format`` method in the correct order, because they are matched *positionally* into the ``{}`` places for interpolation where there is more than one.

It is also important that you give ``format`` the same amount of arguments as there are ``{}`` waiting for interpolation in the string. If you have ``{}`` in a string that you do not pass arguments for, you may not get an error, but you will see a weird ``undefined`` value you probably did not intend suddenly inserted into your string. You can see an example below.

For example,

.. activecode:: interpolation_4
 
   name = "Sally"
   greeting = "Nice to meet you"
   s = "Hello, {}. {}."

   print s.format(name,greeting) # will print Hello, Sally. Nice to meet you.

   print s.format(greeting,name) # will print Hello, Nice to meet you. Sally. 

   print s.format(name) # 2 {}s, only one interpolation item! Not ideal.


Another option is to specifically refer to keywords (think back to keyword arguments for functions!) for interpolation values, like below.

.. activecode:: interpolation_4a
 
   names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
   for name, scores in names_scores:
       print "The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2])


Sometimes, you may want to use the ``.format`` method to insert the same value into a string multiple times. You can do this by simply passing the same string into the format method, assuming you have included ``{}`` s in the string everywhere you want to interpolate them. But you can also use positional passing references to do this! The order in which you pass arguments into the ``format`` method matters: the first one is argument ``0``, the second is argument ``1``, and so on.

For example,

.. activecode:: interpolation_5
 
   # this works
   names = ["Jack","Jill","Mary"]
   for n in names:
       print "'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello")

   # but this also works!
   names = ["Jack","Jill","Mary"]
   for n in names:
       print "'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello")


You can imagine some ways in which this method for string interpolation is very useful for complex programs and programs where you want to compile data together and print it out, or write it to a file. A set of strings might all be the same except for one varying piece of data, so for instance, you can use code like some you see in this section to generate all of those strings with one for loop that's neat and easy to read! 

Overall, using ``.format`` for string interpolation is much neater and easier to edit later on than just using string concatenation.
