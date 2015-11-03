..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".



Invoking the Parent Class' Method
=================================

Sometimes the parent class has a useful method, but you just need to execute a little extra code when running the subclass' method. You can override the parent class' method in the subclass' method with the same name, but also invoket he parent class' method. Here's how.

Say you wanted the `` Dog `` subclass of `` Pet `` to say "Arf! Thanks!" when the `` feed_me `` method is called, as well as the code in the original method.

.. activecode:: feed_me_example
    :nocanvas:
    :include: tamagotchi_1
    :include: inheritance_cat_example

    from random import randrange

    class Dog(Pet):
    	def feed_me(self):
    		Pet.feed_me(self)
    		print "Arf! Thanks!"

    # Now let's create a Dog instance, and see this work.

    dog1 = Dog("Spot")
    dog1.feed_me()

    # For Pet instances, the extra code won't run
    another_pet = Pet("Generic")
    another_pet.feed_me() 

This technique is very often used with the `` __init__ `` method for a subclass. Suppose that some extra instance variables are defined for the subclass. When you invoke the constructor, you pass all the regular parameters for the parent class, plus the extra ones for the subclass. The subclass' `` __init__ `` method then stores the extra parameters in instance variables and calls the parent class' 	`` __init__ `` method to store the common parameters in instance variables and do any other initialization that it normally does.

Let's say we want to create a subclass of `` Pet ``, called `` Bird ``, and we want it to take an extra parameter, `` chirp_number ``, with a default value of 1, and have an extra instance variable, `` self.chirp_number ``. (We'll decide how to use this special bird instance variable later on.)

.. activecode:: super_methods_1
    :nocanvas:
    :include: tamagotchi_1
    :include: inheritance_cat_example

    class Bird(Pet):
    	def __init__(self,name="Kitty",chirp_number=1):
    		super(Bird,self,name).__init__() # call the parent class's constructor
    		# basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
    		self.chirp_number = 1 # now, also assign the new instance variable

Having done this, perhaps we also would want to redefine the `` hi `` method for the `` Bird `` class, so instead of what happens in the `` Pet `` class, a `` Bird `` makes a sound whatever number of times its `` chirp_number `` is set to. We'll see how to do this in the following section.
