..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _mkdir_and_cp_sect:

Unix for utility
----------------

Unix commands are helpful for many reasons. The command line, as you've read, is basically a textual interface for doing things in your computer. The images you're probably used to, like icons of folders you can click on to see what's inside them, are useful for many people and make a lot of conceptual sense to most people. However, there are a lot of mechanics you are likely to want to do quickly on your computer, especially if you are a programmer or if you are working with a bunch of files for any reason. Some of these that we'll take a look at are the actions of making a new folder and copying one or more files from one place in your computer to another. 

You may be used to right-clicking and hitting *New folder*, or opening a file in a program and using the menu to go *Edit > Copy* and then *Edit > Paste*, for instance. But those clicks take time and require you to have opened the right windows. In this section we'll learn Unix commands for these things, among others, that will let you pop open your command line window and let you create a new folder or copy a file anywhere.

The mkdir command
-----------------

The ``mkdir`` command creates a brand new directory. 

Say you have accessed your ``Desktop`` folder and you are interested in making a new directory in your ``Desktop`` called ``Funny_pictures``. You might want to use the ``pwd`` command to ensure that you are where you think you are in your file system. Assuming you are, and that's where you want to make your new folder, it's easy: ``mkdir Funny_pictures``. There you go -- now you can ``cd Funny_pictures`` and ``ls`` to see what's inside it (although until you put files in it, there's nothing to see with ``ls``, of course).

But now, go back to what you know about folders and paths. Say you've navigated to your ``Desktop``. You know (and can check using your Unix skills) that you have a folder inside the Desktop called ``106`` and a folder inside *that* directory called ``ps1``. But now, you want to make *another* folder inside the ``ps1`` directory, called **ps1_subfolder**. All you need to do is use the ``mkdir`` command with the full path (or the relative path to where you are currently navigated). 

For example, knowing the full path of the new folder you want to create, you'd type at your command prompt: ``mkdir ~/Desktop/106/ps1/ps1_subfolder``. 

You can then use ``cd`` or ``ls`` to check that the new directory really exists. ``~/Desktop/106/ps1/ps1_subfolder`` is the *full path* of the brand new directory that you want to make. ``mkdir`` means "make a directory that has the path that comes after this command". As long as no identically named directory exists, and the path is a valid one, you'll be fine. 

(Remember, you can't create a directory inside a file -- that doesn't make sense -- and you can't create more than one directory at the same time this way. If ``ps1`` did *not* exist, that command above would not work: first you'd need to use your file system windows or ``mkdir`` to create ``ps1``, and then you could put a new directory called ``ps1_subfolder`` inside of it.)


The cp command
--------------

The ``cp`` command is a useful way to copy files from one place to another in your computer, and a command that is particularly useful for programming, once you begin using multiple files. Just like using *Edit > Copy* and *Edit > Paste* clicks, it doesn't change anything about your original file -- it just copies it to another place as well, with one quick command. And just like using the edit menu to copy and paste, you still have to be careful about which copy you start working on!

The syntax goes like this: ``cp`` **<path of the file you want to copy>** **<path of the location you want that file copied to>**, with a space in between each, at your Unix command prompt.

Say you want to copy the file ``test.txt`` from your ``106/ps1`` folder to your ``Desktop`` (so it will exist in the ``ps1`` folder, and there will *also* be a copy on your ``Desktop``): ``cp ~/Desktop/106/ps1/test.txt ~/Desktop``. 

There are a couple Unix tricks that are especially useful when you are using the ``cp`` command. First, the use of ``.`` and ``..``. If you want to copy a file to the place you are currently navigated to in your command prompt, you can type ``cp <whatever file path you want to copy>> .`` That means, "copy <that file path> to here."

You can do the same using the ``..`` that you learned about for the ``cd`` command. ``.`` means **the current directory**, but ``..`` means **the directory one level up from here**.

The other useful thing to know for ``cp`` (and other Unix commands) is that the asterisk, ``*``, means "all". So, for example, if you want to copy ALL of the files from your desktop to your ``ps2`` folder, you could type: ``cp ~/Desktop/* ~/Desktop/106/ps2``. (I wouldn't recommend doing this, though. That's probably a lot of files you don't need in your 106 folder.)

You cannot copy **directories** this way, though -- only plain files. You can use the ``cp`` command to copy directories, but it requires using an addition to the command called a **flag** that we haven't learned about yet.

You can imagine how you can combine use of the commands you already know with the ``cp`` and the ``mkdir`` commands to do useful things. You now know enough Unix commands to make new directories and copy whole sets of files from one folder to another with just a keyboard and your command prompt. Or you can make a new folder, copy files into that new folder, and list the file names to check that the files you expect to be there are indeed there.



