
The Shannon Game: Guessing the Next Letter in a Text
----------------------------------------------------

In the Shannon Game, a player tries to guess the first letter in a string. Eventually, after some guesses, the player makes a correct guess. Then, the player tries to guess the next letter. And so on, until all the letters have been revealed. For fun, try playing it at `this website <http://www.math.ucsd.edu/~crypto/java/ENTROPY/>`_.

What if we want to make a computer program play the game? We can again use the structure of a rule-based classifier or predictor. Here, we have a guesser function whose inputs are a string of letters that have already been revealed, plus a list of tuples that represent the guessing rules. The output will again be an ordered list of letters to guess. One natural rule to use is that if the last letter was a 'q', the first thing to guess for the next letter is 'u'. If that fails, the next best guess is 'a', since there are a few words in English that have the combination 'qi', and 'i' is the third best guess, if the text might include some transliteration of Chinese words or names.

In the code below, we implement a guesser function and a list of two rules. The first handles what to guess if the previous letter was 'q' and the second rule is the default or fallback case, just guessing all the letters in alphabetic order. Just to make the code a little easier to read, here the sequences of guesses is represented as a string rather than as a list of characters.

.. activecode:: prediction_7
   :nocanvas:

   alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
   def guesser(prev_txt, rls):
       all_guesses = []
       for (f, guesses) in rls:
           if f(prev_txt):
               # append all the guesses that are new
               for guess in guesses:
                    if guess not in all_guesses:
                       all_guesses.append(guess)
       return all_guesses

   rules = [(lambda x: x[-1] == "Q", "UAI"),
            (lambda x: True, alphabet)]
   print guesser(" ", rules)
   print guesser(" THE Q", rules)
   print guesser(" THE QUALIT", rules)


Let's simplify that a little. Notice that in the above, the first rule considers only the very last letter in prev_txt (the most recent letter that was revealed). Suppose we restrict ourselves to guessing rules that consider only the last letter or last few letters in prev_txt. Then we don't need the first element of a rule to be a function that takes prev_txt as an input. Instead, the first part of the rule can just be a string to compare against the ending of prev_txt.

For example, if the rule was ("ca", "bdklmnp"), it would match any text where the last two revealed letters were "ca".

With that simplification, the following code is equivalent to the code above.

.. activecode:: prediction_7a
    :nocanvas:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    def guesser(prev_txt, rls):
        all_guesses = []
        for (suffix, guesses) in rls:
            if (suffix == None) or ((len(prev_txt) >= len(suffix)) and (prev_txt[-len(suffix):] == suffix)):
                # append all the guesses that are new
                for guess in guesses:
                    if guess not in all_guesses:
                        all_guesses.append(guess)
        return all_guesses



    rules = [("Q", "UAI"),
             (None, alphabet)]

    ### Code that follows creates a string, test_txt, with a snippet from Sherlock Holmes
    ### all converted to capitals with punctuation and extra spaces removed

    def collapse(txt):
        # turn newlines and tabs into spaces and collapse multiple spaces to just one
        # gets rid of anything that's not in our predefined alphabet.
        txt = txt.upper()
        txt = txt.replace("\r", " ").replace("\n", " ").replace("\t", " ")
        res = ""
        prev = ""
        for c in txt:
            if c in alphabet:
                # if not second space in a row, use it
                if c != " " or prev != " ":
                    res += c
                # current character will be prev on the next iteration
                prev = c
        return res

    test_txt = collapse("""
        "Ah," said Holmes, "I think that what you have been good enough
    to tell us makes the matter fairly clear, and that I can deduce
    all that remains. Mr. Rucastle then, I presume, took to this
    system of imprisonment?"

    "Yes, sir."

    "And brought Miss Hunter down from London in order to get rid of
    the disagreeable persistence of Mr. Fowler."

    "That was it, sir."

    "But Mr. Fowler being a persevering man, as a good seaman should
    be, blockaded the house, and having met you succeeded by certain
    arguments, metallic or otherwise, in convincing you that your
    interests were the same as his."

    "Mr. Fowler was a very kind-spoken, free-handed gentleman," said
    Mrs. Toller serenely.

    "And in this way he managed that your good man should have no
    want of drink, and that a ladder should be ready at the moment
    when your master had gone out."

    "You have it, sir, just as it happened."

    "I am sure we owe you an apology, Mrs. Toller," said Holmes, "for
    you have certainly cleared up everything which puzzled us. And
    here comes the country surgeon and Mrs. Rucastle, so I think,
    Watson, that we had best escort Miss Hunter back to Winchester,
    as it seems to me that our locus standi now is rather a
    questionable one."

    And thus was solved the mystery of the sinister house with the
    copper beeches in front of the door. Mr. Rucastle survived, but
    was always a broken man, kept alive solely through the care of
    his devoted wife. They still live with their old servants, who
    probably know so much of Rucastle's past life that he finds it
    difficult to part from them. Mr. Fowler and Miss Rucastle were
    married, by special license, in Southampton the day after their
    flight, and he is now the holder of a government appointment in
    the island of Mauritius. As to Miss Violet Hunter, my friend
    Holmes, rather to my disappointment, manifested no further
    interest in her when once she had ceased to be the centre of one
    of his problems, and she is now the head of a private school at
    Walsall, where I believe that she has met with considerable success.
    """)


Let's see whether having that extra rule makes us any better at playing the Shannon game. Below we define a function ``performance`` that takes a text as input and a list of rules. It goes through the letters in the text one at a time. For each letter, it calls guesser to generate a list of guesses. Then it figures out how many guesses would be required to guess the next character, if it went through the list of guesses one at a time. It adds that to the running total. AT the end, we have a count of the total number of guesses that would be required by our guesser to play the Shannon game on the provided text. We've included a snippet of text from Sherlock Holmes to run the performance function on. Adding the rule of guessing U after Q reduces our total guesses, but only by a little, because the text we're guessing doesn't have very many qs in it.

.. activecode:: prediction_7b:
    :nocanvas:
    :include: prediction_7a

    def performance(txt, rls):
        # txt is a string
        # rls is a list of tuples; each tuple represents one rule
        # Run the guesser on txt and print out the overall performance

        tot = 0 # initialize accumulator for total guesses required
        prev_txt = ""
        for c in txt:
            to_try = guesser(prev_txt, rls)
            # find out position of the next character of txt, in the guesses list to_try
            # That's how many guesses it would take before you make the right guess
            guess_count = to_try.index(c)
            tot += guess_count
            # c has now been revealed, so add it to prev_txt
            prev_txt += c
        # done with the for loop; print the overall performance
        print "%d characters to guess\t%d guesses\t%.2f guesses per character, on average\n" % (len(txt) -1, tot, float(tot)/(len(txt) -1))



    print "Without the U after Q rule"
    performance(test_txt, [(None, alphabet)])

    print "With the U after Q rule"
    performance(test_txt, [('Q', ['U']), (None, alphabet)])

Claude Shannon originally devised this game as a way to estimate the *entropy* of the English language. Suppose we had the very best guesser possible (perhaps some combination of a human who understands English and a computer program that does all kinds of statistical and computational wizardry.) Rather than just counting the total number of guesses it makes, as our performance function did, we could keep track of how often it took one guess, two guesses, three guesses, and so on. From those frequencies, we can infer probabilities (the fraction of all letters that required that many guesses). Then, a lower bound on the entropy of English can be computed from those probabilities, as argued in his classic paper: ``Shannon, Claude E. "Prediction and entropy of printed English." Bell system technical journal 30.1 (1951): 50-64.``

We can see below that guessing in alphabetic order yields an estimate of 4.85 bits per character, much higher than Shannon's estimate of around 1.3 bits per character. So we'll need to make a better guesser!

.. activecode:: prediction_7c:
    :include: prediction_7a

    import math
    def entropy(txt, rls):
        guess_frequencies = {}
        prev_txt = ""
        for c in txt:
            to_try = guesser(prev_txt, rls)
            guess_count = to_try.index(c) + 1
            if guess_count in guess_frequencies:
                guess_frequencies[guess_count] += 1
            else:
                guess_frequencies[guess_count] = 1
            prev_txt += c

        print "guess_frequencies:", guess_frequencies
        # from frequencies, compute entropy
        acc = 0.0
        for i in range(len(guess_frequencies.keys())):
            guess_count = guess_frequencies.keys()[i]
            probability = guess_frequencies[guess_count] / float(len(txt))
            if i < len(guess_frequencies.keys()) - 1:
                next_guess_count = guess_frequencies.keys()[i+1]
                next_probability = guess_frequencies[next_guess_count] / float(len(txt))
            else:
                next_probability = 0
            acc += guess_count * (probability-next_probability) * math.log(guess_count, 2)

        print "entropy:", acc
        return acc


    entropy(test_txt, [(None, alphabet)])