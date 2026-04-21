import random
print("Welcome to rock paper session game")

user_input=input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.")
computer_choice = random.randint(0,2)
print(f"computer choice is {computer_choice}")

if user_input == 0 and computer_choice == 1:
    print("You win!")
elif user_input == 1 and computer_choice == 2:
    print("You lose!")
elif user_input == 2 and computer_choice == 0:
    print("You win!")
elif computer_choice == user_input:
    print("DRAW!!")

