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

