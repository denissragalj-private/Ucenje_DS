import os
import sys
import datetime
import time

# --- Postavke i konstante programa ---

# Naziv datoteke u koju će se spremiti tablica.
# Fiksna vrijednost koja se koristi kao zadana opcija.
file_name = 'mnozenje.txt'

# ANSI escape kodovi za boje i reset
# Konstante se koriste kako bi se kod učinio čitljivijim i lakšim za održavanje.
# Umjesto ponavljanja kodova, jednostavno se pozivaju nazivi varijabli (npr. YELLOW).
RESET = "\033[0m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BLUE = "\033[94m"
ORANGE = "\033[38;5;208m"

# --- Funkcije za interakciju s korisnikom i vizualni prikaz ---

def clear_terminal():
    """
    Čisti terminal ovisno o operativnom sustavu.
    Koristi 'cls' za Windows i 'clear' za ostale sustave (Linux, macOS).
    """
    if os.name == 'nt':  # Provjerava je li operativni sustav Windows
        os.system('cls')
    else:  # Svi ostali operativni sustavi
        os.system('clear')

def print_banner():
    """
    Ispisuje vizualni banner na početku programa.
    Koristi ANSI kodove za boje kako bi banner bio atraktivan.
    """
    clear_terminal()
    print(YELLOW + "################################################################" + RESET)
    print(YELLOW + "#" + " " * 62 + "#" + RESET)
    print(YELLOW + "#" + f"{'Dobrodošli u Dinamičku Tablicu Množenja!':^62}" + "#" + RESET)
    print(YELLOW + "#" + " " * 62 + "#" + RESET)
    print(YELLOW + "################################################################" + RESET)
    print()
    print(GREEN + "Ovaj program generira tablicu množenja po vašem izboru." + RESET)
    print()
    
def display_progress_bar(duration=2, message="Generiram tablicu: "):
    """
    Prikazuje jednostavnu traku napretka u terminalu.
    Simulira rad koji traje određeno vrijeme (duration).
    Koristi `sys.stdout.write` i `sys.stdout.flush` za dinamičko ažuriranje
    istog retka u terminalu, bez ispisivanja novog retka svaki put.
    """
    sys.stdout.write(message + "[")
    sys.stdout.flush()
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        progress = elapsed_time / duration
        if progress > 1:
            progress = 1
        
        bar_length = 20
        filled_length = int(bar_length * progress)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        
        sys.stdout.write(f"\r{message}[{bar}] {int(progress * 100)}%")
        sys.stdout.flush()
        
        if progress >= 1:
            break
        
        time.sleep(0.1) # Pauza od 0.1 sekunde za glatki prikaz
    print("\n")


# --- Funkcije za generiranje i ispis tablice ---

def generiraj_tablicu_tekst(table_size, output_stream=sys.stdout, use_colors=True):
    """
    Generira tekstualnu tablicu množenja zadane veličine i ispisuje je na zadani stream.
    Ključna funkcija koja stvara tablicu.
    
    Argumenti:
        table_size:    Cijeli broj koji definira do kojeg broja ide tablica (npr. 10 za 10x10).
        output_stream: Objekt datoteke (npr. sys.stdout za terminal ili otvorena datoteka)
                       gdje će se ispisati tablica.
        use_colors:    Boolean. Ako je True, ispisuje se s ANSI bojama.
    
    Kako radi:
    1. Privremeno preusmjerava `sys.stdout` na `output_stream` kako bi sve `print`
       naredbe išle na željeno mjesto (terminal ili datoteku).
    2. Dinamički izračunava širinu svake ćelije kako bi se tablica pravilno poravnala,
       bez obzira na veličinu unosa (npr. 10x10 ili 100x100).
    3. Koristi ugniježđene petlje (for petlja unutar for petlje) za iteraciju kroz
       retke i stupce tablice.
    4. Ispisuje zaglavlje, vodoravne linije i glavni sadržaj tablice koristeći f-stringove
       za formatiranje i poravnanje teksta.
    5. Vraća `sys.stdout` na prvobitno stanje nakon završetka kako ne bi utjecao
       na ostatak programa.
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

    # Dinamički izračunava širinu ćelije na temelju najvećeg broja u tablici.
    # Dodaje se +2 za padding (jedan razmak s lijeve i desne strane) radi boljeg poravnanja.
    cell_content_width = len(str(table_size * table_size))
    header_content_width = len(str(table_size))
    
    header_col_width = header_content_width + 2
    cell_col_width = cell_content_width + 2

    # Pomoćna funkcija za ispis vodoravne linije okvira
    def print_horizontal_line():
        print(_YELLOW + "|" + "-" * header_col_width + _BLUE + "|", end="")
        for _ in range(table_size):
            print(_YELLOW + "-" * cell_col_width + "|", end="")
        print(_RESET)
    
    # Ispis gornjeg okvira
    print_horizontal_line()

    # Ispis zaglavlja stupaca (brojevi od 1 do table_size)
    print(_YELLOW + "|" + _RED + f"{'x': ^{header_col_width}}" + _BLUE + "|", end="")
    for n_head in range(1, table_size + 1):
        print(_CYAN + f"{n_head: ^{cell_col_width}}" + _YELLOW + "|", end="")
    print(_RESET)

    # Ispis linije ispod zaglavlja
    print(_YELLOW + "|" + _ORANGE + "=" * header_col_width + _BLUE + "|", end="")
    for _ in range(table_size):
        print(_ORANGE + "=" * cell_col_width + _YELLOW + "|", end="")
    print(_RESET)

    # Ispis glavnog dijela tablice (rezultati množenja)
    for i in range(1, table_size + 1):
        if i > 1:
            print_horizontal_line()

        # Ispis zaglavlja reda
        print(_YELLOW + "|" + _GREEN + f"{i: ^{header_col_width}}" + _BLUE + "|", end="")

        # Ispis rezultata u redu
        for n in range(1, table_size + 1):
            rezultat = i * n
            print(_MAGENTA + f"{rezultat: ^{cell_col_width}}" + _YELLOW + "|", end="")
        print(_RESET)

    # Ispis donjeg okvira
    print_horizontal_line()

    sys.stdout = original_stdout # Vrati stdout na originalno stanje

# --- Funkcije za izvješćivanje i glavni programski tok ---

def generate_summary_text(table_size, saved, file_name=None, use_colors=True):
    """
    Generira i vraća tekst završnog izvješća kao string.
    Ova funkcija je "čista" jer ne ispisuje ništa, već samo vraća string.
    
    Argumenti:
        table_size: Cijeli broj.
        saved:      Boolean.
        file_name:  String.
        use_colors: Boolean. Ako je True, koristi ANSI boje.
    """
    _RESET = RESET if use_colors else ""
    _YELLOW = YELLOW if use_colors else ""
    _BLUE = BLUE if use_colors else ""
    _RED = RED if use_colors else ""

    summary_text = f"\n{_BLUE}################################################################{_RESET}\n"
    summary_text += f"{_BLUE}#{' ':62}#{_RESET}\n"
    summary_text += f"{_BLUE}#{'ZAVRŠNO IZVJEŠĆE':^62}#{_RESET}\n"
    summary_text += f"{_BLUE}#{' ':62}#{_RESET}\n"
    summary_text += f"{_BLUE}################################################################{_RESET}\n"
    summary_text += f"\n{_BLUE}Tablica množenja generirana je za {_YELLOW}{table_size}x{table_size}{_BLUE} veličinu.{_RESET}\n"
    if saved:
        summary_text += f"{_BLUE}Datoteka je uspješno spremljena.{_RESET}\n"
        summary_text += f"{_BLUE}Naziv datoteke: {_YELLOW}{file_name}{_RESET}\n"
    else:
        summary_text += f"{_RED}Datoteka nije spremljena na disk.{_RESET}\n"
    summary_text += f"\n{_BLUE}Hvala vam na korištenju programa!{_RESET}\n\n"
    return summary_text


def print_summary(table_size, saved, file_name=None):
    """
    Ispisuje završno izvješće na konzolu pozivom funkcije `generate_summary_text`.
    """
    print(generate_summary_text(table_size, saved, file_name, use_colors=True))


def main():
    """
    Glavna funkcija programa. Sadrži glavni tok izvršavanja:
    1. Ispisuje banner.
    2. U petlji traži unos od korisnika za veličinu tablice i obrađuje pogreške.
    3. Prikazuje traku napretka generiranja.
    4. Generira i ispisuje tablicu u terminal.
    5. Pita korisnika želi li spremiti datoteku.
    6. Ako korisnik želi spremiti, pita za detalje (naziv, boje) i pokreće proces
       zapisivanja, s trakom napretka.
    7. Zapisuje tablicu i završno izvješće u datoteku, koristeći 'try...except' blok
       za sigurno rukovanje greškama.
    8. Ispisuje završno izvješće na konzolu.
    """
    print_banner()

    # Petlja za unos veličine tablice
    while True:
        try:
            table_size = int(input(GREEN + "Unesite željenu veličinu tablice (npr. '10' za 10x10): " + RESET))
            if table_size <= 0:
                print(RED + "Veličina mora biti pozitivan broj. Molim unesite ponovo." + RESET)
            else:
                break
        except ValueError:
            print(RED + "Neispravan unos. Molim unesite cijeli broj." + RESET)

    print()
    display_progress_bar(duration=2)
    generiraj_tablicu_tekst(table_size, sys.stdout, use_colors=True)

    print("\n---")
    
    # Petlja za provjeru unosa korisnika (želi li spremiti datoteku)
    while True:
        user_save_choice = input(GREEN + "Želite li spremiti tablicu u datoteku? Unesite 'da' ili 'ne': " + RESET)
        if user_save_choice.lower().startswith('d') or user_save_choice.lower().startswith('y'):
            should_save = True
            break
        elif user_save_choice.lower().startswith('n'):
            should_save = False
            break
        else:
            print(RED + "Neispravan unos. Molim unesite 'da' ili 'ne'." + RESET)
    
    actual_file_name = None
    if should_save:
        # Pitajte korisnika za naziv datoteke
        user_file_name = input(GREEN + f"Unesite naziv datoteke (ostavite prazno za '{file_name}'): " + RESET)
        if user_file_name:
            if not user_file_name.lower().endswith('.txt'):
                user_file_name += '.txt'
            actual_file_name = user_file_name
        else:
            actual_file_name = file_name
        
        # Petlja za provjeru unosa korisnika (boje)
        while True:
            prompt_color_message = (
                f"{GREEN}Želite li spremiti tablicu sa **ANSI kodovima za boju** u datoteku '{actual_file_name}'?\n"
                f"{YELLOW}Ako odaberete **'da'**, tablica će biti obojana kada je otvorite u terminalu.\n"
                f"{RESET}Ako odaberete **'ne'**, tablica će biti zapisana kao običan, crno-bijeli tekst.\n"
                f"{GREEN}Unesite **da** ili **ne**: "
            )
            user_input = input(prompt_color_message + RESET)
            if user_input.lower().startswith('d') or user_input.lower().startswith('y'):
                use_colors_in_file = True
                break
            elif user_input.lower().startswith('n'):
                use_colors_in_file = False
                break
            else:
                print(RED + "Neispravan unos. Molim unesite 'da' ili 'ne'." + RESET)
        
        print()
        display_progress_bar(duration=3, message=f"Zapisujem tablicu u datoteku '{actual_file_name}': ")

        try:
            # Stvorite datoteku i zapišite u nju s UTF-8 kodiranjem
            with open(actual_file_name, 'w', encoding='utf-8') as f:
                # Dohvatite trenutni datum i vrijeme za zapis u datoteku
                current_time = datetime.datetime.now()
                formatted_time = current_time.strftime("%d.%m.%Y. %H:%M")
                
                # Zapišite datum i vrijeme na početak datoteke
                f.write(f"Datum zapisivanja: {formatted_time}\n")
                f.write(f"Tablica množenja {table_size}x{table_size}\n\n")
                
                # Zatim zapišite tablicu množenja s bojama ili bez, ovisno o korisnikovom izboru
                generiraj_tablicu_tekst(table_size, f, use_colors=use_colors_in_file)
                # Zapišite završno izvješće u datoteku
                f.write(generate_summary_text(table_size, should_save, actual_file_name, use_colors=use_colors_in_file))
            
            # Ispis putanje datoteke da je lakše pronađete
            absolute_path = os.path.abspath(actual_file_name)
            print(GREEN + f"Tablica množenja uspješno je zapisana u datoteku." + RESET)
            print(f"Puna putanja datoteke: {YELLOW}{absolute_path}{RESET}")
            print(f"Veličina datoteke: {YELLOW}{os.path.getsize(actual_file_name)}{RESET} bajtova.")

        except IOError as e:
            print(RED + f"Greška pri pisanju u datoteku: {e}" + RESET)

    print_summary(table_size, should_save, actual_file_name)


# --- Glavni dio programa (MAIN) ---
# Ovo osigurava da se kod unutar 'main' funkcije pokreće samo
# kada se skripta izvršava izravno, a ne kada je uvezena kao modul.
if __name__ == "__main__":
    main()
