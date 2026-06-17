print("Welcome to the game!")
name = input("what's your name? ")
age = int(input("What's your age? "))

health = 10 

if age >= 18:
    print(name,",", "You are old enough to play this game.")

    weapon = input("Choose a weapon Sword or Knife (S/K)?: ")
    if weapon == "":
        print()
    

    wants_to_play = input("Do you want to start playing (yes/no)? ").lower()
    if wants_to_play == "yes":
        print("You will start with", health, "health.")
        print("Let's start!") 

        choose_sides = input("Choose Left or Right (L/R)?: ")
        if choose_sides == "L":
            ans = input("Nice, you follow the path and reached the lake. Now would you like to swim or go around (S/A)?: ")

            if ans == "S":
                print("You reached the other side of the lake by swimming.")
            elif ans == "A":
                print("You chose to go around but were bit by a snake on your way across the lake so you lost 5 health.")
                health -= 5 

            ans = input("You noticed a house and a river. so which one do you choose (H/R)?: ")
            if ans == "H":
                print("You went to the house and the owner greeted you. He is scared by you so you lost 5 health")
                health -= 5 
                if health <= 0:
                    print("You now have 0 health and YOU LOST")
                else: 
                    print("You survived... YOU WIN.")
            
            else:
                print("You chose the river but stumbled and fell in the river, YOU DIED.")

        else:
            print("You fell down and died.")

    else:
        print("see you next time...")

else:
    print("You aren't old enough to play this game", ",", name, ".")



