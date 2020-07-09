import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# convert all whitespace characters into space
chars_whitespace = '\n \t \r'.split(" ")
for whitespace in chars_whitespace:
    words = words.replace(whitespace, " ")

#remove consecutive spaces
words = words.replace("  ", " ")

# TODO: analyze which words can follow other words
follow_words = dict()
# create start and end words dict
start_words = dict()
end_words = dict()

end_punctuation = [".", "?", "!"]

words_array = words.split(" ")

for word_id in range(len(words_array)):
    word = words_array[word_id]

    #skip last word
    if word_id == len(words_array) - 2:
        break
    if word_id+1 < len(words_array):
        next_word = words_array[word_id+1]
        #start new set for words to follow is set doesn't exist
        if word not in follow_words:
            follow_words[word] = []
        #add the next work to the set
        follow_words[word].append(next_word)

        #starts with capital
        is_start = (word[0].isalpha() and word[0] == word[0].upper())
        if is_start and word not in start_words:
            start_words[word] = 1

        #before punctuation
        is_end = (word[-1] in end_punctuation)
        if is_end and word not in end_words:
            end_words[word] = 1

start_array = list(start_words)

# TODO: construct 5 random sentences
for sentence_id in range(5):

    # keep track of whether a closing double quote is needed
    double_quote = False

    # start sentence with a random word from start_words_array
    next_word = random.choice(start_array)
    sentence = next_word
        
    # keep track of whether to look for a word with a double-closing quote (if the current word doesn't already have both)
    if next_word[0] == '"' and next_word[-1] != '"':
        double_quote = True

    # continue picking words until an end word is encountered
    while True:

        # can end sentence if any opening double quotes have been matched
        if next_word in end_words and not double_quote:
            break

        # choose a next word and determine if update double quote count
        next_word = random.choice(follow_words[next_word])
                
        if double_quote:
            
            # do not allow nesting of double quotes. Next word must not begin with a double quote.
            if next_word[0] == '"':
                continue

            # next word has a closing double quote; update count
            elif next_word[-1] == '"':
                double_quote = False
         
        else:

            # do not allow a word with a closing double quote if there was no double opening quote before it
            if next_word[-1] == '"':
                continue

            # next word has an opening double quote; update count (but only if it doesn't end with a double quote)
            elif next_word[0] == '"' and next_word[-1] != '"':
                double_quote = True

        sentence += " " + next_word

    print(sentence, "\n")
