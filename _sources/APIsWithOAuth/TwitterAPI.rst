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

.. _twitter_api:

The Twitter API
===============

The Twitter API is one that works like this. You can see the full documentation for it `online <https://dev.twitter.com/rest/public>`_.

We've provided some code in a file called ``oauth_with_twitter.py`` on Canvas, **Files > Code**. This code automates some of that process you just read about. It's heavily commented so you can go through it and understand how it can help you. It can also be adapted for similar APIs. Its contents are below.

Notice that the request made to an API to get interesting (protected) data is all the way at line **143** in the code. Before that is the prep -- steps 1-7 in the process you just read about, to get data from an API that uses the OAuth protocol.

Also notice the ``import webbrowser`` -- You've seen this before when we wrote code using the Flickr API to open up photos in the browser. Here, we're using the ``webbrowser`` module to open up a browser window where the user can log in to Twitter to authenticate permissions.

In this code, we cache verification tokens so that it's easy to use them again. But caching *data*, as you learned about earlier, is also a good idea when you make requests to the Twitter API, because it has a rate limit (one application, or one IP address, can only make a certain number of requests per day!).

Using the provided code for the Twitter API
-------------------------------------------

The beginning of the ``oauth_with_twitter`` code has a link to ``https://apps.twitter.com/``, where you can fill in information for an application for your Twitter account. (In order to use this, you'll need to sign up for a Twitter account, but you don't need to post anything on it.) A couple notes about this:

* When you fill in a placeholder website in the application process, be sure it is a full URL -- in other words, that it begins with ``http://`` or ``https://``.

* You will need to add a mobile phone number to your Twitter account in order to register an application (this is a new requirement). If you don't feel comfortable doing this, you can get a Google Voice number at this url: ``https://support.google.com/voice/answer/115061?hl=en`` -- you will have to authorize your phone number by typing in a text message code that you receive in order to register a Twitter application.

The ``oauth_with_twitter.py`` code is below. It's lengthy, so it may be easier to open the file yourself on Canvas and examine it in a code editor.

.. sourcecode:: python

    import requests_oauthlib
    import webbrowser
    import json

    def pretty(obj):
        return json.dumps(obj, sort_keys=True, indent=2)
        
    # Get these from the Twitter website, by going to
    # https://apps.twitter.com/ and creating an "app"
    # Don't fill in a callback_url; instead, put in a placeholder for the website
    # Visit the Keys and Access Tokens tab for your app and grab the following two values

    client_key = None # what Twitter calls Consumer Key -- fill in a string here
    client_secret = None # What Twitter calls Consumer Secret -- fill in a string here

    if not client_secret or not client_key:
        print "You need to fill in client_key and client_secret. See comments in the code around line 8-14"
        exit()

    def get_tokens():
        ## Step 1: Obtain a request token which will identify you (the client) in the next step. 
        # At this stage you will only need your client key and secret

        # OAuth1Session is a class defined in the requests_oauthlib module
        # Two values are passed to the __init__ method of OAuth1Session
        # -- the key is passed as the value of the first parameter (whose name we don't know)
        # -- the secret is passed as the value of the parameter that is also called client_secret
        # after this line executes, oauth will now be an instance of the class OAuth1Session
        oauth = requests_oauthlib.OAuth1Session(client_key, client_secret=client_secret)

        request_token_url = 'https://api.twitter.com/oauth/request_token'

        # invoke the fetch_request_token method of the class OAuth1Session on our instance
        # it returns a dictionary that might look like this:
        # {
        #     "oauth_token": "Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik",
        #     "oauth_token_secret": "Kd75W4OQfb2oJTV0vzGzeXftVAwgMnEK9MumzYcM"
        # }
        # It also saves the oauth_token as an instance variable of the object
        # oauth is bound to, so it can be used in later steps
        fetch_response = oauth.fetch_request_token(request_token_url)

        # pull the two values out of the dictionary and store them in a variable for later use
        # note that d.get('somekey') is another way of writing d['somekey']
        resource_owner_key = fetch_response.get('oauth_token')
        resource_owner_secret = fetch_response.get('oauth_token_secret')

        ## Step 2. Obtain authorization from the user (resource owner) to access their protected resources (images, tweets, etc.). This is commonly done by redirecting the user to a specific url to which you add the request token as a query parameter. Note that not all services will give you a verifier even if they should. Also the oauth_token given here will be the same as the one in the previous step.

        base_authorization_url = 'https://api.twitter.com/oauth/authorize'
        # append the query parameters need to make it a full url.
        # they will include the resource_owner_key from the previus step,
        # which was stored in the oauth object above as an instance variable
        # when fetch_request_token was invoked
        authorization_url = oauth.authorization_url(base_authorization_url)

        webbrowser.open(authorization_url)

        # After the user authenticates at Twitter, it would normally "redirect"
        # the browser back to our website. But we aren't running a website.
        # Some services, like Twitter, will let you configure the app to 
        # display a verifier, or the entire redirect url, rather than actually
        # redirecting to it.
        # User will have to cut and paste the verifier or the whole redirect url

        # version where the website provides a verifier
        verifier = raw_input('Please input the verifier>>> ')

        # version where the website provides the entire redirect url
        # redirect_response = raw_input('Paste the full redirect URL here: ')
        # oauth_response = oauth.parse_authorization_response(redirect_response)
        # get back something like this
        #{
        #    "oauth_token": "Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik",
        #    "oauth_verifier": "sdflk3450FASDLJasd2349dfs"
        #}
        # verifier = oauth_response.get('oauth_verifier')

        ## Step 3. Obtain an access token from the OAuth provider. Save this token so it can be re-used later. 
        # In this step we re-use most of the credentials obtained up to this point.

        # make a new instance of OAuth1Session, with several more parameters filled in
        oauth = requests_oauthlib.OAuth1Session(client_key,
                                  client_secret=client_secret,
                                  resource_owner_key=resource_owner_key,
                                  resource_owner_secret=resource_owner_secret,
                                  verifier=verifier)
                                  
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        oauth_tokens = oauth.fetch_access_token(access_token_url)
        # get back something like this
        #{
        #    "oauth_token": "6253282-eWudHldSbIaelX7swmsiHImEL4KiNdrY",
        #    "oauth_token_secret": "2EEfA6BG3ly3sR3RjE0IBSnKmrkVU"
        #}
        resource_owner_key = oauth_tokens.get('oauth_token')
        resource_owner_secret = oauth_tokens.get('oauth_token_secret')
        
        return (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier)

    try:
        # See if you can read the credentials from the file
        # (If you have credentials for the wrong user, or expired credentials
        # just delete the file creds.txt
        f = open("creds.txt", 'r')
        (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier) = json.loads(f.read())
        f.close()
    except:
        # If not, you'll have to get them
        # and then save them in creds.txt
        tokens = get_tokens()
        f = open("creds.txt", 'w')
        f.write(json.dumps(tokens))
        f.close()
        (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier) = tokens
      
    ## Step 4. Access protected resources. 

    # For endpoints that might be interesting to try, see
    # https://dev.twitter.com/rest/tools/console and
    # https://dev.twitter.com/rest/public
    protected_url = 'https://api.twitter.com/1.1/account/settings.json'
    oauth = requests_oauthlib.OAuth1Session(client_key,
                            client_secret=client_secret,
                            resource_owner_key=resource_owner_key,
                            resource_owner_secret=resource_owner_secret)

    # Call the get method. The work of encoding the client_secret 
    # and "signing" the request is taken care of behind the scenes.
    # The results are also processed for you, including calling .read() and 
    # encoding as json.
    #r = oauth.get(protected_url)
    # r is now an instance of the Response class in the requests module
    # documentation at 
    # http://docs.python-requests.org/en/latest/user/quickstart/#response-content

    # Of particular interest to us is the json() method of the Response class
    #print pretty(r.json())


    r = oauth.get("https://api.twitter.com/1.1/search/tweets.json", params = {'q': 'University of Michigan', 'count' : 3}) # request to the Tweet search endpoint, searching for the phrase 'University of Michigan', looking to get 3 Tweets back

    # investigate the data
    print type(r.json())
    # print json.dumps(r.json(), indent=2)
    res = r.json()
    print res.keys()
    # print pretty(res)
    # cache data
    f = open('nested.txt', 'w')
    f.write(json.dumps(res))
    f.close()