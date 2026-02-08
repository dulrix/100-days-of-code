import random  # Import the random module to generate a random choice for the computer

# Define the ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of options for the game
options_list = ["rock", "paper", "scissors"]
# List of ASCII art for each option
art_list = [rock, paper, scissors]

while True:
    try:
        user_input = int(input("Type 0 for rock, 1 for paper, 2 for scissors (or any other key to quit): "))
        if user_input < 0 or user_input > 2:
            print("Invalid input, please try again with 0, 1, or 2")
            continue
    except ValueError:
        print("Exiting game. Goodbye!")
        break

    user_choice = options_list[user_input]
    computer_choice = random.choice(options_list)
    comp_index = options_list.index(computer_choice)

    # Display the user's choice
    print("\nYou chose: ")
    print(art_list[user_input])

    # Display the computer's choice
    print("\nComputer chose: ")
    print(art_list[comp_index])

    if user_choice == computer_choice:
        print("It's a draw!!! ")
    elif user_choice == "rock" and computer_choice == "scissors": 
        print("You won!!!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!!!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!!!")
    else:
        print("You lost mf") 
    print("\n---\n")