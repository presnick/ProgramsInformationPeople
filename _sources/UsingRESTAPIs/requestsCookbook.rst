..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _using_RESTAPIs_chap:

Requests Cookbook
=================

:ref:`Previously<rest_apis_chap>`, you learned about REST APIs and the mechanics of accessing them using the requests module. This chapter describes a process that you can use for writing programs that use the requests module to access data from REST APIs, a cookbook of sorts.

The basic process involves three steps:

1. Make the appropriate call to requests.get()
2. Extract content from response object
3. Process the data data you've extracted

The key to success is to make sure that you debug each of those steps before going on to the next one. This is just a particular case of the :ref:`general advice <debugging_chap>` we gave early in the course: start small and keep it working at every stage, growing the amount that your program does over time.

We cover each of the three steps in its own section.


