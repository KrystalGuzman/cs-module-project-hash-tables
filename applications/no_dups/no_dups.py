def no_dups(s):
    words = s.split(" ")
    words_seen = dict()
    words_with_no_duplicates = []

    for word in words:
        if word not in words_seen:
            words_seen[word] = 1
            words_with_no_duplicates.append(word)
    return " ".join(words_with_no_duplicates)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))