from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # returns a string of the entirety of the input file
    contents = open(file_path).read() 
    return contents


def make_chains(text_string, num_key_words):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    # intergerizes the input from str to int so it can be used in index math 
    num_key_words = int(num_key_words)

    # initialize new dictionary
    chains = {}

    # split on whitespace delimeters
    words = text_string.split()

    # iterates through words to create keys 
    for word_index in range(len(words) - num_key_words):
        # initializes an empty list to store the words that will create the key
        key_word_list = []
        # iterates over an index to add the correct number of words to the key list. 
        # tuplizes key
        for word_count in range(num_key_words):
            key_word_list.append(words[word_index + word_count])
            current_key = tuple(key_word_list)

        # adds key to dictionary, or adds values to existing key
        if current_key not in chains:
            chains[current_key] = [words[word_index + num_key_words]]
        else: 
            chains[current_key].append(words[word_index + num_key_words])

    return chains




def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # initialize empty text for joining purposes
    text = ""

    # sets initial current key to a random key in dictionary
    current_key = choice(chains.keys())

    # a string of punctuation that should end a line
    to_new_line_punctuation = "!-.:;?"
    
    # while we have not reached the condtion of:
    # (current_key[1], Nothing here)
    # concatenates to text until end is reached
    while current_key in chains:
        # picks the next word from the chains dictionary
        random_word = choice(chains[current_key])
        # puts the first word into text (without a space!)
        if text == "":
            text += (random_word + " ")
        # if word has no punctuation, add a space and the word to the text
        elif random_word[-1] not in to_new_line_punctuation:
            text += (random_word + " ")
        # if the word ends with punctuation, have the word end the line. 
        else:
            text += (random_word + "\n")
        # update the key to find the next word. Listizes, slices, adds random word, re-tuplizes. 
        current_key_list = list(current_key)
        current_key_list = current_key_list[1:] + [random_word]
        current_key = tuple(current_key_list)
    
    # initializes an empty string to add to later
    formatted_text = ""

    #splits the text by lines and puts each line in a list
    text_lines = text.split('\n')

    # iterates through the list and capitalizes each letter then adds back to the formatted string
    for line in text_lines:
        new_line = line.capitalize()
        formatted_text += new_line + "\n"
        if formatted_text.count("\n") > 14:
            break


    return formatted_text


# determines what txt file to read as input text 
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# establishes the number of words to put into the dictionary keys. More = better text. 
key_length = raw_input("How many words would you like to use in your Markov key chain? ")

# Get a Markov chain
chains = make_chains(input_text, key_length)

# Produce random text
random_text = make_text(chains)

print "\n", random_text
