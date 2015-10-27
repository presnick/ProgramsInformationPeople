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
* illustration with feed_me()

This technique is very often used with the __init__ method for a subclass. Suppose that some extra instance variables are defined for the subclass. When you invoke the constructor, you pass all the regular parameters for the parent class, plus the extra ones for the subclass. The subclass' __init__ method then stores the extra parameters in instance variables and calls the parent class' __init__ method to store the common parameters in instance variables and do any other initialization that it normally does.
* illustrate with an example
