#Simple quiz game to get used to Python, print/string/input/concatenation/lowercase/tostring

print("Welcome to my computer quiz")
score = 0

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Let's play!")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Well done. You got the correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Well done. You got the correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Well done. You got the correct answer!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + "/3 questions correct.")