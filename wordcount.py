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
    max_freq = 0
    exclude = set(string.punctuation)
    for index, word in enumerate(tokens):
        no_punc = "".join(char for char in word if char not in exclude)
        word = no_punc.lower()
        word_count[word] = word_count.get(word, 0) + 1

        # checks to see if word is more frequent than others
        if word_count[word] > max_freq:
            max_freq = word_count[word]

    # sorts the words by frequency (highest to lowest) then alphabetically
    # based on the frequency
    frequency_list = []
    double_sorted = []
    frequency_sort = sorted(word_count.items(), key=lambda tup: tup[1], reverse=True)
    while max_freq > 0:
        for index, data_pair in enumerate(frequency_sort[::-1]):
            if data_pair[1] == max_freq:
                frequency_list.append(data_pair)
        
        max_freq -= 1

    print double_sorted


get_word_count(input_file)


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

#get_word_count_counter(input_file)
