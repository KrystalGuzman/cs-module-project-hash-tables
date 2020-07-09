def decode_cipher(file_location):

    # store known frequencies of letters for this problem
    freq = dict()

    freq["E"] = 11.53
    freq["T"] = 9.75
    freq["A"] = 8.46
    freq["O"] = 8.08
    freq["H"] = 7.71
    freq["N"] = 6.73
    freq["R"] = 6.29
    freq["I"] = 5.84
    freq["S"] = 5.56
    freq["D"] = 4.74
    freq["L"] = 3.92
    freq["W"] = 3.08
    freq["U"] = 2.59
    freq["G"] = 2.48
    freq["F"] = 2.42
    freq["B"] = 2.19
    freq["M"] = 2.18
    freq["Y"] = 2.02
    freq["C"] = 1.58
    freq["P"] = 1.08
    freq["K"] = 0.84
    freq["V"] = 0.59
    freq["Q"] = 0.17
    freq["J"] = 0.07
    freq["X"] = 0.07
    freq["Z"] = 0.03

# create a dict to store counts of letters
    letter_counts = dict()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # create a second dict to store frequencies of letters
    letter_freq = dict()

    for letter in alphabet:
        letter_counts[letter] = 0
        letter_freq[letter] = 0
    
    # store the total number of letters to calculate percentages later
    total_letters = 0

    # store file contents into a variable
    encrypted = ""

    # open the text file and store data into an array
    with open(file_location) as file:
        encrypted = file.read()
    
    # count letter occurrences
    for character in encrypted:

        if character in letter_counts:
            letter_counts[character] += 1
            total_letters += 1

    # calculate letter frequencies
    for letter in alphabet:
        letter_freq[letter] = letter_counts[letter] / total_letters

    # convert letter frequency dictionaries to a list of tuples to sort later
    letter_freq = letter_freq.items()
    freq = freq.items()

    # sort letter frequencies and known frequencies by frequency (2nd item in each tuple)
    letter_freq = sorted(letter_freq, key=lambda letter: letter[1])
    freq = sorted(freq, key=lambda letter: letter[1])

    # create translation table
    encrypted_letters = "".join([letter_data[0] for letter_data in letter_freq])
    known_letters = "".join([letter_data[0] for letter_data in freq])

    translation = encrypted.maketrans(encrypted_letters, known_letters)

    decrypted = encrypted.translate(translation)

    return decrypted


decrypted = decode_cipher("ciphertext.txt")

with open("decrypted.txt", "w") as file:
    file.write(decrypted)