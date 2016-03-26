..  Copyright (C)  Sam Carton and Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Making Sounds
-------------

Pyglet can also be used to make sounds. Doing so is a three step process:

1) Tell Pyglet what audio driver to use

2) Load a sound file into a Pyglet object with ``pyglet.media.load``

3) Use that object's ``play()`` method.

Here is some code that demonstrates this:

.. code:: python

    import pyglet
    import sys

    #Tell pyglet what driver to use
    pyglet.options['audio'] = ('openal', 'silent')

    class SoundWindow(pyglet.window.Window):

        def __init__(self,*args,**kwargs):
            pyglet.window.Window.__init__(self, *args,**kwargs)



        def on_draw(self):
            print 'The window was drawn!'
            print 'We are going to make a noise'
            sys.stdout.flush()
            self.make_sound()


        def make_sound(self):
            source = pyglet.media.load('bicycle_bell.wav', streaming=False)
            source.play()

    sound_window = SoundWindow()
    pyglet.app.run()

We won't show a screenshot of the result as they are not visual, but trust us--it works. Note that we set the keyword argument ``streaming=False`` in our invocation of ``pyglet.media.load``. This allows us to play the sound multiple times, which in most cases we will want to do. However, if you only wanted to play a sound once, you could omit this parameter.

If you want to run this code for yourself, you will have to download a .wav file and put it in the same directory as this script. The one used in the example can be found here: http://www.wavsource.com/snds_2015-11-01_1874590815319647/sfx/bicycle_bell.wav

You may also need to install the openal package, from http://openal.org.

The full documentation on making sounds (and video) in Pyglet can be found here: https://pyglet.readthedocs.org/en/pyglet-1.2-maintenance/programming_guide/media.html
