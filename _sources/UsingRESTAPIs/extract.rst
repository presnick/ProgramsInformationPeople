..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Extract contents from the Response
==================================

Assume that code like the following has successfully assigned a value to the variable resp.

.. sourcecode:: python


    import requests
    dest_url = <some expr>
    d = <some dictionary>
    resp = requests.get(dest_url, params = d)


It's important to remember that the object returned by requests.get is not a text string. It's a Response object. You can get the contents of the response in one of two ways.

1. ``resp.text`` gets the contents as one long string. If some or all of that string is a dictionary or list encoded in json format, you can call json.loads() to turn the string (or part of it) into the corresponding dictionary or list.
#. If you know that the entire contents consist of a string that is a dictionary or list encoded in json format, you can just access ``resp.json()``. That's equivalent to ``json.loads(resp.text)``.

Before going on, you should add some print statements to check that you have the data you're expecting. You might, for example, find that the contents consist of a message from the website telling you that it was unable to find the requested page or that you are not permitted to access it. If the content isn't what you expected, you should go back to the previous stage of printing the url, copying it into a web browser, and editing the url until you get the right content. You may also find it helpful to run ``print resp.status_code``, to get the numeric code returned by the web server you connected to.

.. sourcecode:: python


    import requests
    import json
    dest_url = <some expr>
    d = <some dictionary>
    resp = requests.get(dest_url, params = d)]
    print resp.status_code
    y = json.loads(resp.text)
    print type(y)
    print y

