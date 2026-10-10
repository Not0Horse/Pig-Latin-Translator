def translate_to_pig_latin(string):
    string_list = string.split()  #divide input into each letter
    vowels = ("a", "e", "i", "o", "u")   #define vowels to check if each word starts with one or not
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    word_list = []   #empty output list. will eventually have each finished word
    for word in string_list:   #itirate through each word and perform operations to turn it into pig latin
        if word.isdigit():   #checking if the word is a number
            word_list.append(word)   #adding the number to the response
            continue   #skipping the function
        word_letters = list(word)   #split word into characters
        suffix = []
        while word_letters and word_letters[-1] not in letters:   #checking and itirating through the end of the word to check if the word ends in something that should go after the pig latin suffix
            suffix.insert(0, word_letters.pop(-1))   #removing and storing (in the correct order) the other suffix
        if word_letters and word_letters[0].lower() not in vowels:   #checking if the first letter of the word is a vowel or not
            removed = [word_letters.pop(0)]   #removing and storing first letter of the word
            while word_letters[0].lower() not in vowels + ("y",):
                removed.append(word_letters.pop(0))   #getting any other consonants that come before the first vowel
            word_letters += removed + ["a", "y"]   #adding the first few consonants and "ay" to the end of the word
        else:
            word_letters += ["w", "a", "y"]   #adding "way" to the end of the word
        word_letters += suffix   #adding the non-letter or number suffix back to the end of the word
        word_list.append("".join(word_letters))   #adding word to word_list after making it into a single string
    return " ".join(word_list)   #returning output

def translate_from_pig_latin(string):
    string_list = string.split()  #divide input into each letter
    vowels = ("a", "e", "i", "o", "u")   #define vowels to check if each word starts with one or not
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    word_list = []   #empty output list. will eventually have each finished word
    for word in string_list:   #itirate through each word and perform operations to turn it into pig latin
        if word.isdigit():   #checking if the word is a number
            word_list.append(word)   #adding the number to the response
            continue   #skipping the function
        word_letters = list(word)   #split word into characters
        if word_letters[-3:] == ["w", "a", "y"]:    #check if word ends in "way"
            for i in range(1,3):
                word_letters.pop(-1)   #if so, just take off "way"
            word_list.append("".join(word_letters)) #and add to output
            continue    #and we're done
        elif word_letters[-2:] == ["a", "y"]:   #if it ends in "ay"
            for i in range(1,2):
                word_letters.pop(-1)   #if so, just take off "ay"
            word_letters.insert(0, word_letters.pop(-1))    #and put the consonant before it at the beginning
        else:
            raise ValueError(word + " is not valid Pig Latin")
    return " ".join(word_list)

print(translate_from_pig_latin(translate_to_pig_latin(input("input: "))))
