import random  # Uvozimo modul za generiranje slučajnih brojeva
import os      # Uvozimo modul za operacije s operacijskim sustavom

def get_choices():
    """Funkcija za dobivanje izbora igrača i računala"""
    # Tražimo od igrača da unese svoj izbor
    # strip() - uklanja razmake na početku i kraju
    # lower() - pretvara sve u mala slova  
    # replace(" ", "") - uklanja sve razmake unutar teksta
    player_choice = input("Enter a choice (rock, paper, scissors): ").strip().lower().replace(" ", "") 

    # Lista svih mogućih opcija za igru
    options = ["rock", "paper", "scissors"]

    # Računalo nasumično bira jednu opciju iz liste
    computer_choice = random.choice(options)

    # Stvaramo rječnik s oba izbora za lakše vraćanje podataka
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer): 
    """Funkcija koja provjerava tko je pobijedio i vraća poruku i pobjednika"""
    # Ispisujemo što je svaki igrač odabrao
    print(f"You chose {player}, computer chose {computer}")

    # Provjera za neriješeno (oba igrača odabrali isto)
    if player == computer:
        return "It's a tie!", "tie"

    # Logika za kamen (rock)
    elif player == "rock":
        if computer == "scissors":
            # Kamen razbija škare - igrač pobjeđuje
            return "Rock smashes scissors! You win!", "player"
        else:
            # Računalo je odabralo papir - papir pokriva kamen
            return "Paper covers rock! You lose.", "computer"

    # Logika za papir (paper)
    elif player == "paper":
        if computer == "rock":
            # Papir pokriva kamen - igrač pobjeđuje
            return "Paper covers rock! You win!", "player"
        else:
            # Računalo je odabralo škare - škare režu papir
            return "Scissors cuts paper! You lose.", "computer"

    # Logika za škare (scissors)
    elif player == "scissors":
        if computer == "paper":
            # Škare režu papir - igrač pobjeđuje
            return "Scissors cuts paper! You win!", "player"
        else:
            # Računalo je odabralo kamen - kamen razbija škare
            return "Rock smashes scissors! You lose.", "computer"

def isprazni_ekran():
    """Funkcija za čišćenje ekrana ovisno o operacijskom sustavu"""
    if os.name == 'nt':  # Provjera je li Windows
        _ = os.system('cls')    # Windows naredba za čišćenje ekrana
    else:
        _ = os.system('clear')  # Linux/macOS naredba za čišćenje ekrana

# GLAVNI DIO PROGRAMA
# Inicijalizacija brojača rezultata na početku programa
player_score = 0     # Brojač pobjeda igrača
computer_score = 0   # Brojač pobjeda računala

# Glavna petlja igre - izvršava se dok korisnik ne izađe
while True:
    isprazni_ekran()  # Očisti ekran prije svakog kruga

    # Prikaži trenutni rezultat
    print(f"Player Score: {player_score}, Computer Score: {computer_score}")
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'quit' or 'exit' to exit\n")

    # Dobij izbore igrača i računala
    choices = get_choices()

    # Provjeri želi li igrač izaći iz igre
    if choices["player"] == "quit" or choices["player"] == "exit":
        print(f"\nYou chose {choices['player']}, Thanks for playing!")
        print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
        break  # Izađi iz petlje i završi program

    # Provjeri je li unos valjan
    elif choices["player"] not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        input("\nPress Enter to continue...")  # Čekaj da korisnik pritisne Enter
        continue  # Vrati se na početak petlje

    # Ako je unos valjan, igraj rundu
    else:  
        # Provjeri tko je pobijedio i dobij poruku s rezultatom
        result, winner = check_win(choices["player"], choices["computer"])
        print(result)  # Ispiši rezultat runde

        # Ažuriraj brojače ovisno o tome tko je pobijedio
        if winner == "player":
            player_score += 1      # Povećaj rezultat igrača za 1
        elif winner == "computer":
            computer_score += 1    # Povećaj rezultat računala za 1
        # Ako je neriješeno (winner == "tie"), ne mijenjamo brojače

        # Čekaj da korisnik pritisne Enter prije sljedeće runde
        input("\nPress Enter to continue...")
