def translate_to_pig_latin(string):
    string_list = string.split()  #divide input into each letter
    vowels = ("a", "e", "i", "o", "u")   #define vowels to check if each word starts with one or not
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    word_list = []   #empty output list. will eventually have each finished word
    for word in string_list:   #itirate through each word and perform operations to turn it into pig latin
        if word.isdigit():
            word_list.append(word)
            continue
        word_letters = list(word)   #split word into characters
        suffix = []
        while word_letters and word_letters[-1] not in letters:   #checking and itirating through the end of the word to check if the word ends in something that should go after the pig latin suffix
            suffix.insert(0, word_letters.pop(-1))   #removing and storing (in the correct order) the other suffix
        if word_letters and word_letters[0].lower() not in vowels:   #checking if the first letter of the word is a vowel or not
            removed = word_letters.pop(0)   #remove and add first letter
            word_letters += [removed, "a", "y"]
        else:
            word_letters += ["w", "a", "y"]
        word_letters += suffix
        word_list.append("".join(word_letters))   #adding word to word_list after making it into a single string
    return " ".join(word_list)   #returning output
print(translate_to_pig_latin(input()))
