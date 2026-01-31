print('''                               
                                       _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 ''')


print("Welcome to Treasure Island.")  # Greeting message for the game
print("Your mission is to find the treasure.")  # Informing the player of their goal
choice1 = input("Would you like to go left or right?  ").lower()  # Asking the player for their first choice
if choice1 == "left":
    print("You've reached a river. You can either swim across or wait for a boat.")  # Presenting the player with a river scenario
    choice2 = input("Swim or wait?  ").lower()  # Asking the player how to proceed at the river
    if choice2 == "wait":
        print("A boat arrives, and you cross the river safely. You reach a temple with three doors.")  # Outcome of waiting for a boat
        choice3 = input("Which door are you gonna choose? Red, blue, or yellow  ").lower()  # Asking the player to choose a door
        if choice3 == "yellow":
            print("You find the treasure! Congratulations, you win!")  # Winning scenario
        elif choice3 == "red":
            print('You enter the red door and find a room filled with fire.'
                  ' You try to escape but get burned. GAME OVER!  ')  # Losing scenario for the red door
        elif choice3 == "blue":
            print('You enter the blue door and find a room filled with beasts.'
                  'They attack you, and you can\'t escape. GAME OVER!  ')  # Losing scenario for the blue door
        else:
            print('You try to open a door that doesn\'t exist.'
                  'You\'re stuck, and the temple starts to collapse. GAME OVER!  ')  # Losing scenario for an invalid door choice
    elif choice2 == "swim":
        print('You start swimming across the river but are attacked by a giant trout.'  
              'You try to defend yourself but are dragged underwater. GAME OVER!  ')  # Losing scenario for swimming
    else:
        print('You can\'t decide what to do, and the river starts to flood. '
              'You\'re swept away by the current. GAME OVER!  ')  # Losing scenario for indecision at the river
elif choice1 == "right":
    print("You venture into the jungle and suddenly fall into a hidden hole. You can't climb out. GAME OVER!  ")  # Losing scenario for going right
else:
    print("You're lost in the jungle. You can't find a path to follow. GAME OVER! ")  # Losing scenario for an invalid first choice