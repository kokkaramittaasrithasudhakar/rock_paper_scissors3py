#project4 rock,paper and scissors
#https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
#Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules:

#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.

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
if __name__ == "__main__":
  import random
  computer_choice = random.randint(0,2)
  # print(computer_choice)
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  
  if user_choice == 0 and computer_choice==2:
    print(f"You chose:\n{rock}\nComputer chose:\n{scissors}\nYou win!")

  elif user_choice == 1 and computer_choice==0 :
    print(f"You chose:\n{paper}\nComputer chose:\n{rock}\nYou win!")

  elif user_choice==2 and computer_choice==1 :
    print(f"You chose:\n{scissors}\nComputer chose:\n{paper}\nYou win!")

  elif user_choice==computer_choice:
    print("It's a draw") 

  else:
    print(f"You chose:\n{user_choice}\nComputer chose:\n{computer_choice}\nYou lose!")