import random # dodao da bi se mogao koristiti random.choice()  
import os # dodao da bi se mogao isprazniti ekran

#postavljanje početnih vrijednosti za globalne varijable
player_score = 0
computer_score = 0
tie_score = 0

# objašnjenje tuple-a: https://www.w3schools.com/python/python_tuples.asp
# objašnjenje rječnika: https://www.w3schools.com/python/python_dictionaries.asp
# objašnjenje funkcija: https://www.w3schools.com/python/python_functions.asp
# objašnjenje globalnih varijabli: https://www.w3schools.com/python/python_variables_global.asp
# objašnjenje os.name: https://www.geeksforgeeks.org/python-os-name-method/
# objašnjenje os.system(): https://www.geeksforgeeks.org/python-os-system-method/
# objašnjenje input(): https://www.w3schools.com/python/ref_func_input.asp
# objašnjenje print(): https://www.w3schools.com/python/ref_func_print.asp
# objašnjenje replace(): https://www.w3schools.com/python/ref_string_replace.asp
# objašnjenje strip(): https://www.w3schools.com/python/ref_string_strip.asp
# objašnjenje lower(): https://www.w3schools.com/python/ref_string_lower.asp
# objašnjenje continue: https://www.w3schools.com/python/ref_keyword_continue.asp
# objašnjenje break: https://www.w3schools.com/python/ref_keyword_break.asp
# objašnjenje if: https://www.w3schools.com/python/ref_keyword_if.asp
# objašnjenje elif: https://www.w3schools.com/python/ref_keyword_elif.asp
# objašnjenje else: https://www.w3schools.com/python/ref_keyword_else.asp
# objašnjenje while: https://www.w3schools.com/python/ref_keyword_while.asp
# objašnjenje for: https://www.w3schools.com/python/ref_keyword_for.asp
# objašnjenje return: https://www.w3schools.com/python/ref_keyword_return.asp
# objašnjenje global: https://www.w3schools.com/python/ref_keyword_global.asp
# objašnjenje def: https://www.w3schools.com/python/ref_keyword_def.asp
# objašnjenje import: https://www.w3schools.com/python/ref_keyword_import.asp
# objašnjenje from: https://www.w3schools.com/python/ref_keyword_from.asp
# objašnjenje as: https://www.w3schools.com/python/ref_keyword_as.asp
# objašnjenje pass: https://www.w3schools.com/python/ref_keyword_pass.asp
# objašnjenje assert: https://www.w3schools.com/python/ref_keyword_assert.asp
# objašnjenje del: https://www.w3schools.com/python/ref_keyword_del.asp
# objašnjenje with: https://www.w3schools.com/python/ref_keyword_with.asp
# objašnjenje yield: https://www.w3schools.com/python/ref_keyword_yield.asp
# objašnjenje lambda: https://www.w3schools.com/python/ref_keyword_lambda.asp
# objašnjenje nonlocal: https://www.w3schools.com/python/ref_keyword_nonlocal.asp
# objašnjenje try: https://www.w3schools.com/python/ref_keyword_try.asp
# objašnjenje except: https://www.w3schools.com/python/ref_keyword_except.asp
# objašnjenje finally: https://www.w3schools.com/python/ref_keyword_finally.asp
# objašnjenje raise: https://www.w3schools.com/python/ref_keyword_raise.asp  
# objašnjenje class: https://www.w3schools.com/python/ref_keyword_class.asp

# dodavanje boja pomoču escape kodova
# https://www.geeksforgeeks.org/print-colors-python-terminal/
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

# dodavanje boja u print() funkciju
# boje se dodaju u print() funkciju kao stringovi primjer: print(Colors.OKGREEN + "Green text" + Colors.ENDC) 
# Colors je klasa koja sadrži boje kao varijable
# Colors.ENDC je varijabla koja vraća boju u normalnu boju terminala
# Colors.OKGREEN je varijabla koja vraća boju u zelenu boju terminala
# Colors.OKBLUE je varijabla koja vraća boju u plavu boju terminala
# Colors.OKCYAN je varijabla koja vraća boju u cijan boju terminala
# Colors.WARNING je varijabla koja vraća boju u žutu boju terminala
# Colors.FAIL je varijabla koja vraća boju u crvenu boju terminala
# Colors.BOLD je varijabla koja vraća boju u bold boju terminala
# Colors.UNDERLINE je varijabla koja vraća boju u underline boju terminala
# Colors.HEADER je varijabla koja vraća boju u magenta boju terminala
# Colors.ENDC je varijabla koja vraća boju u normalnu boju terminala

# dodavanje boja u print("f\ {Colore.OKBLUE} ovo je primjer plave boje sa dodatnom varijablom")
# dodavanje boja u print("f\ {Colore.OKBLUE} ovo je primjer plave boje sa dodatnom varijablom" + Colors.ENDC)
# dodavanje boja u print("f\ {Colore.OKBLUE} ovo je primjer plave boje sa dodatnom varijablom" + Colors.ENDC + Colors.OKGREEN + "ovo je primjer zelene boje" + Colors.ENDC)

# dodao da bi se mogao koristiti boje u print() funkciji
class Collors:
  HEADER = '\033[95m' # dodao da bi se mogao koristiti magenta boja za header
  OKBLUE = '\033[94m' # dodao da bi se mogao koristiti plava boja za header
  OKCYAN = '\033[96m' # dodao da bi se mogao koristiti cijan boja za info poruke
  OKGREEN = '\033[92m' # dodao da bi se mogao koristiti zelena boja za pobjedu
  WARNING = '\033[93m'# dodao da bi se mogao koristiti žuta boja za upozorenja
  FAIL = '\033[91m' # dodao da bi se mogao koristiti crvena boja za poruku o porazu
  ENDC = '\033[0m' # dodao da bi se mogao koristiti normalna boja terminala
  BOLD = '\033[1m' #  dodao da bi se mogao koristiti bold boja
  UNDERLINE = '\033[4m' # dodao da bi se mogao koristiti underline boja
  


# Funkcije za stilizirane poruke
def info_msg(message):
    print(f"{Collors.OKCYAN}{message}{Collors.ENDC}") # Dodao cijan boju za info poruke

def header_msg(message):
    print(f"{Collors.HEADER}{message}{Collors.ENDC}")  # Dodao magenta boju za header

def header_blue(message):
    print(f"{Collors.OKBLUE}{message}{Collors.ENDC}") # Dodao plavu boju za header

def warning_msg(message):
    print(f"{Collors.WARNING}{message}{Collors.ENDC}") # Dodao žutu boju za upozorenja

def win_msg(message):
    print(f"{Collors.OKGREEN}{Collors.BOLD}{message}{Collors.ENDC}") # Dodao zeleno i BOLD za jači efekt pobjede

def lose_msg(message):
    print(f"{Collors.FAIL}{Collors.BOLD}{message}{Collors.ENDC}") # Dodao BOLD za jači efekt poraza

     
''' #trenutno se ne koristi , možda kod nekih novih opcija ili poboljšanja
def score_count():
  player_score = 0
  computer_score = 0
  tie_score = 0
  return player_score, computer_score, tie_score # vraća tuple s vrijednostima varijabli
'''

# Davanje odabira igraču
def get_choices():
  # dodao strip() da bi se izbrisali prazni prostori i lower() da bi se sve pretvorilo u mala slova i imaknuli " " unutar riječi
  # player_choice = input("Enter a choice (rock, paper, scissors): ").strip().lower().replace(" ", "") 
  header_msg("Enter a choice (rock, paper, scissors):")
  player_choice = input("\nYour choice: ").strip().lower().replace(" ", "")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices # vraća rječnik s izborima igrača i računala

# Funkcija za provjeru pobjednika
def check_win(player, computer): 
  global player_score, computer_score, tie_score # dodao global da bi se moglo mijenjati vrijednosti varijabli izvan funkcije
  #print(f"You chose {player}, computer chose {computer}")
  info_msg(f"\nYou chose {player}, computer chose {computer}\n")  
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
'''
while True:
  isprazni_ekran()  # Clear screen
  print(f"{Collors.OKCYAN}Player Score:{Collors.ENDC}{Collors.BOLD} {player_score} {Collors.ENDC} \n{Collors.OKCYAN}Computer Score:{Collors.ENDC}{Collors.BOLD} {computer_score} {Collors.ENDC}")
  # print(f"{Collors.OKGREEN}Welcome to Rock, Paper, Scissors!{Collors.ENDC}") 
  info_msg("\nWelcome to Rock, Paper, Scissors!")
  warning_msg("Enter 'quit' or 'exit' to exit\n")
  
  choices = get_choices()
  # dodao da se moze izaci iz igre
  if choices["player"] == "quit" or choices["player"] == "exit":
    warning_msg(f"\nYou chose {choices['player']}, Thanks for playing!")
    break
  else:  
    result = check_win(choices["player"], choices["computer"])
    print(result)
    info_msg("\nPress Enter to continue...")
    input()
  continue # vraca na pocetak petlje
''' # Staraverzija wail petlje

# nova verzija while petlje
while True:
  isprazni_ekran()
  print(f"{Collors.OKCYAN}Player Score:{Collors.ENDC}{Collors.BOLD} {player_score} {Collors.ENDC} \n{Collors.OKCYAN}Computer Score:{Collors.ENDC}{Collors.BOLD} {computer_score} {Collors.ENDC}")
  info_msg("\nWelcome to Rock, Paper, Scissors!")
  warning_msg("Enter 'quit' or 'exit' to exit\n")

  choices = get_choices()

  # 1. Provjeri želi li igrač izaći
  if choices["player"] == "quit" or choices["player"] == "exit":
    warning_msg(f"\nYou chose {choices['player']}, Thanks for playing!")
    break # Izlazi iz glavne petlje

  # 2. Provjeri je li unos igrača valjan (rock, paper, scissors)
  valid_options = ["rock", "paper", "scissors"] # Bolje je definirati listu ovdje ili globalno
  if choices["player"] not in valid_options:
      lose_msg(f"'{choices['player']}' is an invalid choice! Please choose 'rock', 'paper', or 'scissors' or 'exit' or 'quit'.")
      info_msg("\nPress Enter to continue...")
      input()
      continue # Vraća se na početak petlje za novi unos

  # 3. Ako je unos valjan, nastavi s logikom igre
  else:
    # Pozovi check_win() koja će vratiti string s rezultatom
    result_message = check_win(choices["player"], choices["computer"])

    # Sada, stiliziraj poruku na temelju njenog sadržaja
    if "win" in result_message:
        win_msg(result_message)
    elif "lose" in result_message:
        lose_msg(result_message)
    else: # Ako nije "win" niti "lose", mora biti "It's a tie!"
        info_msg(result_message)

    info_msg("\nPress Enter to continue...")
    input()
  # 'continue' je ovdje suvišan, petlja se automatski nastavlja
  # continue


''' # ispis rezultata i pobjednika bez boja
if computer_score == player_score:
  print(f"\nFinal score:\n  Tie:           {tie_score} \n  Computer win:  {computer_score} \n  You win:       {player_score} \n\n  *** It 's tie! ***")
elif computer_score > player_score:
  print(f"\nFinal score:\n  Tie:           {tie_score} \n  Computer win:  {computer_score} \n  You win:       {player_score} \n\n  Computer win! \n\n *** You lose! :(  *** \n")
else:
  print(f"\nFinal score:\n  Tie:           {tie_score} \n  Computer win:  {computer_score} \n  You win:       {player_score} \n\n  You Win ! \n\n *** Congratelations! :)  *** \n")
input("\nPress Enter to continue...")  
'''
# ispis rezultata i pobjednika sa bojama
info_msg(f"\n------ Final score ------")
info_msg(f"|  Tie:             {Collors.BOLD}{Collors.WARNING} {tie_score}  {Collors.OKCYAN}|")
info_msg(f"|  Computer wins:   {Collors.BOLD}{Collors.FAIL} {computer_score}  {Collors.OKCYAN}|")
info_msg(f"|  Your wins:       {Collors.BOLD}{Collors.OKGREEN} {player_score}  {Collors.OKCYAN}|")
info_msg(f"-------------------------")


if computer_score == player_score:
  header_blue("\n* * *    It's a tie!     * * *") # Neriješeno kao info
elif computer_score > player_score:
  lose_msg("\n*** Computer wins! You lose! :( ***") # Poraz kao crvena
else:
  win_msg("\n*** Congratulations! You Win! :) ***") # Pobjeda kao zelena

# input("\nPress Enter to exit...")
warning_msg("\nPress Enter to exit...")
input()