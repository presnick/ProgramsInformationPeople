..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Caching Response Content
========================

You haven't experienced it yet, but if you get complicated data back from a REST API, it may take you many tries to compose and debug code to process that data in the way that you want. It is a good practice not to keep contacting a REST API to re-request the same data every time you run your program.

To avoid re-requesting the same data, after you have debugged your code that makes the call to requests.get(), you should save the contents in a file on your local machine. Then, you can make your processing program read the data from your local file. After you have your processing code working, then you can have it work on live data from the REST API.

There are three reasons why caching is a good idea during your software development:

1. It reduces load on the website that is providing you data. It is always nice to be courteous when using other people's resources. Moreover, some websites impose rate limits: for example, after 15 requests in a 15 minute period, the site may start sending error responses. That will be confusing and annoying for you.
2. It will make your program run faster. Connections over the Internet can take a few seconds or even tens of seconds if you are requesting a lot of data. It might not seem like much, but debugging is a lot easier when you can make a change in your program, run it, and get an almost instant response.
3. It is harder to debug your processing code if the content that is coming back can change on each run of your code. It's amazing to be able to write programs that fetch real-time data like airport conditions or the latest tweets from Twitter. It can be hard to debug, however, if you are having problems that only occur on certain Tweets (e.g., those in foreign languages). When you encounter problematic data, it's helpful if you save a copy and can debug your program working on that saved, static copy of the data.

The flow chart below describes a simple process for using cached data when it's available, or fetching and saving it when there is no cached data.

.. image:: Figures/CacheFlowchart.png

Here's an example of code that caches the results of a request for current conditions at Detroit's airport. Only on the first run of the code will the function ``get_and_cache_data_from_faa`` be called.

.. sourcecode:: python

    import requests
    import json

    cache_fname = "cached_results.txt"

    def get_and_cache_data_from_faa():
        print "fetching data"
        dest_url = 'http://services.faa.gov/airport/status/DTW'
        d = {'format': 'json'}
        resp = requests.get(dest_url, params = d)
        # cache the contents in a file
        print "caching data"
        f = open(cache_fname, 'w')
        f.write(resp.text)
        f.close()
        # return the contents as json
        return json.loads(resp.text)

    try:
        f = open(cache_fname, 'r')
        txt = f.read()
        data = json.loads(txt)
        f.close()
        print "succeeded at using cached data"
    except:
        data = get_and_cache_data_from_faa()


    print data


Inside the function get_and_cache_data_from_faa, we open the file for writing. Outside that function, the file is opened for reading; that's an attempt to read the cached copy.

All the code for reading the cached copy is wrapped inside a try/except block. The file may not exist, either because this is the first time that the program has been run, or someone deliberately deleted the file in order to force fetching of fresh data, an error will occur during execution of the try block. In that case, the code in the except clause will run, which causes the function get_and_cache_data_from_faa to be executed.