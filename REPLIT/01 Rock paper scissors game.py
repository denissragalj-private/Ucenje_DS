import random
import os

def get_choices():
  # dodao strip() da bi se izbrisali prazni prostori i lower() da bi se sve pretvorilo u mala slova i imaknuli " " unutar rijeći
  player_choice = input("Enter a choice (rock, paper, scissors): ").strip().lower().replace(" ", "") 
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer): 
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!" 
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      # computer chose paper
      return "Paper covers rock! You lose. "
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      # computer chose scissors
      return "Scissors cuts paper! You lose." 
  elif player == "scissors" :
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      # computer chose rock
      return "Rock smashes scissors! You lose."

def isprazni_ekran():
  if os.name == 'nt':  # For Windows
    _ = os.system('cls')
  else:
    _ = os.system('clear') # For macOS and Linux

while True:
  isprazni_ekran()  # Clear screen
  print("Welcome to Rock, Paper, Scissors!")
  print("Enter 'quit' or 'exit' to exit\n")
  choices = get_choices()

  if choices["player"] == "quit" or choices["player"] == "exit":
    print(f"\nYou chose {choices['player']}, Thanks for playing!\n")
    break
  else:  
    result = check_win(choices["player"], choices["computer"])
    print(result)
    input("\nPress Enter to continue...")  # Pause before clearing screen
#stao na 47 minuti videa.