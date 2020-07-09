def word_count(s):
    words = s.lower()
    #convert all whitespace to characters to a space
    chars_whitespace = '\n \t \r'.split(" ")

    for whitespace in chars_whitespace:
        words = words.replace(whitespace, " ")

    # remove chars to be ignored
    chars_to_ignore = '" : ; , . - + = \ / | [ ] } { ( ) * ^ &'.split(" ")

    for char in chars_to_ignore:
        words = words.replace(char, "")

    # turn string into list of words
    words = words.split(" ")

    words_seen = dict()

    for word in words:
        if word == "":
            continue
        if word in words_seen:
            words_seen[word] += 1
        else:
            words_seen[word] = 1
    return words_seen


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))