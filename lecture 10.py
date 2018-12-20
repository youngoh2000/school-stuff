##Regular expressions: . ^ $ * + ? {} [] \ | ()
#{a , b}  means   a or b
#[a , b] means a or b
#ab mean ab
#[a-z]* means 0 or more lowercase English letter
#[[0-9]+ means 1 or more digit
#test = "th is a test"
#print("match:", re.finall('[a-z]+', test))

##test = "ThiS wAs wRIttEn ODdly."
##print("Matches:", re.findall('[A-Z][a-z]', test))
##Match: ['Th', 'As', 'It', 'En', 'Dd']

##test = "This is a *test* phrase."
##print("A s:", re.findall('[a]+', test))
##print("Non A s:", re.findall('[^a]+', test))
##>>> 
##A s: ['a', 'a']
##Non A s: ['This is ', ' *test* phr', 'se.']

##test = "This is a *test* phrase. We want *these* words."
##print("Stars:", re.findall('[*][a-z]+[*]', test)
##>>> 
##Stars: ['*test*', '*these*']


##test = "This is a [test] phrase. Ignore these [words]."
##print("Words in []:", re.findall('\[[a-z]+\]', test))
##>>>
##Words in []: ['[test]', '[words]']

##\d 	decimal digit 		        equiv. to 	[0-9]
##\D 	non-digit char 	                equiv. to 	[^0-9]
##\s 	whitespace char  	        equiv. to 	[ \t\n\r\f\v]
##\S 	non-whitespace char 	 	equiv. to 	[^ \t\n\r\f\v]
##\w 	alphanumeric char 	 	equiv. to 	[a-zA-Z0-9_]
##\W 	non-alphanumeric char  	        equiv. to 	[^a-zA-Z0-9_] 

##test = "tunafish; tuna fish; tuna     fish"
##print("Matches:", re.findall('tuna[ ]?fish', test))
##>>> 
##Matches: ['tunafish', 'tuna fish']
    
##test = "spon; spoon; spooon; spooooooon"
##print("Matches:", re.findall('sp[o]{2,3}n', test))
##>>> 
##Matches: ['spoon', 'spooon']



##import urllib.request
##web_page = urllib.request.urlopen("http://www.soic.indiana.edu/")
##contents = web_page.read().decode(errors="replace")
##web_page.close()
##
####Creating a file name "page.html"
##file_out = open("page.html", "w", encoding="utf-8")
##file_out.write(contents)
##file_out.close()
##print("All done! Open page.html in your browser! ")
##

##Get Content (Grp work)
import urllib.request
import os
def getContent(URL):
    print("accessing: ", URL)
    web_page = urllib.request.urlopen(URL)
    contents = web_page.read().decode(errors="replace")
    web_page.close()
    
    filename = os.path.basename(URL)

    ##if it has a basename then it would hold onto it 
    if not filename:
        filename = "index.html"

    file_out = open("I211Test.html", "w", encoding="utf-8")
    file_out.write(contents)
    file_out.close()
    
    print("All done! Open I211Test.html in your browser! ")
    
getContent("http://cgi.soic.indiana.edu/~dpierz/I211/I211Test.html")
##getContent("http://www.cnn.com/")

##understanding a page (grp work)
##1. 7
##2. 93
##3. <li>   </li>
##4. <h3> </h3>
##5. /career/employers/index.html" 
