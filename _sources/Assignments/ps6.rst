:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500


Activities through 2/21
=======================

You have the following graded activities:

* Before Monday's class:
    * Read :ref:`Optional and Keyword Parameters<optional_params_chap>`, and do the exercises in that chapter

* **By Tuesday 2/16 midnight:**
    * Read `Tutorial on unix diff <http://www.computerhope.com/unix/udiff.htm>`_ (This will help you understand the section of "The Most Human Human" below)
    * Read *The Most Human Human*, Chapter 10, p.237-259.
    * Answer `Reading Response 7 <https://umich.instructure.com/courses/48961/assignments/57683>`_ on Canvas.

.. usageassignment:: prep_11
    :chapters: OptionalAndKeywordParameters
    :assignment_name: Prep a11
    :deadline: 2016-02-16 21:30:00
    :pct_required: 80
    :points: 50

* Before Wednesday's class:
   * Read :ref:`Tuples<tuples_chap>`, and do the exercises in that chapter
   * Read :ref:`Nested Data Structures and Nested Iteration<nested_chap>`, and do the exercises in that chapter

.. usageassignment:: prep_12
    :chapters: Tuples, NestedData
    :assignment_name: Prep a12
    :deadline: 2016-02-18 21:30:00
    :pct_required: 80
    :points: 50

* By Sunday 02/21 at 5PM:
   * Save answers to the exercises in Problem Set 6: :ref:`Problem Set 6 <problem_set_6>`. 

* By Monday 10/23 at 7PM:
   * Be ready for the midterm exam (7 pm), see syllabus.

   * Updated study materials will be announced via Canvas.

   * Suggested practice for making best use of the problem sets for review
      * Go through all the problem sets, looking at your answers and fixing them if they weren't correct.
      * Then make another pass through the problem sets. This time, don't look at your past answer or any solution set. Write new answers from scratch. See how quickly you can solve them. Make a note of any problems that take you a long time to solve.
      * Repeat as necessary. On later iterations of this process, only redo the problems that you did not solve immediately on the previous iteration.

   * We have also included a bunch of practice problems below, at the bottom of this page. None of these are graded. Some have solutions.

.. _unix_pset6:

The last problem on the Problem Set involves using the native Python interpreter, and you will submit files to **Unix Problems 6** on Canvas following the directions in that problem. This is your last problem set in the textbook environment, so make sure you have your Python interpreter installed and the process of running programs via the command line is working.

Problem Set
-----------

.. _problem_set_6:


1. Use a for loop to print the second element of each tuple in the list ``new_tuple_list``.

.. activecode:: ps_6_1

      new_tuple_list = [(1,2),(4, "umbrella"),("chair","hello"),("soda",56.2)]

2. Write three print statements with function calls to the function ``give_greeting``:

   * one that will return the string ``Hello, SI106!!!``
   * one that will return the string ``Hello, world!!!``
   * and one that will return the string ``Hey, everybody!``

You must write only the ``print`` command and function invocations of ``give_greeting`` to earn full credit on this problem.

You can see the function definition in the code below, but that's only so you can understand exactly what the code is doing, so you can choose how to invoke this function. Feel free to make comments to help yourself understand, but otherwise DO NOT change the function definition code! **HINT:** calling the function with different inputs and printing the results, to see what happens, may be helpful! Make sure your final answer prints out all three of the strings listed above.

.. activecode:: ps_6_2

   def give_greeting(greet_word="Hello",name="SI106",num_exclam=3):
      final_string = greet_word + ", " + name + "!"*num_exclam
      return final_string

   #### DO NOT change the function definition above this line (OK to add comments)

   # Write your three print statements with function calls below

   ====

   import test
   print "\n---\n\n"
   print "There are no tests for this problem -- check your output."


3. Define a function called ``mult_both`` whose input is two integers, whose default parameter values are the integers 3 and 4. The function's return value should be the two input integers multiplied together.

.. activecode:: ps_6_3

   # Write your code here

   ====

   import test
   print "\n---\n\n"
   print "Testing whether your function works as expected (calling the function mult_both)"
   try:
      test.testEqual(mult_both(), 12)
      test.testEqual(mult_both(5,10), 50)
   except:
      print "mult_both not defined or yields an error when invoked"



4. You can get data from Facebook that has nested structures which represent posts, or users, or various other types of things on Facebook. We won't put any of our actual Facebook group data on this textbook, because the textbook is publicly available on the internet, but here's a structure that is almost exactly the same as the real thing, with fake data.

Notice that the stuff in the variable ``fb_data`` is basically a big nested dictionary, with dictionaries and lists, strings and integers, inside it as keys and values. (Later in the course we'll learn how to get this kind of thing directly FROM facebook, and then it will be a bit more complicated and have real information from our Facebook group.)

Follow the directions in the comments!

.. activecode:: ps_6_4

      # First, look through the data structure saved in the variable fb_data to get a sense for it.

      fb_data = {
         "data": [
          {
            "id": "2253324325325123432madeup", 
            "from": {
              "id": "23243152523425madeup", 
              "name": "Jane Smith"
            }, 
            "to": {
              "data": [
                {
                  "name": "Your Facebook Group", 
                  "id": "432542543635453245madeup"
                }
              ]
            }, 
            "message": "This problem might use the accumulation pattern, like many problems do", 
            "type": "status", 
            "created_time": "2014-10-03T02:07:19+0000", 
            "updated_time": "2014-10-03T02:07:19+0000"
          }, 
         
          {
            "id": "2359739457974250975madeup", 
            "from": {
              "id": "4363684063madeup", 
              "name": "John Smythe"
            }, 
            "to": {
              "data": [
                {
                  "name": "Your Facebook Group", 
                  "id": "432542543635453245madeup"
                }
              ]
            }, 
            "message": "Here is a fun link about programming", 
            "type": "status", 
            "created_time": "2014-10-02T20:12:28+0000", 
            "updated_time": "2014-10-02T20:12:28+0000"
          }]
         }

      # Here are some questions to help you. We won't grade your
      # answers to these questions, but we suggest that you write
      # them in the code as comments. They may help you think through
      # this big nested data structure. Test your answers using
      # print statements.
      
      # What type is the structure saved in the variable fb_data?
      # What type does the expression fb_data["data"] evaluate to?
      # What about fb_data["data"][1]?
      # What about fb_data["data"][0]["from"]?
      # What about fb_data["data"][0]["id"]?

      # Now write a line of code to assign the value of the first 
      # message ("This problem might...") from the big fb_data data
      # structure to a variable called first_message. Do not hard code your answer! 
      # (That means, write it in terms of fb_data, so that it would work
      # with any content stored in the variable fb_data which has
      # the same structure as that of the fb_data we gave you.)

      # Write a second line of code to assign the value of the name of the second person who posted ("John Smythe") to a variable called second_name. Do not hard code your answer!


      ====

      import test
      print "testing whether variables first_message and second_name were set correctly"
      try:
         test.testEqual(first_message,fb_data["data"][0]["message"])
         test.testEqual(second_name,fb_data["data"][1]["from"]["name"])
      except:
         print "variable(s) not defined, fb_data was changed, or other error occurred"


5. In the next few questions, you’ll build components and then a complete program that lets people play Hangman. Below is an image from the middle of a game...

.. image:: Figures/HangmanSample.JPG

See the flow chart below for a better understanding of what's happening in the code for the Hangman game overall.

.. image:: Figures/HangmanFlowchart.jpg

Your first task is just to understand the logic of the program, by matching up elements of the flow chart above with elements of the code below. In later problems, you'll fill in a few details that aren't fully implemented here.  

For this question, write which lines of code go with which lines of the flow chart box, by answering the questions in comments at the bottom of this activecode box. 

(Note: you may find it helpful to run this program in order to understand it. It will tell you feedback about your last guess, but won't tell you where the correct letters were or how much health you have, and it won't stop if you guess all the letters, so you can't *really* play with this version of the code. Allowing the game to do those things is what you'll do in later problems!)

.. activecode:: ps_6_5

  def blanked(word, guesses):
      return "blanked word"

  def health_prompt(x, y):
      return "health prompt"

  def game_state_prompt(txt ="Nothing", h = 6, m_h = 6, word = "HELLO", guesses = ""):
      res = "\n" + txt + "\n"
      res = res + health_prompt(h, m_h) + "\n"
      if guesses != "":
          res = res + "Guesses so far: " + guesses.upper() + "\n"
      else:
          res = res + "No guesses so far" + "\n"
          res = res + "Word: " + blanked(word, guesses) + "\n"

      return(res)

  def main():
      max_health = 3
      health = max_health
      secret_word = raw_input("What's the word to guess? (Don't let the player see it!)")
      secret_word = secret_word.upper() # everything in all capitals to avoid confusion
      guesses_so_far = ""
      game_over = False

      feedback = "let's get started"

      # Now interactively ask the user to guess
      while not game_over:
          prompt = game_state_prompt(feedback, health, max_health, secret_word, guesses_so_far)
          next_guess = raw_input(prompt)
          next_guess = next_guess.upper()
          feedback = ""
          if len(next_guess) != 1:
              feedback = "I only understand single letter guesses. Please try again."
          elif next_guess in guesses_so_far:
              feedback = "You already guessed that"
          else:
              guesses_so_far = guesses_so_far + next_guess
              if next_guess in secret_word:
                  if blanked(secret_word, guesses_so_far) == secret_word:
                      feedback = "Congratulations"
                      game_over = True
                  else:
                      feedback = "Yes, that letter is in the word"
              else: # next_guess is not in the word secret_word
                  feedback = "Sorry, " + next_guess + " is not in the word."
                  health = health - 1
                  if health <= 0:
                      feedback = " Waah, waah, waah. Game over."
                      game_over= True
  
      print(feedback)
      print("The word was..." + secret_word)

  import sys #don't worry about this line; you'll understand it next week
  sys.setExecutionLimit(60000)     # let the game take up to a minute, 60 * 1000 milliseconds
  main()

  # What line(s) of code do what's mentioned in box 1?

  # What line(s) of code do what's mentioned in box 2?

  # What line(s) of code do what's mentioned in box 3?

  # What line(s) of code do what's mentioned in box 4?

  # What line(s) of code do what's mentioned in box 5?

  # What line(s) of code do what's mentioned in box 6?

  # What line(s) of code do what's mentioned in box 7?

  # What line(s) of code do what's mentioned in box 8?

  # What line(s) of code do what's mentioned in box 9?

  # What line(s) of code do what's mentioned in box 10?

  # What line(s) of code do what's mentioned in box 11?

         
6. The next task you have is to create a correct version of the ``blanked`` function. It should take 2 inputs: a word, and a string of the letters that have been guessed already. It should return a string with the same number of characters as the word, but with the UNrevealed characters replaced by an underscore (a ``_``). **HINT:** Iterate through the letters in the word, accumulating characters as you go. If you try to iterate through the guesses, it's harder.

.. activecode:: ps_6_6

         
    # Sample calls to this function
    # (Remember, these won't work until you define the function blanked)
    print blanked("hello", "elj")
    #should output _ell_
    print blanked("almost","amsvr")
    # should output a_m_s_ 


    ====

    import test
    try:
        print "testing blanking of hello when e,l, and j have been guessed"
        test.testEqual(blanked("hello", "elj"), "_ell_")
        print "testing blanking of hello when nothing has been guessed"
        test.testEqual(blanked("hello", ""), "_____")
        print "testing blanking of ground when r and n have been guessed"
        test.testEqual(blanked("ground", "rn"), "_r__n_")
        print "testing blanking of almost when all the letters have been guessed"
        test.testEqual(blanked("almost","vrnalmqpost"),"almost")
    except:
        print "The function blanked has not been defined yet or has an error."


7. Now you have to create a good version of the ``health_prompt`` function: Define a function called ``health_prompt``. The first parameter should be the current health the player has (an integer), and the second parameter should be the maximum health a player can have (an integer). The function should return a string with + signs for the current health, and - signs for the health that has been lost so far.

.. activecode:: ps_6_7

    # Define your function here.




    # Sample invocations of the function.

    print health_prompt(3, 7)
    #this statement should produce the output
    #health: +++----

    print health_prompt(0, 4)
    #this statement should produce the output
    #health: ----

    ====

    import test
    try:
        print "testing health_prompt(3, 7)"
        test.testEqual(health_prompt(3,7), "+++----")
        print "testing health_prompt(0, 4)"
        test.testEqual(health_prompt(0, 4), "----")
        print "testing health_prompt(5,5)"
        test.testEqual(health_prompt(5,5), "+++++")
    except:
        print "The function health_prompt is not defined or has an error"

   
8. You have all the pieces of a fully functioning hangman program! Now you can put together a program on your own computer to play Hangman. Directions follow.

	Below is all of the code for the hangman program, *except* for the two functions you just defined in problems 6 and 7. (It does not include the special lines allowing it to run in the textbook, and it does not have those function definitions, so this code will not run as expected! It's just provided for you to copy.)

	Copy your two function definitions, from the last two problems, into a Python file, and save it as ``hangman.py`` in your ``106`` folder (anywhere in it you want). Then copy the code in the box below into that file, beneath the function definitions you just copied in.

	Finally, make one more change to the program: add a little bit of code so that after a user types in a secret word to guess, 27 blank lines are printed. (This will let you play the game with a friend -- after you enter in a word, a bunch of blank lines will print out, and then when they get the computer to play, they won't see the word you typed!)

	Save this Python program, and run it with the command line: ``cd`` to the correct directory, and then type ``python hangman.py``, as you learned last week.

	**Submit your python file called hangman.py AND a screenshot of you successfully running the code and playing the game to Unix Problems 6 on Canvas.**


.. activecode:: ps_6_8
   
    def game_state_prompt(txt ="Nothing", h = 6, m_h = 6, word = "HELLO", guesses = ""):
        res = "\n" + txt + "\n"
        res = res + health_prompt(h, m_h) + "\n"
        if guesses != "":
            res = res + "Guesses so far: " + guesses.upper() + "\n"
        else:
            res = res + "No guesses so far" + "\n"
        res = res + "Word: " + blanked(word, guesses) + "\n"
 
        return(res)

    def main():
        max_health = 3
        health = max_health
        secret_word = raw_input("What's the word to guess? (Don't let the player see it!)")
        secret_word = secret_word.upper() # everything in all capitals to avoid confusion
        guesses_so_far = ""
        game_over = False

        feedback = "let's get started"

        # Now interactively ask the user to guess
        while not game_over:
            prompt = game_state_prompt(feedback, health, max_health, secret_word, guesses_so_far)
            next_guess = raw_input(prompt)
            next_guess = next_guess.upper()
            feedback = ""
            if len(next_guess) != 1:
                feedback = "I only understand single letter guesses. Please try again."
            elif next_guess in guesses_so_far:
                feedback = "You already guessed that"
            else:
                guesses_so_far = guesses_so_far + next_guess
                if next_guess in secret_word:
                    if blanked(secret_word, guesses_so_far) == secret_word:
                        feedback = "Congratulations"
                        game_over = True
                    else:
                        feedback = "Yes, that letter is in the word"
                else: # next_guess is not in the word secret_word
                    feedback = "Sorry, " + next_guess + " is not in the word."
                    health = health - 1
                    if health <= 0:
                        feedback = " Waah, waah, waah. Game over."
                        game_over= True

        print(feedback)
        print("The word was..." + secret_word)

    main()




Practice Problems: Earlier Semester Material
--------------------------------------------

1. See comments in code for instructions.

.. activecode:: rv_1_1

   s = "supercalifragilisticexpialidocious"
   # How many characters are in string s? Write code to print the answer.


   # How many vowels are in string s? Write code to print the answer.


   lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]
   # How many characters are in each element of list lp?
   # Write code to print the length (number of characters) of each element of the list on a separate line.
   ## Do NOT write 8+ lines of code to do this.

   # The output you get should be:
   # 5
   # 13
   # 11
   # 12
   # 3
   # 12
   # 11
   # 6

2. See comments in code for instructions.

.. activecode:: rv_1_2

   ic = 93252759253293024
   # What is the value if you add 5 to the integer in ic?

   dcm = [9, 4, 67, 89, 98324, 23, 34, 67, 89, 34, 56, 67, 90, 3242, 9893, 5]
   # add 14 to each element of the list dcm and print out the result from each computation

   # The output you get should be:
   # 23
   # 18
   # 81
   # 103
   # 98338
   # 37
   # 48
   # 81
   # 103
   # 48
   # 70
   # 81
   # 104
   # 3256
   # 9907
   # 19

3. See comments in code for instructions.

.. activecode:: rv_1_3

   pl = "keyboard smashing: sdgahgkslghgisaoghdwkltewighigohdjdslkfjisdoghkshdlfkdjgdshglsdkfdsgkldhfkdlsfhdsklghdskgdlhgsdklghdsgkdslghdskglsdgkhdskfls"
   # What is the last character of the string value in the variable pl? Find it and print it. Do not hard code (this should work no matter what string value pl has).

   plts = ["sdsagdsal","sdadfsfsk","dsgsafsal","tomorrow","cooperative","sdgadtx","289,670,452","!)?+)_="]
   # What is the last character of each element in the list plts?
   # Print the last character of each element in the list on a separate line.
   # HINT: You should NOT have to count the length of any of these strings manually/by yourself.

   # Your output should be:
   # l
   # k
   # l
   # w
   # e
   # x
   # 2
   # =


4. See comments in code for instructions.

.. activecode:: rv_1_4

   bz = "elementary, my dear watson"
   # Write code to print the fifth character of string bz.
   # Your output should be:
   # e

   # Write code to print the seventh character of string bz.
   # Your output should be:
   # t

5. See comments in code for instructions.

.. activecode:: rv_1_5

   nm = "Irene"
   # write code to print out the string "Why hello, Irene" using the variable nm.


   hlt = ['mycroft','Lestrade','gregson','sherlock','Joan','john','holmes','mrs hudson']
   # Write code to print "Nice to meet you," in front of each element in list hlt on a separate line.

   # Your output should look like:
   # Nice to meet you, mycroft
   # Nice to meet you, Lestrade
   # Nice to meet you, gregson
   # Nice to meet you, sherlock
   # Nice to meet you, Joan
   # Nice to meet you, john
   # Nice to meet you, holmes
   # Nice to meet you, mrs hudson


6. See comments in code for instructions.

.. activecode:: rv_1_6

   z = True
   # Write code to print the type of the value in the variable z.

   ab = 45.6
   # Write code to print the type of the value in the variable ab.


7. See comments in code for instructions.

.. activecode:: rv_1_7

   fancy_tomatoes = ["hello", 6, 4.24, 8, 20, "newspaper", True, "goodbye", "False", False, 5967834, "6578.31"]

   # Write code to print the length of the list fancy_tomatoes.


   # Write code to print out each element of the list fancy_tomatoes on a separate line.
   # (You can do this in just 2 lines of code!)

   # Your output should look like:
   # hello
   # 6
   # 4.24
   # 8
   # 20
   # newspaper
   # True
   # goodbye
   # False
   # False
   # 5967834
   # 6578.31


   # Now write code to print out the type of each element of the list fancy_tomatoes on a separate line.

   # Your output should look like:
   # <type 'str'>
   # <type 'int'>
   # <type 'float'>
   # <type 'int'>
   # <type 'int'>
   # <type 'str'>
   # <type 'bool'>
   # <type 'str'>
   # <type 'str'>
   # <type 'bool'>
   # <type 'int'>
   # <type 'str'>

8. The following code runs, but not the way we expect it to. **You want to print out the first character of each string in the list of strings.** So the following output should print out:

``h``

``g``

``l``

``4``

``6``

Instead, you'll see something different when you run the code. Go through it carefully, understand what is happening, and then fix the code so that the output above appears. Good practice: explain to someone else (or yourself) why exactly it is working incorrectly (semantic errors!) and what is happening on each line, and then fix it.

.. activecode:: rv_1_8

   list_of_strings = ["hello","goodbye","lampshade","45","63"]
   for i in list_of_strings:
       if i in list_of_strings:
           print list_of_strings[0]



Functions Practice Problems
---------------------------

We strongly suggest that you try to do the problems yourself before looking at the solutions (which are heavily commented)

1. Define (and write an invocation of) a function called ``get_vowels`` which takes an **input** of a string and **returns the total number of vowels in the string**.

.. tabbed:: func_review_1

  .. tab:: Problem

      .. activecode:: fr_1

          # Write your code here!


          # Here's a sample function call.
          print get_vowels("Hello all") # This should print: 3

  .. tab:: Solution

      .. activecode:: fr_1a

          def get_vowels(s):
              vowels = "aeiou"
              total = 0
              for v in vowels:
                  total += s.count(v)
              return total

          print get_vowels("Hello all")

2. Define (and call) a function called ``sum_a_list`` which **takes any list of integers** and **returns the sum of all integers in the list**.

.. tabbed:: func_review_2

  .. tab:: Problem

      .. activecode:: fr_2

          # Write your code here!


          # Here's a sample function call.
          print sum_a_list([1,4,7,5]) # this should print: 17

          # Extra practice:
          # how would you change this function just a LITTLE
          # so that the function could also take a string of digits
          # and return the sum of all those digits.
          # (Hint: to do this, you only have to type 5 more characters.)

  .. tab:: Solution

      .. activecode:: fr_2a

          def sum_a_list(lt): # function definition statement with one parameter
              tot = 0 # intiialize accumulator to 0
              for i in lt: # iterate over the list that is passed in to the function
                  tot = tot + i # each time you get to a new integer in the list, add that integer to the accumulator
              return tot # the for loop is over, so outdent and return the accumulator from the function

          print sum_a_list([1,4,7,5]) # call the function, and print out the result with a print statement

          # Here's the version of the function that will work
          #   for EITHER a list of integers or a string of digits
          def sum_a_list_or_digitstring(lt):
              tot = 0
              for i in lt:
                  tot = tot + int(i)
              return tot

          print sum_a_list_or_digitstring("1475")


3. Define (and call!) a function called ``common_word`` that **takes a string** and **prints a tuple** of **the most commonly used word in the string** and **the number of times that word is used**. (If there's more than one word that's used most frequently, the function should **print** all of those words.)

.. tabbed:: func_review_3

  .. tab:: Problem

      .. activecode:: fr_3

          # Write your code here!


          # Here's a sample function call.
          common_word("hello hello hello is what they said to the class!") # should print: hello


          # For extra practice: you've done something like this before --
          # how would you change this function to print the LONGEST word in the string?



  .. tab:: Solution

      .. activecode:: fr_3a

          def common_word(s):
              d = {}
              sp = s.split() # split my string by whitespace, so into 'words'
              for w in sp:
                  if w in d:
                      d[w] = d[w] + 1
                  else:
                      d[w] = 1
              kys = d.keys() # get all the keys from the dict you built, in a list
              most_common = kys[0] # start at the beginning of the list -- this is the most common so far!
              for k in d: # go through the keys in the dictionary
                  if d[k] > d[most_common]: # if the value of the key is bigger than the value of the most common key SO FAR, then you have a new most common key so far
                      most_common = k # so reassign the most_common key
              for ky in d: # now that we know the value of the most common key, go through the keys of the dictionary again
                  if d[ky] == d[most_common]: # for every key that has the same value as the most common one
                      print ky, d[ky] # print the key and its value
                      # note that we do NOT return anything here!
                      # because we asked to print stuff out

          common_word("hello hello hello is what they said to the class!") # should print: hello

          # Think further: what would happen if you put a return statement where that print statement is? why wouldn't that work?


4. Define (and call!) a function called ``smallest_value_name`` that **takes a dictionary** with key-value pairs of names and integer values, like this: ``{"Nick": 56, "Paul":73, "Jackie":42}``, and **returns the name associated with the *lowest integer value**. (So in the case of that example dictionary, the function should return ``Jackie``.)

.. tabbed:: func_review_4

  .. tab:: Problem

      .. activecode:: fr_4

          # Write your code here!

          # Here's a sample call
          df = {"Nick": 56, "Paul":73, "Jackie":42}
          print smallest_value_name(df) # should print: Jackie

  .. tab:: Solution

      .. activecode:: fr_4a

          # Here's one solution
          def smallest_value_name(d):
              kys = d.keys() # returns a list of the keys in the dictionary d
              m = kys[0] # start off examining the first key in the list
              for k in kys: # for each key in the list of keys
                  if d[k] < d[m]: # if the value associated with that key is smaller than the value associated with the key saved in the variable m (the smallest so far)
                      m = k # then reassign m so it has the same value as this new key, k
              return m # when the loop is over, m contains the key that has the smallest value, so return that from the function!

          # Here's another solution
          def smallest_val_name_diff(d):
              its = d.items() # returns a list of tuples (key, value) in dictionary d and stores it in its
              tn = its[0]
              for t in its:
                  if t[1] < tn[1]:
                      tn = t
              return tn[0]

          # Sample calls of these solution functions
          d_new = {"Nick": 42, "Paul":73, "Jackie":57}
          print smallest_value_name(d_new) # should print Nick

          print smallest_val_name_diff(d_new)
          # both these calls above print Nick
