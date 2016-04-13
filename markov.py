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


def make_chains(text_string, num_key_words = 2):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    # initialize new dictionary
    chains = {}

    # split on whitespace delimeters
    words = text_string.split()


    # Iterates through words[], creates or appends word to key
    for i in range(len(words)-num_key_words):
        # makes a tuple num_of_words long
        empty_list_of_words_for_key = []

        for x in range(num_key_words):
            empty_list_of_words_for_key.append(words[i])
        
        key_tuple = tuple(empty_list_of_words_for_key)
        print key_tuple
        # if key does not currently exist, append as follows into dict:
        # (tuple_item_0th, tuple_item_1th) = [following word]
        if key_tuple not in chains:
            chains[key_tuple] = [words[i + num_key_words]]
        else:
            # if it does exist, only append to the value
            # ex: [following word, other word that follows tuple combination]
            chains[key_tuple].append(words[i + num_key_words])

    # # Iterates through words[], creates or appends word to key
    # for i in range(len(words)-num_key_words):
    #     # if key does not currently exist, append as follows into dict:
    #     # (tuple_item_0th, tuple_item_1th) = [following word]
    #     if (words[i], words[i+1]) not in chains:
    #         chains[(words[i], words[i+1])] = [words[i+2]]
    #     else:
    #         # if it does exist, only append to the value
    #         # ex: [following word, other word that follows tuple combination]
    #         chains[(words[i], words[i+1])].append(words[i+2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # initialize empty text for joining purposes
    text = ""
    # sets initial current key to a random key in dictionary
    current_key = choice(chains.keys())

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
        # if the word has new-line-punctuation, add space + word + new line
        else:
            text += (random_word + "\n")
        # update the key to find the next word
        current_key = (current_key[1], random_word)
    
    # initializes an empty string to add to later
    formatted_text = ""

    #splits the text by lines and puts each line in a list
    text_lines = text.split('\n')

    # iterates through the list and capitalizes each letter then adds back to the formatted string
    for line in text_lines:
        new_line = line.capitalize()
        formatted_text += new_line + "\n"


    return formatted_text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# make_key_code(input_text, 4)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains)

print random_text
