import random 


rock_art = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper_art = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors_art = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")





ai_choices = ["Rock" , "Paper" , "Scissors"]

choice_chosen = str(input("Pick Rock, Paper, or Scissors: ").lower())




ai_choice = random.choice(ai_choices)



if choice_chosen == "rock":
  print (rock_art)
  if ai_choice == ai_choices[0]:
    print(f"{rock_art}\nTie , AI chose {ai_choice}")
  elif ai_choice == ai_choices[1]:
    print(f"{paper_art}\nLost , AI chose {ai_choice}")
  else: 
    print(f"{scissors_art}\nWon , AI chose {ai_choice}")
    
elif choice_chosen == "paper":
  print(paper_art)
  if ai_choice == ai_choices[0]:
    print(f"{rock_art}\nWon , AI chose {ai_choice}")
  elif ai_choice == ai_choices[1]:
    print(f"{paper_art}\nTie , AI chose {ai_choice}")
  else:
    print(f"{scissors_art}\nLost , AI chose {ai_choice}")

elif choice_chosen == "scissors":
  print(scissors_art)
  if ai_choice == ai_choices[0]:
    print(f"{rock_art}\nLost , AI chose {ai_choice}")
  elif ai_choice == ai_choices[1]:
    print(f"{paper_art}\nWon , AI chose {ai_choice}")
  else:
    print(f"{scissors_art}\nTie , AI chose {ai_choice}")
    

  

