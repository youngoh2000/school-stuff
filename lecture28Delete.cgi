#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi
import MySQLdb
string = "i211f18_oh42"     
password = "my+sql=i211f18_oh42"	
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html ="""
<html>
<body>
<h1>Faculty Member Deleted!</h1>
<p><a href="lecture28view.cgi">Go Back</a></p>
</body>
</html>
</html>"""

try:
    form = cgi.FieldStorage()
    fid = form.getfirst("fid", "")
    SQL = "DELETE FROM Faculty WHERE FacultyID = " + fid + ";"
    cursor.execute(SQL)
    db_con.commit()
    
except Exception as e:		
    print('<p>Something went wrong with the SQL!</p>')
    print (SQL, "Error:", e)

print(html)

