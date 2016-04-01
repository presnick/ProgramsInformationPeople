:orphan:

..  Copyright (C) Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
:linenothreshold: 500

.. _requests_oauthlib:

Requests OAuthLib Library
-------------------------

You've already seen one way of using the OAuth Protocol in programs that run on your own computer (not online/in a web application), when we learned about the Facebook API. Regenerating an access token with certain permissions and including it in your request, made with ``requests.get``, from the ``requests`` library (LINK), allowed you to prove that you had the correct permissions to access the data you wanted from your account.

However, there is a more general library that allows you to use OAuth in applications without dealing with the inner complexities of the OAuth Protocol, called ``requests_oauthlib``.

In order to use it, you'll need to ``pip install requests_oauthlib`` (using whatever method of ``pip`` installation works for you -- the full path, for Windows users, or ``sudo``, for Mac users).

This installs an external library that is a lot like the ``requests`` library you've seen before, except that it handles OAuth neatly.

When you make requests that require an OAuth token, you'll need to provide a little bit more information than you provide when you make a request to an API like the FAA API or like Flickr. Instead of using the **get** method in the ``requests`` library, you'll be making an instance of a class in the ``requests_oauthlib`` library called an **OAuth1Session**.

.. admonition:: Note. 

   There are actually 2 versions of the OAuth Protocol: OAuth 1.0 and 2.0. We will not be discussing the difference in depth in this course, but that's the reason you see "OAuth1", for example -- it refers to the version of the set of security rules we're using to ensure that users' accounts are safe! These protocols (sets of rules) are not perfect, but how they are risky is also outside the bounds of this course.

Since you will be running a program that is not online, we've written a little bit of code to help you manage the OAuth token exchange so you can get data back from a service that uses the OAuth protocol and does not have a special key tool the same way Facebook does. The person who runs your program (the user) will need to open up a web browser window to log in to their account on the service, in order to authenticate, and essentially say *"it's okay if you, consumer application, use <this specific data being asked for> from my account on your service".*

The overall process of making a request using ``requests_oauthlib`` is as follows (we'll provide code that does this, to show you how it works):

1. Import the requests_oauthlib library

2. Register for a developer account/application on the service you want to get data from. 

3. You'll need a **client key** and a **client secret** in your program. Different services call these pieces of information different things, but many will provide you with them. Twitter, for example, calls them **Consumer Key** and **Consumer Secret**. They're basically two long unique strings of characters which help a service authenticate a specific consumer: *the person who made you does definitely have a developer account/application on my service, so it's ok that you're trying to get data from my service!*

4. Create an *instance* of the OAuth1 session class that is defined in the ``requests_oauthlib`` library.

5. Use pre-defined methods of that OAuth1 class in order to 
get a request token -- something that will identify you, the **consumer** (or **client**).

6. Get authorization from the **user** (the owner of resources, like you 'own' the data in your Twitter account) to access their protected resources (e.g. their images, or tweets, etc). 

7. Get an access token from the OAuth provider, and save it so you can use it later to make secure requests for protected data (like tweets or images).

8. Make a request, and access protected resources. Get back a bunch of nested data to play with and parse as usual.
