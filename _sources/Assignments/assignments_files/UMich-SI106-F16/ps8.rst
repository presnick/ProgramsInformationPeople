:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. highlight:: python
    :linenothreshold: 500


Activities through 11/11
========================

* **Before Monday's class 11/7:**
    * Read :ref:`Python modules <modules_chap>`, and if you haven't already, make sure to read about the :ref:`pip module installer <pip_chap>`
    * Read :ref:`Try/Except <exceptions_chap>` and :ref:`String Formatting<formatting_chap>`
    * You may find it helpful to read this `External Tutorial on Reading CSV Files <https://thenewcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files>`_
    * Read :ref:`Writing files<write_text_file_chap>` (also note :ref:`Writing CSV files<csv_chap>`)
    * Read :ref:`Using REST APIs<using_RESTAPIs_chap>`
    * We suggest you read :ref:`How to Fix Common Problems with Python Interpreter<gotchas_chap>`, which may also be helpful as we move forward. (Not graded, but very useful.)
    * You may want to review :ref:`REST APIs<rest_apis_chap>` (not graded this week, just a suggestion)

.. usageassignment::
  :subchapters: PythonModules/intro-ModulesandGettingHelp, PythonModules/Therandommodule, Installation/pip, Exceptions/intro-exceptions, Exceptions/using-exceptions, StringFormatting/intro-PrintinginPython2.7, StringFormatting/Interpolation, StringFormatting/CSV, Files/WritingTextFiles, UsingRESTAPIs/cachingResponses, UsingRESTAPIs/flickr
  :assignment_name: Prep 16
  :deadline: 2016-11-07 20:40
  :pct_required: 80
  :points: 50

* Note that your reading responses will from now onbe due on **Sunday nights**, at the same time as your Problem Sets. Of course, you can always turn them in early!
    
* **Before Wednesday's class, 11/9:**
    * We will post a file on Canvas in Files > Code Samples that shows code to access the Flickr API, which is commented thoroughly. You may want to download this, look at it, and try it out! (This goes back to the information from the :ref:`Using REST APIs chapter<using_RESTAPIs_chap>` you read for Monday.)
    * Read the sections listed below from the :ref:`Classes<chap_constructor>` chapter, and try the exercises in those sections.

.. usageassignment::
  :subchapters: Classes/intro-ClassesandObjectstheBasics, Classes/ObjectsRevisited, Classes/UserDefinedClasses, Classes/ImprovingourConstructor, Classes/AddingOtherMethodstoourClass,   Classes/ObjectsasArgumentsandParameters, Classes/ConvertinganObjecttoaString, Classes/InstancesasReturnValues, Classes/sorting_instances, Classes/ClassVariablesInstanceVariables, Classes/ThinkingAboutClasses, Classes/ClassesHoldingData, Classes/Tamagotchi
  :assignment_name: Prep 17
  :deadline: 2016-11-09 20:40
  :pct_required: 80
  :points: 50


* **Before Sunday 11/13 at 11:59 PM:**

  * Complete all of :ref:`Problem Set 8 <problem_set_8>` and the Demonstrate Your Understanding assignment for this week (linked below), and submit each on Canvas.
  * Complete :ref:`Reading Response 9<reading_response_9>`.


This Week's Reading Responses
-----------------------------

.. _reading_response_9:

.. external:: rr_9

  `Reading Response 9 <https://umich.instructure.com/courses/105657/assignments/131320>`_ on Canvas.


.. _problem_set_8:

Problem Set
-----------

Go `HERE to see the Problem Set 8 assignment <https://umich.instructure.com/courses/105657/assignments/131300>`_, where you can find the location of the file to download and edit, where you can submit your Python file for this assignment.

You'll see very abbreviated instructions for each step, inside the file you download from Canvas. Here on this page, you'll see extended instructions for each step to complete the problem set.

Note especially for this problem set, since you're getting real live data, we cannot test everything. You'll have to both look at our tests and examine your output to ensure that you have the correct results! (We will look at your results and output when we grade the problem set.)

----

The FAA (Federal Aviation Administration) has put out a REST API for accessing current information about US airports. You'll be using it in the following exercises.

.. note::

    Almost all of the following exercises build on one another. You can use code you wrote in earlier exercises in later ones. If you keep this in mind, this problem set'll be even easier for you!

    You should also note that this problem set goes very step-by-step. One little piece at a time, you'll build up to Problem 6, where you put everything together that you've done up to that point.

    In problems 6 and 7, you define functions. Remember: you should only define each function once. Then, after defining them, invoke them!


.. external:: ps_8_start

    1. Point your web browser to the following URL: ``http://services.faa.gov/airport/status/DTW?format=json``

    The text that is shown in your browser is a JSON-formatted dictionary. It can easily be converted into a python dictionary and processed in a manner similar to what we have done with the Facebook feed previously. The exercise below guides you through the process of writing python code that uses this RESTful API to extract information about some airports. Pointing your browser to this link is not graded. But you should do it, because it'll provide you with understanding for the remainder of the problem set.

.. external:: ps_8_01

    **PROBLEM 1: Encoding query parameters in a URL**

    Manually create the dictionary you will need to pass to the params argument when you make a request. The key in the dictionary should be ``'format'``, and its value should be ``'json'``, since this is the only parameter required by the FAA REST API. You could discover this via reading their documentation, but in this case, we're just telling you so. 

    Save the dictionary you create in a variable called url_parameters. You should do this in 3 or fewer lines of code (it can also be done in 1 line!).

.. external:: ps_8_02
    
    **PROBLEM 2: Making a request and saving a response object**

    Next, write the whole assignment statement to do the following:
    - make a request to the base url for the FAA api
    - concatenate the airport code string ``"DTW"`` to the base url, 
    - and pass that as well as the ``url_parameters`` dictionary you already created to the ``requests.get`` method. 

    We've provided a bit of code in the file for you to use as you do this:

    .. sourcecode:: python

        baseurl = 'http://services.faa.gov/airport/status/'
        airport = 'DTW'

    Save the response that will be returned when the ``request.get`` method is called properly to a variable called ``airport_response``. (We're doing this small step by small step.) So, after this code is executed, ``airport_response`` should contain a *response object* from the FAA API.

.. external:: ps_8_03

    **PROBLEM 3: Grabbing data off the web**

    Put the request you made above in a proper try/except clause. If it doesn't work, your code should print out ``That didn't work``. 

    If the request is successful, your code should use the ``.json()`` method on the response you get back to turn the data into one big Python dictionary. Save the Python dictionary in the variable ``airport_data``.

    If you're wondering what you got back, you can use the ``pretty`` function we provided for you in the code file like so: ``print pretty(airport_data)``. This will show you an easier-to-read version of the data you got. 

    Note that you can't do anything with the result of an invocation of the ``pretty`` function, it is just for you to look at data and read it easily. Print is for people, and so is ``pretty`` -- the result of that is mostly useless to your program.

.. external:: ps_8_04

    **PROBLEM 4: Extracting relevant information from a dictionary**

    Now you have a JSON-formatted Python dictionary with a bunch of data from the FAA about the airport with code **DTW**.  

    Remember how you had to concatenate the "DTW" string to the base url for the API, and then add the parameters, to make a request to this API!

    Now, going back to the skills you learned in the Nested Data chapter:

    From the airport data dictionary, extract the airport code (e.g. ``DTW``), the ``reason`` field from within the ``status``, the current temperature, and the last time the data was updated.

    Save these pieces of info in variables called, respectively: ``airport_code``, ``status_reason``, ``current_temp``, ``recent_update``.

    To see what you saved in these variables, you may want to run code like:

    .. sourcecode:: python

        print airport_code
        print status_reason
        print current_temp
        print recent_update


.. external:: ps_8_05

    **PROBLEM 5: Generalizing your code**

    At this point, you'll consider the code you've written so far in your file, and make it generalizable. Which means... FUNCTIONS.

    Define a function called ``get_airport()`` that acPROBLcepts a three-letter airport code string as input, and returns a Python dictionary (like the one you saved in ``airport_data`` above) with data about that airport. 

    This function should work no matter where it is called, with just the input of an airport code like "DTW" or "PDX"! It should *not* depend upon global variables. (So, if you input ``"DTW"`` into your ``get_airport`` function, you should get a different result returned than if you invoke the function with the input ``"LAX"``, and so on.

    You can assume that the requests module is available in your file, though (you do not have to import it again in your function definition of ``get_airport``).

.. external:: ps_8_06

    **PROBLEM 6: More code generalization**

    Now, write another function called ``extract_airport_data()`` that accepts an airport code string as input, like ``"LAX"``, and returns a tuple: of the airport code, status reason, current temp, and recent update. This function should call the ``get_airport()`` function.

.. external:: ps_8_07

    **PROBLEM 7: Create examples of using your newly defined functions**

    Now, iterate over the ``fav_airports`` list we've provided in your code file and print out the abbreviated info for each one, by calling ``extract_airport_data()``.

    After that code is executed, you should see 4 different tuples of airport data, each on a separate line. 

.. external:: ps_8_08

    **PROBLEM 8: Error handling and exceptions**

    We have provided an invocation of ``extract_airport_data`` with a bogus airport code in the code file, like so:

    ``print extract_airport_data("XYZ")``

    If you run it as is, it should throw an exception.

    Wrap the call to ``extract_airport_data`` in a try/except block, so that you should see: ``Sorry, that didn't work.`` printed out when you run your code. 

    (Note that the call to the function should be wrapped in a try/except -- the try/except block should not go inside your function! Go back to the Exceptions chapter to consider why we push you to do this.)

.. external:: ps_8_09

    **PROBLEM 9: Dealing with real live data**

    We've provided a list of airport codes in the variable ``possible_airports``, in the problem set code file. But not all of them are valid airports! Write code that iterates over this list and prints out a tuple of the airport data for each one. *But*, if it's not a valid airport code, your code should print ``Failed for airport <whatever the code is that didn't work>``, e.g. ``Failed for airport JAC``. Use a try/except block to do this.

.. external:: ps_8_10

    **Using real live data to write a CSV file**

    Finally, instead of printing out the results of code like you wrote above, you'll write the data to a CSV file. Iterate over the same list ``possible_airports`` again, but this time, write code to write to a CSV file called ``airport_temps.csv`` with 4 columns: ``airport_code``, ``status_reason``, ``current_temp``, ``recent_update``. Your resulting CSV file should have at least 5 lines: 4 lines for real airport data, and 1 line for the column headers.

    In a case where you encounter an invalid airport code, you should *not* write to the CSV file. Instead, you should print to the console: ``Failed for airport <whatever the bad airport code is>``. Use a try/except block to do this.

    **Make sure the CSV file you create is called airport_temps.csv. We will run tests on the CSV files post-submission, and we depend on the name of the file being correct.**

    Open the document in Excel or Google Sheets to make sure that it is properly formatted. You should make sure you have not included any extra parentheses in each cell when you open it in a spreadsheet program -- when you view the document in Excel or Google Sheets, each individual element of the tuple returned by ``extract_airport_data`` should be separate, in each cell, with no extraneous data.

    **You should not upload the CSV file your code creates -- when we run your code, it'll appear!**


.. external:: ps8_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/105657/assignments/131291>`_ assignment on Canvas.

