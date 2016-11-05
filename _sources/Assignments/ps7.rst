:orphan:

..  Copyright (C) Paul Resnick, Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Activities through 11/4
=======================

* **Before class Monday 10/31:**

  * You may want to review the :ref:`Flickr API<flickr_api_chap>` and :ref:`Caching Responses<caching_responses>` from last week (we are not grading this, of course, just a suggestion)
  * We are posting a file on Canvas in Files > Code Samples that shows code to access the Flickr API which is commented thoroughly. You may want to download this, look at it, and try it out!
  * Read the sections listed below from the :ref:`Classes <chap_constructor>` chapter, and try the exercises in those sections.

.. usageassignment::
  :subchapters: Classes/intro-ClassesandObjectstheBasics, Classes/ObjectsRevisited, Classes/UserDefinedClasses, Classes/ImprovingourConstructor, Classes/AddingOtherMethodstoourClass,   Classes/ObjectsasArgumentsandParameters, Classes/ConvertinganObjecttoaString, Classes/InstancesasReturnValues, Classes/sorting_instances, Classes/ClassVariablesInstanceVariables, Classes/ThinkingAboutClasses, Classes/ClassesHoldingData, Classes/Tamagotchi
  :assignment_name: Prep 14
  :deadline: 2016-10-31 21:40
  :pct_required: 80
  :points: 50


* **Before Tuesday 11/1 at 11:59 PM:** 

  * **Reading Response 8 Deadline has been extended to Sunday Nov 6 at 11:59 PM**


* **Before Wednesday's class, 11/2:**

  * Read the sections listed below of :ref:`Inheritance <inheritance_chap>` and try the exercises in those sections.

.. usageassignment::
  :subchapters: Inheritance/intro, Inheritance/inheritVarsAndMethods, Inheritance/OverrideMethods, Inheritance/InvokingSuperMethods, Inheritance/TamagotchiRevisited
  :assignment_name: Prep 15
  :deadline: 2016-11-02 21:40
  :pct_required: 80
  :points: 50


** Wednesday, November 2 at 7 PM is the Second Chance Midterm. More info TBA in Canvas announcement.**


* **Before Sunday 11/6 at 11:59 PM:**

  * Complete all of :ref:`Problem Set 7 <problem_set_7>` and submit the Demonstrate Your Understanding assignment for this week on Canvas (linked in Problem Set below).
  * Complete :ref:`Reading Response 8<reading_response_8>`.

This Week's Reading Responses
-----------------------------

.. _reading_response_8:

.. external:: rr_8

  `Reading Response 8 <https://umich.instructure.com/courses/108426/assignments/139269>`_ on Canvas.

.. _problem_set_7:

Problem Set
-----------

Go `HERE to see the Problem Set 7 assignment <https://umich.instructure.com/courses/108426/assignments/139255>`_, where you can find the files you need to download and edit, and where you can submit files for this assignment. (Note that there are multiple files you will need to download this week!)

Much like the last couple weeks, you'll see abbreviated instructions and provided code for each step in the ``506_ps7.py`` file you download from Canvas. Here on this page, you'll see extended instructions for each problem.

.. note::

	Reminder: we do not debug code when grading, so we cannot grade code that does not run! Make sure your code runs before submitting it -- you should comment out any code that does not.

**Files you will need to have downloaded and saved in the same directory in order to run this problem set:**

* ``506_ps7.py``
* ``sample_diction.txt``
* ``cached_results.txt``

.. external:: ps_7_1

    1. We have provided the following class definition to represent a Photo object (both here, and in your ``506_ps7.py`` file. Take a look at the code, and make sure you understand it. Then, write one line of code, which should create an instance of the class ``Photo`` and save that instance in the variable ``my_photo``. You should write this code so that, after that line of code is executed, ``my_photo.title`` should have the value ``"Photo1"``, ``my_photo.author`` should have the value ``"Ansel Adams"``, and ``my_photo.tags`` should have the value ``['Nature', 'Mist', 'Mountain']``.

    The code you are provided is as follows:

    .. sourcecode:: python

    	class Photo(object): 

		    def __init__(self, title, author, tags):
		        self.title = title
		        self.author = author
		        self.tags = tags

.. external:: ps_7_2

	2. Now suppose that we want to revise the ``Photo`` class. Instead of passing into the constructor three separate values, the revised constructor (the ``__init__`` function) should take a single dictionary of data as input, and extract the three values from it so that the ``title``, ``author``, and ``tags`` attributes of an instance will hold the correct values (a string, a string, and a list, respectively).

	Define a class called ``Photo2`` with a constructor that does this! (It's important you call it exactly that, because that is what we are testing.) 

	The structure of the dictionary that your ``Photo2`` class should accept is the same as the way the FlickR API returns data about photos. We have provided a sample dictionary representing 1 FlickR photo in the same format that Flickr returns it. We've read that data in from a file (``sample_diction.txt`` contains a nested Python dictionary with information from searching for photos by tags ``"mountains,rivers"`` on Flickr), so there is a sample dictionary that you could pass in as input to your ``Photo2`` class saved in the variable ``sample_diction``.

	Feel free to add some print statements and other investigative code to understand the structure of ``sample_diction``. You may also find it useful to open the file "sample_diction.txt" in a text editor, or copy and paste its contents into ``http://www.jsoneditoronline.org/``. Also see the :ref:`Classes representing data<classes_rep_data>` sub-chapter for an example of writing and reading code like the code you'll need to produce to do this. 

	**NOTE** that in the dictionary that represents a photo from FlickR, there are two keys with plausible associated values to extract for each tag, ``'raw'`` and ``'_content'``; the only difference between their values is capitalization. Please extract the data from the ``'raw'`` key for each tag.


.. external:: ps_7_description

	**Your goal for the rest of the problem set is to build a tag recommender for FlickR.** For example: if you like photos tagged "mountains", what other tags would be good for you to look at? In other words, which 5 tags co-occur most frequently with the "mountains" tag on FlickR?

	We will provide tasks here, in English, and space indicated in the problem set file for you to write code that does what we describe. You should use the function definitions we provide in order to write all the rest of the code. Basically, you'll need to translate our English for each step into code in your ``506_ps7.py`` file.

	We have provided a few things to help you with the remainder of this problem set:

	* A bunch of code that can be used to get a response from a REST API and cache it in a file, and/or retrieve data that has already been saved (cached) so that you can process it. This code is almost exactly the same as the code you saw in the Caching Responses subchapter in the textbook, but it has a bunch of annotations to help you understand it, and some small additions to help you with this problem set. The Section 7 caching code handout (you can find this on Canvas) includes questions that may also help you understand it!
	* A file, ``cached_results.txt`` that has data from FlickR which represents a search for 50 photos with the tag "sunset"

	If you run the ``506_ps7.py`` program, you'll see output describing what's happening in the code. We'd suggest that you do this before attempting to go further in the problem set!

	**Do not change the cache file name in the code:** we have provided data in ``cached_results.txt`` for you to process, which is what the tests for this problem set rely on. Because we've already cached data from FlickR for you, everyone should have the same results, since you are all working from the same cached data. That makes it possible for us to grade your work much more easily!

	If you wish to run your tag recommender on live data, you can change the cache file name or delete the cache file from the directory where you run the program. But still, **make sure when you submit your problem set, it is relying on the default cache file name**, ``cached_results.txt``.

	Textbook sections that may help particularly:
	`Caching Responses <https://www.programsinformationpeople.org/runestone/static/506F16/UsingRESTAPIs/cachingResponses.html>`_ ,
	`Getting tags from Flickr <https://www.programsinformationpeople.org/runestone/static/506F16/UsingRESTAPIs/flickr.html>`_


.. external:: ps_7_3

	3. The function ``get_with_caching`` returns the **text** attribute of a response from an API when you pass in the correct information to make a request. Now, you should write code to make a request to Flickr for 50 photos which are tagged with the key "sunset", and write code to load the text data you get back as a Python object. 

	Remember that for FlickR data, you have to index the ``.text`` attribute ``[14:-1]`` in order to get nicely formatted JSON data you can use ``json.loads`` on.

	Save it in a variable ``search_result_diction``.

.. external:: ps_7_4

	4. Now, get a list of photo ids from the nested dictionary. Save it in a variable called ``photo_ids_list``.

	Then, get information from FlickR about each photo id in the list. Create an instance of the ``Photo2`` class you defined earlier in the problem set for each of the photo ids, and accumulate all the instances into a list called ``photo_instances``. 

	To do this, follow these steps:

	(a) Accumulate a list of photo ids from the big nested dictionary that you saved in the ``search_result_diction`` variable into ``photo_ids_list``.

	(b) Make a request to the flickr API, but instead of using the ``flickr.photos.search`` method that you see in the example of getting tags from FlickR, use the method ``flickr.photos.getInfo``. There is documentation about how to use that method at this URL: ``https://www.flickr.com/services/api/flickr.photos.getInfo.html``, where you can find out what extra parameters you need. 

	You should wrap this request in a try/except clause -- what if that photo's been deleted from Flickr? You don't want your whole program to break, you just want to go on to the next one.

	(c) Get a Python dictionary from the response for each request, and pass that dictionary you get from each to a new instance of ``Photo2`` (see problems 1 and 2 and the Classes chapter)

	(d) Accumulate the instance that you create into a list called ``photo_instances``.

	**Note** that this can take quite a long time to run on all 50 photos. You may want to test your process on a small slice of the list (5 photos), and then, once you know it works (if you're getting output from print statements that you expect), then run it on all 50 to see if you pass the tests!


.. external:: ps_7_5

	5. Accumulate frequencies of related tags.

	You started out with data about 50 different photos, including the tags that the photo owners used to describe the photos. They all have the tag 'sunset', since that's the tag we searched for, but some have additional tags, like 'river' and 'nature' and others. Accumulate a dictionary of counts for each of those tags; call the dictionary ``counts_diction``. 

	(See :ref:`Dictionary Accumulation<dictionary_accum_chap>` for reminders/examples. You'll also probably need to do nested data investigation to access the tags in the nested data, just like you practiced during the past couple weeks.)

.. external:: ps_7_6

	6. Sort all the tags in descending order, based on how often they were used in the 50 photos. Save the sorted list in a variable called ``sorted_tags``. 

	Break any ties alphabetically, so that if "alpha" and "bravo" both have a count of 5, "alpha" will appear first in the sort order, and if "alpha" and "Alpha" both have a count of 5, "Alpha" will appear first.

.. external:: ps_7_7

	7. Save the 5 most common tags (*besides* "sunset") in a list called ``most_common_tags``.

	Then print, for the user to see, the five tags (other than the searched on tag, **sunset**) that were used most frequently!

	HINT 1: Take a slice of the sorted list.

	HINT 2: Depending on how you wrote the code to do earlier steps, you'll probably need to skip the first element in the sorted list. That will almost certainly be "sunset", since *all* the photos have that tag.

.. external:: ps_7_end

	You've now created a tag recommender!

	Save your file, *make sure it runs*, and upload it to the Canvas assignment. You should not upload any other files.

.. external:: ps7_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/108426/assignments/139245>`_ assignment on Canvas.
