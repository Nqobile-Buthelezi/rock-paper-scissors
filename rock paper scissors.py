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

#Write your code below this line 👇
print("Welcome to my Rock, Paper, Scissors game!")
choices = [rock, paper, scissors]

user_choice = input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_choice = random.randint(0, 2)

if user_choice == "0":
  print(choices[int(user_choice)])
  print("Computer chose:\n")
  print(choices[computer_choice])
  if computer_choice == 1:
    print("You lose.")
  elif computer_choice == 0:
    print("It's a draw")
  else:
    print("You win")
elif user_choice == "1":
  print(choices[int(user_choice)])
  print("Computer chose:\n")
  print(choices[computer_choice])
  if computer_choice == 2:
    print("You lose.")
  elif computer_choice == 1:
    print("It's a draw")
  else:
    print("You win")
elif user_choice == "2":
  print(choices[int(user_choice)])
  print("Computer chose:\n")
  print(choices[computer_choice])
  if computer_choice == 0:
    print("You lose.")
  elif computer_choice == 2:
    print("It's a draw")
  else:
    print("You win")
else:
  print("That's not a valid answer sorry.")