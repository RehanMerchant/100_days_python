import sys
import random

print("Welcome to rock, paper and scissor game!!")

user_input = int(input("0 for rock, 1 for paper and 2 for scissor: "))

if not user_input>=0 or not user_input<3:
    print("Invalid Input")
    sys.exit()

computer_input = random.randint(0,2)

choice = ""
if computer_input == 0:
    choice="Rock"
elif computer_input ==1:
    choice="Paper"
else:
    choice="Scissor"

print(f"Computer choice {choice}")

if user_input ==0 and computer_input == 2:
    print("You win")
elif user_input == computer_input:
    print("Draw")
elif computer_input > user_input:
    print("Computer wins")
else:
    print("You Win")

