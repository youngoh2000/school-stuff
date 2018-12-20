import xml.etree.ElementTree as ET

root = ET.parse("students.xml")
##root.iter goes through each student
students = root.iter("student")

for student in students:
    print("student ID:", student.find("id").text, "\n")
