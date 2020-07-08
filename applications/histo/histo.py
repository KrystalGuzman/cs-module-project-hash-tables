# allow sorting by multiple criteria
from operator import itemgetter

# copy of word_count function
def word_count(s):

    words = s.lower()

    # convert all whitespace chars to a space
    chars_whitespace = '\n \t \r'.split(" ")
    
    for whitespace in chars_whitespace:
        words = words.replace(whitespace, " ")

    # remove chars to be ignored
    chars_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for char in chars_to_ignore:
        words = words.replace(char, "")

    # turn string into an array of individual words        
    words = words.split(" ")

    words_seen = dict()

    for word in words:

        # skip empty strings
        if word == "":
            continue

        if word in words_seen:
            words_seen[word] += 1
        else:
            words_seen[word] = 1

    return words_seen

# make histogram
def make_histogram(file_path):

    with open(file_path) as file:
        text = file.read()

    # create a dict using the word_count function to store word freq
    freq = word_count(text)

    # turn the dict into an list and sort by number of occurrences, ascending
    # https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key
    freq_list = sorted(freq.items(), key=lambda kv:(-kv[1], kv[0]))
    # find length of longest word
    longest_word_length = len(freq_list[0][0])

    for word_data in freq_list:
        if len(word_data[0]) > longest_word_length:
            longest_word_length = len(word_data[0])

    # output words and their occurences. Output one "#" for each occurence
    for word_data in freq_list:

        word_formatted = word_data[0] + (longest_word_length - len(word_data[0])) * " "
        histogram_bar = "#" * word_data[1]

        histogram_row = word_formatted + "  " + histogram_bar

        print(histogram_row)
    
make_histogram("robin.txt")