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

Activities through 12/6
=======================

* Before Monday's class:
   * View slides ``FB Graph API`` in Canvas
   * Use pip to install the facebook-sdk module (not the "facebook" module, which works a little differently)
   * Do the :ref:`FaceBook API exercises <fb_api_exercises>`.
   * Review the section on :ref:`Debugging nested data <debug_nested_chap>`

* By Tuesday midnight (if you didn't do these things already):
    * Read *The Success of Open Source*, Chapter 4
    * Read about the `Drupal open source community <https://medium.com/@heyrocker/this-article-was-originally-a-keynote-presentation-at-the-pacific-northwest-drupal-summit-in-5e7c7f93131b>`_. Drupal is a "Content Management System" that makes it relatively easy to develop websites that have dynamic content and interactive features like commenting and tagging. Note: it may be helpful in reading the article to know that "Dries" is `Dries Buytaert <http://buytaert.net/>`_, the person who started Drupal and "webchick" is the username chosen by `Angie Byron <http://www.webchick.net/about>`_, a prominent member of the community.
    * :ref:`Reading response 11 <reading_response_11>`

* Before Wednesday's class:
   * Download the code file from Canvas, oauth_with_twitter.py
   * install the requests_oauthlib python module (using pip)
   * Follow the instructions in it to create an app for yourself on dev.twitter.com
   * Read about `Paging in Twitter API requests <https://dev.twitter.com/rest/public/timelines>`_ Paging is necessary when the site only gives you one *page* of results at a time, and you have to make another request to get more.
   * Try to understand the code in oauth_with_twitter.py, including the paging code. We will go over it in class.
   * Answer the question :ref:`below <twitter_oauth_checkin>`

* Before Thursday's section meeting:
   * Complete the project plan. Download the file project_plan.py from Canvas. You should modify it and upload it to Canvas.

* By Sunday 12/6 at 5PM:
   * Complete Problem Set 12, via Canvas.

* By Sunday midnight:
    * Read *The Success of Open Source*, Chapter 5
    * :ref:`Reading response 12 <reading_response_12>`

.. usageassignment:: prep_22
    :subchapters: RESTAPIs/FBAPI, NestedData/DebuggingNestedData
    :assignment_name: Prep a22
    :deadline: 2015-12-01 21:30:00
    :pct_required: 80
    :points: 50

.. _reading_response_11:

Reading Response (Tuesday night)
--------------------------------

Answer the following questions.
    1. The linux project uses git to organize the work of all the contributors. Take a look at the `linux project on github <https://github.com/torvalds/linux>`_. Take a look at the recent commits. Click around to see how many people have made contributions recently. Also check out the github page for `Runestone <https://github.com/bnmnetp/runestone>`_ and for `this textbook, which is built on Runestone <https://github.com/presnick/ProgramsInformationPeople>`_. Report on something interesting you found from exploring these public git repositories.

    2. The chapter describes forking as something that could fragment developer efforts and thus slow down progress of a project. If you tried to make a "fork" of Linux today, would it be technically feasible to do so? What do you think would happen?

    3. Pages 116-119 describes the genesis of "Bitkeeper", which later was replaced by git. Why would the promise of switching to use something like git have helped to defuse a potential forking of the Linux project?

    4. What seems similar and what seems different between the Linux project's developer community and the Drupal project's developer community?

.. activecode:: rr_11_1

   # Fill in your response in between the triple quotes
   s = """

   """
   print s

.. _reading_response_12:

Reading Response (Sunday night)
--------------------------------


Answer the following questions. 

1. Weber argues that there are several motivations for people to contribute to open source projects. Which of these do you find most plausible? Which least?

#. At an aggregate level, rather than an individual level, Weber argues that because open source projects are "antirival" goods, they can survive having only a small fraction of the participants making positive contributions. First, define "antirival" in your own words. Then say whether you think Weber's argument would work just as well for a "nonrival" good as for an "antirival" good.  

.. activecode:: rr_12_1

   # Fill in your response in between the triple quotes
   s = """

   """
   print s



.. _twitter_oauth_checkin:

Wednesday Prep Question
-----------------------

What is the value associated with the "language" attribute in the dictionary that is returned when you run oauth_with_twitter.py after pasting in your keys?

.. activecode:: twitter_oauth_1

   # Fill in your response in between the triple quotes
   s = """

   """
   print s




