#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import cgi

string = "i211f18_oh42"     
password = "my+sql=i211f18_oh42"	
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()
name = form.getfirst('name', 'none')


html = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<title>Results</title></head>
    <body>
	<h1> Current Votes </h1>
	<table width = "400" border=1>
	<tr><th>Mascot</th><th>Votes</th></tr>
	
	<tr><td>{name}</td><td>{vote1}</td></tr>
	<tr><td>{name2}</td><td>{vote2}</td></tr>
	<tr><td>{name3}</td><td>{vote3}</td></tr>
	<tr><td>{name4}</td><td>{vote4}</td></tr>
	<table>
    <h2>The winner is</h2>
    {image}
    </body>
</html>
"""
try:
    SQL = "SELECT Contestant, Name FROM Contestants WHERE ;"
    cursor.execute(SQL)
    result = cursor.fetchall()
    
except Exception as e:		
    print('<p>Something went wrong with the SQL!</p>')
    print (SQL, "Error:", e)
else:
##    table = ""
##    for selections in result
##        if name == selections[1]
