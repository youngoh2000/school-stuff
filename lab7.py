#! /usr/bin/env python3
print('Content-type: text/html\n')
file1= open("top100moviesAFI.txt","r")
AFI=file1.readlines()
file1.close()

file2= open("top100moviesRT.txt","r")
RT=file2.readlines()
file2.close()

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Top Movie</title>
</head>
<body>
    <table border=1>{content}</table>
</body>
</html>"""

emptyStr = ""

all_movies = set(AFI) | set(RT)

for movie in sorted(all_movies):
    if movie in AFI:
        AFIrank = AFI.index(movie)
    else:
        AFIrank = "--"
    if movie in RT:
        RTrank = RT.index(movie)
    else:
        RTrank = "--"
    emptyStr += "<tr>" +"<td>"+movie+"</td>"+"<td>"+str(AFIrank)+"</td>"+"<td>"+str(RTrank)+"</td>" + "</tr>"
print(html.format(content = emptyStr))
