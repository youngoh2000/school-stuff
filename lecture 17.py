data = [["Item", "Cost", "Type"], ["Coke", "$2", "Drink"],
        ["Water", "$0", "Drink"], ["Fries", "$4", "Appetizer"],
        ["Onion Rings", "$3", "Appetizer"], ["Steak", "$12", "Entree"],
        ["Chicken", "$8", "Entree"], ["Caesar Salad", "$7", "Entree"]]
print(data)

out = open("template3.html", "w")

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hello</title>
</head>
<body>
    <table border=1>{content}</table>
        
    
</body>
</html>"""



emptyStr = ""
for individualData in data:
##    print(individualData)
    emptyStr += "<tr>"
    for td in individualData:
        emptyStr += "<td>" + str(td) + "</td>"
##        print(td)
    emptyStr += "</tr>"
out.write(html.format(content = emptyStr))
out.close()

import re
import urllib.request
def html(url):
    web_page = urllib.request.urlopen(url)
    content = web_page.read().decode(errors = "replace")
    web_page.close()
    trFind = re.find("(?<=<tr>).+?(?=</tr>)", content)
    print(trFind)


#main
html("view-source:file:///C:/Users/Young%20Oh/Documents/template3.html")
