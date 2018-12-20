import re

file = open("template3.html", "r")
contents = file.read()
file.close()
print(contents)

row = re.findall("(?<=<tr>).+?(?=</tr)", contents)
print(row)
data = []
for item in row:
    line = re.findall("(?<=<td>).*?(?=</td>)", item)
    data.append(line)
print(data)
