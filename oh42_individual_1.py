##Question 2##
##activate random module
import random
def game():
    ##allow the user to make a choice
    choice = input("rock, paper or scissors:" )
    ##allow the AI to make a choice
    aiChoice = ["rock","paper","scissors"]
    ##comChoice randomizes the ai's choices in aiChoice
    comChoice = random.choice(aiChoice)
    ##if arguments for user's choice and Ai's choice
    if comChoice == "rock" and choice.lower() == "paper":
        ##to know what Ai has picked
        print("Ai picks", comChoice)
        print("Ai wins")
    elif comChoice == "rock" and choice.lower() == "rock":
        print("Ai picks", comChoice)
        print("Tie")
    elif comChoice == "scissors" and choice.lower() == "scissors":
        print("Ai picks", comChoice)
        print("Tie")
    elif comChoice == "scissors" and choice.lower() == "Paper":
        print("Ai picks", comChoice)
        print("Ai wins")
    elif comChoice == "paper" and choice.lower() == "rock":
        print("Ai picks", comChoice)
        print("Ai wins")
    elif comChoice == "paper" and choice.lower() == "paper":
        print("Ai picks", comChoice)
        print("Tie")
    ##if User picks the correct counter
    else:
        print("Ai picks", comChoice)
        print("User Wins")

##Question 3##
def duplicate():
    ##Ask the user to enter a string
    choice = input("Enter a string: ")
    ##an empty string to append letters in choice
    emptyString = str()
    ##Going through each letter
    for letter in choice:
        ##duplicate individual letters by letter + letter
        emptyString += letter + letter
    print(emptyString)

##Question 4##
def TrueFalse():
    ##Boolean
    result = False
    ##a list
    listA = ["a", "b", "c", "d", "e", "f", "g"]
    print("The first list is:", listA)
    ##ask user to enter a list separated by commas 
    listB = input("Enter a list to compare: ")
    ##Going through each letters in listA
    for letterA in listA:
        ##Going through each letters in listB
        for letterB in listB:
            ##comparing letterA to letterB to check if at least one is common
            if letterA == letterB:
                result = True
                return result
    return result
