import re

##replace groups of 1 or more letters with cats
##result: cats cats cats.
####test = "all is cats."
####print(re.sub("[\w]+", "cats", test))

##lookaheads
##result ["cat","bat"]
test = "cat yes hat no bat yes rat no mat no"
##find the 3 letters behind of "yes"
print(re.findall('[\w]{3}(?= yes)', test))
##finds letters after "no" and behind "yes"
print(re.findall("(?<=no ).+?(?= yes)", test))


##lookbehind
##result ["we want from here"]
test2 = "filler start we want from here"
##finds all after "start"
print(re.findall('(?<=start)[\w ]+', test2))

##redact (group work)- redacts email, name and number
def redaction():
    file = open("message.txt", "r")
    content=file.read()
    file.close()


    print(re.sub("[\w.-]+[@][\w.-]+|[(]?[\d]{3}[)]?[][\d-]{8}|[A-Z][a-z]*[][A-Z][a-z]*", "reacted", content))

##url finder(grp work)
    ##use source code)
import urllib.request
def url(url):
    web_page = urllib.request.urlopen(url)
    content = web_page.read().decode(errors = "replace")
    web_page.close()
    hits = re.findall('(?<=href=").+?(?=")', content)
    return hits


url("https://www.sice.indiana.edu/about/contact/index.html")
