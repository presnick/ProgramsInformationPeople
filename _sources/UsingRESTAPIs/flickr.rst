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

Let's put this all together to make a little retrieval tool for flickr images containing particular tags. Of course, in a browser, you can just use flickr's search tool. But doing this through the API opens up other possibilities that you can explore for features not provided on the regular flickr website.

Below is some code that queries the flickr API for images that have a particular tag (I have found that searching for "mountains" usually produces beautiful images that are "safe for work", so the example below does that search.) 

.. note:

    To run this code, you will need to copy it to a file on your local machine (not an activecode window), and **paste in an api_key that you get from flickr**.

.. sourcecode:: python

    import requests
    import json
    import webbrowser

    def pretty(obj):
        return json.dumps(obj, sort_keys=True, indent=2)

    # apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
    # paste the key (not the secret) as the value of the variable flickr_key
    flickr_key = 'yourkeyhere'

    cache_fname = "cached_flickr.txt"


    def flickrREST(baseurl = 'https://api.flickr.com/services/rest/',
        method = 'flickr.photos.search',
        api_key = flickr_key,
        format = 'json',
        extra_params={}):
        d = {}
        d['method'] = method
        d['api_key'] = api_key
        d['format'] = format
        for k in extra_params:
            d[k] = extra_params[k]
        resp = requests.get(baseurl, params = d)
        # print resp.url
        # cache the contents in a file
        print "caching data"
        f = open(cache_fname, 'w')
        f.write(resp.text)
        f.close()
        # return the contents as text in this case
        return resp.text


    def extract_ids(resp_txt):
        # try:
            # d = result.json()
        # except:
            # print "can't interpret result as json; first 60 characters shown below"
            # print result.text[0:60]
            # print

        d = json.loads(resp_txt[14:-1])
        # print pretty(d)
        # print d.keys()
        # print d['photos'].keys()
        photo_ds = d['photos']['photo']
        # print photo_ids
        return photo_ds

    def flickrdemo():
        try:
            f = open(cache_fname, 'r')
            txt = f.read()
            f.close()
            print "succeeded at using cached data"
        except:
            txt = flickrREST(extra_params = {'tags':'mountains, Switzerland, cows', 'tag_mode':'all', 'per_page':5})


        photo_ds = extract_ids(txt)

        # print len(photo_ds)
        # for k in photo_ds[0]:
            # print k
        for photo in photo_ds:
            owner = photo['owner']
            pid = photo['id']
            url = 'https://www.flickr.com/photos/{}/{}'.format(owner, pid)
            webbrowser.open(url)

    try:
       flickrdemo()
    except:
       print "Error in flickrdemo()"


flickrREST takes various parameter values defining what to ask for from flickr. It then calls requests.get and returns whatever it returns.

Flickr does something a little weird with its result string. Instead of just sending back a JSON-formatted dictionary, it sends back a string that begins with 14 extra characters-- "jsonFlickrApi("-- and ends with an extra close parentheses character at the end. So we use the slice operator to strip out those extra characters. That is loaded into a python dictionary using json.loads().

Finally, we loop through the list of photo dictionaries that were returned, extracting two fields, owner and pid. Those are used to create new URLs that are in the format flickr expects for displaying a webpage containing a single image. Each of those URLs is passed to the webbrowser.open() function. If all goes well, that should open five browser tabs, each with a picture that some flickr user had tagged with the words "mountains", "Switzerland", and "cows".

.. note:

    If any of that code is puzzling, try uncommenting some of the print statements that are also included.