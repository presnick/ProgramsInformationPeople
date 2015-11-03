..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Overriding Methods
==================

If a method is defined for a class, and also defined for its parent class, the subclass' method is called and not the parent's. This follows from the rules for looking up attributes.

If you assign `` x = 5 `` and later in the same program, assign `` x = 12 ``, as we've seen many times now, the variable `` x `` will hold the value `` 12 `` at the end of the program, assuming nothing else has changed it.

Similarly (we'll see more about this later in the textbook), if you define a variable in a program `` str = "hello" `` for example, that's just fine, _except_ it could cause you a problem: now, you can't use the built-in Python `` str() `` function to turn things into type String, because the name `` str `` is now bound to the string `` "hello" `` instead of to the function that makes things the `` String `` type.

Now that we are looking at class inheritance, we can use the same idea to understand overriding methods. We've seen how to invoke superclass methods, methods that belong to a parent class, inside a method of the same name in the inherited class. But what if you wanted a method on the `` Bird `` class to do a very different thing from what it does on the original `` Pet `` class? 

To follow along with our example, let's take the `` Bird `` class we just defined, which has a new, extra parameter called `` chirp_number ``, and a new instance variable, `` self.chirp_number ``. For the `` Bird `` method `` hi ``, we want the sound a bird makes to appear `` self.chirp_number `` times.

.. activecode:: override_methods_1
    :nocanvas:

    from random import randrange

    class Bird(Pet):
    	def __init__(self,name="Kitty",chirp_number=1):
    		super(Bird,self,name).__init__() # call the parent class's constructor
    		# basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
    		self.chirp_number = 1 # now, also assign the new instance variable

    	# Now let's define the new hi method for Bird.
    	def hi(self):
    		for i in range(self.chirp_number):
    			print self.sounds[randrange(len(self.sounds))]

    # Now let's try it with some class instances and see 

    p1 = Pet("Spark") # create an instance of Pet with the name Spark
    print p1 # print the string representation of the pet
    p1.hi() # call the hi method on the pet

    b1 = Bird("Sylvester",4) # create a Bird instance with the name Sylvester and the chirp_number 4
    print b1 # print the string representation of the bird, which is just like the pet representation
    b1.hi() # call the hi method on the bird -- see that it does something different! 
    # The Bird hi method was called, not the Pet hi method, because this is a Bird instance.

Knowing all this, we can make a more complex version of the Tamagotchi game, with different types of pets, avoiding complex and confusing if/elif/else statements.
