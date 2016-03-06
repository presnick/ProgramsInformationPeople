..  Copyright (C)  Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _thinking_about_classes:

Defining Classes with Data from the Internet
--------------------------------------------

Considering those questions when you write a new class definition is always important, but it can be especially tricky when you are using classes to deal with data that you get from an API request.

Using the `iTunes Search API <https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api>`_ as an example, we'll look at an example of defining a class to represent a song.

This API has several parameters, some of which are optional. The ones we'll care about for now are ``term``, whose value is a string term to search for (``the beatles`` maybe), and ``entity``, which can be ``song`` or ``album``.

You can read the documentation and make a few requests to the API to see what the nested data response you get looks like. 

It turns out that if you make a request like this:

``resp = requests.get("",params={"term":"beatles","entity":"song"}).json()``

you get data back that *includes* a big list of dicitionaries that represent songs. You have to parse through the nested data a little bit to save that list in a variable (remember the :ref:`Nested Data Structures<nested_chap>` chapter!), but once you're there, you can play around with it and look at the information it contains. Here's an example of part of that list.

``
[{u'artistId': 136975,
  u'artistName': u'The Beatles',
  u'artistViewUrl': u'https://itunes.apple.com/us/artist/the-beatles/id136975?uo=4',
  u'artworkUrl100': u'http://is3.mzstatic.com/image/thumb/Music/v4/40/d0/29/40d029b5-4c32-53d2-69d1-ea04a513c345/source/100x100bb.jpg',
  u'artworkUrl30': u'http://is3.mzstatic.com/image/thumb/Music/v4/40/d0/29/40d029b5-4c32-53d2-69d1-ea04a513c345/source/30x30bb.jpg',
  u'artworkUrl60': u'http://is3.mzstatic.com/image/thumb/Music/v4/40/d0/29/40d029b5-4c32-53d2-69d1-ea04a513c345/source/60x60bb.jpg',
  u'collectionCensoredName': u'Abbey Road',
  u'collectionExplicitness': u'notExplicit',
  u'collectionId': 401186200,
  u'collectionName': u'Abbey Road',
  u'collectionPrice': 12.99,
  u'collectionViewUrl': u'https://itunes.apple.com/us/album/here-comes-the-sun/id401186200?i=401187150&uo=4',
  u'country': u'USA',
  u'currency': u'USD',
  u'discCount': 1,
  u'discNumber': 1,
  u'isStreamable': True,
  u'kind': u'song',
  u'previewUrl': u'http://a184.phobos.apple.com/us/r1000/017/Music6/v4/e7/78/b5/e778b5ed-87d7-d81c-ef4e-ce2065ac8b55/mzaf_7495287073647867305.plus.aac.p.m4a',
  u'primaryGenreName': u'Rock',
  u'releaseDate': u'1969-09-26T07:00:00Z',
  u'trackCensoredName': u'Here Comes the Sun',
  u'trackCount': 17,
  u'trackExplicitness': u'notExplicit',
  u'trackId': 401187150,
  u'trackName': u'Here Comes the Sun',
  u'trackNumber': 7,
  u'trackPrice': 1.29,
  u'trackTimeMillis': 185733,
  u'trackViewUrl': u'https://itunes.apple.com/us/album/here-comes-the-sun/id401186200?i=401187150&uo=4',
  u'wrapperType': u'track'}]``

This is a little difficult to parse (look back at the NESTED DATA CHAPTER), but we can skip ahead to the class definition (try using the API yourself!).

You know that once you've made a request to this API and gotten some data, you'll be able to access a bunch of dictionaries, and each dictionary holds a bunch of information about a song. 

Next, you can answer the questions we posed in the last section about your class definition. Here, we'll choose some answers so we can write an example class definition -- but the way you answer these questions will depend upon what program you want to write! If you want your class instances to be able to do slightly different things, you would write different methods. If different information is important to you, you would create different instance variables, and so on.

**What is the data that you want to deal with?** Dictionaries that represent songs, where each contains key-value pairs that hold information about a song.

**What will one instance of your class represent?** One song.

**What information should each instance have as instance variables?** Each instance represents one song, and each song has an artist and a title as instance variables.

**What instance methods should each instance have?** Each song instance should have a method that returns the artist's name. And each song instance should have a method that returns the number of vowels in the song's title. (Maybe because you want to do some linguistic analysis about song titles in your program.)

**What should the printed version of an instance look like?** A printed version of a song instance should show the song title and the artist's name.

Finally, you should ask yourself: what information gets passed into the constructor of the class to create an instance of this class? 

In this case, you have a bunch of dictionaries available in the data you got back from the API request above. And each dictionary represents a song. So you can pass in a song dictionary to the constructor!

Below is an example of the class definition we just described.

.. activecode:: classdata_1

    class Song:
        """ A class to represent one song, from data received from the iTunes API. """

        def __init__(self, song_dictionary):

            self.title = song_dictionary[u"trackName"]
            self.artist = song_dictionary[u"artistName"]

        def get_song_artist(self):
        	return self.artist

        def title_number_vowels(self):
        	vowels = "aeiou"
        	tot = 0
        	for ch in self.title:
        		if ch in vowels:
        			tot = tot + 1
        	return tot

        def __str__(self):
        	return "Title: {}\nArtist: {}".format(self.title,self.artist)


