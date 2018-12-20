#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import cgi

string = "i211f18_oh42"     
password = "my+sql=i211f18_oh42"	
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


html="""
<html>
<head><meta charset="utf-8">
<title>Faculty Add</title></head>
    <body>
	<h1> Faculty Edit </h1>
	<form action="FacultyUpdate.cgi" method="get">
	<input type="hidden" name="fid" value="1" />
	{content}
	
##	<p>Name: <input type="text" name="name" value="John Idle" /></p>
##	<p>Title: <input type="text" name="title" value="Students" /><p>
##	<p>Email: <input type="text" name="email" value="eidle@indiana.edu" /><p>
##	<p>Areas: <input type="text" name="areas" value="Comedy, Music" /><p>
	<input type="submit" value="Edit Faculty">
	</form>
</body> 
</html>
</html>"""

try:
    
    SQL = "SELECT FROM Faculty WHERE FacultyID =" + ;"
    cursor.execute(SQL)
    result = cursor.fetchall()

except Exception as e:		
    print('<p>Something went wrong with the SQL!</p>')
    print (SQL, "Error:", e)
else:
    tableEdit =""
    for row in result:
##        table += "<tr>"
##        for entry in row:
##            table += "<td align='center'>" +str(entry)+ "</td> + <td  align='center'><a href='FacultyEdit.cgi?"
##        table +="</tr>"
##    print(html.format(content = table))
