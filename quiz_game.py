# based on 'Mini Python Projects' by Tech with Tim

print("Welcome to the ultimate computer quiz!")

playing = input("Would you like to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play : ")

# question 1
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    answer = "Central Processing Unit"
    print("Sorry, that is not correct. The correct answer is " + str(answer) + " You'll get it next time :D ")

    

# question 2
answer = input("What does GPU stand for? ")

if answer.lower() == "graphical processing unit": 
    print("Correct!")
    score += 1
else: 
    answer = "Graphical Processing Unit"
    print("Sorry, that is not correct. The correct answer is " + str(answer) + " You'll get it next time :D ")


# question 3
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory": 
    print("Correct!")
    score += 1
else: 
    answer = "Random Access Memory"
    print("Sorry, that is not correct. The correct answer is " + str(answer) + " You'll get it next time :D ")



# question 4
answer = input("What does UPS stand for? ")

if answer.lower() == "uninterrrupted power supply": 
    print("Correct!")
    score += 1
else: 
    answer = "Uninterrupted Power Supply"
    print("Sorry, that is not correct. The correct answer is " + str(answer) + " You'll get it next time :D ")


print("Congratulations! You got " + str(score) + " questions correct")
print("That is a " + str((score / 4) * 100) + " %")