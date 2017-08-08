:orphan:

..  Copyright (C) Jackie Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Activities through 3/5 (through Spring Break)
=============================================

* **Before class Monday 2/20:**
  
  * Read :ref:`Try/Except <exceptions_chap>`
  * Read :ref:`String Formatting<formatting_chap>`
  * You may find it helpful to read this `External Tutorial on Reading CSV Files <https://thenewcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files>`_
  * Read :ref:`Writing files<write_text_file_chap>` (also note :ref:`Writing CSV files<csv_chap>`)
  * Read :ref:`Python modules <modules_chap>`
  * Make sure to read :ref:`pip module installer <pip_chap>` (and install the ``pip`` module by downloading the `get-pip.py` program and running it with admin permissions -- see Canvas announcement/instructions for help with this if you have any problems!) 
  * Read :ref:`How to Fix Common Problems using your native machine's Python<gotchas_chap>`, which may also be helpful as we move forward.
  * Read :ref:`Fetching data <requests_chap>`

.. usageassignment::
  :subchapters: PythonModules/intro-ModulesandGettingHelp, PythonModules/Therandommodule, Exceptions/intro-exceptions, Exceptions/using-exceptions, StringFormatting/intro-PrintinginPython2.7, StringFormatting/Interpolation, StringFormatting/CSV, Files/WritingTextFiles,  Installation/pip, NativeInterpreterGotchas/FixCommonProblems, Requests/intro, Requests/fetching_a_page, Requests/how_the_Internet_works, Requests/urls, Requests/http, Requests/requests_details
  :assignment_name: Lecture Prep 11
  :deadline: 2017-02-20 17:30
  :pct_required: 75
  :points: 50

* **Before Wednesday's class, 2/22:**

  * Read :ref:`REST APIs<rest_apis_chap>`
  * Check out `this iTunes Search API documentation <https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/>`_ and consider how to use it to make an API request. You don't have to understand it, but you *should* have taken a good look at it.
  * Read `this document about APIs and Caching <https://paper.dropbox.com/doc/Rest-APIs-and-Caching-506W17-draft-GUSnNpkwXNWBaXIQs451y>`_ (it's a draft, but it contains important information)
  

.. usageassignment::
  :subchapters: RESTAPIs/intro, RESTAPIs/RequestURLs, RESTAPIs/DebugURLs, RESTAPIs/jsonlib, RESTAPIs/unicode, RESTAPIs/requestsCookbook
  :assignment_name: Lecture Prep 12
  :deadline: 2017-02-22 18:30
  :pct_required: 75
  :points: 50

* **Before Sunday 2/26 at 11:59 PM:**

  * Complete all of :ref:`Problem Set 6 <problem_set_6>` and the Demonstrate Your Understanding assignment for this week.
  * (If we need to reassess this deadline, we will do so.)

.. _problem_set_6:

Problem Set
-----------

Go `HERE to see the Problem Set 6 assignment <https://umich.instructure.com/courses/150918/assignments/231794>`_, where you can find where to edit and submit files for this assignment.

Note especially for this problem set, since you're getting real live data, we cannot test everything. You'll have to both look at our tests and instructions and examine your output to ensure that you have reasonable results. We will look at your results and output when we grade the problem set. **As always, we do not grade problem sets that do not run.** Make sure you have no syntax errors!

----

The FAA (Federal Aviation Administration) has put out a REST API for accessing current information about US airports. You'll be using it in problems 3-10 of your problem set this week!

.. note::

    Almost all of the exercises in the problem set build on one another, either in terms of the skills you practice in them or the literal code you write for them! You can (and in some cases must) use code you wrote in earlier exercises in later ones. If you keep this in mind, this problem set may be even easier for you.

    All detailed instructions for this problem set can be found in the ``506W17_ps6.py`` file you download from Canvas! Here is just a very high-level outline of all the problems.

.. external:: ps_6_01

    1. **PROBLEM 1** deals with opening JSON files and using file operations and ``json`` module functions.

.. external:: ps_6_02

    2. **PROBLEM 2** also addresses ``json`` module functions and Python file operations -- but this time writing files!

.. external:: ps_6_03

    **Interlude:** The rest of the exercises deal with the Federal Aviation Administration API and using processes to get data from an API.

    First, point your web browser to the following URL: ``http://services.faa.gov/airport/status/DTW?format=json``

    The text that is shown in your browser is a string formatted in a JSON way that lives at that particular URL place on the internet. It can easily be converted into a python dictionary and processed with the understand, extract, repeat method for nested data. 

    The exercises below guide you through the process of writing python code that uses this RESTful API to extract information about some airports. Pointing your browser to this link is not graded. But you should do it, because it may help provide you with understanding for the remainder of the problem set!

.. external:: ps_6_04

    **PROBLEM 3:** *Encoding query parameters in a URL, making a request, and dealing with a response object*

    See detailed instructions in your file!

    You will save the response that will be returned when the ``request.get`` method is called properly to a variable called ``airport_response``. So, after this code is executed, ``airport_response`` should contain a *response object* from the FAA API.

.. external:: ps_6_05

    **PROBLEM 4:** *Grabbing data off the web and making it usable in a Python program, beginning work with a complex dictionary data structure*

    See detailed instructions in your file!
    
    
.. external:: ps_6_06

    **PROBLEM 5:** *Extracting relevant information from a dictionary*

    Now you should have a JSON-formatted Python dictionary with a bunch of data from the FAA about the airport with code **DTW**.  

    Now, going back to the skills you learned in the Nested Data chapter: From the airport data dictionary, extract the airport code (e.g. ``DTW``), the ``reason`` field from within the ``status``, the current temperature, and the last time the data was updated.

    To see what you saved in these variables, you may want to run code like:

    .. sourcecode:: python

        print airport_code
        print status_reason
        print current_temp
        print recent_update

    See further detailed instructions in your file!


.. external:: ps_6_07

    **PROBLEM 6:** *Generalizing your code*

    At this point, you'll consider the code you've written so far in your file, and make it generalizable. Which means... FUNCTIONS.

    *See further detailed instructions in your file* for writing a function called ``get_airport`` which takes an airport code as input e.g. ``DTW`` or ``PHX``, and returns a Python dictionary with data about that airport.

.. external:: ps_6_08

    **PROBLEM 7:** *More code generalization*

    Now, write another function called ``extract_airport_data()`` that accepts an airport code string as input, like ``"LAX"``, and returns a tuple: of the airport name, status reason, current temp, and recent update. This function should call the ``get_airport()`` function.

    See instructions in your file!

.. external:: ps_6_09

    **PROBLEM 8:** *Examples of using your newly defined functions*

    In this problem, you'r using the code you just wrote in earlier problems! See detailed instructions in your file. 


.. external:: ps_6_10

    **PROBLEM 9:** *Dealing with real live data and error handling*

    We've provided a list of airport codes in the variable ``possible_airports``, in the problem set code file. But not all of them are valid airport codes! So you'll need to use a ``try/except`` block.

    See detailed instructions in the file.

.. external:: ps_6_11

    **PROBLEM 10:** *Writing data to a CSV file*

    See detailed instructions in your file!

    Your resulting CSV file should have at least 5 lines: 4 lines for real airport data, and 1 line for the column headers. The content of each cell should have well-formatted data: no extra parentheses, just the specific value that corresponds to that header!

    **Make sure the CSV file you create is called airport_temps.csv. We will run tests on the CSV files post-submission, and we depend on the name of the file being correct.**

    Open the document in Excel or in Google Drive to make sure that it is properly formatted.

.. external:: ps6_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/150918/assignments/231781>`_ assignment on Canvas.

