# put your code here.
import string
import sys
import collections

input_file = sys.argv[1]


def get_word_count(file_name):

    data_file = open(file_name)

    word_count = {}
    tokens = []

    # splits file into lines, then splits each line on a space
    for line in data_file:
        line = line.rstrip()

        # makes one large list of words instead of working line by line
        tokens = tokens + line.split(" ")

    # goes through each token and strips punctuation and makes lowercase
    # to eliminate doubles, and does dictionary counting
    exclude = set(string.punctuation)
    for index, word in enumerate(tokens):
        no_punc = "".join(char for char in word if char not in exclude)
        word = no_punc.lower()
        word_count[word] = word_count.get(word, 0) + 1

    # iterates through word_count to print out the key-value pairs
    # uses iteritems() for longer dictionaries
    if len(word_count) > 100:
        for word, count in word_count.iteritems():
            print "%s %d" % (word, count)
    else:
        for word, count in word_count.items():
            print "%s %d" % (word, count)


#get_word_count(input_file)


def get_word_count_counter(file_name):

    data_file = open(file_name)

    #word_count = {}
    tokens = []

    # splits file into lines, then splits each line on a space
    for line in data_file:
        line = line.rstrip()

        # makes one large list of words instead of working line by line
        tokens = tokens + line.split(" ")

    # goes through each token and strips punctuation and makes lowercase
    # to eliminate doubles, and does dictionary counting
    exclude = set(string.punctuation)
    for index, word in enumerate(tokens):
        no_punc = "".join(char for char in word if char not in exclude)
        tokens[index] = no_punc.lower()

    counter = collections.Counter(tokens)
    for word, count in counter.most_common():
        print "%s %d" % (word, count)

get_word_count_counter(input_file)
