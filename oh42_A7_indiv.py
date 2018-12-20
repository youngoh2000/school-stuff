##Young Oh
##Group 2

##Question 1
import xml.etree.ElementTree as ET
import datetime, os
def display_book(data):
    root = ET.parse(source="library.xml")
    books = root.iter("book")
    for book in books:
        if book.attrib["id"] == data:
            title = book.find("title").text
            author = book.find("author").text
            price = book.find("price").text
            return "Title: "+ title,"Author: "+ author,"Price: "+ price
            
#main Question 1
display = display_book("bk107")
for output in display:
    print(output)

##Question 2
root = ET.parse(source="library.xml")
books = root.iter("book")
def december():
    for book in books:

        publishDate = book.find("publish_date").text.split("-")
##        print(publishDate)
        dateSort = datetime.date(int(publishDate[0]),int(publishDate[1]), int(publishDate[2]))
##        print(dateSort)

        if dateSort.strftime("%B") in "December":
            title = book.find("title").text
            author = book.find("author").text
            price = book.find("price").text
##            print("Title:",title,"\n","Author:",author,"\n","Price: ",price)
    return title, author, price
answer = december()
for answerz in answer:
    print(answerz)
##Question 3



