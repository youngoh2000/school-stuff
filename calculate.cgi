#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   #parses form data

html = """<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Calculate 1 CGI</title></head>
    <body>
        <h1>Your number</h1>
        <p>{content}</p>
    </body>
</html>"""

user = form.getfirst('number1','0')
user2 = form.getfirst('number2', '0')
print(html.format(content = user + user2))
