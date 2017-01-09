# put your code here.
import string


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
    for word, count in word_count.items():
        print "%s %d" % (word, count)


#get_word_count("test.txt")


def get_word_count_long(file_name):

    data_file = open(file_name)

    word_count = {}
    tokens = []

    # splits file into lines, then splits each line on a space
    for line in data_file:
        line = line.rstrip()

        # makes one large list of words instead of working line by line
        tokens.extend(line.split(" "))

    # goes through each token and strips punctuation and makes lowercase
    # to eliminate doubles, and then performs the dictionary counting
    exclude = set(string.punctuation)
    for index, word in enumerate(tokens):
        no_punc = "".join(char for char in word if char not in exclude)
        word = no_punc.lower()
        word_count[word] = word_count.get(word, 0) + 1

    # iterates through word_count to print out the key-value pairs
    for word, count in word_count.iteritems():
        print "%s %d" % (word, count)

get_word_count_long("twain.txt")
