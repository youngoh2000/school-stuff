#YOUNG OH
#group 2
#1: Develop an algorithm to solve all remaining steps in this problem.
##To load the data from a file, strip and split into a list by looping through teams.txt
##to print the information, manually print out the index positions of each team and scores by data[][]
##To create a list of names of teams with less than 5 letters, loop through the data file.
##If the length of name[0], the name of the team is less than 5. If so list the teams

##To create a list of names of the 3 teams with the highest wins, first loop through the range of length of data which will be 6 times.
##append the list into a sorted lst which would only indicate the highest numbers
##then create a comprehension list by looping data. Then compare the number of wins to the the lst that contains top 3 wins
##if so print out the names while sorting

#2: Use a list comprehension to load the data from a file named “teams.txt”. There’s a sample filePreview the document on Canvas with the data shown above.
data = [word.strip().split(" ") for word in open("teams.txt", "r")]
print(data)

print()
#3: Print out the information read in from the file formatted as shown in the example.
#Bear - sharks - cats - hedgehogs - ants - aardvark
print(data[0][0], "have won", data[0][1],"games")
print(data[1][0], "have won", data[1][1],"games")
print(data[2][0], "have won", data[2][1],"games")
print(data[3][0], "have won", data[3][1],"games")
print(data[4][0], "have won", data[4][1],"games")
print(data[5][0], "have won", data[5][1],"games")

print()
#4: Use a list comprehension to create a list of the names of teams with less than 5 letters in their name.
lessThanFive = [name[0] for name in data if len(name[0]) < 5]
print("Teams with names shorter than 5 letters:", lessThanFive)

print()
#5: Use a list comprehension to create a list of the names of the three teams with the highest wins.
lst = []
for i in range(len(data)):
    lst.append(int(data[i][1]))
print(sorted(lst))
newList = sorted(lst)[3:]
print(newList)

threeTeams = sorted([name[0] for name in data if int(name[1]) >= newList[0]])
print("The three teams with the most wins are:", sorted(threeTeams))
