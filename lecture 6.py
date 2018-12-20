##two vowels v3##
def vowelz():
    userInput = input("Enter a file name with .txt: ")
    words = [word.strip() for word in open(userInput, "r")]
    wordz = [word for word in open(userInput, "r")]
    print("All lines in the file:", words)
    print(wordz)
                ##split in every spaces of the list 
    two_v_words = [individualWord for word in words for individualWord in word.split(" ")\
                   if len([vowelCount for vowelCount in individualWord if vowelCount in "aeiou"]) >=2]

    print("Words that contain 2 or more vowels:", two_v_words)

##what it looks like##
##cool = []
##for word in words:
##    ##split gets rid of the spaces in word
##    for individualWord in word.split(" "):
##        cool.append(individualWord)

##leet speak##
def leet():
    userInput = input("Enter a phrase to translate: ")
    translation = {"1": "i","3":"e", "4":"a", "5":"s", "7":"t"}
    ##loop through individual letters in the phrase
    translate = [translation.get(letter, translation) for letter in userInput]
    print(translate)

##    for letter in userInput:
##        if letter in translation:
##            letter.replace(translation[letter], translation.values()
