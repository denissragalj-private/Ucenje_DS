import os
import sys
import datetime

# Naziv datoteke za zapis tablice
file_name = 'mnozenje.txt'

# Poruka za korisnika pri zapisivanju u datoteku
PROMPT_MESSAGE = (
    f"Želite li spremiti tablicu sa **ANSI kodovima za boju** u datoteku '{file_name}'?\n"
    f"Ako odaberete **'da'**, tablica će biti obojana kada je otvorite u terminalu.\n"
    f"Ako odaberete **'ne'**, tablica će biti zapisana kao običan, crno-bijeli tekst.\n"
    f"Unesite **da** ili **ne**: "
)

# ANSI escape kodovi za boje i reset
RESET = "\033[0m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BLUE = "\033[94m"
ORANGE = "\033[38;5;208m"

# Funkcija za čišćenje terminala
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generiraj_tablicu_tekst(output_stream=sys.stdout, use_colors=True):
    """
    Generira tekstualnu tablicu množenja i ispisuje je na zadani stream.
    
    Argumenti:
        output_stream: Objekt datoteke (npr. sys.stdout ili otvorena datoteka)
                       gdje će se ispisati tablica.
        use_colors:    Boolean. Ako je True, ispisuje se s ANSI bojama.
                       Ako je False, ispisuje se bez boja.
    """
    original_stdout = sys.stdout
    sys.stdout = output_stream

    # Postavi boje na prazan string ako ne koristimo boje
    _RESET = RESET if use_colors else ""
    _YELLOW = YELLOW if use_colors else ""
    _CYAN = CYAN if use_colors else ""
    _GREEN = GREEN if use_colors else ""
    _MAGENTA = MAGENTA if use_colors else ""
    _RED = RED if use_colors else ""
    _BLUE = BLUE if use_colors else ""
    _ORANGE = ORANGE if use_colors else ""

    # Gornji okvir
    print(_YELLOW + "|***" + _BLUE + "|"+_YELLOW, end="")
    for _ in range(10):
        print("****|", end="")
    print(_RESET)

    # Zaglavlje stupaca
    print(_YELLOW +"|" + _RED + " x " + _BLUE + "|" + _RESET, end="")
    for n_head in range(1, 11):
        print(_CYAN + f"{n_head:4d}" + _YELLOW + "|" + _RESET, end="")
    print()

    # Linija ispod zaglavlja
    print(_YELLOW +"|" +_ORANGE + "==="+ _BLUE +"|" + _ORANGE, end="")
    for _ in range(10):
        print(_ORANGE + "===="+ _YELLOW + "|", end="")
    print(_RESET)

    # Glavni dio tablice
    for i in range(1, 11):
        if i == 1:
            pass
        else:
            print(_YELLOW + "|---"+ _BLUE +"|"+_YELLOW + "----|" * 10 + _RESET)

        print(_YELLOW+"|"+_GREEN + f"{i:3d}" + _BLUE + "|" + _RESET, end="")

        for n in range(1, 11):
            rezultat = i * n
            print(_MAGENTA + f"{rezultat:4d}" + _YELLOW + "|" + _RESET, end="")
        print()

    # Donji okvir
    print(_YELLOW + "****" + _BLUE + "*"+_YELLOW, end="")
    for _ in range(10):
        print("*****", end="")
    print(_RESET)

    sys.stdout = original_stdout # Vrati stdout na originalno stanje

def main():
    """Glavna funkcija koja pokreće program."""
    clear_terminal()

    print(GREEN + "Generiram tablicu na ekranu (s bojama)..." + RESET)
    generiraj_tablicu_tekst(sys.stdout, use_colors=True)

    print("\n---")

    # Petlja za provjeru unosa korisnika
    while True:
        user_input = input(GREEN + PROMPT_MESSAGE + RESET)
        if user_input.lower().startswith('d') or user_input.lower().startswith('y'):
            use_colors_in_file = True
            break
        elif user_input.lower().startswith('n'):
            use_colors_in_file = False
            break
        else:
            print(RED + "Neispravan unos. Molim unesite 'da' ili 'ne'." + RESET)
    
    print(GREEN + f"Zapisujem tablicu u datoteku '{file_name}'..." + RESET)
    try:
        # Stvorite datoteku i zapišite u nju s UTF-8 kodiranjem
        with open(file_name, 'w', encoding='utf-8') as f:
            # Dohvatite trenutni datum i vrijeme za zapis u datoteku
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d.%m.%Y. %H:%M")
            
            # Zapišite datum i vrijeme na početak datoteke
            f.write(f"Datum zapisivanja: {formatted_time}\n\n")
            
            # Zatim zapišite tablicu množenja s bojama ili bez, ovisno o korisnikovom izboru
            generiraj_tablicu_tekst(f, use_colors=use_colors_in_file)
        
        # Ispis putanje datoteke da je lakše pronađete
        absolute_path = os.path.abspath(file_name)
        print(GREEN + f"Tablica množenja uspješno je zapisana u datoteku." + RESET)
        print(f"Puna putanja datoteke: {YELLOW}{absolute_path}{RESET}")
        print(f"Veličina datoteke: {YELLOW}{os.path.getsize(file_name)}{RESET} bajtova.")

    except IOError as e:
        print(RED + f"Greška pri pisanju u datoteku: {e}" + RESET)

# --- Glavni dio programa (MAIN) ---
if __name__ == "__main__":
    main()
