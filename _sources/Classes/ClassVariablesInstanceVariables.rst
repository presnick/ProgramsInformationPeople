..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Class Variables and Instance Variables
--------------------------------------

Class variables are shared by all instances.

How to set instance variables:
* <obj>.varname = <expr>

How to set class variables:
* varname = <expr> at top-level in class definition

How interpreter looks up attributes:
* first check for instance variable
* if not found, check for class variable (this is repeat from something in previous chapter)

Methods are class variables.

Example...