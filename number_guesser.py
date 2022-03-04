# importing a modole that's built-in to python
# random module creates random number
import random 

# ask user a number for the top range
# check if top range is a digit
# if a digit convert it to int 
# if top range is less than 0 quit the game
# Else if not a digit exit the game

# use top range to create a random number using random module

# create a while loop
# inside the loop
# ask for a guess
# if user guess is a digit convert it to int
# Else tell user to type a number and continue
# if user guess is equals the random number print you got it and break
# else if user guess is greater than say greater else below less

top_of_range = input("Enter the top range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Next time enter a number greater than 0, goodbye")
        quit()

else:
    print("Please enter a number next time, goodbye.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    
        if user_guess == random_number:
            print("You got it correct!")
            break
        elif user_guess > random_number:
            print("You need to guess lower.")
            continue
        else:
            print("You need to guess higher")
            continue

    else:
        print("Please enter a number between 0 and " + str(top_of_range))
       

print("Number of guesses: " + str(guesses))