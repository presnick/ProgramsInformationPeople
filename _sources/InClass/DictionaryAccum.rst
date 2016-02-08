..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Dictionary Accumulation In Class Code Samples
=============================================

.. activecode:: session8_0

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"

    ######Count occurrences of letter i###########
    icount = 0
    for letter in str2:
       if letter == 'i':
          icount += 1
    print icount

    icount = 0
    for letter in "team":
       if letter == 'i':
          icount += 1
    print icount

.. activecode:: session8_1

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"

    ######Method 1: a list of counters ###########
    vcounts= [0,0,0,0,0]
    vowels = ['a', 'e', 'i', 'o', 'uu']
    for letter in str2:
       if letter in vowels:
          vcounts[vowels.index(letter)] += 1
    for vowel in vowels:
       print vowel + ": " + str(vcounts[vowels.index(vowel)])

.. activecode:: session8_2

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"
    vowels = ['a', 'e', 'i', 'o', 'uu']

    ######Method 2: a dictionary of counters ########
    # initialize the accumulators
    d = {}
    d['a'] = 0
    d['e'] = 0
    d['i'] = 0
    d['o'] = 0
    d['u'] = 0
    # alternative way to initialize
    d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    # one more way to initialize
    d = {}
    for vowel in vowels:
       d[vowel] = 0

    for letter in str2:
       if letter in vowels:
          d[letter] += 1

    for vowel in vowels:
       print vowel + ": " + str(d[vowel])

.. activecode:: session8_3

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"
    vowels = ['a', 'e', 'i', 'o', 'uu']

    ######Method 2: a dictionary of counters ########
    # initialize the accumulators
    d = {}
    d['a'] = 0
    d['e'] = 0
    d['i'] = 0
    d['o'] = 0
    d['u'] = 0
    # alternative way to initialize
    d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    # one more way to initialize
    d = {}
    for vowel in vowels:
       d[vowel] = 0

    for letter in str2:
       if letter in vowels:
          d[letter] += 1

    for vowel in vowels:
       print vowel + ": " + str(d[vowel])

.. activecode:: session8_4

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"
    vowels = ['a', 'e', 'i', 'o', 'uu']

    ######Method 3: create counters as needed######
    d = {}
    for letter in str2:
       if letter in d:
          d[letter] += 1
       else:
          d[letter] = 1

    for vowel in vowels:
       if vowel in d:
          print vowel + ": " + str(d[vowel])
    print d

.. activecode:: session8_5

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"
    vowels = ['a', 'e', 'i', 'o', 'uu']

    #######Accumulating from a dictionary: how many vowels?#######
    d = {}
    for letter in str2:
       if letter in d:
          d[letter] += 1
       else:
          d[letter] = 1

    tot = 0
    for letter in d.keys():
       if letter in vowels:
          tot += d[letter]
    print tot

.. activecode:: session8_6

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"
    vowels = ['a', 'e', 'i', 'o', 'uu']

    ####### Scrabble values: combining two dictionaries######
    d = {}
    for letter in str2:
       if letter in d:
          d[letter] += 1
       else:
          d[letter] = 1

    letter_values = {' ': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'uu':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

    tot = 0
    for letter in d: # same as iterating over d.keys()
       tot = tot + letter_values[letter] * d[letter]

    print tot

.. activecode:: session8_7

    mystr = 'By a route obscure and lonely, haunted by ill angels only'
    str2 = "a brain train"
    vowels = ['a', 'e', 'i', 'o', 'uu']

    ####### which letter occurs most frequently? ########
    d = {}
    for letter in str2:
       if letter in d:
          d[letter] += 1
       else:
          d[letter] = 1

    letters = d.keys()
    best_letter_so_far = letters[0]
    for let in letters:
       if d[let] > d[best_letter_so_far]:
          best_letter_so_far = let

    print best_letter_so_far + " has the highest value, " + str(d[best_letter_so_far])
