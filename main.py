print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'. ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake there's a island in the middle of the lake "
                    "type 'swim' to swim acros or "
                    "type 'waite' to wait for a boat ").lower()
    if choice2 == "waite":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors."
                        " One yellow, one red, adn one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("IT'S A ROOM FULL OF FIRE. GAME OVER!")
        elif choice3 == "yellow":
            print("YOU WIN THE PRIZE")
        elif choice3 == "blue":
            print("YOU ENTER A ROOM FULL OF BUGS. GAME OVER!")
        else:
            print("TIME KILLED YOU. GAME OVER!")


    else:
        print("You got attacked by an angry trout. GAME OVER!")



else:
    print("You fell into a hole. GAME OVER")
