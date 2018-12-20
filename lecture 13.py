import re
import urllib.request
test = "abcdd"
#goal = "bc"

##finds letters after a and before d; however, adding [0] will make into string
myString = re.findall("(?<=a).+?(?=d)", test, re.DOTALL)[0]

##print(myString)

##head and body (group work)
def headbody(url):
    web_page = urllib.request.urlopen(url)
    content = web_page.read().decode(errors = "replace")
    web_page.close()
    head = re.findall("(?<=<head).+?(?=</head>)", content, re.DOTALL)[0]
    body = re.findall("(?<=<body).+?(?=</body>)", content, re.DOTALL)[0]
    print("Searching:", url)
    print("Head:",head)
    print("Body:",body)

#main
##target = input("searching")
##head, body = headbody(target)

#headbody("http://cgi.soic.indiana.edu/~dpierz/test.html")

##wiki browsing (group work)
def browsing(url):
    web_page = urllib.request.urlopen(url)
    content = web_page.read().decode(errors = "replace")
    web_page.close()
    body = re.findall("(?<=<body).+?(?=</body>)", content, re.DOTALL)[0]
    wiki = re.findall('(?<=<a href=").+?(?=" title=)', body)
    cool = [cooler for cooler in wiki if "wiki" and not ".org" in cooler]
    print(cool)
    
##browsing("https://en.wikipedia.org/wiki/Airy_wave_theory")



import urllib.request, re

def wiki_list(url):
    web_page = urllib.request.urlopen(url)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    body = re.findall('(?<=<body).+?(?=</body>)', lines, re.DOTALL)[0]
    hits = re.findall('(?<=href=").+?(?=")', body)
    wiki_links = [link for link in hits if "wiki" in link and ".org" not in link]
    return wiki_links

#main
url_list = wiki_list("http://en.wikipedia.org/wiki/Airy_wave_theory")

for url in url_list:
    print("\t", url)
