..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Writing Test Cases
==================

It is a good idea to write one or more test cases for each function, method, or class that you define. We will start with functions, and then move on to classes.


Testing functions
-----------------

A function defines an operation that can be performed. If the function takes one or more parameters, it is supposed to work properly on a variety of possible inputs. Each test case will check whether the function works properly on **one set of possible inputs**. 

A useful function will do some combination of three things, given its input parameters:

* Return a value. For these, you will write **return value tests**.
* Modify the contents of some mutable object, like a list or dictionary. For these you will write **side effect tests**.
* Print something or write something to a file. Tests of whether a function generates the right printed output are beyond the scope of this testing framework; you won't write these tests.

Testing whether a function returns the correct value is the easiest test case to define. You simply check whether the result of invoking the function on a particular input produces the particular output that you expect. If f is your function, and you think that it should transform inputs x and y into output z, then you could write a test as ``self.assertEqual(f(x, y), z)``. Or, to give a more concrete example, if you have a function ``square``, you could have a test case ``self.assertEqual(square(3), 9)``. Call this a **return value test**.

To test whether a function makes correct changes to a mutable object, you will need more than one line of code. You will first set the mutable object to some value, then run the function, then check whether the object has the expected value. Call this a **side effect test** because you are checking to see whether the function invocation has had the correct side effect on the mutable object.

An example follows, testing the ``update_counts`` function. This function takes a string called ``letters`` and updates the counts in ``counts_diction`` that are associated with each character in the string. To do a side effect test, we first create a dictionary with initial counts for some letters. Then we invoke the function. Then we assert that the dictionary has the correct counts for some letters (those correct counts are computed manually when we write the test. We have to know what the correct answer should be in order to write a test). You can think of it like writing a small exam for your code -- we would not give you an exam without knowing the answers ourselves.

.. activecode:: simple_test_3

    def square(x):
        return x*x

    def update_counts(letters, counts_dict):
        for c in letters:
            if c in counts_dict:
                counts_dict[c] = counts_dict[c] + 1
            else:
                counts_dict[c] = 1

    from unittest.gui import TestCaseGui # because we're in the textbook interface

    class myTests(TestCaseGui):

        def test_return_value(self):
            self.assertEqual(square(3), 9)

        def test_side_effect(self):
            counts_dict = {'a': 3, 'b': 2}
            update_counts("aaab", counts_dict)
            # 3 more occurrences of a, so 6 in all
            self.assertEqual(counts_dict['a'], 6)
            # 1 more occurrence of b, so 3 in all
            self.assertEqual(counts_dict['b'], 3)

    myTests().main()

.. sourcecode:: python



Because each test checks whether a function works properly on specific inputs, the test cases will never be complete: in principle, a function might work properly on all the inputs that are tested in the test cases, but still not work properly on some other inputs. That's where the art of defining test cases comes in: you try to find specific inputs that are representative of all the important kinds of inputs that might ever be passed to the function.

The first test case that you define for a function should be an "easy" case, one that is prototypical of the kinds of inputs the function is supposed to handle. Additional test cases should handle "extreme" or unusual inputs, sometimes called **edge cases**. For example, if you are defining the "square" function, the first, easy case, might be an input like 3. Additional extreme or unusual inputs around which you create test cases might be a negative number, 0, a floating point number, and a very, very large number. 

If you were writing tests on a function that takes any list as input and returns a value that is a computation on that input list, you might test the function's return value when it is invoked on an empty list, a list with only one value, a list with an element that is a list itself, a list that has many elements...

