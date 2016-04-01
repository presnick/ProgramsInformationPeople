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
------

As you write more and more complex programs with APIs, you will begin to notice that only so much data appears in each initial response you get back. For example, with Facebook, the default number of posts you get back from your Timeline is 25.

But you can also get the next 25, and the next, and the next (until you reach the end of your Timeline -- or really, the beginning, since you see the most recent posts first). You use paging to do that!

Different APIs manage paging in different ways. Generally, the data you get back will have some way of accessing *more* data, and you have to follow that path in order to collect the next set, e.g. the next 25 posts, or the next 100 tweets.

Of course, this is useful because it allows you to get more data, and for social media APIs, it allows you to trace back further in history and ensure that you get all the data you want to analyze or examine.

It's best to look at specific examples, since different APIs handle paging data differently. You can see Twitter's explanation at ``https://dev.twitter.com/rest/public/timelines``.

There is code at the bottom of the ``oauth_with_twitter.py`` code on Canvas that shows an example of using paging. We get my last 25 tweets, 5 at a time, and accumulate a list of all the data. 

Then we cache the data (Python lists are json-formatted, so loading a list into a string and writing it to a file is just fine!). 

Then, we can open the data any time later and manipulate it to learn things from it -- for instance, how many vowels I used in those 25 tweets, or how many favorites those 25 tweets received in total...
