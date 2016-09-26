..  Copyright (C)  Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Indefinite Iteration In Class Code Samples
==========================================

.. activecode:: session10_free
    
    # This is provided for your convenience. You can write any code here.


.. activecode:: session10_0

    sum = 0
    while sum <= 10:
        n = int(raw_input("Please enter a number to add to the sum. When you reach a sum larger than ten, the total sum will print out. Your number: "))
        sum = sum + n
    print sum


.. activecode:: session10_2

    all_nums_entered = []
    while len(all_nums_entered) < 10:
        n = int(raw_input("Please enter a number to add to the list of numbers: "))
        all_nums_entered.append(n)

    print "You entered 10 numbers! Here they are: "
    for num in all_nums_entered:
        print num


Listener loop pattern, example

.. activecode:: session10_first

    theSum = 0
    x = -1
    while x != 0:
        x = int(raw_input("Next number to add up (enter 0 if you want to stop): "))
        theSum = theSum + x

    print theSum



The flag pattern, examples

.. activecode:: session10_3

    # example of the flag pattern

    x = True

    while x:
        entered = int(raw_input("Enter a number: "))
        print entered
        if entered % 2 == 0:
            x = False
            # Any code under here will execute
            print "Sorry, you entered an even number. The loop is over now!"


    # This is a flag for whether an even number has been entered
    # Effectively: enter odd numbers, loop will quit, using the flag pattern, when you enter something else
    # And if you don't enter a number, you'll get an error


.. activecode:: session10_4

    # another example of the flag pattern

    fl = True

    special_letters = "aeiouy"

    while fl:
        entered = raw_input("Enter a single letter: ")
        if entered in special_letters:
            fl = False
            print "You guessed one of the special letters. You guessed:", entered
            print "The special letters were: "
            for ch in special_letters:
                print ch


Control flow structures with while loops

.. activecode:: session10_5

    # Code to accumulate a list of odd numbers that the user enters
    # And stop when the user types 0

    n = 2
    odd_nums_lst = []
    while n != 0:
        n = int(raw_input("Enter a number. Enter 0 to quit:"))
        if n % 2 == 0:
            continue
        odd_nums_lst.append(n)

    print "List of odd numbers you entered:", odd_nums_lst


.. activecode:: session10_6

    fl = True

    special_letters = "aeiouy"

    while fl:
        entered = raw_input("Enter a single letter: ")

        if entered == "quit":
            break
        elif len(entered) > 1:
            print "You broke the rules! Try again."
            continue
        elif entered in special_letters:
            fl = False
            print "You guessed one of the special letters. You guessed:", entered
            print "The special letters were:"
            for ch in special_letters:
                print ch


Fix an error in the listener loop pattern:

.. activecode:: session10_1

    print "Enter even numbers. When you enter anything that is not an even number, the loop will stop."

    # This code as is will give you an error.
    # What line of code should you add to keep you from getting an error?

    while first_num % 2 == 0:
        first_num = int(raw_input("Enter an even number: "))

    print "all done!"