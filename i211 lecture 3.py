##Group work 1
##numberList = []
##while True:
##    
##    name = input("Please enter a number or STOP:")
##    if name.upper() == "STOP":
##        break
##    numberList.append(int(name))
##print("The Total sum is", sum(numberList))
##
##
##sum = 0
##while True:
##    num = input("enter")
##    if num.upper() == "STOP"
##    break
##    sum += int(num)
##print(num)

##work 2
##even = []
##odd = []
##other = []
##for i in range(10):
##    number = eval(input("Please enter a number: "))
##    if number%2 == 0:
##        even.append(number)
##    elif number%2 == 1:
##        odd.append(number)
##    else:
##        other.append(number)
##print("Evens:", even)
##print("Odds:", odd)
##print("others:", other)

##work 3
scores = {"Dave": 125, "Abby": 100, "Carrie": 275, "Ben":150}
print(sorted(scores))
name = input("Please Enter a Player Name: ")

if name in scores:
    randomName = scores.get(name, "Dave")
    print("The score for", name, "is", randomName)
