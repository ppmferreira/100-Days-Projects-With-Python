print("Welcome to Treasure Island")
print("Your mission is to find the hidden treasure. 🏴‍☠️")

choice1 = input ("You arrive at a crossroads. Do you want to go 'left' or 'right? ").lower()
if choice1 == "left":
    choice2 = input("You reach a river. Do you 'swim' or 'wait' for a boat? ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at a castle with three doors: 'red', 'blue', 'yellow'. Whitch one do you choose? ").lower()
        if choice3 ==  "yellow":
            print("Congratulations! You found the treasure! 🎉💰")
        elif choice3 == "red":
            print("Oh no! The room is full of fire. Game over. 🔥")
        elif choice3 == "blue":
            print("You were eaten by wild beasts. Game over. 🐺")
        else:
            print("Invalid choice. Game over. ❌")
    elif choice2 == "swim":
        print("You were attacked by a giant crocodile. Game over. 🐊")
    else:
        print("Invalid choice. Game over. ❌")
elif choice1 == "right":
    print("You fell into a deep hole. Game over. 🕳️")
else:
    print("Invalid choice. Game over. ❌")