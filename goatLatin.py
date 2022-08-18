def toGoatLatin(sentence: str) -> str:
    def transformWord(word, index):
        if word[0].lower() in 'aeiou':
            word += 'ma'
        else:
            word = word[1:] + word[0] + "ma"
        word += "a" * (index + 1)
        return word
    ret = ""
    for index, word in enumerate(sentence.split()):
        ret += transformWord(word, index)
        ret += " "
    return ret[:-1]

print(toGoatLatin("I speak Goat Latin"))
