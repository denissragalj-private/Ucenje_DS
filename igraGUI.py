import random
import time # Dodajemo time modul za simulaciju "razmišljanja"

# --- ANSI Escape Kodovi za Boje i Stilove ---
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Boje teksta (Foreground colors)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m" # Svijetloplava
LIGHT_GRAY = "\033[37m" # Standardna siva
GOLD = "\033[33m" # Približno zlatna, često izgleda kao žuta

# --- Globalne varijable za bodove ---
player_score = 0
computer_score = 0
draw_count = 0

# --- Pomoćne funkcije za ispis u terminal ---
def print_styled(message, color=RESET, style=None):
    """
    Ispisuje poruku u terminal s navedenom bojom i stilom.
    """
    styled_message = ""
    if style:
        # Može prihvatiti listu stilova ili pojedinačni stil
        if isinstance(style, list):
            for s in style:
                styled_message += s
        else:
            styled_message += style
    
    styled_message += color + message + RESET
    print(styled_message)

def clear_terminal():
    """Čisti terminalski ekran."""
    # Za Windows:
    # import os
    # os.system('cls')
    # Za Unix/Linux/macOS:
    # os.system('clear')
    # Jednostavnija varijanta koja radi svugdje, ali samo ispiše puno praznih redova
    print("\n" * 50) 


# --- Logika igre ---
def get_computer_choice():
    """Generira nasumični odabir računala."""
    return random.choice(['papir', 'škare', 'kamen'])

def determine_winner(player_choice, computer_choice):
    """Određuje pobjednika na temelju odabira igrača i računala."""
    if player_choice == computer_choice:
        return "Neriješeno!"
    elif (player_choice == 'papir' and computer_choice == 'kamen') or \
         (player_choice == 'škare' and computer_choice == 'papir') or \
         (player_choice == 'kamen' and computer_choice == 'škare'):
        return "Pobijedio si! 🎉"
    else:
        return "Računalo je pobjedilo! 💻"

# --- Glavna logika igre ---
def play_round():
    """Pokreće jednu rundu igre Kamen, Papir, Škare."""
    global player_score, computer_score, draw_count

    print_styled("\nOdaberi svoj potez:", GOLD, BOLD)
    print_styled("1. Kamen", LIGHT_GRAY)
    print_styled("2. Papir", LIGHT_GRAY)
    print_styled("3. Škare", LIGHT_GRAY)
    print_styled("4. Prikaži rezultat", LIGHT_GRAY)
    print_styled("5. Nova igra", LIGHT_GRAY)
    print_styled("6. Kraj igre", LIGHT_GRAY)

    player_choice = ""
    while True:
        choice_input = input(f"{YELLOW}Unesi broj svog odabira: {RESET}").strip()
        
        if choice_input == '1':
            player_choice = 'kamen'
            break
        elif choice_input == '2':
            player_choice = 'papir'
            break
        elif choice_input == '3':
            player_choice = 'škare'
            break
        elif choice_input == '4':
            display_score()
            print("\n") # Dodaj novi red za bolji razmak
            return # Vrati se na glavni loop za novi odabir
        elif choice_input == '5':
            new_game()
            return # Vrati se na glavni loop za novi odabir
        elif choice_input == '6':
            end_game()
            return # Vrati se na glavni loop za novi odabir
        else:
            print_styled("Nevažeći odabir. Molim te unesi broj od 1 do 6.", RED)

    print_styled(f"\nTvoj izbor:      {player_choice.capitalize()}", LIGHT_GRAY)

    # Simulacija "razmišljanja" računala
    for i in range(4):
        print(f"Računalo razmišlja{'.' * (i % 4)}{' ' * (3 - (i % 4))}", end='\r') # \r vraća kursor na početak reda
        time.sleep(0.5) # Pričekaj 0.5 sekundi
    print(" " * 30, end='\r') # Očisti liniju nakon animacije

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    print_styled(f"Izbor računala: {computer_choice.capitalize()}", LIGHT_GRAY)
    print_styled("-" * 40, LIGHT_GRAY)

    if "Pobijedio si" in result:
        player_score += 1
        print_styled(f"Ishod:      {result}", GREEN, BOLD)
    elif "Računalo je" in result:
        computer_score += 1
        print_styled(f"Ishod:      {result}", RED, BOLD)
    else:
        draw_count += 1
        print_styled(f"Ishod:      {result}", CYAN, BOLD)
    
    print_styled("-" * 40, LIGHT_GRAY)


def display_score():
    """Prikazuje trenutni rezultat."""
    print_styled("\n--- TRENUTNI REZULTAT ---", GOLD, BOLD)
    print_styled(f"Igrač: {player_score}", GREEN)
    print_styled(f"Računalo: {computer_score}", RED)
    print_styled(f"Neriješeno: {draw_count}", CYAN)
    print_styled("-------------------------", GOLD)

def new_game():
    """Resetira bodove i započinje novu igru."""
    global player_score, computer_score, draw_count
    player_score = 0
    computer_score = 0
    draw_count = 0
    clear_terminal()
    print_styled("****************************************", GOLD, BOLD)
    print_styled("  Započeta je nova igra! Sretno!      ", GOLD, BOLD)
    print_styled("****************************************", GOLD, BOLD)
    print_styled("  Odaberi svoj potez unosom broja.\n", LIGHT_GRAY)

def end_game():
    """Završava igru i prikazuje konačne rezultate."""
    clear_terminal()
    print_styled("\n" + "=" * 40, GOLD, BOLD)
    print_styled("           Konačni rezultat:        ", GOLD, BOLD)
    print_styled("-" * 40, GOLD, BOLD)
    print_styled(f"  Igrač {player_score} - Računalo {computer_score} - Neriješeno {draw_count}", GOLD, BOLD)
    print_styled("*" * 40, GOLD, BOLD)

    winner_message_text = ""
    message_color = RESET

    if player_score > computer_score:
        winner_message_text = "Čestitam! Pobjedili ste! :)"
        message_color = GREEN
    elif computer_score > player_score:
        winner_message_text = "Izgubili ste ! :("
        message_color = RED
    else: # Neriješeno
        winner_message_text = "Neriješeno je !    :| "
        message_color = CYAN
    
    # Ispis poruke sa žutim zvjezdicama i obojenim tekstom
    total_stars_line_length = 40
    stars_on_side = 3
    padding_length = total_stars_line_length - (2 * stars_on_side) - len(winner_message_text)
    left_padding = " " * (padding_length // 2)
    right_padding = " " * (padding_length - (padding_length // 2))

    print_styled(GOLD + BOLD + "*" * total_stars_line_length + RESET)
    print(f"{GOLD}{BOLD}{'*' * stars_on_side}{RESET}{left_padding}{message_color}{BOLD}{winner_message_text}{RESET}{right_padding}{GOLD}{BOLD}{'*' * stars_on_side}{RESET}")
    print_styled(GOLD + BOLD + "*" * total_stars_line_length + RESET)

    print_styled(f"*" * 40, GOLD, BOLD)
    print_styled(f"            KRAJ IGRE!              ", GOLD, BOLD)
    print_styled(f"*" * 40, GOLD, BOLD)
    print_styled(f"        Klikni 'Izlaz' za Kraj ili ", LIGHT_GRAY)
    print_styled(f"      'Nova Igra' za ponovni početak. ", LIGHT_GRAY)
    print_styled(f"=" * 40 + "\n", GOLD, BOLD)

# --- Uvodna poruka ---
def display_intro_message():
    intro_message = f"""
{GOLD}{BOLD}============== * * * * * =============== {RESET}
{GOLD}{BOLD}          Dobrodošli u igru{RESET}
{GOLD}{BOLD}                * * * Kamen, papir, škare!          {RESET}
{GOLD}{BOLD}============== * * * * * =============== {RESET}
{LIGHT_GRAY}Ovo je jednostavna igra u kojoj se možeš  {RESET}
{LIGHT_GRAY}igrati protiv računala.                  {RESET}
{LIGHT_GRAY}----------------------------------------  {RESET}
{LIGHT_GRAY}Bit će zatraženo da uneseš svoj odabir    {RESET}
{LIGHT_GRAY}kamen, papir ili škare za igru. Ili za    {RESET}
{LIGHT_GRAY}izlaz (unosom broja).             {RESET}
{LIGHT_GRAY}----------------------------------------  {RESET}
{LIGHT_GRAY}Računalo će odabrati jednu od tri opcije{RESET}
{LIGHT_GRAY}----------------------------------------  {RESET}
{LIGHT_GRAY}Pobjednik se određuje na temelju pravila{RESET}
{LIGHT_GRAY}----------------------------------------  {RESET}
{LIGHT_GRAY}Možeš igrati dok ne odlučiš izaći.        {RESET}
{GOLD}{BOLD}============== * * * * * ===============  {RESET}
{GOLD}{BOLD}              Pravila:                   {RESET}
{GOLD}{BOLD}============== * * * * * ===============  {RESET}
{LIGHT_GRAY} 1.) Kamen udara škare,{RESET}
{LIGHT_GRAY} 2.) Škare režu papir,{RESET}
{LIGHT_GRAY} 3.) Papir pokriva kamen.{RESET}
{LIGHT_GRAY}----------------------------------------  {RESET}
{LIGHT_GRAY} 4.) Ako oba igrača odaberu istu opciju,  {RESET}
{LIGHT_GRAY}     izjednačeno je.
{GOLD}{BOLD}============== * * * * * ===============  {RESET}
{GOLD}{BOLD}              S r e t n o !              {RESET}
{GOLD}{BOLD}============== * * * * * ===============  {RESET}
"""
    print(intro_message)
    time.sleep(5) # Pričekaj 5 sekundi
    clear_terminal()

# --- Glavni loop igre ---
def main_game_loop():
    display_intro_message()
    new_game() # Započni novu igru nakon uvoda

    while True:
        play_round()
        # Ako je end_game() pozvan unutar play_round(), loop će se prekinuti.
        # Provjeravamo stanje globalne varijable (ako je npr. dodana 'game_active' = False)
        # ili jednostavno dopuštamo da se funkcija 'end_game' brine o izlazu.
        # Trenutno, 'end_game' samo ispisuje poruku i ne izlazi iz aplikacije,
        # pa korisnik mora ručno izaći nakon što vidi poruku.
        # Možemo dodati 'exit()' u end_game() ako želimo automatski izlaz.
        
        # Pitanje korisniku želi li nastaviti ili izići nakon svake runde
        if not ask_to_continue():
            break

def ask_to_continue():
    """Pita korisnika želi li nastaviti igru."""
    while True:
        print_styled("\nŽeliš li nastaviti igru?", GOLD)
        print_styled("1. Da (Nova runda)", LIGHT_GRAY)
        print_styled("2. Prikaži rezultat", LIGHT_GRAY)
        print_styled("3. Nova igra", LIGHT_GRAY)
        print_styled("4. Kraj igre", LIGHT_GRAY)
        
        choice = input(f"{YELLOW}Unesi broj svog odabira: {RESET}").strip()
        
        if choice == '1':
            clear_terminal()
            return True
        elif choice == '2':
            display_score()
            # Ne čistimo terminal ovdje, da korisnik može vidjeti rezultat
            # i odmah izabrati sljedeću akciju
            continue # Ostani u petlji dok korisnik ne odabere 'Da' ili 'Kraj igre'
        elif choice == '3':
            new_game()
            return True # Vrati se na glavni loop za novi odabir (počinje nova runda)
        elif choice == '4':
            end_game()
            return False # Prekini glavni loop
        else:
            print_styled("Nevažeći odabir. Molim te unesi broj od 1 do 4.", RED)

# --- Pokretanje igre ---
if __name__ == "__main__":
    main_game_loop()
    print_styled("\nHvala što ste igrali!", GOLD, BOLD)