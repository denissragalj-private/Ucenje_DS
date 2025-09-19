import random
import os

#postavljanje početnih vrijednosti za varijable
player_score = 0
computer_score = 0
tie_score = 0

def score_count():
  player_score = 0
  computer_score = 0
  tie_score = 0
  return player_score, computer_score, tie_score

def get_choices():
  # dodao strip() da bi se izbrisali prazni prostori i lower() da bi se sve pretvorilo u mala slova i imaknuli " " unutar riječi ili na krajevima
  player_choice = input("Enter a choice (rock, paper, scissors): ").strip().lower().replace(" ", "") 
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer): 
  global player_score, computer_score, tie_score
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    tie_score = tie_score + 1
    return "It's a tie!" 
  elif player == "rock":
    if computer == "scissors":
      player_score = player_score + 1
      return "Rock smashes scissors! You win!"
    else:
      # computer chose paper
      computer_score = computer_score + 1
      return "Paper covers rock! You lose. "
  elif player == "paper":
    if computer == "rock":
      player_score = player_score + 1
      return "Paper covers rock! You win!"
    else:
      # computer chose scissors
      computer_score = computer_score + 1
      return "Scissors cuts paper! You lose." 
  elif player == "scissors" :
    if computer == "paper":
      player_score = player_score + 1
      return "Scissors cuts paper! You win!"
    else:
      # computer chose rock
      computer_score = computer_score + 1
      return "Rock smashes scissors! You lose."

def isprazni_ekran():
  if os.name == 'nt':  # For Windows
    _ = os.system('cls')
  else:
    _ = os.system('clear') # For macOS and Linux

while True:
  isprazni_ekran()  # Clear screen
  print(f"Player Score: {player_score}, Computer Score: {computer_score}")
  print("Welcome to Rock, Paper, Scissors!")
  print("Enter 'quit' or 'exit' to exit\n")
  choices = get_choices()
  # dodao da se moze izaci iz igre
  if choices["player"] == "quit" or choices["player"] == "exit":
    print(f"\nYou chose {choices['player']}, Thanks for playing!")
    break
  else:  
    result = check_win(choices["player"], choices["computer"])
    print(result)
    input("\nPress Enter to continue...") 
  continue # vrača se na while

if computer_score == player_score:
  print(f"\nFinal score:\n  Tie:           {tie_score} \n  Computer win:  {computer_score} \n  You win:       {player_score} \n\n*** It 's tie! ***")
elif computer_score > player_score:
  print(f"\nFinal score:\n  Tie:           {tie_score} \n  Computer win:  {computer_score} \n  You win:       {player_score} \n\n  Computer win! \n\n*** You lose! :(  *** \n")
else:
  print(f"\nFinal score:\n  Tie:           {tie_score} \n  Computer win:  {computer_score} \n  You win:       {player_score} \n\n  You Win ! \n\n*** Congratelations! :)  *** \n")
input("\nPress Enter to continue...")  
  #ZAVRŠNO - DŠ.