def translate_to_pig(string):
    string_list = string.split()
    vowels = ("a", "e", "i", "o", "u")
    word_list = []
    for word in string_list:
        word_letters = list(word)
        if not word_letters[0].lower() in vowels:
            removed = word_letters.pop(0)
            word_letters.append(removed)
            word_letters.append("a")
            word_letters.append("y")
        else:
            word_letters.append("w")
            word_letters.append("a")
            word_letters.append("y")
        word_list.append("".join(word_letters))
    return " ".join(word_list)
print(translate_to_pig(input()))
