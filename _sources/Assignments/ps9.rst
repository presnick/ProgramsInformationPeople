:orphan:

..  Copyright (C) Jackie Cohen, Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Activities through 11/18
========================

* **Before class Monday 11/14:**

  * Read about the :ref:`Facebook API <fb_api_exercises>`.
  * Read the `Facebook Graph API overview <https://developers.facebook.com/docs/graph-api/overview>`_
  * Try out the `Facebook Graph API Explorer <https://developers.facebook.com/tools/explorer/>`_. You should try at least a couple different requests in the explorer and explore the resulting data (try copying it into jsoneditoronline.org!).
  * Read about `Paging with the Facebook API <https://developers.facebook.com/docs/graph-api/using-graph-api#paging>`_, focusing on **Offset-based pagination**, which we will focus on in lecture / will discuss further on Wednesday.

.. usageassignment::
  :subchapters: FacebookAPI/FBAPI
  :assignment_name: Prep 18
  :deadline: 2016-11-14 22:40
  :pct_required: 50
  :points: 50

* **Before class Wednesday 11/16:**

  * Read the following listed sections of :ref:`APIs with OAuth <requests_oauthlib>`
  * Take a look at the ``sample_twitter.py`` code file (Canvas > Files > Code Samples > sample_twitter.py). Try it out, and collect questions you have about it for lecture and section.

.. usageassignment::
  :subchapters: APIsWithOAuth/RequestsOAuthLib, APIsWithOAuth/TwitterAPI, APIsWithOAuth/Paging
  :assignment_name: Prep 19
  :deadline: 2016-11-16 22:40
  :pct_required: 80
  :points: 50

* **Before Sunday 11/20 at 11:59 PM:**

  * Complete and submit your :ref:`Problem Set 9 <problem_set_9>`, and save an answer to your Demonstrate Understanding for this week (linked below).
  * Complete :ref:`Reading Response 10 <reading_response_10>`.

This Week's Reading Responses
-----------------------------

.. _reading_response_10:

.. external:: rr_10

  `Reading Response 10 <lhttps://umich.instructure.com/courses/108426/assignments/139259>`_ on Canvas.


.. _problem_set_9:

Problem Set
-----------

Go `HERE to see the Problem Set 9 assignment <https://umich.instructure.com/courses/108426/assignments/139257/edite>`_, where you can find the file you need to download and edit, and where you can submit your file for this assignment.

.. note::

    Reminder: we do not debug code when grading, so we cannot grade code that does not run! Make sure your code runs before submitting it -- you should comment out any code that does not.

.. note::

    There are a few things in this problem set that cannot be tested: you'll have to examine your output and how your problems work to be 100% sure they work correctly, but passing the tests will give you good guidance about whether or not your code is doing what it should!

.. external:: ps_9_01
    
    **PROBLEM 1**

    We've provided a file ``samplepost.txt`` that contains a sample of data representing a Facebook post. Using this for data investigation (try copying and pasting it into jsoneditoronline.org!), fill in the definition of the class ``Post`` to hold information about one post on Facebook.

    We've provided a skeleton of the ``Post`` class with some code:

    .. sourcecode:: python

        class Post():
            """object representing status update"""
            def __init__(self, post_dict={}):
                if 'message' in post_dict:
                    self.message = post_dict['message']
                else:
                    self.message = ""
                
            def positive(self):
                return None
                           
            def negative(self):
                return None

            def emo_score(self):
                return None

    Add to that code in your ``506_ps9.py`` file so that it fulfills the following instructions.

    If the post dictionary has a ``'comments'`` key, set an instance variable ``self.comments`` to hold the list of comment dictionaries you extract from ``post_dict``. Otherwise, set ``self.comments`` to be an empty list: ``[]``.

    Note that something similar has already been done for the contents (``message``) of the original post, so you can use that as a template! Extracting the list of comment dictionaries from a post_dict is a little bit harder. Take a look at the sample of what a ``post_dict`` looks like in the file samplepost.txt / using jsoneditoronline in order to do nested data investigation.

    Now, similarly, *if* the post has any likes, set ``self.likes`` to the value of the list of likes dictionaries. Otherwise, if there are no ``'likes'``, set ``self.likes`` to hold an empty list.

    Finally, finish defining three methods of the class Post:

    ``positive`` should return the number of words in the message that are in the list of positive words called ``pos_ws`` (provided in our code)

    ``negative`` should return the number of words in the message that are in the list of negative words called ``neg_ws`` (provided in our code)

    ``emo_score`` should return an integer: the difference between the positive and negative scores for that post. 

    (Careful: "disgusting" and "disgust", for example, are 2 different words -- so if the word "disgust" is in a message, it should only get 1 negative count for that, not two.)

.. activecode:: ps_9_02

    **PROBLEM 2**

    We've provided the following code in your ``506_ps9.py`` file, where you'll need it for the problem set. In this code window, add comments that describe what these lines of code do.
    ~~~~
    sample = open('samplepost.txt').read()
    sample_post_dict = json.loads(sample)
    p = Post(sample_post_dict)

.. external:: ps_9_03
    
    **PROBLEM 3**

    Now, get a json-formatted version of your last 100 posts on Facebook.

    We've provided some code here for you to use in order to do this:

    We've provided a place for you to put your Facebook access token than you get from ``https://developers.facebook.com/tools/explorer``. (See your assigned readings/lecture materials for more detail.) Remember that in order to get data from our class FB group, you will need to use **version 2.3**, so that is the version we've included in the baseurl and shown in class and you will need to select the **user_groups** permission after you click Get Token. Also remember that every few hours, you'll need to get a new access token from the Graph explorer.

    We've saved the base url for Facebook in a variable, ``baseurl``. The baseurl looks like this: ``https://graph.facebook.com/v2.3/me/feed``. 'All the data from my own Facebook feed.' You'll also see we've provided a variable in your file called ``GROUP_ID``. You should replace the ``me`` in the baseurl with that variable's value if you want to get data from the course FB group.

    We've also built your necessary params dictionary to get data about Facebook posts, their comments, and their likes, though you can try other parameters as well!

    .. sourcecode:: python

        url_params = {}
        url_params["access_token"] = access_token
        url_params["fields"] = "comments{comments{like_count,from,message,created_time},like_count,from,message,created_time},likes,message,created_time,from"

    This will get you pretty complex data -- but you've seen data similar to it before, when we first did nested data investigation.

    Given all this stuff, you should write code to make a request to the Facebook API, and you should retrieve up to 200 posts from your Facebook feed or from the class FB group, using paging. Convert the data you collect into a Python object, and save it in the variable ``fb_data``.

.. external:: ps_9_04
    
    **PROBLEM 4**

    Given all this Facebook data you have, use a list comprehension to create a list of instances of class ``Post``. Save that list of Post instances in a variable called ``post_insts``.

    **NOTE:** This requires understanding -- but only one line of code, given the code you have already written above!

.. external:: ps_9_05
    
    **PROBLEM 5**

    Write code to compute the 3 people who liked the most posts in the feed, and save those people's names in a list called ``top_likers``. Compute the 3 people who commented most frequently in the feed, and save those people's names in a list called ``top_commenters``.

    HINT: creating dictionaries and sorting may both be useful here.

.. external:: ps_9_06
    
    **PROBLEM 6**

    Define a function called ``unique_facebookers`` that takes as input a list of ``Post`` instances.
    
    The function should return the string "commenters" if the number of unique people who commented on all of those posts is larger than the number of unique people who liked at least one post in your data. 

    If the number of unique people who liked posts in your data is bigger than the number who commented, the function should return the string "likers". 

    If the count of unique people who liked posts in your feed is equal to the count of unique people who made comments in your feed, it should return the string "equal". 

    For example: if the comments on my posts are made by, in order: Mary, Tess, Nat, Jackson, Tess, and Mary, then 4 unique people commented. If the following people liked my posts, overall: Nat, Jackson, Jackson, Mary, then 3 unique people liked my posts. If this were the case in my Post instances list, invoking my ``unique_facebookers`` function on my list should return ``"commenters"``. 

    Note that this is NOT the same as looking at whether there were more comments or likes overall!


.. external:: ps_9_07
    
    **PROBLEM 7**

    Write code to output a .csv file called emo_scores.csv that lets you make scatterplots (in Excel or Google sheets) showing net positivity (emo_scores) on x-axis and comment-counts and like-counts on the y-axis. 
    
    Each row in the CSV should represent one post, and should include: emo score, comment counts, and like counts, in that order.

    Use the CSV to create a scatterplot of your data, which you can do in Excel or Google Sheets. Then, post a screenshot of your scatterplot to our facebook group! (You do not have to do this, but we encourage it.)

    You can see what the scatterplot might look like in ``emo_scores.xlsx``, included in the assignment files. (In the example case, there's not an obvious correlation between positivity and how many comments or likes. There may not be, but you find that out by exploring the data!)

    **Submit your generated .CSV to Canvas.** Please make sure it is saved with the exact name **emo_scores.csv** -- our grading process depends upon it having the correct name!

    Can you see any trends or possible relationships between likes, comments, and emo_scores once you generate a scatterplot? (Something to consider/discuss. Not graded.)


.. external:: ps9_dyu

    Complete this week's `Demonstrate Your Understanding <https://umich.instructure.com/courses/108426/assignments/139247>`_ assignment on Canvas.