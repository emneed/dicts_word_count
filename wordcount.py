# put your code here.


def get_word_count(file_name):

    data_file = open(file_name)

    word_count = {}
    tokens = []

    # splits file into lines, then splits each line on a space
    for line in data_file:
        line = line.rstrip()

        # makes one large list of words instead of working line by line
        tokens = tokens + line.split(" ")

    # looks for each word as a key in the dictionary, creates key if not found
    # increments key's value by one otherwise
    for word in tokens:
        word_count[word] = word_count.get(word, 0) + 1

    # iterates through word_count to print out the key-value pairs
    for word, count in word_count.items():
        print "%s %d" % (word, count)

get_word_count("test.txt")
