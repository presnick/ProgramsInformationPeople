
Training a Classifier/Predictor
-------------------------------

.. index:: training data, training set


Rather than hand-coding the rules that are used in a rule-based classifier or predictor, we can use data. 

For example, for the gender classifier described in a previous section, instead of hard-coding the rules, you could try to learn them. Suppose that you were given long lists of male and female names, like the ones below, but with many more examples.

.. activecode:: prediction_8
   :nocanvas:
   
   males = ['Barde', 'Ali', 'Marcio', 'Tyrone', 'Gabriel', 'Gerrard', 'Lawrence', 'Knox', 'Kurtis', 'Adrian', 'Arlo', 'Wilburt', 'Barney', 'Thadeus', 'Kalil', 'Zacharia', 'Ruben', 'Yigal', 'Paddie', 'Francis', 'Eliot', 'Bud', 'Zebulen', 'Hartwell', 'Daniel', 'Gerold', 'Reynold', 'Solomon', 'Kingsly', 'Haydon', 'Edgardo', 'Ford', 'Gregorio', 'Cory', 'Drew', 'Rodrique', 'Flin', 'Ginger', 'Bard', 'Wye', 'Yacov', 'Theo', 'Lindsey', 'Penn', 'Raleigh', 'Phineas', 'Ulric', 'Dion', 'Zary', 'Ricardo']
   
   females = ['Erinna', 'Orelee', 'Melisandra', 'Dorotea', 'Alvinia', 'Leena', 'Milli', 'Beckie', 'Sascha', 'Cortney', 'Cheri', 'Shanda', 'Catrina', 'Anestassia', 'Cher', 'Randy', 'Charline', 'Brigit', 'Rafaelia', 'Shelagh', 'Cherish', 'Zorana', 'Shay', 'Beatrice', 'Jeannette', 'Briana', 'Lynne', 'Kattie', 'Tobye', 'Marietta', 'Vilma', 'Meggi', 'Ondrea', 'Idell', 'Yoshi', 'Fanechka', 'Andria', 'Denys', 'Darb', 'Roby', 'Philippa', 'Alecia', 'Lanni', 'Hatti', 'Simonette', 'Celeste', 'Inesita', 'Else', 'Hulda', 'Lela']

In machine learning, we refer to a set of labeled examples like this as *training data*. You could then consider various features, such as last letters or first letters, or the presence of certain letter combinations. For each of those features, you could count up how many of the male and female names in the training set match the feature (e.g., have the last letter 'i'). If the feature is much more common in examples labeled as female than male, then you could add a new rule to the rule set, outputting "female" when the feature is present.

Let's use training data to create rules for a rule-based predictor for the Shannon Game. The interesting twist will be that the training data will consist not only of some publicly available English texts, but also the sequence of letters that have already been revealed from the current text. The features will be the most recent letter or letters that have been revealed. Thus, for example, using publicly available English texts, you might learn a rule that following a 'q' the next letter is almost always 'u'. Using the previously revealed letters from the current text, you might learn that if the most recent letters are "Mr. ", then the next letter is likely to be "C".

First, let's make a base rule to fall back on that guesses all the letters in the alphabet but rather than guessing them in alphabetic order, guesses them in order of how frequently they appear in our training data of English text.

Suppose that we have an English corpus stored in the string train_txt. We first count how frequent all the letters are, accumulating results in a dictionary. We then sort the letters by their frequency, using the pattern in :ref:`Sorting Dictionaries <sort_dictionaries>`.

.. activecode:: prediction_9
    :nocanvas:
    :include: prediction_training_helpers

    # produce a dictionary with letters and counts
    def letter_frequencies(txt):
        d = {}
        for c in txt:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        return d

    fs = letter_frequencies(train_txt)


    # sort the letters by how frquently they appear
    sorted_lets = sorted(fs.keys(), key = lambda c: fs[c], reverse=True)

    # Define a default rule
    freqs_rule = (None, sorted_lets)

How much better do we do at guessing the next letter, just by guessing letters in order of their frequency in the training text?

.. activecode:: prediction_10
    :nocanvas:
    :include: prediction_training_helpers

    import sys
    sys.setExecutionLimit(60000)     # let it take up to a minute, 60 * 1000 milliseconds

    performance(test_txt, [(None, alphabet)])
    performance(test_txt, [(None, sorted_lets), (None, alphabet)])

Now, suppose that we try to learn some context-sensitive rules, like guessing 'U' after a 'Q'?

Let's create a nested dictionary to store the frequency of letters that follow each letter in the alphabet, using the input training text. The structure of the dictionary we will create looks like this:

.. code-block:: python

    {'A':{'B':2,'C':4},
     'D':{'E':6,'A':7}}

This would reflect training data where B came after A 2 times in the training text, and C came after A 4 times in the data, E came after D 6 times, and so on.

.. activecode:: prediction_11
    :nocanvas:
    :include: prediction_training_helpers

    def next_letter_frequencies(txt):
        # txt is a big text string
        r = {} # initialize the accumulator, an empty ditionary
        for i in range(len(txt)-1):
            # loop through the positions (indexes) of txt;
            # each iteration, we'll be looking at the
            # letter txt[i] and the following letter, txt[i+1]
            if txt[i] not in r:
                # first time we've seen the current letter
                # make an empty dictionary for counts of what letters come next
                r[txt[i]] = {}
            next_letter_freqs = r[txt[i]]  # dictionary of counts of what letters come next after txt[i]
            next_letter = txt[i+1]  # next letter is txt[i+1]
            if next_letter not in next_letter_freqs:
                # first time seeing next_letter after txt[i+1]
                next_letter_freqs[next_letter] = 1
            else:
                next_letter_freqs[next_letter] = next_letter_freqs[next_letter] + 1
        return r

    counts = next_letter_frequencies(train_txt)
    print counts

Given that counts dictionary, we can create a different guessing rule for each possible previous letter. The keys of the outer dictionary are possible last letters. The keys in each inner dictionary represent a possible next letter, and the value associated with the key is how frequently that next letter occurred. If we sort the inner dictionary's keys based on the associated values, we can get a sorted list of next guesses to make.

.. activecode:: prediction_12
    :nocanvas:
    :include: prediction_training_helpers

    context_sensitive_rules = []
    for c in counts.keys():
        fs = counts[c]
        sorted_lets = sorted(fs.keys(), key = lambda c: fs[c], reverse=True)
        context_sensitive_rules.append((c, sorted_lets))
    # make default rule for letters in test_txt that weren't in train_txt
    context_sensitive_rules.append((None, alphabet))

    import sys
    sys.setExecutionLimit(60000)     # let it take up to a minute, 60 * 1000 milliseconds

    performance(test_txt, [(None, sorted_lets), (None, alphabet)])
    performance(test_txt, context_sensitive_rules)
    entropy(test_txt, context_sensitive_rules)

We got another big improvement from that. Our estimated entropy is down to 2.61 bits per character. That's a big improvement, but still quite a bit higher than Shannon's estimate of around 1.3, based on people doing the predicting.  We could go even farther with training our predictor, generating additional rules in various ways. For example, with a larger training corpus we could sort our next guesses based on what follows from the previous *two* characters instead of the last character. Or, once we get to the end of a word, we might estimate frequencies of complete words. Within a word, we might maintain a dictionary of possible completions of the current word. Challenge: see how much additional improvement you can make!


.. mchoice:: prediction_4
   :answer_a: labeled data used to make a classifier or predictor perform better over time.
   :answer_b: a process of making a dataset better over time.
   :feedback_a: The data are used to "train" a classifier. We make it perform well, at least on the training data.
   :feedback_b: The data are not getting trained. They are being used to train the classifier.
   :correct: a

   What does "training data" refer to?


.. activecode:: prediction_training_helpers

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZs "

    def guesser(prev_txt, rls):
        all_guesses = []
        for (suffix, guesses) in rls:
            if (suffix == None) or ((len(prev_txt) >= len(suffix)) and (prev_txt[-len(suffix):] == suffix)):
                # append all the guesses that are new
                for guess in guesses:
                    if guess not in all_guesses:
                        all_guesses.append(guess)
        return all_guesses


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


    train_txt = collapse("""
    IN the year 1878 I took my degree of Doctor of Medicine of the
    University of London, and proceeded to Netley to go through the course
    prescribed for surgeons in the army. Having completed my studies there,
    I was duly attached to the Fifth Northumberland Fusiliers as Assistant
    Surgeon. The regiment was stationed in India at the time, and before
    I could join it, the second Afghan war had broken out. On landing at
    Bombay, I learned that my corps had advanced through the passes, and
    was already deep in the enemy's country. I followed, however, with many
    other officers who were in the same situation as myself, and succeeded
    in reaching Candahar in safety, where I found my regiment, and at once
    entered upon my new duties.

    The campaign brought honours and promotion to many, but for me it had
    nothing but misfortune and disaster. I was removed from my brigade and
    attached to the Berkshires, with whom I served at the fatal battle of
    Maiwand. There I was struck on the shoulder by a Jezail bullet, which
    shattered the bone and grazed the subclavian artery. I should have
    fallen into the hands of the murderous Ghazis had it not been for the
    devotion and courage shown by Murray, my orderly, who threw me across a
    pack-horse, and succeeded in bringing me safely to the British lines.

    Worn with pain, and weak from the prolonged hardships which I had
    undergone, I was removed, with a great train of wounded sufferers, to
    the base hospital at Peshawar. Here I rallied, and had already improved
    so far as to be able to walk about the wards, and even to bask a little
    upon the verandah, when I was struck down by enteric fever, that curse
    of our Indian possessions. For months my life was despaired of, and
    when at last I came to myself and became convalescent, I was so weak and
    emaciated that a medical board determined that not a day should be lost
    in sending me back to England. I was dispatched, accordingly, in the
    troopship "Orontes," and landed a month later on Portsmouth jetty, with
    my health irretrievably ruined, but with permission from a paternal
    government to spend the next nine months in attempting to improve it.

    I had neither kith nor kin in England, and was therefore as free as
    air--or as free as an income of eleven shillings and sixpence a day will
    permit a man to be. Under such circumstances, I naturally gravitated to
    London, that great cesspool into which all the loungers and idlers of
    the Empire are irresistibly drained. There I stayed for some time at
    a private hotel in the Strand, leading a comfortless, meaningless
    existence, and spending such money as I had, considerably more freely
    than I ought. So alarming did the state of my finances become, that
    I soon realized that I must either leave the metropolis and rusticate
    somewhere in the country, or that I must make a complete alteration in
    my style of living. Choosing the latter alternative, I began by making
    up my mind to leave the hotel, and to take up my quarters in some less
    pretentious and less expensive domicile.

    On the very day that I had come to this conclusion, I was standing at
    the Criterion Bar, when some one tapped me on the shoulder, and turning
    round I recognized young Stamford, who had been a dresser under me at
    Barts. The sight of a friendly face in the great wilderness of London is
    a pleasant thing indeed to a lonely man. In old days Stamford had never
    been a particular crony of mine, but now I hailed him with enthusiasm,
    and he, in his turn, appeared to be delighted to see me. In the
    exuberance of my joy, I asked him to lunch with me at the Holborn, and
    we started off together in a hansom.
    """)

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

    # produce a dictionary with letters and counts
    def letter_frequencies(txt):
        d = {}
        for c in txt:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        return d

    fs = letter_frequencies(train_txt)


    # sort the letters by how frquently they appear
    sorted_lets = sorted(fs.keys(), key = lambda c: fs[c], reverse=True)

    def next_letter_frequencies(txt):
        # txt is a big text string
        r = {} # initialize the accumulator, an empty ditionary
        for i in range(len(txt)-1):
            # loop through the positions (indexes) of txt;
            # each iteration, we'll be looking at the
            # letter txt[i] and the following letter, txt[i+1]
            if txt[i] not in r:
                # first time we've seen the current letter
                # make an empty dictionary for counts of what letters come next
                r[txt[i]] = {}
            next_letter_freqs = r[txt[i]]  # dictionary of counts of what letters come next after txt[i]
            next_letter = txt[i+1]  # next letter is txt[i+1]
            if next_letter not in next_letter_freqs:
                # first time seeing next_letter after txt[i+1]
                next_letter_freqs[next_letter] = 1
            else:
                next_letter_freqs[next_letter] = next_letter_freqs[next_letter] + 1
        return r

    counts = next_letter_frequencies(train_txt)

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

