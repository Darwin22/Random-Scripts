#High_Low_Guess_Game.py

#What = The following code is small script to play a high low guess game. The user enters a number
# computer checks the number is equal to a random number selected . Computer tells whether the number
# is higher or lower. If the user guess the correct number congratulation message comes up

###################################################################################################
#WHY =  Just for fun
import random

no_guess = 0
name = raw_input ("Hello, What is your name: ")

computer_num = random.randint(1,100)
print("Well "+ name+ " Lets play a game. Choose a number between 1 and 100 and the computer will decide whether you have guessed the right number: ")

while no_guess <6:
    if no_guess > 0:
        guess = int(raw_input("Take another guess "))
    else:
        guess = int(raw_input("Take a guess: "))

    no_guess += 1

    if guess < computer_num:
        print "Your guess is low"
    elif guess > computer_num:
        print "Your guess is high"
    else:
        break

if guess == computer_num:
    no_guess = str(no_guess)
    print "Good job "+ name+ " You guessed the number " + str(computer_num)+ "  in " +no_guess+ " guesses"

if guess != computer_num:
    computer_num = str(computer_num)
    print "Sorry the number I was thinking was "+ computer_num


