#! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi

form = cgi.FieldStorage()
html = """
<!doctype html>
<html>
    <head>
	<meta charset="utf-8">
	<title>Calculate 1</title>
    </head>
    <body>
	<p>{content}</p>
    </body>
</html>"""
try:
	total = eval(form.getfirst('one','0')) + eval(form.getfirst('two','0'))
except:
	total = "Error invalid numbers"

print(html.format(content = 'The total is: '+str(total)))
