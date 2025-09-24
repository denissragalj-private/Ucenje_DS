import random               # za generiranje nasumičnog odabira računala
import os                   # za čišćenje ekrana
import time                 # za pauze i animacije

# --- Klasa za boje i funkcije za poruke ostaju iste ---
class Boja:
    ROZA = '\033[95m'       # za naslove i važne poruke (ROZA) - magenta
    PLAVA = '\033[94m'      # za obične poruke (OKBLUE) - plava
    CIAN = '\033[96m'       # za informativne poruke (OKCYAN) - cijan
    ZELENA = '\033[92m'     # za uspješne poruke (OKGREEN) - zelena
    ZUTA = '\033[93m'       # za upozorenja (ZUTA) - žuta
    CRVENA = '\033[91m'     # za upozorenja (WARNING) - žuta
    KRAJ = '\033[0m'        # za greške i poruke o gubitku (FAIL) - crvena
    BOLD = '\033[1m'        # za vraćanje na normalnu boju
    UNDERLINE = '\033[4m'   # za podcrtani tekst

def obavijest_poruka(poruka):
    print(f"{Boja.CIAN}{poruka}{Boja.KRAJ}")

def zaglavlje_poruka(poruka):
    print(f"{Boja.ROZA}{poruka}{Boja.KRAJ}")

def zaglavlje_plava(poruka):
    print(f"{Boja.PLAVA}{poruka}{Boja.KRAJ}")

def zaglavlje_plava_bold(poruka):
    print(f"{Boja.PLAVA}{Boja.BOLD}{poruka}{Boja.KRAJ}")

def upozorenje_poruka(poruka):
    print(f"{Boja.ZUTA}{poruka}{Boja.KRAJ}")

def pobjedio_poruka(poruka):
    print(f"{Boja.ZELENA}{Boja.BOLD}{poruka}{Boja.KRAJ}")

def izgubio_poruka(poruka):
    print(f"{Boja.CRVENA}{Boja.BOLD}{poruka}{Boja.KRAJ}")

def isprazni_ekran():
    if os.name == 'nt':
        _ = os.system('cls')
        time.sleep(0.2)
    else:
        _ = os.system('clear')
        time.sleep(0.2)

def progres_bar(poruka="Učitavam igru ..."): 

    for i in range(101):
        time.sleep(0.025)
        print(f"\r{Boja.CIAN}{i} % {poruka} {Boja.KRAJ}{Boja.BOLD}{Boja.KRAJ}", end='', flush=True)
        # time.sleep(0.01)
        if i == 100:
            print(f"\r{Boja.CIAN}{i} % {poruka} {Boja.KRAJ}{Boja.BOLD}{Boja.KRAJ}", end='', flush=True)
            time.sleep(0.2)
            #isprazni_ekran()
            break    

def progres_bar_unazad(poruka="Čistim memoriju ..."):
    for i in range(100, -1, -1):  # Počinje od 100, ide do -1 (uključuje 0), smanjuje se za 1
        time.sleep(0.05)
        print(f"\r{Boja.CIAN}{poruka} {i} % {Boja.KRAJ}{Boja.BOLD}{Boja.KRAJ}", end='', flush=True)
        if i == 0:  # Provjerava kada dosegne 0
            time.sleep(0.2)
            # isprazni_ekran() # Ovdje možete dodati vašu funkciju za čišćenje ekrana
            break        



# --- Glavna petlja programa koja omogućava ponovno igranje ---
while True:
    # Postavljanje/resetiranje vrijednosti na početku svake nove igre
    player_score = 0
    computer_score = 0
    tie_score = 0
    isprazni_ekran()
    obavijest_poruka(f"------------------------------------------")
    progres_bar()
    obavijest_poruka(f"\n-------------------------------------------")
    time.sleep(1)
    isprazni_ekran()
    zaglavlje_plava_bold("============== * * * * * =============== ")
    zaglavlje_plava("            Dobrodošli u igru             ")       
    zaglavlje_plava("                 * * *                  ")    
    zaglavlje_plava("           kamen, papir, škare!          ")
    zaglavlje_plava_bold("============== * * * * * =============== ")
    obavijest_poruka("Ovo je jednostavna igra u kojoj se možeš ")
    obavijest_poruka("igrati protiv računala.                  ")
    obavijest_poruka(f"----------------------------------------")
    obavijest_poruka("Bit će zatraženo da uneseš svoj odabir   ")
    obavijest_poruka("kamen, papir ili škare za igru. Ili za   ")
    obavijest_poruka("izlaz (izlaz / quit / exit).             ")
    obavijest_poruka(f"----------------------------------------")
    obavijest_poruka("Računalo će odabrati jednu od tri opcije.")
    obavijest_poruka(f"----------------------------------------")
    obavijest_poruka("Pobjednik se određuje na temelju pravila.")
    obavijest_poruka(f"----------------------------------------")
    obavijest_poruka("Možeš igrati dok ne odlučiš izaći.       ")
    zaglavlje_plava_bold("============== * * * * * =============== ")
    pobjedio_poruka("              Pravila:                   ")
    zaglavlje_plava_bold("============== * * * * * =============== ")
    obavijest_poruka(" 1.) Kamen udara škare,\n 2.) Škare režu papir,\n 3.) Papir pokriva kamen.")
    zaglavlje_plava_bold(f"----------------------------------------")
    obavijest_poruka(" 4.) Ako oba igrača odaberu istu opciju,\n     izjednačeno je.")
    zaglavlje_plava_bold("============== * * * * * =============== ")
    pobjedio_poruka("              S r e t n o !          ")
    zaglavlje_plava_bold("============== * * * * * =============== ")
    zaglavlje_plava_bold("")
    obavijest_poruka("\nPritisni Enter za nastavak...")
    input()
    isprazni_ekran()

    # Funkcije za dohvat odabira i provjeru pobjednika moraju biti definirane
    # ili dostupne unutar ovog opsega. Najbolje ih je definirati izvan petlje.

    def get_choices():
        zaglavlje_poruka("Unesi odabir (kamen, papir, škare): ") 
        zaglavlje_plava("ili upiši izlaz za izlazak iz igre (quit/exit/izlaz)") 
        player_choice = input("\nVaš odabir: ").strip().lower().replace(" ", "")
        options = ["kamen", "papir", "škare"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices

    # Važno: Moramo proslijediti trenutne rezultate u funkciju
    # ili nastaviti koristiti globalne varijable kao što ste i radili.
    # Korištenje globalnih varijabli je u redu za ovaj jednostavan primjer.
    def check_win(player, computer):
        global player_score, computer_score, tie_score
        obavijest_poruka(f"\nVaš odabir {player}, Računalo bira {computer}\n")
        if player == computer:
            tie_score += 1
            return "Nerješeno !"
        elif player == "kamen":
            if computer == "škare":
                player_score += 1
                return "Kamen udara škare! Pobijedili ste!"
            else:
                computer_score += 1
                return "Papir pokriva kamen. Izgubili ste!"
        elif player == "papir":
            if computer == "kamen":
                player_score += 1
                return "Papir pokriva kamen! Pobijedili ste!"
            else:
                computer_score += 1
                return "Škare režu papir. Izgubili ste!"
        elif player == "škare":
            if computer == "papir":
                player_score += 1
                return "Škare režu papir! Pobijedili ste!"
            else:
                computer_score += 1
                return "Kamen udara škare. Izgubili ste!"
    while True:
        isprazni_ekran()
        print(f"{Boja.CIAN}Vaši bodovi:{Boja.KRAJ}{Boja.BOLD} {player_score} {Boja.KRAJ} \n{Boja.CIAN}Bodovi računala:{Boja.KRAJ}{Boja.BOLD} {computer_score} {Boja.KRAJ}")
        #obavijest_poruka("\nDobrodošli u kamen, papir, škare!")
        #upozorenje_poruka("Unesite izlaz, quit ili exit za izlazak iz igre\n")

        choices = get_choices()

        if choices["player"] in ["quit", "izlaz", "exit"]:
            upozorenje_poruka(f"\nOdabrali ste izlaz iz igre. Hvala na igranju!")
            break  # Izlazi iz petlje za partiju i ide na ispis rezultata

        valid_options = ["kamen", "papir", "škare"]
        if choices["player"] not in valid_options:
            upozorenje_poruka(f"'{choices['player']}' nepostoječi odabir! \n\nMolimo odaberite 'kamen', 'papir'\nili 'škare' za nastavak igre \n\nili 'izlaz/quit/exit' za izlazak iz igre." )
            obavijest_poruka("\nPretisni Enter za nastavak...")
            input()
            continue

        result_poruka = check_win(choices["player"], choices["computer"])

        if "Pobijedili" in result_poruka:
            pobjedio_poruka(result_poruka)
        elif "Izgubili" in result_poruka:
            izgubio_poruka(result_poruka)
        else:
            obavijest_poruka(result_poruka)

        obavijest_poruka("\nPretisnite Enter za nastavak...")
        input()

    # --- Ispis rezultata nakon završetka partije ---
    obavijest_poruka(f"\n---------- Ukupni Bodovi -----------")
    obavijest_poruka(f"|     Nerješeno              {Boja.BOLD}{Boja.ZUTA}{tie_score:<3}{Boja.CIAN}   |")
    obavijest_poruka(f"|     Pobjeda računala:      {Boja.BOLD}{Boja.CRVENA}{computer_score:<3}{Boja.CIAN}   |")
    obavijest_poruka(f"|     Vaše pobjede:          {Boja.BOLD}{Boja.ZELENA}{player_score:<3}{Boja.CIAN}   |")
    obavijest_poruka(f"------------------------------------")


    if computer_score == player_score:
        zaglavlje_plava("\n* * * N E R J E Š E N O !   * * *")
    elif computer_score > player_score:
        izgubio_poruka("\n*** Računalo je pobjedilo :) Vi ste izgubili :( ***")
    else:
        pobjedio_poruka("\n*** Čestitam! Pobjedili ste! :) ***")

    # --- Pitanje za ponovnu igru ---
    play_again = input("\nŽeliš li igrati ponovo? (da/ne): ").strip().lower()
    if play_again not in ["da", "d"]:
       obavijest_poruka(f"------------------------------------")
       obavijest_poruka(f"Odabrao si izlaz, doviđenja !")
       obavijest_poruka(f"------------------------------------")
       progres_bar(f" {Boja.BOLD} Izlazim iz programa... {Boja.KRAJ}")
       obavijest_poruka(f"\n------------------------------------")
       progres_bar_unazad("Ostatci igre u memoriji ...")
       obavijest_poruka(f"\n------------------------------------")
       time.sleep(4)
       isprazni_ekran()
       exit()
        #break # Izlazi iz glavne (vanjske) petlje i završava program
    # Ako korisnik unese 'yes' ili 'y', vanjska petlja se automatski
    # nastavlja (continue) i započinje novu igru s resetiranim rezultatima.