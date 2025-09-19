import random
import os

# --- Klasa za boje i funkcije za poruke ostaju iste ---
class Collors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def info_msg(message):
    print(f"{Collors.OKCYAN}{message}{Collors.ENDC}")

def header_msg(message):
    print(f"{Collors.HEADER}{message}{Collors.ENDC}")

def header_blue(message):
    print(f"{Collors.OKBLUE}{message}{Collors.ENDC}")

def warning_msg(message):
    print(f"{Collors.WARNING}{message}{Collors.ENDC}")

def win_msg(message):
    print(f"{Collors.OKGREEN}{Collors.BOLD}{message}{Collors.ENDC}")

def lose_msg(message):
    print(f"{Collors.FAIL}{Collors.BOLD}{message}{Collors.ENDC}")

def isprazni_ekran():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# --- Glavna petlja programa koja omogućava ponovno igranje ---
while True:
    # Postavljanje/resetiranje vrijednosti na početku svake nove igre
    player_score = 0
    computer_score = 0
    tie_score = 0

    # Funkcije za dohvat odabira i provjeru pobjednika moraju biti definirane
    # ili dostupne unutar ovog opsega. Najbolje ih je definirati izvan petlje.

    def get_choices():
        header_msg("Enter a choice (rock, paper, scissors):")
        player_choice = input("\nYour choice: ").strip().lower().replace(" ", "")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices

    # Važno: Moramo proslijediti trenutne rezultate u funkciju
    # ili nastaviti koristiti globalne varijable kao što ste i radili.
    # Korištenje globalnih varijabli je u redu za ovaj jednostavan primjer.
    def check_win(player, computer):
        global player_score, computer_score, tie_score
        info_msg(f"\nYou chose {player}, computer chose {computer}\n")
        if player == computer:
            tie_score += 1
            return "It's a tie!"
        elif player == "rock":
            if computer == "scissors":
                player_score += 1
                return "Rock smashes scissors! You win!"
            else:
                computer_score += 1
                return "Paper covers rock! You lose. "
        elif player == "paper":
            if computer == "rock":
                player_score += 1
                return "Paper covers rock! You win!"
            else:
                computer_score += 1
                return "Scissors cuts paper! You lose."
        elif player == "scissors":
            if computer == "paper":
                player_score += 1
                return "Scissors cuts paper! You win!"
            else:
                computer_score += 1
                return "Rock smashes scissors! You lose."

    # --- Petlja za jednu partiju igre (više rundi) ---
    while True:
        isprazni_ekran()
        print(f"{Collors.OKCYAN}Player Score:{Collors.ENDC}{Collors.BOLD} {player_score} {Collors.ENDC} \n{Collors.OKCYAN}Computer Score:{Collors.ENDC}{Collors.BOLD} {computer_score} {Collors.ENDC}")
        info_msg("\nWelcome to Rock, Paper, Scissors!")
        warning_msg("Enter 'quit' or 'exit' to end the match\n")

        choices = get_choices()

        if choices["player"] in ["quit", "exit"]:
            warning_msg(f"\nYou chose to end the match. Thanks for playing!")
            break  # Izlazi iz petlje za partiju i ide na ispis rezultata

        valid_options = ["rock", "paper", "scissors"]
        if choices["player"] not in valid_options:
            lose_msg(f"'{choices['player']}' is an invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            info_msg("\nPress Enter to continue...")
            input()
            continue

        result_message = check_win(choices["player"], choices["computer"])

        if "win" in result_message:
            win_msg(result_message)
        elif "lose" in result_message:
            lose_msg(result_message)
        else:
            info_msg(result_message)

        info_msg("\nPress Enter to continue...")
        input()

    # --- Ispis rezultata nakon završetka partije ---
    info_msg(f"\n------ Final score ------")
    info_msg(f"|  Tie:               {Collors.BOLD}{Collors.WARNING}{tie_score:<3}{Collors.OKCYAN}|")
    info_msg(f"|  Computer wins:     {Collors.BOLD}{Collors.FAIL}{computer_score:<3}{Collors.OKCYAN}|")
    info_msg(f"|  Your wins:         {Collors.BOLD}{Collors.OKGREEN}{player_score:<3}{Collors.OKCYAN}|")
    info_msg(f"-------------------------")


    if computer_score == player_score:
        header_blue("\n* * * It's a tie!   * * *")
    elif computer_score > player_score:
        lose_msg("\n*** Computer wins! You lose! :( ***")
    else:
        win_msg("\n*** Congratulations! You Win! :) ***")

    # --- Pitanje za ponovnu igru ---
    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:                  
        # negacija u if , ova funkcija vodi na break ako odgovor nije: yes ili y 
        # u suprotnom se nastavlja petlja jel je ova funkcija neostvarena
        warning_msg("\nThanks for playing! Press Enter to exit...")
        input()
        break # Izlazi iz glavne (vanjske) petlje i završava program
    # Ako korisnik unese 'yes' ili 'y', vanjska petlja se automatski
    # nastavlja (continue) i započinje novu igru s resetiranim rezultatima.