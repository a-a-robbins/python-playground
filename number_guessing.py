# based on 'Mini Python Projects' by Tech with Tim

import random

randNum = random.randrange(0, 11)
#print(randNum)

#randInt = random.randint(0, 11)
#print(randInt)

topOfRange = input("Type a number: ")

if topOfRange.isdigit(): 
    topOfRange = int(topOfRange)

    if topOfRange <= 0: 
        print("Please type a number greater than 0 next time")
        #make me recursive so I don't have to quit
        quit()

else: 
    print("Please print a number that is larger than 0 next time")
    quit()

randNum = random.randint(0, topOfRange)

score = 0

while True: 
    score += 1
    guess = input("Guess a number between 0 and " + str(topOfRange) + ": ")
    if guess.isdigit(): 
        guess = int(guess)
    else: 
        print("Please type a number next time")
        continue
    
    if guess == randNum: 
        print("Congrats, you got it!")
        break
    elif guess > randNum:
            print("Sorry, that's not the one...guess lower next time")
    else: 
            print("Sorry, that's not the one...guess higher next time")
    continue

print("It took", score, "guesses")