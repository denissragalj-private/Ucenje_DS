import tkinter as tk # Uvoz modula tkinter pod aliasom tk. Ovo je standardni način uvoza Tkintera.
import random # Uvoz modula random za generiranje nasumičnih odabira računala.

# --- Globalne varijable za bodove ---
# Deklaracija globalnih varijabli koje će pratiti rezultat igre.
# Globalne su jer se pristupaju i mijenjaju iz različitih funkcija.
player_score = 0 # Broj pobjeda igrača.
computer_score = 0 # Broj pobjeda računala.
draw_count = 0 # Broj neriješenih ishoda.
# Varijabla za praćenje indeksa linije "Računalo razmišlja..."
# Ovo se koristi za dinamičko ažuriranje teksta u terminalu (brisanje i ponovno ispisivanje).
thinking_line_index = None 

# --- Logika igre (nepromijenjena) ---
def get_computer_choice():
    """Generira nasumični odabir računala."""
    # Koristi random.choice() za odabir jedne od tri opcije iz liste.
    return random.choice(['papir', 'škare', 'kamen'])

def determine_winner(player_choice, computer_choice):
    """Određuje pobjednika na temelju odabira igrača i računala."""
    # Logika igre kamen, papir, škare.
    if player_choice == computer_choice:
        return "Neriješeno!"
    # Provjera svih uvjeta u kojima igrač pobjeđuje.
    elif (player_choice == 'papir' and computer_choice == 'kamen') or \
         (player_choice == 'škare' and computer_choice == 'papir') or \
         (player_choice == 'kamen' and computer_choice == 'škare'):
        return "Pobijedio si! 🎉"
    else:
        # Ako nije neriješeno i igrač nije pobijedio, računalo je pobijedilo.
        return "Računalo je pobjedilo! 💻"

# --- GUI pomoćne funkcije ---
def add_message_to_terminal(message):
    """Pomoćna funkcija za dodavanje teksta u simulirani terminal."""
    # Terminal output je tk.Text widget. Da bismo ga mogli mijenjati, moramo ga staviti u NORMAL stanje.
    terminal_output.config(state=tk.NORMAL)
    # Ubacujemo poruku na kraj (tk.END) terminala.
    terminal_output.insert(tk.END, message)
    # Nakon dodavanja teksta, vraćamo ga u DISABLED stanje da korisnik ne može direktno upisivati.
    terminal_output.config(state=tk.DISABLED)
    # Pomicanje scrollbara na dno kako bi se vidjela najnovija poruka.
    terminal_output.see(tk.END)

def update_score_display():
    """Ažurira labele s trenutnim bodovima."""
    # Ažurira tekst score_label widgeta s trenutnim vrijednostima globalnih varijabli za bodove.
    score_label.config(text=f"Rezultat:\n Igrač {player_score}      -      Računalo {computer_score}      -      Neriješeno {draw_count}")

def enable_player_buttons():
    """Omogućuje gumbe za odabir poteza."""
    # Mijenja stanje gumba na NORMAL kako bi postali klikabilni.
    papir_button.config(state=tk.NORMAL)
    skare_button.config(state=tk.NORMAL)
    kamen_button.config(state=tk.NORMAL)

def disable_player_buttons():
    """Onemogućuje gumbe za odabir poteza."""
    # Mijenja stanje gumba na DISABLED kako bi postali neklikabilni (npr. dok računalo "razmišlja").
    papir_button.config(state=tk.DISABLED)
    skare_button.config(state=tk.DISABLED)
    kamen_button.config(state=tk.DISABLED)

# --- Glavna logika igre unutar GUI-ja ---
def play_round(player_choice):
    """
    Funkcija koja pokreće jednu rundu igre, uključujući simulaciju "razmišljanja".
    """
    disable_player_buttons() # Onemogući gumbe dok računalo "razmišlja"

    add_message_to_terminal(f"Tvoj izbor:      {player_choice.capitalize()}\n")

    def animate_thinking(dots_count):
        """
        Pomoćna funkcija za animaciju "Računalo razmišlja..." u terminalu.
        Rekurzivno se poziva pomoću root.after() za simulaciju animacije.
        """
        global thinking_line_index # Pristup globalnoj varijabli.

        terminal_output.config(state=tk.NORMAL) # Omogući terminal za izmjene.

        if thinking_line_index: # Ako postoji prethodna linija "razmišljanja"...
            try:
                # Pokušaj dohvatiti početak i kraj linije po indeksu i obrisati je.
                line_start = terminal_output.index(f"{thinking_line_index} linestart")
                line_end = terminal_output.index(f"{thinking_line_index} lineend")
                terminal_output.delete(line_start, f"{line_end}+1c") # +1c uključuje newline znak.
            except tk.TclError:
                # Hvatanje greške ako linija više ne postoji (npr. ako je terminal obrisan).
                thinking_line_index = None 
                return # Prekini izvršavanje funkcije.

        # Kreiranje poruke s animiranim točkicama (0, 1, 2, 3 točkice).
        current_message = "Računalo razmišlja" + "." * (dots_count % 4) 
        terminal_output.insert(tk.END, current_message + "\n") # Ubaci novu poruku.

        # Pohrani indeks nove linije "Računalo razmišlja..."
        # tk.END + "-2c" znači "dva znaka prije kraja" (kako bi uhvatili liniju prije novog retka).
        thinking_line_index = terminal_output.index(tk.END + "-2c") 

        terminal_output.config(state=tk.DISABLED) # Onemogući terminal.
        terminal_output.see(tk.END) # Pomakni prikaz na kraj.

        if dots_count < 4: # Ako animacija nije završila (manje od 4 točkice)...
            # Planiraj sljedeći poziv funkcije animate_thinking nakon 300 ms.
            # Lambda funkcija se koristi da bismo mogli proslijediti argument (dots_count + 1).
            root.after(300, lambda: animate_thinking(dots_count + 1))
        else:
            # Animacija je završila, sada računalo donosi odluku i prikazuje rezultat.
            computer_choice = get_computer_choice() # Računalo bira.
            result = determine_winner(player_choice, computer_choice) # Određuje se pobjednik.

            global player_score, computer_score, draw_count # Deklaracija da koristimo globalne varijable.
            # Ažuriranje bodova na temelju ishoda.
            if "Pobijedio si" in result:
                player_score += 1
            elif "Računalo je" in result:
                computer_score += 1
            else:
                draw_count += 1

            update_score_display() # Ažuriraj prikaz bodova.

            terminal_output.config(state=tk.NORMAL) # Omogući terminal za brisanje "razmišljanja".
            if thinking_line_index: # Ako linija "razmišljanja" još postoji...
                try:
                    # Obriši liniju "Računalo razmišlja..."
                    line_start = terminal_output.index(f"{thinking_line_index} linestart")
                    line_end = terminal_output.index(f"{thinking_line_index} lineend")
                    terminal_output.delete(line_start, f"{line_end}+1c")
                except tk.TclError:
                    pass # Ignoriraj grešku ako linija više ne postoji.
            terminal_output.config(state=tk.DISABLED) # Onemogući terminal.

            # Dodaj rezultate runde u terminal.
            add_message_to_terminal(f"Izbor računala: {computer_choice.capitalize()}\n")
            add_message_to_terminal("-" * 40 + "\n")
            add_message_to_terminal(f"Ishod:      {result}\n")
            add_message_to_terminal("-" * 40 + "\n")

            enable_player_buttons() # Omogući gumbe za sljedeću rundu.
            terminal_output.see(tk.END) # Pomakni prikaz na kraj.
            thinking_line_index = None # Resetiraj indeks za sljedeću animaciju.

    animate_thinking(0) # Pokreni animaciju "razmišljanja" s 0 točkica.

def new_game():
    """Funkcija za pokretanje nove igre."""
    global player_score, computer_score, draw_count, thinking_line_index # Pristup globalnim varijablama.

    # Resetiranje svih bodova i indeksa.
    player_score = 0
    computer_score = 0
    draw_count = 0
    thinking_line_index = None 
    update_score_display() # Ažuriraj prikaz bodova na 0.

    terminal_output.config(state=tk.NORMAL) # Omogući terminal.
    terminal_output.delete(1.0, tk.END) # Brisanje cijelog sadržaja terminala (od prve linije, prvog znaka do kraja).
    terminal_output.config(state=tk.DISABLED) # Onemogući terminal.

    # Dodavanje poruka o početku nove igre.
    add_message_to_terminal("****************************************\n")
    add_message_to_terminal(f"  Započeta je nova igra! Sretno!      \n")
    add_message_to_terminal("****************************************\n")
    add_message_to_terminal(f"  Odaberi svoj potez klikom na gumb.\n")
    add_message_to_terminal("****************************************\n")

    enable_player_buttons() # Omogući gumbe za igranje.

def end_game():
    """Funkcija za prikaz konačnih bodova i proglašenje pobjednika."""
    clear_terminal_and_end_game() # Briše terminal prije prikaza konačnih rezultata.
    add_message_to_terminal("\n" + "=" * 40 + "\n")
    add_message_to_terminal(f"           Konačni rezultat:        \n")
    add_message_to_terminal(f"-" * 40 + "\n")
    add_message_to_terminal(f"  Igrač {player_score} - Računalo {computer_score} - Neriješeno {draw_count}\n")
    add_message_to_terminal(f"*" * 40 + "\n")

    # --- Logika za proglašenje pobjednika ---
    winner_message = ""
    if player_score > computer_score:
        winner_message = "\n*** Čestitam! Pobjedili ste! :)    ***"
    elif computer_score > player_score:
        winner_message = "\n*** Izgubili ste ! :(      ***"
    else: # Neriješeno
        winner_message = "\n*** Neriješeno je !    :|   ***"

    add_message_to_terminal(f"***" + " " * 34 + "***") # Dodatni prazan red za formatiranje.
    add_message_to_terminal(winner_message + "\n") # Ispiši poruku o pobjedniku.
    add_message_to_terminal(f"***" + " " * 34 + "***\n")
    add_message_to_terminal(f"*" * 40 + "\n")
    add_message_to_terminal(f"            KRAJ IGRE!              \n")
    add_message_to_terminal(f"*" * 40 + "\n")
    add_message_to_terminal(f"        Klikni 'Izlaz' za Kraj ili \n")
    add_message_to_terminal(f"      'Nova Igra' za ponovni početak. \n")
    add_message_to_terminal(f"=" * 40 + "\n")
    disable_player_buttons() # Onemogući gumbe jer je igra završena.

def exit_application():
    """Funkcija za izlazak iz aplikacije."""
    root.destroy() # Uništava glavni Tkinter prozor i završava aplikaciju.

# --- Postavljanje GUI prozora ---
root = tk.Tk() # Stvara glavni prozor aplikacije. Ovo je korijen (root) cijelog GUI-ja.
root.title("Papir Škare Kamen - Simulirani Terminal") # Postavlja naslov prozora.
root.geometry("420x800") # Postavlja početnu veličinu prozora (širina x visina u pikselima).
root.resizable(False, False) # Onemogućuje promjenu veličine prozora od strane korisnika (širina, visina).

# Labela za prikaz rezultata
# tk.Label je widget za prikaz teksta ili slika.
score_label = tk.Label(root, text="Rezultat: Igrač 0 - Računalo 0 - Neriješeno 0", font=("Arial", 12, "bold"), fg="darkgreen")
score_label.pack(pady=5) # .pack() je geometry manager koji organizira widgete u blokove.
                         # pady dodaje vertikalni razmak (padding) oko widgeta.

# Naslov/Upute
title_label = tk.Label(root, text="Odaberi svoj potez:", font=("Arial", 10, "bold"))
title_label.pack(pady=10)

# Okvir za gumbe za odabir poteza
# tk.Frame je widget koji služi kao spremnik za druge widgete, pomaže u organizaciji rasporeda.
player_choices_frame = tk.Frame(root)
player_choices_frame.pack()

# Gumbi za odabir poteza (inicijalno onemogućeni)
# tk.Button je interaktivni widget na koji se može kliknuti.
# text: Tekst prikazan na gumbu.
# width, height: Veličina gumba.
# command: Funkcija koja se poziva kada se gumb klikne.
# lambda: Koristi se za prosljeđivanje argumenata funkciji play_round().
papir_button = tk.Button(player_choices_frame, text="Papir", width=12, height=2, command=lambda: play_round('papir'))
# .grid() je geometry manager koji organizira widgete u rešetku (redove i stupce).
papir_button.grid(row=0, column=0, padx=5, pady=5) # row=0, column=0 postavlja ga u prvi red, prvi stupac. padx/pady dodaje razmak.
papir_button.config(state=tk.DISABLED) # Inicijalno je gumb onemogućen.

skare_button = tk.Button(player_choices_frame, text="Škare", width=12, height=2, command=lambda: play_round('škare'))
skare_button.grid(row=0, column=1, padx=5, pady=5)
skare_button.config(state=tk.DISABLED)

kamen_button = tk.Button(player_choices_frame, text="Kamen", width=12, height=2, command=lambda: play_round('kamen'))
kamen_button.grid(row=0, column=2, padx=5, pady=5)
kamen_button.config(state=tk.DISABLED)

# --- Simulirani terminalski prozor ---
terminal_frame = tk.Frame(root, bd=3, relief="sunken") # Okvir s obrubom i reljefom "sunken" (udubljeno).
terminal_frame.pack(pady=15, padx=22, fill=tk.BOTH, expand=True) # fill=tk.BOTH ga rasteže u oba smjera, expand=True dopušta mu da zauzme dodatni prostor.

# tk.Text je widget za višeredni tekst, idealan za terminalski izlaz.
# wrap="word": Omogućuje prijelom teksta na granicama riječi.
# font: Postavlja font.
# bg, fg: Boja pozadine i prednjeg plana (teksta).
# insertbackground: Boja kursora.
terminal_output = tk.Text(terminal_frame, wrap="word", font=("Consolas", 11), bg="black", fg="lime green", insertbackground="white")
terminal_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # side=tk.LEFT ga smješta na lijevu stranu unutar okvira.

# tk.Scrollbar je widget za pomicanje sadržaja.
scrollbar = tk.Scrollbar(terminal_frame, command=terminal_output.yview) # Povezuje scrollbar s y-pogledom terminal_outputa.
scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # Smješta scrollbar na desnu stranu i rasteže ga vertikalno.

terminal_output.config(yscrollcommand=scrollbar.set) # Govori terminal_outputu da koristi scrollbar za pomicanje.

# --- Opcije igre: Nova Igra, Kraj i Izlaz ---
options_frame = tk.Frame(root) # Okvir za gumbe s opcijama.
options_frame.pack(pady=10)

new_game_button = tk.Button(options_frame, text="Nova Igra", width=12, height=2, command=new_game, bg="lightgreen")
new_game_button.grid(row=0, column=0, padx=5) # Smješten u rešetku.

end_game_button = tk.Button(options_frame, text="Kraj", width=12, height=2, command=end_game, bg="orange")
end_game_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(options_frame, text="Izlaz", width=12, height=2, command=exit_application, bg="salmon")
exit_button.grid(row=0, column=2, padx=5)

# --- Proširena uvodna poruka ---
# Višeredni string za uvodnu poruku.
full_intro_message = """
============== * * * * * =============== 
          Dobrodošli u igru
                * * * Kamen, papir, škare!         
============== * * * * * =============== 
Ovo je jednostavna igra u kojoj se možeš  
igrati protiv računala.                  
----------------------------------------  
Bit će zatraženo da uneseš svoj odabir    
kamen, papir ili škare za igru. Ili za    
izlaz (izlaz / quit / exit).             
----------------------------------------  
Računalo će odabrati jednu od tri opcije
----------------------------------------  
Pobjednik se određuje na temelju pravila
----------------------------------------  
Možeš igrati dok ne odlučiš izaći.        
============== * * * * * ===============  
              Pravila:                   
============== * * * * * ===============  
 1.) Kamen udara škare,
 2.) Škare režu papir,
 3.) Papir pokriva kamen.
----------------------------------------  
 4.) Ako oba igrača odaberu istu opciju,  
     izjednačeno je.
============== * * * * * ===============  
              S r e t n o !              
============== * * * * * ===============  
"""

# Funkcija koja ispisuje uvod i pokreće igru nakon pauze
def start_intro_and_game():
    """
    Funkcija koja inicijalno prikazuje uvodnu poruku, ažurira prikaz bodova
    i zatim, nakon određenog kašnjenja, briše terminal i započinje igru.
    """
    add_message_to_terminal(full_intro_message) # Dodaje cijelu uvodnu poruku u terminal.
    update_score_display() # Prikaz početnog rezultata (0) odmah.

    # Pauza od 5 sekundi (5000 milisekundi) prije nego što se pozove clear_terminal_and_start_game.
    # root.after() je ključna Tkinter metoda za odgodu izvršavanja funkcija.
    root.after(5000, clear_terminal_and_start_game)

def clear_terminal_and_end_game():
    """Briše terminalski ekran i prikazuje poruku za kraj igre."""
    # Slično kao i clear_terminal_and_start_game, ali bez ponovnog pokretanja gumba.
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END) 
    terminal_output.config(state=tk.DISABLED)

def clear_terminal_and_start_game():
    """Briše terminalski ekran i prikazuje poruku za početak igre."""
    terminal_output.config(state=tk.NORMAL) # Omogući terminal za brisanje.
    terminal_output.delete(1.0, tk.END) # Briše cijeli sadržaj terminala.
    terminal_output.config(state=tk.DISABLED) # Onemogući terminal.

    add_message_to_terminal("****************************************\n")
    add_message_to_terminal(" Spremni za igru! Odaberite svoj potez.\n")
    add_message_to_terminal("****************************************\n")
    enable_player_buttons() # Omogući gumbe za igru nakon što je uvod završen i terminal očišćen.

# --- Pokretanje uvoda i igre pri startu aplikacije ---
start_intro_and_game() # Prvo što se poziva kada se aplikacija pokrene.

# Pokretanje glavne petlje Tkinter aplikacije
# root.mainloop() je obavezna linija za svaku Tkinter aplikaciju.
# Ona pokreće "event loop" (petlju događaja) koja čeka na događaje (klikove mišem, pritiske tipki, itd.)
# i poziva odgovarajuće funkcije. Aplikacija ostaje otvorena dok se ova petlja ne prekine (npr. pozivom root.destroy()).
root.mainloop()