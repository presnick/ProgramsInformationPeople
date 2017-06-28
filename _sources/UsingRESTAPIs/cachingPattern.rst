..  Copyright (C)  Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _caching_responses:

More about Caching Response Content
===================================

Now that you've seen a bunch of code that will rely on a caching pattern to get data from an API, we'll break it down and examine more closely what it does. 

Your goal as you look at this code should be to try to understand its structure, and understand how you could write similar code that requests and caches data from a different API, and/or how you could add a function that accesses data from another API to the same program.

When you begin writing a program that will use caching for expensive operations that get data, the first thing you need to do, if you follow the pattern we're using in this book, is set up your cache.

You'll need to:

* Decide what the file that holds your cached data will be called, and save that in a variable. That variable will be a *global* variable for the whole file. (We use ``CACHE_FNAME``.)

* Try to open a file saved as that name.

* Try to read the contents of that file into a string.

* Try to load the data in the contents of that file into a Python object, and save that data in a variable (we use ``CACHE_DICTION``), which will be global for the entire program, so that you can access the cached data anytime later.

* If any one of those things doesn't work, create a variable (``CACHE_DICTION``) to hold the data you'll be caching during the program. 

During the program, you'll add key-value pairs to it... and each time, you'll dump the dictionary to a JSON-formatted string and save that string to a file with the ``CACHE_FNAME`` name.

This code does that:

.. sourcecode::

	CACHE_FNAME = 'cache_file_name.json' 
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    except:
        CACHE_DICTION = {} 


.. note::

	The reason you see the variables CACHE_FNAME and CACHE_DICTION in all caps is because it's convention to use all caps for variable names that are intended to be global variables in a program, which may be used throughout the program.

	Paying attention to stylistic conventions in programming like this is helpful, not because it changes how the code works in any particular way, but because it will make it easier for other programmers to read your code. And knowing these conventions will make it easier for you to understand others' code!

It's important to understand your end goal with this pattern of caching responses. 

A cache file made with a program like this will eventually contain a JSON-formatted string which represents data from a big, complicated Python dictionary. This dictionary's keys will be strings, each of which represent a request. For example, a string that represents "a request for data about 50 photos tagged with the word 'mountains'". The value corresponding to that key will be a dictionary or list that comes from making specifically that request (e.g. a request for data about 50 photos on Flickr tagged with the word 'mountains').



