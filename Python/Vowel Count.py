def getCount(inputStr):
    vowels = "aeiou";
    return sum([c in vowels for c in inputStr]);