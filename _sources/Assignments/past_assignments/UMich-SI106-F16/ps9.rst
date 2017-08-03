:orphan:

..  Copyright (C) Jackie Cohen, Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. highlight:: python
    :linenothreshold: 500

Activities through 11/18
========================

* **Before Monday's class 11/14:**
    * Read :ref:`Class Inheritance <inheritance_chap>` and try all the exercises in the below listed sections.

.. usageassignment::
  :subchapters: Inheritance/intro, Inheritance/inheritVarsAndMethods, Inheritance/OverrideMethods, Inheritance/InvokingSuperMethods,  Inheritance/TamagotchiRevisited
  :assignment_name: Prep 18
  :deadline: 2016-11-14 20:40
  :pct_required: 80
  :points: 50

* **Before Wednesday's class 11/16:**
    * Read :ref:`Testing <test_cases_chap>` and try the exercises in the below listed sections.
    * Read `this overview of Git version control <https://swcarpentry.github.io/git-novice/01-basics/>`_. (This is the first page of a whole lesson on Git. You need only read this page, but you may find the resources interesting!)
    * Read this tutorial on GitHub. (You will not need to create or use a GitHub repository for this course, but these readings will help prepare you for the reading and reading response upcoming, and some later chapters in the Weber book.)
         * `Part I of tutorial <http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1>`_
         * `Part II of tutorial <http://readwrite.com/2013/10/02/github-for-beginners-part-2>`_

.. usageassignment::
  :subchapters: Testing/intro-TestCases, Testing/Testingfunctions, Testing/Testingclasses
  :assignment_name: Prep 19
  :deadline: 2016-11-16 20:40
  :pct_required: 80
  :points: 50

* **Before Sunday 11/20 at 11:59 PM:**
    * Complete all of :ref:`Problem Set 9 <problem_set_9>` and the Demonstrate Your Understanding assignment for this week (linked below), and submit each on Canvas.
    * Complete :ref:`Reading Response 10 <reading_response_10>`.



This Week's Reading Responses
-----------------------------

.. _reading_response_10:

.. external:: rr_10

  `Reading Response 10 <https://umich.instructure.com/courses/105657/assignments/131309>`_ on Canvas.


.. _problem_set_9:

Problem Set
-----------

Go `HERE to see the Problem Set 9 assignment <https://umich.instructure.com/courses/105657/assignments/131301>`_, where you can find the location of the file to download and edit, and where you can submit your Python file for this assignment. 

**Files you will need to have downloaded and saved in the same directory in order to run this problem set:**

* ``506_ps7.py``
* ``sample_diction.txt``
* ``cached_results.txt``

.. note::

    **We do not give points for problem set code that does not run!** Just like in the textbook, we grade your code by running it, and we will not debug your code to get it to run. You should check to be absolutely sure your problem set runs before submitting it and comment out any code that causes an error, as demonstrated in lecture.

.. external:: ps_9_1

    **PROBLEM 1**

    We have provided the following class definition to represent a Photo object (both here, and in your ``106_ps9.py`` file. Take a look at the code, and make sure you understand it. Then, write one line of code, which should create an instance of the class ``Photo`` and save that instance in the variable ``my_photo``. You should write this code so that, after that line of code is executed, ``my_photo.title`` should have the value ``"Photo1"``, ``my_photo.author`` should have the value ``"Ansel Adams"``, and ``my_photo.tags`` should have the value ``['Nature', 'Mist', 'Mountain']``.

    The code you are provided is as follows:

    .. sourcecode:: python

    	class Photo(object): 

		    def __init__(self, title, author, tags):
		        self.title = title
		        self.author = author
		        self.tags = tags


.. external:: ps_9_2

	**PROBLEM 2**

	Now suppose that we want to revise the ``Photo`` class. Instead of passing into the constructor three separate values, the revised constructor (the ``__init__`` function) should take a single dictionary of data as input, and extract the three values from it so that the ``title``, ``author``, and ``tags`` attributes of an instance will hold the correct values (a string, a string, and a list, respectively).

	Define a class called ``Photo2`` with a constructor that does this! (It's important you call it exactly that, because that is what we are testing.) 

	The structure of the dictionary that your ``Photo2`` class should accept is the same as the way the FlickR API returns data about photos. We have provided a sample dictionary representing 1 FlickR photo in the same format that Flickr returns it. We've read that data in from a file (``sample_diction.txt`` contains a nested Python dictionary with information from searching for photos by tags ``"mountains,rivers"`` on Flickr), so there is a sample dictionary that you could pass in as input to your ``Photo2`` class saved in the variable ``sample_diction``.

	Feel free to add some print statements and other investigative code to understand the structure of ``sample_diction``. You may also find it useful to open the file "sample_diction.txt" in a text editor, or copy and paste its contents into ``http://www.jsoneditoronline.org/``. Also see the :ref:`Classes representing data<classes_rep_data>` sub-chapter for an example of writing and reading code like the code you'll need to produce to do this. 

	**NOTE** that in the dictionary that represents a photo from FlickR, there are two keys with plausible associated values to extract for each tag, ``'raw'`` and ``'_content'``; the only difference between their values is capitalization. Please extract the data from the ``'raw'`` key for each tag.

.. external:: ps_9_3
	
	**PROBLEM 3**

	We've provided a definition of a class Student, similar to one you may have seen in lecture. Do not change that code:

	.. sourcecode:: python

		class Student():
		    def __init__(this_Student, name, years_at_umich=1):
		        this_Student.name = name
		        this_Student.years_UM = years_at_umich
		        this_Student.bonus_points = random.randrange(1000)

		    def shout(this_Student, phrase_to_shout):
		        print phrase_to_shout  # print is for ppl!

		    def __str__(this_Student):
		        return "My name is {}, and I've been at UMich for about {} years.".format(this_Student.name,this_Student.years_UM)

		    def year_at_umich(this_Student):
		        return this_Student.years_UM

	You should define a subclass of ``Student``, ``Programming_Student``.

	* The ``Programming_Student`` class should have an instance variable called ``number_programs_written`` whose value gets passed into the Programming_Student constructor after the ``years_at_umich``. The default value for the ``number_programs_written`` instance variable should be 0.

	* The ``Programming_Student`` class should also have a method called ``write_programs``. The ``write_programs`` method accepts an optional parameter called ``progs``, which should be an integer representing the number of programs the Programming_Student will write. Its default value is ``1``. When the write_programs method is called on an instance of Programming_Student, the ``progs`` number should be added to the instance's ``number_programs_written``.

	* The ``Programming_Student`` class should also have a method called ``productivity``. The productivity method should return the average number of programs that the Programming_Student has written per year (that is, divide its ``number_programs_written`` by its ``years_UM``  -- using float division, not integer divison, so you can get a decimal in your answer).

	* When the ``shout`` method is called for the ``Programming_Student`` class, the phrase ``"Also, Python is pretty cool."`` should print after the phrase to shout. You should be calling the parent ``shout`` method to make this happen.

	* The printed representation of an instance of ``Programming_Student`` should look something like ``"My name is Julie, I've been at UMich for about 100 years, and I have written 90 programs while here."``, where **Julie**, **100**, and **90** are in the place of the instance variable values for each instance you create. Override the Student ``__str__`` method for the Programming_Student class to make that happen.


.. external:: ps_9_4

	**PROBLEM 4**

	The function ``get_with_caching`` returns the **text** attribute of a response from an API when you pass in the correct information to make a request.

	Remember, this function takes four parameters as input:
		* A base url
		* A URL parameters dictionary
		* The name of a variable for a dictionary to save cached data in
		* The name of a file where the cached data should be saved in on your computer

	When the function gets what it needs to make a request, it checks in the cache dictionary: 'do I have a key that is the same as the URL that the programmer is asking for?' If it does, it returns data that has *already* been retrieved for that request (and prints out *retrieving data that you had already saved that goes along with the request for URL:* ...). 

	If it does not have that URL as a key, it actually does make a request to the API to get new data, and saves the new data in your cache.

	We have provided you the correct base url and the correct parameters dictionary to make a request to the Flickr API that searches for 50 photos tagged with "sunset". (See the code samples in the textbook Flickr chapter and ``flickr_demo.py`` on Canvas for more explanation of the Flickr API!) 

	We have also provided you with pre-cached data for a request to the Flickr API. Since we have provided you some data already, when you give ``get_with_caching`` the correct input, it will return to you the text output that we already saved! That is what you want to use. It's important that you do this Flickr data work with the data we provide, saved in ``cached_results.txt``, not brand new live data, so that we can accurately grade your work, and you can easily see whether or not your code is working properly!

	In this problem set, the dictionary that should hold all of your cached data is saved in a variable called ``saved_cache``. We have already set that up as well, inside the caching pattern code we have provided.

	**To complete this problem,** you should write an invocation to the ``get_with_caching`` function that retrieves the data about sunset-tagged photos that we have provided you: invoke ``get_with_caching`` with the proper parameters. Then, write code to load the text data that gets returned from ``get_with_caching`` as a Python object. Save that Python object in a variable called ``search_result_diction``.

	You only need to write 2 lines of code to do this (you can do it in 1, but it's probably easier to do it in 2).

	**Before you do that,** you should read all these instructions and try to understand them, and read the code we have provided for you and try to make sure you have a a high-level sense for what it does! What does ``get_with_caching`` return? How would you explain it to someone else? Why should you use a function like this? Talk about this with a classmate or a another friend, and think about a way to explain what you want to be doing in this problem in your own words!

	Also remember that for FlickR data, you have to index the ``.text`` attribute ``[14:-1]`` in order to get nicely formatted JSON data you can use ``json.loads`` on.

.. external:: ps_9_5

	**PROBLEM 5**

	Now, accumulate a list of **photo ids** from the nested dictionary saved in ``search_result_diction``. Save the list of photo ids in a variable called ``photo_ids_list``.


.. external:: ps_9_6

	**PROBLEM 6: OPTIONAL CHALLENGE, building a Flickr tag recommender**

	The rest of this problem set is *optional*. Next week we will provide code that builds on problems 4 and 5 in this problem set to make a tag recommender for Flickr -- a tool that will help answer the question, "If you like photos tagged with this tag, what other tags should you try searching for?"

	As a challenge, we have provided English instructions for building this tag recommender. If you want to try doing this on your own, we encourage you to! 

	We have also provided tests for this part of the problem set, so you can check your work if you choose to do it. **You do not need to pass these tests for Problem 6! This is totally optional.**

	**Tag recommender instructions:**

	* For each of the ids in ``photo_ids_list``, make a request to the flickr API, like you did in problem 4, but instead of using the ``flickr.photos.search`` method that you see in the example of getting tags from FlickR, use the method ``flickr.photos.getInfo``. There is documentation about how to use that method at this URL: ``https://www.flickr.com/services/api/flickr.photos.getInfo.html``, where you can find out what parameters you need. (You will add to the cached data when you do this -- that's OK, it's ok to save more data!) 

	* You should be able to get a Python dictionary from the response for each one of those requests, and use that dictionary you get from each to create a new instance of ``Photo2``. Append each of those new ``Photo2`` instances to a list in a variable called ``photo_instances``.

	* Accumulate a dictionary of counts for the tags on all 50 of the photo instances you have in your list; save the dictionary in a variable ``counts_diction``. 

	* Sort all the tags in descending order, based on how often they were used in the 50 photos. Save the sorted list in a variable called ``sorted_tags``. (Break any ties alphabetically, so that if "alpha" and "bravo" both have a count of 5, "alpha" will appear first in the sort order, and if "alpha" and "Alpha" both have a count of 5, "Alpha" will appear first.)

	* Print, for the user to see, the five tags (other than the searched on tag, **sunset**) that were used most frequently! **HINT 1:** Take a slice of the sorted list. | **HINT 2:** Depending on how you wrote the code to do earlier steps, you'll probably need to skip the first element in the sorted list, or the first two ("sunset" and "Sunset"), so you get the most common tags from your photo search *other than* the one you searched for. ("If you like photos tagged with sunset, you'll like photos tagged with the phrase sunset!" doesn't really make sense!)


.. external:: ps9_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131292>`_ assignment on Canvas.