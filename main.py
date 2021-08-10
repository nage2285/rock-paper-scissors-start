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

#print(rock)

#print(paper)

#print(scissors)

#input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

game_images = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

user_choice1 = int(user_choice)
print(game_images[user_choice1]) 

computer_choice = random.randint(0,2)
#print("Computer chose {computer_choice}")
print("Computer chose:")
print(game_images[computer_choice]) 

if user_choice1 == 0 and computer_choice == 2 :
  #print(rock + "\nComputer chose:" + scissors + "\n You win!" )
  print("\n You win!" ) 
elif user_choice1 == 1 and computer_choice == 2:
  #print(paper + "\nComputer chose:" + scissors + "\n You lose!")
  print("\n You lose!")
elif user_choice1 == 2 and computer_choice == 0:
  #print(scissors + "\nComputer chose:" + rock + "\n You lose!")
  print("\n You lose!")
elif user_choice1 == 1 and computer_choice == 0:
  #print(paper + "\nComputer chose:" + rock + "\n You win!")
  print("\n You win!")
elif user_choice1 == 2 and computer_choice == 1:
  #print(scissors + "\nComputer chose:" + paper + "\n You win!")
  print("\n You win!")
elif user_choice1 == computer_choice :
  #print(rock + "\nComputer chose:" + rock + "\n It's a draw!")
  print("\n It's a draw!")
else:
  print("Your number choice is invalid!")


#Rock = 0
#Paper = 1
#Scissors = 2

#List = ["Rock", "Paper", "Scissors"]

#Item_count = len(List)
#print(Item_count)

#print(type(List))

#random_input = random.randint(0, Item_count - 1)

#List1 = List[random_input]
#print(List1)
#print(random_input)


#print(type(Rock))

#win = 3
#lose = 4
#draw = 5

#List2 = ["win", "lose", "draw"]

#random_output = random.randint(3,5)

#Item_count1 = len(List2)

#List2 = str(List2)

#if Rock == 0:
 # print(rock + "\nComputer chose:" + paper + "\n You lose!" )

#elif Paper == 1:
 # print(rock + "\nComputer chose:" + scissors + "\n You win!")

#else :
 # print(rock + "\nComputer chose:" + rock + "\n It's a draw!")



