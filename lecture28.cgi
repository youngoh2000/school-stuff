#! /usr/bin/env python3

print('Content-type: text/html\n')
##
import cgi

form = cgi.FieldStorage()
NAME = form.getfirst("name", "")
TITLE = form.getfirst("title", "")
Email = form.getfirst("email", "")
Areas = form.getfirst("areas", "")

import MySQLdb

string = "i211f18_oh42"     
password = "my+sql=i211f18_oh42"	
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


html = """
    <html>
    <head><meta charset="utf-8">
    <title>Faculty Add</title></head>
            <h1> Faculty Table </h1>
        <body>
            <table border='1' width='30%'>
            <tr><th>FacultyID</th>
            <th>Name</th>
            <th>Title</th>
            <th>Email</th>
            <th>Areas</th>
            <th>Edit</th>
            <th>Delete</th>
            </tr>
            {content}
            </table>
            </form>
        </body>
    </html>
</html>"""


try:    
    SQL = "INSERT INTO Faculty (NAME, TITLE, Email, Areas)"
    SQL += "VALUES ('" + NAME + "', '" + TITLE + "', '" + Email + "', '" + Areas + "');"
    cursor.execute(SQL)
    db_con.commit()
    
    SQL = "SELECT * FROM Faculty;"
    cursor.execute(SQL)
    result = cursor.fetchall()

except Exception as e:		
    print('<p>Something went wrong with the SQL!</p>')
    print (SQL, "Error:", e)
else:
    
    table =""
    for row in result:
        table += "<tr>"
        for entry in row:
            table += "<td align='center'>" +str(entry)+ "</td>"
        table += "<td align='center'>" + "<a href='lecture28Edit.cgi?fid=" + str(row[0]) + "'>Edit</a>" + "</td>"+ "<td align='center'>" + "<a href='lecture28Delete.cgi?fid=" + str(row[0]) + "'>Delete</a>" + "</td>"+"</tr>"
print(html.format(content = table))



