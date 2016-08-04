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
    
    
.. _fb_api_exercises:

Facebook API Exercises
----------------------

Download the code file ``fbapi.py`` from Canvas. It contains code to get data from the Facebook API. 

(In order to run it, you will need to have ``pip install`` ed the ``requests`` library, discussed when you learned about using APIs.)

You will also need to get your own Facebook Authentication token at ``https://developers.facebook.com/tools/explorer`` (you'll need to sign in with your Facebook account, click ``Get Token``, and copy that long string of characters that appears). You can also see results from sample requests to the Facebook API on that page, and choose different authentication permissions -- in other words, choosing what rights you have to see different data on Facebook.

We won't cover all the details of this in this course, but try running the following code -- and play around with it to see if you can print out different post messages from our course Facebook group.

The reason you need this special authentication token from Facebook, which you'll need to regenerate on that same page every couple of hours in order to run your code, is because the Facebook API requires a type of authorization that the FAA API and the Flickr API did not. 

This is pretty intuitive -- Facebook is likely to have a lot of personal data accessible when you log in! Providing your access token, and associating certain permissions with it, as seen in class, and inputting that access token as a query parameter, allows you to make a request to the Facebook API that gets you data *you* can access (data for a closed group you are part of, or data from your own Facebook feed, for example).

.. sourcecode:: python

    import requests
    import json

    access_token = None
    group_id = None
    if access_token is None:
        access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")
    if group_id is None:
        group_id = raw_input("\nCopy and paste your userid or FB group id: ")
    url_params = {}
    url_params["access_token"] = access_token
    url_params["fields"] = "message,comments,likes"
    baseurl = "https://graph.facebook.com/{}/feed".format(group_id)
    r = requests.get(baseurl ,params=url_params)
    print r.url
    d = json.loads(r.text)
    print d.keys()


To see more about the Facebook Graph API and other options it allows, you can look at the URL: ``https://developers.facebook.com/docs/graph-api/reference``, and to try out API requests, you can play with the `Graph API Explorer <https://developers.facebook.com/tools/explorer>`_. We're going to largely focus on the individual and group feeds, and the posts: who each post is from, each post's comments, and each post's likes. (As we write this, Facebook Reactions were recently rolled out -- but the API allows us to get data just about *likes*, which we'll do for this course.)

You can see that this already gives you a very complicated structure of data! But you can use the Graph API explorer to give you an idea of what different information you can get from the Facebook Graph API and how it might be useful for you. You might also find it helpful to use `jsoneditoronline.org <http://www.jsoneditoronline.org/>`_ to help make sense of the results that come back, and figure out how to extract data from the nested dictionary.


.. mchoice:: fb_api_1
   :answer_a: EDT
   :answer_b: GMT
   :answer_c: Ann Arbor
   :answer_d: en_US
   :feedback_a: 
   :feedback_b:
   :feedback_c:
   :feedback_d:
   :correct: d
   
   Use the same setup to run a GET request on me?fields=locale. In the results, what is the value associated with the "locale" key?
     
   
.. mchoice:: fb_api_4
   :multiple_answers:
   :answer_a: You would like your code to be compressed so that it uses less space on your file system
   :answer_b: You would like to be able to see or revert to any past version of any of the files in your project
   :answer_c: You want to collaborate with others, working in parallel on a project and merging your changes together occasionally
   :answer_d: You would like your code to automatically be checked for syntax errors
   :answer_e: You would like to distribute your code in a public repository that others can easily fork or comment on
   :feedback_a: If you just want compression, use one of the compression programs like gzip or compress.
   :feedback_b: git makes all of your past saved versions accessible.
   :feedback_c: git lets multiple work independently on files. If you work on separate parts of a file, it will merge them automatically. If two people edit the same line, then git will mark where there are conflicts and you can resolve them manually.
   :feedback_d: There are programs like lint that automatically check for syntax and coding style errors, but they are not an integral part of revision control system.
   :feedback_e: Sites like github, bitbucket, and assembla provide a way to publicly share repositories.
   :correct: b,c,e
     
   Which of the following are reasons to use a version control system like github?

   
   
   