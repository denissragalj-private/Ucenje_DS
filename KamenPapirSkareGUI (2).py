import tkinter as tk
import random

# --- Globalne varijable za bodove ---
player_score = 0
computer_score = 0
draw_count = 0 # Nova varijabla za neriješeno

# --- Logika igre (nepromijenjena) ---
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
        return "Računalo je pobijedilo! 💻"

# --- GUI pomoćne funkcije ---
def add_message_to_terminal(message):
    """Pomoćna funkcija za dodavanje teksta u simulirani terminal."""
    terminal_output.config(state=tk.NORMAL) # Omogući pisanje privremeno
    terminal_output.insert(tk.END, message)
    terminal_output.config(state=tk.DISABLED) # Onemogući korisniku da tipka
    terminal_output.see(tk.END) # Pomicanje na dno

def update_score_display():
    """Ažurira labele s trenutnim bodovima."""
    score_label.config(text=f"Rezultat: Igrač {player_score} - Računalo {computer_score} - Neriješeno {draw_count}")

# --- GUI logika ---
def play_game(player_choice):
    """
    Funkcija koja se poziva klikom na gumb za odabir poteza.
    Ažurira bodove i dodaje poruke u simulirani terminalski prozor.
    """
    global player_score, computer_score, draw_count # Dodaj draw_count
    
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    # Ažuriranje bodova
    if "Pobijedio si" in result:
        player_score += 1
    elif "Računalo je pobijedilo" in result:
        computer_score += 1
    else: # Ovo je slučaj kada je rezultat "Neriješeno!"
        draw_count += 1
    
    update_score_display() # Ažuriraj prikaz bodova
    
    # Dodavanje poruka u Text widget (simulirani terminal)
    add_message_to_terminal(f"Tvoj izbor: {player_choice.capitalize()}\n")
    add_message_to_terminal(f"Izbor računala: {computer_choice.capitalize()}\n")
    add_message_to_terminal(f"Ishod: {result}\n")
    add_message_to_terminal("-" * 30 + "\n\n") # Dodaj separator i dva nova retka za razmak

def new_game():
    """Funkcija za pokretanje nove igre."""
    global player_score, computer_score, draw_count # Dodaj draw_count
    
    player_score = 0 # Resetiraj bodove
    computer_score = 0 # Resetiraj bodove
    draw_count = 0 # Resetiraj neriješene
    update_score_display() # Ažuriraj prikaz bodova na 0-0-0

    terminal_output.config(state=tk.NORMAL) # Omogući pisanje
    terminal_output.delete(1.0, tk.END) # Briše sav postojeći tekst
    terminal_output.config(state=tk.DISABLED) # Onemogući pisanje
    
    # Ponovno ispisivanje početne poruke za novu igru
    add_message_to_terminal("****************************************\n")
    add_message_to_terminal("  Započeta je nova igra! Sretno!      \n")
    add_message_to_terminal("****************************************\n")
    add_message_to_terminal("Odaberi svoj potez klikom na gumb.\n\n")

    # Omogući gumbe za odabir poteza nakon "Nove igre"
    papir_button.config(state=tk.NORMAL)
    skare_button.config(state=tk.NORMAL)
    kamen_button.config(state=tk.NORMAL)

def end_game():
    """Funkcija za prikaz konačnih bodova."""
    add_message_to_terminal("\n" + "=" * 40 + "\n")
    add_message_to_terminal("         KRAJ IGRE!         \n")
    add_message_to_terminal(f"  Konačni rezultat: Igrač {player_score} - Računalo {computer_score} - Neriješeno {draw_count}\n")
    add_message_to_terminal("=" * 40 + "\n\n")
    add_message_to_terminal("Klikni 'Izlaz' za zatvaranje aplikacije ili 'Nova Igra' za ponovni početak.\n")
    
    # Onemogući gumbe za odabir poteza nakon "Kraja"
    papir_button.config(state=tk.DISABLED)
    skare_button.config(state=tk.DISABLED)
    kamen_button.config(state=tk.DISABLED)

def exit_application():
    """Funkcija za izlazak iz aplikacije."""
    root.destroy() # Zatvara glavni prozor i završava aplikaciju

# --- Postavljanje GUI prozora ---
root = tk.Tk()
root.title("Papir Škare Kamen - Simulirani Terminal")
root.geometry("500x600") 
root.resizable(False, False)

# Naslov/Upute
title_label = tk.Label(root, text="Odaberi svoj potez:", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Labela za prikaz rezultata (sada uključuje i neriješeno)
score_label = tk.Label(root, text="Rezultat: Igrač 0 - Računalo 0 - Neriješeno 0", font=("Arial", 14, "bold"), fg="darkgreen")
score_label.pack(pady=5)

# Okvir za gumbe za odabir poteza
player_choices_frame = tk.Frame(root)
player_choices_frame.pack()

# Gumbi za odabir poteza
papir_button = tk.Button(player_choices_frame, text="Papir", width=12, height=2, command=lambda: play_game('papir'))
papir_button.grid(row=0, column=0, padx=5, pady=5)

skare_button = tk.Button(player_choices_frame, text="Škare", width=12, height=2, command=lambda: play_game('škare'))
skare_button.grid(row=0, column=1, padx=5, pady=5)

kamen_button = tk.Button(player_choices_frame, text="Kamen", width=12, height=2, command=lambda: play_game('kamen'))
kamen_button.grid(row=0, column=2, padx=5, pady=5)

# --- Simulirani terminalski prozor ---
terminal_frame = tk.Frame(root, bd=2, relief="sunken")
terminal_frame.pack(pady=15, padx=10, fill=tk.BOTH, expand=True)

terminal_output = tk.Text(terminal_frame, wrap="word", font=("Consolas", 10), bg="black", fg="lime green", insertbackground="white")
terminal_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(terminal_frame, command=terminal_output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

terminal_output.config(yscrollcommand=scrollbar.set)

# --- Opcije igre: Nova Igra, Kraj i Izlaz ---
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

new_game_button = tk.Button(options_frame, text="Nova Igra", width=15, height=2, command=new_game, bg="lightgreen")
new_game_button.grid(row=0, column=0, padx=5)

end_game_button = tk.Button(options_frame, text="Kraj", width=15, height=2, command=end_game, bg="orange")
end_game_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(options_frame, text="Izlaz", width=15, height=2, command=exit_application, bg="salmon")
exit_button.grid(row=0, column=2, padx=5)

# --- Inicijalna poruka pri pokretanju i početni prikaz bodova ---
add_message_to_terminal("****************************************\n")
add_message_to_terminal("  Dobrodošao u igru Papir Škare Kamen!  \n")
add_message_to_terminal("****************************************\n")
add_message_to_terminal("Pravila su jednostavna: \n")
add_message_to_terminal("  - Papir pobjeđuje Kamen\n")
add_message_to_terminal("  - Škare pobjeđuju Papir\n")
add_message_to_terminal("  - Kamen pobjeđuje Škare\n")
add_message_to_terminal("Odaberi svoj potez klikom na gumb.\n\n")
update_score_display() # Prikaz početnog rezultata

# Pokretanje glavne petlje Tkinter aplikacije
root.mainloop()