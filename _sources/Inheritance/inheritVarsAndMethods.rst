intro.rst..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Inheriting Variables and Methods
================================

Mechanics of defining a subclass
* generic
* Dog and Cat classes

Inheriting variables and methods
* illustrate inherited and new variables and methods

How interpreter looks up attributes:
* first check for instance variable
* if not found, check for class variable (this is repeat from something in previous chapter)
* if no class variable found, look for class variable in parent
* if not there, look in it's parent, etc.
* if not found anywhere, signal an error

.. index:: Mechanics of defining a subclass

Mechanics of Defining a Subclass
--------------------------------

We said that inheritance provides us a more elegant way of, for example, creating  `` Dog `` and `` Cat `` types, rather than making a very complex `` Pet `` class. In the abstract, this is pretty intuitive: all pets have certain things, but dogs are different from cats, which are different from birds. Going a step further, a Collie dog is different from a Labrador dog, for example. Inheritance provides us with an easy and elegant way to represent these differences.

Basically, it works by defining a new class, and using a special syntax to show what the new class _inherits from._ So if you wanted to define a `` Dog `` class as a special kind of `` Pet ``, you would say that the `` Dog `` type inherits from the `` Pet `` type. In the definition of the inherited class, you only need to specify the methods and instance variables that are different from the parent class (the **parent class**, or the **superclass**,  is what we may call the class that is _inherited from_. In the example we're discussing, `` Pet`` would be the superclass of `` Dog `` or `` Cat ``).

Here is an example. Say we want to define a class `` Cat `` that inherits from `` Pet ``. Assume we have the `` Pet `` class that we defined earlier.

We want the `` Cat `` type to be exactly the same as `` Pet ``, _except_ we want the sound cats start out with to be "meow", not "mrrp", and we want the `` Cat `` class to have its own special method called `` chasing_rats ``, which only `` Cat ``s have, not just any pet.

.. activecode:: inheritance_cat_example
    :nocanvas:
    :include: tamagotchi_1

    class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    	sounds = ['Meow!']

    	def chasing_rats(self):
    		return "What are you doing, Pinky? Taking over the world?!"

That's all we need! The elegance of inheritance allows us to specify just the differences in the new, inherited class. In that code, we make sure the `` Cat `` class inherits from the `` Pet `` class, and in the new definition, we only need to define the things that are different from the ones in the `` Pet `` class.

In this case, the only difference is that the class variable `` sounds `` starts out with the string `` "Meow" `` instead of the string `` "mrrp" ``. 

We can still use all the `` Pet `` methods in the `` Cat `` class. You can call the `` __str__ `` method on an instance of `` Cat `` the same way you could call it on an instance of `` Pet ``, or the `` hi `` method. 

In the original Tamagotchi game in the last chapter, you saw code that created instances of the `` Pet `` class. Now let's write a little bit of code that uses instances of the `` Pet `` class AND instances of the `` Cat `` class.

.. activecode:: tamagotchi_2
    :nocanvas:
    :include: inheritance_cat_example

    p1 = Pet("Fido")
    print p1 # we've seen this stuff before!

    p1.feed()
    p1.hi()
    print p1

    cat1 = Cat("Fluffy")
    print cat1 # this uses the same __str__ method as the Pets do

    cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
    cat1.hi()
    print cat1

    print cat1.chasing_rats() 

    #print p1.chasing_rats() # This line will give us an error. The Pet class doesn't have this method!

And you can continue the inheritance tree. We inherited `` Cat `` from `` Pet ``. Now say we want a subclass of `` Cat `` called `` Cheshire ``. A Cheshire should inherit everything from `` Cat ``, which means it inherits everything that Cat inherits from `` Pet ``, too. But the `` Cheshire `` class has its own special method, `` smile ``.

.. activecode:: inheritance_bobtail_example
	:nocanvas:
    :include: inheritance_cat_example

    class Bobtail(Cat): # this inherits from Cat, which inherits from Pet

    	def smile(self): # this method is specific to instances of Bobcat
    		print ":D :D :D"

    # Let's try it with instances.
    cat1 = Cat("Fluffy")
    cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
    cat1.hi()
    print cat1

    print cat1.chasing_rats() 

    new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
    new_cat.hi() # same as Pet and Cat!
    new_cat.chasing_rats() # OK, because Bobtail inherits from Cat
    new_cat.smile() # Special for Bobtail instances

    # cat1.smile() # This line would give you an error, because the Cat class does not have this method!

