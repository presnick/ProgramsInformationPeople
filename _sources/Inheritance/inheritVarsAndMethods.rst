intro.rst..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Inheriting Variables and Methods
================================

.. index:: Mechanics of defining a subclass

Mechanics of Defining a Subclass
--------------------------------

We said that inheritance provides us a more elegant way of, for example, creating  ``Dog`` and ``Cat`` types, rather than making a very complex ``Pet`` class. In the abstract, this is pretty intuitive: all pets have certain things, but dogs are different from cats, which are different from birds. Going a step further, a Collie dog is different from a Labrador dog, for example. Inheritance provides us with an easy and elegant way to represent these differences.

Basically, it works by defining a new class, and using a special syntax to show what the new class _inherits from._ So if you wanted to define a ``Dog`` class as a special kind of ``Pet``, you would say that the ``Dog`` type inherits from the ``Pet`` type. In the definition of the inherited class, you only need to specify the methods and instance variables that are different from the parent class (the **parent class**, or the **superclass**,  is what we may call the class that is _inherited from_. In the example we're discussing, `` Pet`` would be the superclass of ``Dog`` or ``Cat``).

Here is an example. Say we want to define a class ``Cat`` that inherits from ``Pet``. Assume we have the ``Pet`` class that we defined earlier.

We want the ``Cat`` type to be exactly the same as ``Pet``, _except_ we want the sound cats start out with to be "meow", not "mrrp", and we want the ``Cat`` class to have its own special method called ``chasing_rats``, which only ``Cat``s have, not just any pet.

.. activecode:: inheritance_cat_example
    :nocanvas:
    :include: tamagotchi_1

    class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
        sounds = ['Meow!']

        def chasing_rats(self):
            return "What are you doing, Pinky? Taking over the world?!"

That's all we need! The elegance of inheritance allows us to specify just the differences in the new, inherited class. In that code, we make sure the ``Cat`` class inherits from the ``Pet`` class, and in the new definition, we only need to define the things that are different from the ones in the ``Pet`` class.

In this case, the only difference is that the class variable `` sounds `` starts out with the string ``"Meow"`` instead of the string ``"mrrp"``. 

We can still use all the ``Pet`` methods in the ``Cat`` class, this way. You can call the ``__str__`` method on an instance of ``Cat`` to ``print`` an instance of ``Cat``, the same way you could call it on an instance of ``Pet``, and the same is true for the ``hi`` method -- it's the same for instances of ``Cat`` and ``Pet``. But the ``chasing_rats`` method is special: it's only usable on ``Cat`` instances, because ``Cat`` is a subclass of ``Pet`` which has that additional method.

In the original Tamagotchi game in the last chapter, you saw code that created instances of the ``Pet`` class. Now let's write a little bit of code that uses instances of the ``Pet`` class AND instances of the ``Cat`` class.

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

And you can continue the inheritance tree. We inherited ``Cat`` from ``Pet``. Now say we want a subclass of ``Cat`` called ``Cheshire``. A Cheshire cat should inherit everything from ``Cat``, which means it inherits everything that ``Cat`` inherits from ``Pet``, too. But the ``Cheshire`` class has its own special method, ``smile``.

.. activecode:: inheritance_cheshire_example
    :nocanvas:
    :include: inheritance_cat_example

    class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

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
    new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
    new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

    # cat1.smile() # This line would give you an error, because the Cat class does not have this method!

    # None of the subclass methods can be used on the parent class, though.
    p1 = Pet("Teddy")
    p1.hi() # same as all the others
    #p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
    #p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.


.. index:: How the interpreter looks up attributes

How the interpreter looks up attributes
---------------------------------------

So what is happening in the Python interpreter when you write programs with classes, subclasses, and instances of both parent classes and subclasses?

**This is how the interpreter looks up attributes:**

1. First, it checks for an instance variable or an instance method by the name it's looking for.
2. If an instance variable or method by that name is not found, it checks for a class variable. (See the previous chapter for an explanation of the difference between **instance variables** and **class variables**.)
3. If no class variable is found, it looks for a class variable in the parent class.
4. If no class variable is found _there_, the interpreter looks for a class variable in THAT class's parent, if it exists -- the "grandparent" class (that's how you can think about it, though most programmers won't use the "grandparent" terminology).
5. This process goes on until the last parent is reached, at which point Python will signal an error.

Let's look at this with respect to some code.

Say you write the lines: 

``new_cat = Cheshire("Pumpkin")
  print new_cat.name``

In the second line, after the instance is created, Python looks for the instance variable ``name`` in the ``new_cat`` instance.  In this case, it exists. The name on this instance of ``Cheshire`` is ``Pumpkin``. There you go!

When the following lines of code are written and executed:

``cat1 = Cat("Sepia")
  cat1.hi()``

Python looks for ``hi`` on the instance of ``Cat``. It does not find it -- the ``Cat`` class does not have a specific ``hi`` instance variable or method. 

(Be careful here -- if you had set an **instance variable** on Cat called ``hi``, you would not be able to use the **instance method** that it inherited anymore. We'll see more about this later.)

Next, it looks for an instance variable ``hi`` on the parent class of ``Cat``, ``Pet``. It finds that -- there's an **instance method** called ``hi`` on the class ``Pet``. It is being called, with ``()``, and it is a method, so it can be called. All is well.

However, for Python lines like

``p1 = Pet("Teddy")
  p1.chasing_rats()``

That won't go so well. Python looks for an instance variable or method called ``chasing_rats`` on the ``Pet`` class. It doesn't exist. ``Pet`` has no parent classes, so Python signals an error.


We've seen this idea before. 

Remember: if you assign ``x = 5`` in a program, and later in the same program, assign ``x = 12``, as we've seen many times now, the variable ``x`` will hold the value ``12`` at the end of the program, assuming nothing else has changed it.

Similarly, if you define a variable in a program ``str = "hello"`` for example, that's just fine, _except_ it could cause you a problem: now, you can't use the built-in Python ``str()`` function to turn things into type String, because the name ``str`` is now bound to the string ``"hello"`` instead of to the function that makes things the ``String`` type. The same sort of thing is happening here. Trace through the code you write with classes and instances and follow that list, thinking about how Python is evaluating your code. As always, that can help you diagnose errors.

