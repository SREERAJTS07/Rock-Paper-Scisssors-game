import random

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

game_images = [rock, paper, scissors]
while True:
    user_choice = input("What do you choose? "
                        "Type '0' for Rock, '1' for Paper, '2' for Scissors, "
                        "or 'q' to quit.\n")

    if user_choice.lower() == 'q':
        break

    if user_choice not in ['0', '1', '2']:
        print("Invalid input. Please enter '0', '1', '2', or 'q' to quit.")
        continue

    user_choice = int(user_choice)
    computer_choice = random.randint(0, 2)
    print("Computer chose:")

    if user_choice == computer_choice:
        print(game_images[user_choice])
        print(game_images[computer_choice])
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
            user_choice == 2 and computer_choice == 1):
        print(game_images[user_choice])
        print(game_images[computer_choice])
        print("You win!")
    else:
        print(game_images[user_choice])
        print(game_images[computer_choice])
        print("You lose")
