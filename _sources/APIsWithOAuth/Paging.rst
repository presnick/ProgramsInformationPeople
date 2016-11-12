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

.. _paging_apis:

Paging
======

As you write more and more complex programs with APIs, you will begin to notice that only a limited amount of data appears in each initial response you get back. For example, with Facebook, the default number of posts you get back is 25.

But you can also get the next 25, and the next, and the next (until you reach the end of your feed -- or really, the beginning, since you see the most recent posts first). You use paging to do that!

Different APIs manage paging in different ways. Generally, the data you get back will have some way of accessing *more* data, and you have to follow that path in order to collect the next set, e.g. the next 25 posts, or the next 100 tweets.

Of course, this is useful because it allows you to get more data, and for social media APIs, it allows you to trace back further in history and ensure that you get all the data you want to analyze or examine.

It's best to look at specific examples, since different APIs handle paging data differently. You can see `Twitter's explanation <https://dev.twitter.com/rest/public/timelines>`_. Twitter's approach is to have you request a page of results with ids less than some maximum number. Twitter assigns ids in ascending order, so if you requests tweets with ids less than the lowest id on the current page, you'll get the next most recent tweets related to your request.

There is code at the bottom of the ``oauth_with_twitter.py`` code on Canvas that shows an example of using paging. We get my last 25 tweets, 5 at a time, and accumulate a list of all the data. The code is reproduced at the bottom of this page.

The process is even easier with Facebook. In each response dictionary, if there is another page of data available, Facebook provides a key called ``paging``. Its value is a dictionary with keys ``previous`` and ``next``. Their values are full urls. Use one of those urls as a baseurl in a call to requests.get and you'll get another page of results back.

After we retrieve many pages of results, we cache the data (Python lists are json-formatted, so loading a list into a string and writing it to a file is just fine!).

Then, we can open the data any time later and manipulate it to learn things from it -- for instance, how many vowels I used in those 25 tweets, or how many favorites those 25 tweets received in total...


Caching the combined results can be especially useful when dealing with Twitter. Twitter has a ``rate limit``. If you make too many requests in a short period of time, it will reject further requests from you for a while (usually about 15 minutes). So, once you've managed to collect all the results you want, it's better to cache them and then work with the cached data as you're debugging your code that processes the data.

.. sourcecode:: python

    ####PAGING
    # Getting multiple pages of results can be tricky. See Twitter's explanation at
    # https://dev.twitter.com/rest/public/timelines
    # (Other sites handle paging slightly differently; you'll have to read the documentation.)

    # Let's get my (or your) last 25 tweets, 5 at a time.
    # Twitter actually lets you get more than 25 at a time, but not more than 200, so this is practice for when you want to get more than 200. You could get the last 1000, 200 at a time, using the same pattern.

    # To pass parameters using the requests_oauthlib module, we use the same
    # get() method used in the requests module.
    # see documentation at
    # http://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls


    collected_tweets = [] # where I'll collect all the tweet data I get as I page through my results, 5 at a time
    ids = []
    max_id = None
    my_params = {'count' : 5} # query parameters for 1st request

    for i in range(5): # get five pages of results and accumulate all the results in list collected_tweets
        if len(ids) > 0: # if we have already started the paging process
            my_params['max_id'] = min(ids) - 1
            # Twitter suggests that you take the minimum of the ids you got before, then subtract one from it, to make sure you get only ones you haven't received before. We can use the built-in min function here (could also accumulate by hand).
        # Regardless, now we need to make a request to the logged in user's timeline with the query parameters
        r = oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json",params = my_params)  # passes {'count': 5, 'max_id': whatever} ...
        # Now, append this data to a list so we can collect all the paged results
        collected_tweets.append(r.json())
        next_five_ids = [tweet['id'] for tweet in r.json()]  # get the ids from the tweets we just got
        ids = ids + next_five_ids # add them to the list, and start the for loop process over again

    print ids
    # print pretty(collected_tweets)

    # cache the data we got back and collected
    fr = open("paging_nested.txt","w") # Choose a file to save my data in
    fr.write(json.dumps(collected_tweets)) # Use json.dumps to put the Python object into a nice string that I can write to a file, and then write it to a file
    fr.close()

    # Now, can investigate using this data that got cached.
    # If you're testing with the data in the file only, you may want to comment out all the code above this for a while so you don't inadvertently make a lot of requests to Twitter and then run out of request privileges for the day!
