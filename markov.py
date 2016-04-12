from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # returns a string of the entirety of the input file
    contents = open(file_path).read() 
    return contents


def make_chains(text_string):
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

    # split on whitespace or newline delimeters
    words = text_string.split()

    # Iterates through words[], creates or appends word to key
    for i in range(len(words)-2):
        # if key does not currently exist, append as follows into dict:
        # (tuple_item_0th, tuple_item_1th) = [following word]
        if (words[i], words[i+1]) not in chains:
            chains[(words[i], words[i+1])] = [words[i+2]]
        else:
            # if it does exist, only append to the value
            # ex: [following word, other word that follows tuple combination]
            chains[(words[i], words[i+1])].append(words[i+2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # initialize empty text for joining purposes
    text = ""
    # sets initial current key to a random key in dictionary
    current_key = choice(chains.keys())
    
    # while we have not reached the condtion of:
    # (current_key[1], Nothing here)
    # concatenates to text until end is reached
    while current_key in chains:
        random_word = choice(chains[current_key])
        text += (" " + random_word)
        current_key = (current_key[1], random_word)

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
