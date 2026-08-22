def translate_to_pig(string):
    string_list = string.split()  #divide input into each letter
    vowels = ("a", "e", "i", "o", "u")   #define vowels to check if each word starts with one or not
    word_list = []   #empty output list. will eventually have each finished word
    for word in string_list:   #itirate through each word and perform operations to turn it into pig latin
        word_letters = list(word)   #split word into characters
        
        if not word_letters[0].lower() in vowels:   #checking if the first letter of the word is a vowel or not
            removed = word_letters.pop(0)   #remove and add first letter
            word_letters.append(removed)
            word_letters.append("a")
            word_letters.append("y")
        else:
            word_letters.append("w")
            word_letters.append("a")
            word_letters.append("y")
        word_list.append("".join(word_letters))   #adding word to word_list after making it into a single string
    return " ".join(word_list)   #returning output
print(translate_to_pig(input()))
