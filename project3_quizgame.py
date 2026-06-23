print("Hello, Welcome to the ultimate quiz game!")

playing = input("Do you want to start playing? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets start the game :)")
score = 0 

answer = input("What's the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score/4)*100) + "%.") 
