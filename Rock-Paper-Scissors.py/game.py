import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game=[rock,paper,scissors]
while True:

   user_choice = int(input ('\n select your option! type 0 for rock , 1 for paper, 2 for scissors'))
   print("user_choice:", user_choice)

   computer_choice = random.randint(0,2)
   print("computer_choice:", computer_choice)

   if user_choice >=3 or user_choice < 0: 
    print("wrong option< choosse correct option")
   else:
    print("user_choice \n",game [user_choice])    
    print ("computer choice \n",game[computer_choice])
   if user_choice == 0 and computer_choice == 2:
       print(" rock smashes scissors! you won!")
   elif computer_choice == 0 and user_choice == 2:
       print(" rock smashes scissors! you lose!")
   elif computer_choice > user_choice: 
       print("you lose!")
   elif user_choice > computer_choice: 
       print ("youwin!")
   elif user_choice == computer_choice :
       print("match tie!")
