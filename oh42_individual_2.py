##Homework 2##
##Question 1#
def hangman():
    ##number of tries
    tries = 6
    ##the word to guess
    secretCode = "secret"
    ##empty list for correct letters
    correctLetter = []
    ##while number of tries is greater than zero
    while tries > 0:
        ##empty string to be displayed
        display = " "
        ##loop through individual letters in secret code
        for letter in secretCode:
            ##check if individual letters match correct letters  
            if letter in correctLetter:
                ##if so, add the correct letters to the display
                display += letter
            else:
                ##if so, add empty space for incorrect letters 
                display += " "
        ##printing out the guess letters
        print("What you have so far:", display)
        ##check if display matches secret code
        if display == secretCode:
            ##then end
            break
        ##ask user for input
        userInput = input("Enter one letter: ")
        ##check if user's input is in secretCode's letters
        if userInput in secretCode:
            print("Correct guess")
            ##append the correct letter into correctletter list
            correctLetter.append(userInput)
        else:
            print("Incorrect Guess")
            ##if it is the incorrect guess deduct 1 from number of tries
            tries -= 1
            break
        ##print the number of guesses left
        print(tries, "guesses left")            
    ##if number of tries remains above 0 then user wins
    if tries:
        print("You won!")
    ##if not, user loses
    else:
        print("You lost")

##Question 2##
import random
def game():
    ##allow the user to make a choice
    choice = input("rock, paper or scissors:" )
    ##allow the AI to make a choice
    aiChoice = ["rock","paper","scissors"]
    ##comChoice randomizes the ai's choices in aiChoice
    comChoice = random.choice(aiChoice)
    ##check for user's choice and Ai's choice
    ##paper beats rock, paper loses..etc
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
