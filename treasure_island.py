print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('You\'re at the crossroad. Where do you want to go? Type "left" or "right". ')
road_direction = input("").lower()

if road_direction == "left":
  print('You are at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
  traveling_way = input("").lower()
  if traveling_way == "wait":
    print("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    house_colour = input("").lower()
    if house_colour == "red":
      print("Burned by fire. Game over.")
    elif house_colour == "yellow":
      print("You found the treasure! You win!")
    elif house_colour == "blue":
      print("Eaten by beasts. Game over.")
    else:
      print("Game over.")
  else:
    print("Attacked buy trout. Game over.")
else:
  print("Fall into a hole. Game over.")