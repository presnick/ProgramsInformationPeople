..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _flickr_api_chap:

Searching for tags on flickr
============================

Consider another service, the image sharing site flickr. People interact with the site using a web browser. An API is available to make it easier for application programs to fetch data from the site and post data to the site. That allows third parties to make applications that integrate elements of flickr. Flickr provides the API as a way to increase the value of its service, and thus attract more customers. You can explore the `official documentation about the site <https://www.flickr.com/services/api/>`_.

Here we will explore some aspects of one endpoint that flickr provides for searching for photos matching certain criteria. Check out the `full documentation <https://www.flickr.com/services/api/flickr.photos.search.html>`_ for details.

The structure of a URL for a photo search on flickr is:

* base URL is ``https://api.flickr.com/services/rest/``
* ``?``
* key=value pairs, separate by &s:
   * One pair is ``method=flickr.photos.search``. This says to do a photo search, rather than one of the many other operations that the API allows. Don't be confused by the word "method" here-- it is not a python method. That's just the name flickr uses to distinguish among the different operations a client application can request.
   * ``format=json``. This says to return results in JSON format.
   * ``per_page=10``. This says to return 10 results at a time.
   * ``tags=mountains``. This says to return photos that are tagged with the word "mountains".
   * ``api_key=...``. Flickr only lets authorized applications access the API. Each request must include a secret code as a value associated with api_key. Anyone can get a key. See the `documentation for how to get one <https://www.flickr.com/services/api/misc.api_keys.html>`_. We recommend that you get one so that you can test out the sample code in this chapter.

Let's put everything together to make a little retrieval tool for flickr images containing particular tags. Of course, in a browser, you can just use flickr's search tool. But doing this through the API opens up other possibilities that you can explore for features not provided on the regular flickr website.

Below is some code that queries the flickr API for images that have a particular tag (I have found that searching for "mountains", "Switzerland", and "cows" usually produces beautiful images that are "safe for work", so the example below does that search.)

.. note:

    To run this code, you will need to copy it to a file on your local machine (not an activecode window), and **paste in an api_key that you get from flickr**.

.. sourcecode:: python

    import requests
    import json
    import pickle
    import webbrowser

    def canonical_order(d):
        alphabetized_keys = sorted(d.keys())
        res = []
        for k in alphabetized_keys:
            res.append((k, d[k]))
        return res

    def requestURL(baseurl, params = {}):
        req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
        prepped = req.prepare()
        return prepped.url

    def get_with_caching(base_url, params_diction, cache_diction, cache_fname):
        full_url = requestURL(base_url, params_diction)
        # step 1
        if full_url in cache_diction:
            # step 2
            print "retrieving cached result for " + full_url
            return cache_diction[full_url]
        else:
            # step 3
            response = requests.get(base_url, params=params_diction)
            print "adding cached result for " + full_url
            # add to the cache and save it permanently
            cache_diction[full_url] = response.text
            fobj = open(cache_fname, "w")
            pickle.dump(cache_diction, fobj)
            fobj.close()
            return response.text

    # apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
    # paste the key (not the secret) as the value of the variable flickr_key
    flickr_key = 'paste your key here'

    def flickrdemo(cache_fname):
        params_d = {}
        params_d['method'] = 'flickr.photos.search'
        params_d['api_key'] = flickr_key
        params_d['format'] = 'json'
        params_d['tags'] = ['mountains, Switzerland, cows']
        params_d['tag_mode'] = 'all'
        params_d['per_page'] = 5

        try:
            fobj = open(cache_fname, 'r')
            saved_cache = pickle.load(fobj)
            fobj.close()
        except:
            saved_cache = {}
        resp_text = get_with_caching('https://api.flickr.com/services/rest/', params_diction=params_d, cache_diction = saved_cache, cache_fname = cache_fname)
        parsed_response = json.loads(resp_text[14:-1])

        print parsed_response
        photo_ds = parsed_response['photos']['photo']
        for photo in photo_ds:
            owner = photo['owner']
            pid = photo['id']
            url = 'https://www.flickr.com/photos/{}/{}'.format(owner, pid)
            webbrowser.open(url)

    flickrdemo("cache_file.txt")

For documentation on how to do a flickr search for a particular tag, see the official documentation at https://www.flickr.com/services/api/flickr.photos.search.html. Based on that documentation, we set the parameters method, api_key, format, tags, tag_mode, and per_page. Note that in the code below, we have printed out the full url that is generated by requests.get. Try pasting it into a browser window and then editing the URL manually to try to change the search.

Flickr does something a little weird with its result string. Instead of just sending back a JSON-formatted dictionary, it sends back a string that begins with 14 extra characters-- ``"jsonFlickrApi("`` -- and ends with an extra close parentheses character ``)`` at the end. So we use the slice operator to strip out those extra characters. That is loaded into a python dictionary using ``json.loads()``.

Finally, we loop through the list of photo dictionaries that were returned, extracting two fields, owner and pid. Those are used to create new URLs that are in the format flickr expects for displaying a webpage containing a single image. Each of those URLs is passed to the webbrowser.open() function. If all goes well, that should open five browser tabs, each with a picture that some flickr user had tagged with the words "mountains", "Switzerland", and "cows".

Note that if you run exactly this code a second or third time (you should!), you will be getting the *cached* data -- not brand new live data. You should see evidence of that printed out in the console!

.. note:

    If any of that code is puzzling, try adding some print calls or breaking down the complex expressions into a series of shorter statements.