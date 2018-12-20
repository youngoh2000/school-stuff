##New Match (grp Work)
import xml.etree.ElementTree as ET

def id_find(num):
    root = ET.parse(source="students.xml")
    students = root.iter("Student")
    for student in students:
        if student.find("id").text == num:
            name = student.find("name/first").text + " "
            name += student.find("name/last").text
            return name
    return "Not Found"
print(id_find("0019846768"))
print(id_find("0019846789"))
print(id_find("2349846434"))

print()
print("***Second answer***")

##Fee Finder
def fee_find(name):
    root = ET.parse(source="students.xml")
    fee = root.find("Student/fees")
    students = root.iter("Student")
    for student in students:
        if student.find("name/first").text + " " + student.find("name/last").text == name:
            return name + " " + "owes" + " " + student.find("fees").text + " " + fee.attrib["units"] + " " + fee.attrib["c"] + " " + "in fees"
    return "Not Found"

print(fee_find("Rose Dawson"))
print(fee_find("Jack Sparrow"))
print(fee_find("No Body"))
