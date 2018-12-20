##SUB to rpelace replace all instances of a pattern with another string
##test = "all is cats."
###replace groups of 1 or more letters with cats
##print(re.sub('[\w]+', "cats", test))
##>>> 
##cats cats cats.

##Overhead(front)        (?= something)
##test = "cat yes hat no bat yes rat no mat no"
###matches all three letter words followed by ' yes'
##print(re.findall('[\w]{3}(?= yes)', test))
##>>> 
##['cat', 'bat']

##Lookbehind(back)    (?<= something)
##test = "filler start we want from here"
###matches after the word 'start'
##print(re.findall('(?<=start)[\w ]+', test))
##>>> 
##[' we want from here']

##   . in a regular expression will match any character except a new line "\n"
## re.DOTALL changes . to match anything, including "\n"
##ex  re.findall(".+(?=The End)", novel, re.DOTALL)


import re
def cool():
    ##print(re.findall("<pattern>", string)
    test = "this is a *test* phrase."

    #search for groups of 1 or more letters
    print("Matches:", re.findall("[a-z]+", test))

    test2 = "ThiS wAs wRIttEn ODdly."
    ##looks for Capital letter followed by lowercase letter 
    print("Matches:", re.findall("[A-Z][a-z]",test2))

    test3 = "This is a *test* phrase."
    print("A s:", re.findall("[a]+", test3))
    print("Non As:", re.findall("[^a]+", test3))

    test4 = "This is a *test* phrase. We want *these* words."
    print("Stars:", re.findall('[*][a-z]+[*]', test4))

    ##using ?    :which means 0 or 1
    ##result ['tunafish', 'tuna fish']
    test5 = "tunafish; tuna fish; tuna     fish"
    print("Matches:", re.findall('tuna[ ]?fish', test5))

    ##using x{min, max}
    ##result ['spoon', 'spooon']
    test = "spon; spoon; spooon; spooooooon"
    print("Matches:", re.findall('sp[o]{2,3}n', test))

    ##using |   :which means A or B
    ##result ['cat', dog']
    test = "A cat or a dog."
    print("Matches:", re.findall('cat|dog', test))

##Two vowels (grp work)
    ##get a result of ['loon','aww','meek','ziiim']
def Vowels():
    test = "test loon etta planet aaw meek ziiim try"
    print(test)
    print("match:", re.findall("[\w]*[aeiou][aeiou][\w]", test))
##Vowels()


##Email addresses v1(grp work)
import urllib.request    
def email():
    cool = input("Search what page?: ")
    web_page = urllib.request.urlopen(cool)
    contents = web_page.read().decode(errors="replace")
    web_page.close()
    
    print("the email addresses in", cool)
    print(re.findall("[\w.-]+[@][\w.-]+", contents))
    

##main
email()
