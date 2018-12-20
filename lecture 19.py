out = open("lecture19.html", "w")

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
count = 0
count2 = 0
for row in range(10):
    emptyStr += "<tr>"
    for column in range(10):
    
        emptyStr += "<td>" + "Row"+ str(row+1) + "," + "Column" + str(column+1) + "</td>"
    emptyStr += "</tr>"
out.write(html.format(content = emptyStr))
out.close()
