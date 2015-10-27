..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _inheritance_chap:

Introduction: Class Inheritance
===============================

Classes can "inherit" methods and class variables from other classes. We'll see the mechanics of how this works in subsequent sections. First, however, let's motivate why this might be valuable. It turns out that inheritance doesn't let you do anything that you couldn't do without it, but it makes some things a lot more elegant. You will also find it's useful when someone else has defined a class in a module or library, and you just want to override a few things without having to reimplement everything they've done.

Consider our Tamagotchi game. Suppose we wanted to make some different kinds of pets that have the same structure as other pets, but have some different attributes or behave a little differently. For example, suppose that dog pets should show their emotional state a little differently than cats or act differently when they are hungry or when they are asked to fetch something.

Could implement this by making instance variable for the pet type and dispatching on that instance variable in all the methods.

<code example here>

But that's not an elegant way to do it. It obscures the parts of being a pet that are common to all pets and it distributes all the unique stuff about being a dog or a cat into lots of different methods. You can imagine that if there were lots of different types of pets, those methods would start to have long and complex if..elif..elif code clauses. Class inheritance will give us a more elegant way to do it.
