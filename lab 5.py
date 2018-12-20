import re
def warm():
    textFile = open("quote.txt", "r")
    contents = textFile.read()
    textFile.close()

        
    print("caps: ", re.findall("[A-Z][\w]*", contents))
    print("ing: ", re.findall("[\w]*[ing]", contents))
    print("Two 'a': ", re.findall("[\w]*a[\w]@a[\w]*", contents))


import urllib.request
def phone(url):
    web_page = urllib.request.urlopen("https://www.sice.indiana.edu/about/contact/index.html")
    contents = web_page.read().decode(errors="replace")
    web_page.close()

    print("Searching: ", url)
    print(re.findall("[(]+[\d]{3}[)][ ][\d]{3}[-][\d]{4}", contents))

phone("https://www.sice.indiana.edu/about/contact/index.html")
