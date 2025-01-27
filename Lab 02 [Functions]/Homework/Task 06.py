

import random
def check(user,computer):
  if user== "rock":
    if computer=="paper":
       return computer
    elif computer== "scissor":
       return user
    else:
       return None

  elif user== "paper":
    if computer=="rock":
       return user
    elif computer== "scissor":
       return computer
    else:
       return None

  else:
    if computer=="rock":
       return computer
    elif computer== "scissor":
       return user
    else:
       return None

def playRockPaperScissor(rounds):
  user_point= 0
  computer_point=0
  for i in range (rounds):
    user=input()
    computer=random.choice(["rock","paper","scissor"])
    print(f'Computer:{computer}')

    winner =check(user,computer)
    if winner== None:
       continue
    if winner==user:
      user_point+=1
    else:
      computer_point+=1
  print(f"Your Score:{user_point}\nComputer's Score: {computer_point}")
  if user_point== computer_point:
      print("Draw!")
  elif user_point> computer_point:
      print("You have won the game!")
  else:
      print("Computer has won the game!")
round= int(input())
playRockPaperScissor(round)