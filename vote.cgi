#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import cgi

string = "i211f18_oh42"     
password = "my+sql=i211f18_oh42"	
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<title>Vote!</title></head>
    <body>
	<h1> Vote for the next SICE msacot now </h1>
	<form action="RecordVote.cgi" method="post">
	<p><strong>Name : </strong><input type="text" name="name"></p>
	<p><input type="radio" name="choice" value="1" /> 
        {radioContent}
	<input type="submit" value="Submit Vote">
	</form>
    </body>
</html>
"""

try:
    SQL = "SELECT ContestantID, Name, Description FROM Contestants;"
    cursor.execute(SQL)
    result = cursor.fetchall()
except Exception as e:		
    print('<p>Something went wrong with the SQL!</p>')
    print (SQL, "Error:", e)
else:				
    ##Table creating
    radio =""
    for selections in result:
        radio += "<p>"
        radio += "<input type='radio' name='choice' value='" + str(selections)[1] + "'/>""<strong>" + str(selections[1]) + "</strong>" + " :" + str(selections[2])
        radio +="<p>"

    #results
    print(html.format(radioContent = radio))
