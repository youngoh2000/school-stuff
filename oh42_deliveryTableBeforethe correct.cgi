#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi
##This is the data from the input
form = cgi.FieldStorage()
itemCGI = form.getfirst("item", "")
costCGI = eval(form.getfirst("cost", "0"))
droneCGI = form.getfirst("delivery_method", "")
droneCost = ""

import MySQLdb

string = "i211f18_oh42"     
password = "my+sql=i211f18_oh42"	
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def table(result):
    html = """
        <html>
            <head><meta charset="utf-8">
                <title>Robot Delivery System Confirmation</title></head>
                <body>
                <h1>Robot Delivery System Confirmation</h1>
                <p>You have selected to have a {Item} delivered by {Robot}.</p>
                <p>Your total comes to {TotalCost}</p>
            <h2>Delivery Records</h2>
        <table border="1">
        {content}

            </body>
        </html>
        </html>"""
    ##Total Cost
    if droneCGI == "drone":
        droneCost = str(10)
        costCGI += 10
    elif droneCGI == "self driving car":
        droneCost = str(20)
        costCGI += 20
    elif droneCGI == "giant robot":
        droneCost = str(1000)
        costCGI += 1000


    ##Table creating
    table =""
    for row in result:
        table += "<tr>"
        for entry in row:
            table += "<td align='center'>" +str(entry)+ "</td>"
        table +="</tr>"
    #result
    print(html.format(content = table, Item = itemCGI, Robot = droneCGI, TotalCost = costCGI))


try:
    ##Adds the input into rows
    SQL = "INSERT INTO Deliveries (Item, Cost, Method, Shipping)"
    SQL += "VALUES ('" + itemCGI + "', '" + str(costCGI) + "', '" + droneCGI + "', '" + droneCost + "');"
    cursor.execute(SQL)
    db_con.commit()

    ##Gets all the current data in Faculty
    SQL = "SELECT * FROM Faculty;"
    cursor.execute(SQL)
    result = cursor.fetchall()

    

except Exception as e:		
    print('<p>Something went wrong with the SQL!</p>')
    print (SQL, "Error:", e)
else:				
    table(result)



