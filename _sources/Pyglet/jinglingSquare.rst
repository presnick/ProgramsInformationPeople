..  Copyright (C)  Sam Carton and Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

A Movable Sqaure with Jingles
-----------------------------

The ultimate goal is to put drawing objects together with event detection to create interactive visual applications.

Here we give one example, a simple little game that lets the player move a white square around the window using the arrow keys, and which makes a jingling noise when they hit the space key:

.. code:: python

    import pyglet
    import sys
    pyglet.options['audio'] = ('openal', 'silent')

    class GameWindow(pyglet.window.Window):

        square_speed = 6

        def __init__(self,*args,**kwargs):
            pyglet.window.Window.__init__(*args,**kwargs)

            image = pyglet.image.load('white_square.png')
            self.image_sprite = pyglet.sprite.Sprite(image,
                      x=self.width//2, y=self.height//2)

        def on_key_press(self, symbol, modifiers):
            '''
            If the user presses an arrow key, move the square accordingly.
            If they press space bar, make a noise.
            If they press Q or ESC, quit
            :param symbol:
            :param modifiers:
            :return:
            '''

            if symbol == pyglet.window.key.Q or symbol == pyglet.window.key.ESCAPE:
                print 'Exit key detected. Exiting game...'
                exit(0)
            elif symbol == pyglet.window.key.SPACE:
                self.make_sound()
            elif symbol == pyglet.window.key.UP:
                self.image_sprite.set_position(self.image_sprite.x,self.image_sprite.y+self.square_speed)
            elif symbol == pyglet.window.key.DOWN:
                self.image_sprite.set_position(self.image_sprite.x,self.image_sprite.y-self.square_speed)
            elif symbol == pyglet.window.key.RIGHT:
                self.image_sprite.set_position(self.image_sprite.x+self.square_speed,self.image_sprite.y)
            elif symbol == pyglet.window.key.LEFT:
                self.image_sprite.set_position(self.image_sprite.x-self.square_speed,self.image_sprite.y)


        def on_draw(self):
            self.clear()
            self.image_sprite.draw()


        def make_sound(self):
            source = pyglet.media.load('bicycle_bell.wav', streaming=False)
            source.play()


    game_window = GameWindow()
    pyglet.app.run()

You can see that most of the "game logic", such as it is, takes place in the ``on_key_press()`` method. In this method, the game interprets the key being pressed, and makes a decision about what to do based on what key was pressed. In this case, it just changes the position of the sprite, moving it in a direction determined by the key press. The ``on_draw()`` method updates the window to accommodate the new situation. In this case it just clears it completely and redraws the one sprite that is part of the window.

Most games, at least most simple games, are going to look like this: a few visual elements that move around and change based on user input, as interpreted through event-handling functions such as ``on_key_press()`` or ``on_mouse_click()``.
