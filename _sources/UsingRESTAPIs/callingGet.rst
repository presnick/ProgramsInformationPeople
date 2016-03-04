..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Make The Right Call to requests.get()
=====================================

The first step in using a REST API is to make a call to requests.get(). As described in the section on the :ref:`The requests module<requests_details_chap>`, the .get() method takes as its first parameter a string that's the url endpoint. It takes an optional parameter called ``params`` whose value should be a dictionary. Its key-value pairs will be encoded as necessary and everything will be concatenated together. Go back and review that section if you need to refresh your memory.

The trick in writing your program is to test whether you've set everything up right for your call to requests.get(), and to diagnose what's wrong if it's not all correct. To assist in that, assign the results of the call to a variable, so that you can later probe that variable. For example,

.. sourcecode:: python


    import requests
    dest_url = <some expr>
    d = <some dictionary>
    resp = requests.get(dest_url, params = d)

Of course, in the code above, you'd need to set dest_url and d appropriately based on your understanding of the particular REST API that you're making a request to. To figure out what dest_url and d should be, you will need to look at the documentation for the REST API, and probably some examples of URL requests that are provided in the documentation.

If you have an example URL, look for the ? in it. The stuff after the question mark will probably be key-value pairs that should go in d, while the stuff before the ? will have to be part of the string bound to the dest_url variable.

Runtime Errors in executing requests.get()
------------------------------------------

The first thing that might go wrong is that you get an error during execution of the fourth line. There are two possibilities for what's gone wrong in that case.

The first possibility is that the variable dest_url is either not bound to a string, or is bound to a string that isn't a valid URL. For example, it might be bound to the string ``"http://foo.bar/bat"``. foo.bar is not a valid domain name that can be resolved to an ip address, so there's no server to contact. That will yield an error of type requests.exceptions.ConnectionError. Here's a complete error message:

.. sourcecode:: python

    requests.exceptions.ConnectionError: HTTPConnectionPool(host='foo.bar', port=80): Max retries exceeded with url: /bat?key=val (Caused by <class 'socket.gaierror'>: [Errno 11004] getaddrinfo failed)

A second possibility is that the value provided for the params parameter is not a valid dictionary or doesn't have key-value pairs that can be converted into text strings suitable for putting into a URL. For example, if you execute ``requests.get("http://github.com", params = [0,1])``, [0,1] is a list rather than a dictionary and the python interpreter generates the error, ``TypeError: 'int' object is not iterable``.

If you do get an error when you run the the call to requests.get(), and it's not obvious to you how to fix it, try the following steps.

1. Get rid of the optional `params = ...` from your call. If that gets rid of the error, the problem was the value you provided for params. Print out that value and see if it's a dictionary with the key-value pairs you wanted to be part of the URL.

2. If that doesn't solve the problem, it must be a problem with the string bound to the variable dest_url. Try executing ``print type(dest_url)`` and ``print dest_url`` to see if something is wrong with it.

Checking if You Have the Right URL
----------------------------------

If requests.get() executes without generating a runtime error, you are still not done with your error checking. No error means that your computer managed to connect to some web server and get some kind of response, but it doesn't mean that it got the data you were hoping to get.

Fortunately, the response object returned by requests.get() has the ``.url`` attribute, which will help you with debugging. It's a good practice during program development to have your program print it out.

.. sourcecode:: python


    import requests
    dest_url = <some expr>
    d = <some dictionary>
    resp = requests.get(dest_url, params = d)
    print resp.url

Execute the program. The url will print out. You can eyeball it and perhaps notice problems.

Better yet, copy and paste it into a browser. Then see what the browser fetches. If it's approximately what you were expecting, then you can move on to the next step.

If not, you may find it helpful to edit the URL in the browser and see if that fixes it. It's a lot easier to debug a URL in the browser, where you can see exactly what the URL is, than to edit the url and d variables in the program above, where you may have a misconception about what exactly is in them or how they are turned into a url by the requests.get() command. Once you find a url that works in the browser, you'll have to figure out how to translate it into appropriate values for your dest_url and d variables.

