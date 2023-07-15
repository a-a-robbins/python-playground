# based on 'Mini Python Projects' by Tech with Tim

import random

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True: 
    userInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if userInput == "q": 
        break
    
    if userInput not in options: 
        continue

    randNum = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2

    computerPick = options[randNum]
    print("Computer picked", computerPick)

    if(userInput == "rock" and computerPick == "scissors"): 
        print("You won!")
        userWins += 1
    elif(userInput == "paper" and computerPick == "rock"): 
        print("You won!")
        userWins += 1
    elif(userInput == "scissors" and computerPick == "paper"): 
        print("You won!")
        userWins += 1
    else: 
        print("You lost!")
        computerWins += 1


print("Congrats, you won ", userWins, "times. The computer won", computerWins, "times.")