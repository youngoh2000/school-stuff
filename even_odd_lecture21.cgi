#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi, random

num = random.randrange(1,101)

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title></head>
    <body>
        <p>You guessed {user}</p>
        <p>computer chose {comp}</p>
	<p>{message}</p>
    </body>
</html>"""

form = cgi.FieldStorage()
guess = form.getfirst('guess', 'even')

if (num % 2 == 0 and guess == "even") or \
(num % 2 == 1 and guess == "odd"):
    message ="Congratulations! You guessed right."
else:
    message ="Sorry, you guessed wrong"

print(html.format(user = guess, comp = num, message = message))
