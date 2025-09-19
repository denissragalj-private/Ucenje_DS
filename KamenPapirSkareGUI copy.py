import tkinter as tk
import random

# --- Globalne varijable za bodove ---
player_score = 0
computer_score = 0
draw_count = 0
# Varijabla za praćenje indeksa linije "Računalo razmišlja..."
thinking_line_index = None 

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
        return "Računalo je pobjedilo! 💻"

# --- GUI pomoćne funkcije ---
def add_message_to_terminal(message):
    """Pomoćna funkcija za dodavanje teksta u simulirani terminal."""
    terminal_output.config(state=tk.NORMAL)
    terminal_output.insert(tk.END, message)
    terminal_output.config(state=tk.DISABLED)
    terminal_output.see(tk.END)

def update_score_display():
    """Ažurira labele s trenutnim bodovima."""
    score_label.config(text=f"Rezultat:\n Igrač {player_score}     -     Računalo {computer_score}     -     Neriješeno {draw_count}")

def enable_player_buttons():
    """Omogućuje gumbe za odabir poteza."""
    papir_button.config(state=tk.NORMAL)
    skare_button.config(state=tk.NORMAL)
    kamen_button.config(state=tk.NORMAL)

def disable_player_buttons():
    """Onemogućuje gumbe za odabir poteza."""
    papir_button.config(state=tk.DISABLED)
    skare_button.config(state=tk.DISABLED)
    kamen_button.config(state=tk.DISABLED)

# --- Glavna logika igre unutar GUI-ja ---
def play_round(player_choice):
    """
    Funkcija koja pokreće jednu rundu igre, uključujući simulaciju "razmišljanja".
    """
    disable_player_buttons() # Onemogući gumbe dok računalo "razmišlja"

    add_message_to_terminal(f"Tvoj izbor:     {player_choice.capitalize()}\n")

    def animate_thinking(dots_count):
        global thinking_line_index 

        terminal_output.config(state=tk.NORMAL)

        if thinking_line_index:
            try:
                line_start = terminal_output.index(f"{thinking_line_index} linestart")
                line_end = terminal_output.index(f"{thinking_line_index} lineend")
                terminal_output.delete(line_start, f"{line_end}+1c")
            except tk.TclError:
                thinking_line_index = None 
                return 

        current_message = "Računalo razmišlja" + "." * (dots_count % 4) 
        terminal_output.insert(tk.END, current_message + "\n")

        thinking_line_index = terminal_output.index(tk.END + "-2c") 

        terminal_output.config(state=tk.DISABLED)
        terminal_output.see(tk.END) 

        if dots_count < 4: 
            root.after(300, lambda: animate_thinking(dots_count + 1))
        else:
            computer_choice = get_computer_choice()
            result = determine_winner(player_choice, computer_choice)

            global player_score, computer_score, draw_count
            if "Pobijedio si" in result:
                player_score += 1
            elif "Računalo je" in result:
                computer_score += 1
            else:
                draw_count += 1

            update_score_display()

            terminal_output.config(state=tk.NORMAL)
            if thinking_line_index:
                try:
                    line_start = terminal_output.index(f"{thinking_line_index} linestart")
                    line_end = terminal_output.index(f"{thinking_line_index} lineend")
                    terminal_output.delete(line_start, f"{line_end}+1c")
                except tk.TclError:
                    pass 
            terminal_output.config(state=tk.DISABLED)

            add_message_to_terminal(f"Izbor računala: {computer_choice.capitalize()}\n")
            add_message_to_terminal("-" * 40 + "\n")
            add_message_to_terminal(f"Ishod:     {result}\n")
            add_message_to_terminal("-" * 40 + "\n")

            enable_player_buttons() 
            terminal_output.see(tk.END)
            thinking_line_index = None 

    animate_thinking(0)

def new_game():
    """Funkcija za pokretanje nove igre."""
    global player_score, computer_score, draw_count, thinking_line_index

    player_score = 0
    computer_score = 0
    draw_count = 0
    thinking_line_index = None 
    update_score_display()

    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END) # Brisanje ekrana
    terminal_output.config(state=tk.DISABLED)

    add_message_to_terminal("****************************************\n")
    add_message_to_terminal(f"  Započeta je nova igra! Sretno!      \n")
    add_message_to_terminal("****************************************\n")
    add_message_to_terminal(f"  Odaberi svoj potez klikom na gumb.\n")
    add_message_to_terminal("****************************************\n")

    enable_player_buttons() 

def end_game():
    """Funkcija za prikaz konačnih bodova i proglašenje pobjednika."""
    clear_terminal_and_end_game()
    add_message_to_terminal("\n" + "=" * 40 + "\n")
    add_message_to_terminal(f"           Konačni rezultat:       \n")
    add_message_to_terminal(f"-" * 40 + "\n")
    add_message_to_terminal(f"  Igrač {player_score} - Računalo {computer_score} - Neriješeno {draw_count}\n")
    add_message_to_terminal(f"*" * 40 + "\n")

    # --- Logika za proglašenje pobjednika ---
    winner_message = ""
    if player_score > computer_score:
        winner_message = "\n***    Čestitam! Pobjedili ste! :)   ***"
    elif computer_score > player_score:
        winner_message = "\n***         Izgubili ste   !  :(     ***"
    else: # Neriješeno
        winner_message = "\n***          Neriješeno je  !   :|   ***"

    add_message_to_terminal(f"***" + " " * 34 + "***")
    add_message_to_terminal(winner_message + "\n") # Ispiši poruku o pobjedniku
    add_message_to_terminal(f"***" + " " * 34 + "***\n")
    add_message_to_terminal(f"*" * 40 + "\n")
    add_message_to_terminal(f"               KRAJ IGRE!             \n")
    add_message_to_terminal(f"*" * 40 + "\n")
    add_message_to_terminal(f"       Klikni 'Izlaz' za Kraj ili \n")
    add_message_to_terminal(f"     'Nova Igra' za ponovni početak. \n")
    add_message_to_terminal(f"=" * 40 + "\n")
    disable_player_buttons() 

def exit_application():
    """Funkcija za izlazak iz aplikacije."""
    root.destroy()

# --- Postavljanje GUI prozora ---
root = tk.Tk()
root.title("Papir Škare Kamen - Simulirani Terminal")
root.geometry("420x800") 
root.resizable(False, False)

# Labela za prikaz rezultata
score_label = tk.Label(root, text="Rezultat: Igrač 0 - Računalo 0 - Neriješeno 0", font=("Arial", 12, "bold"), fg="darkgreen")
score_label.pack(pady=5)

# Naslov/Upute
title_label = tk.Label(root, text="Odaberi svoj potez:", font=("Arial", 10, "bold"))
title_label.pack(pady=10)

# Okvir za gumbe za odabir poteza
player_choices_frame = tk.Frame(root)
player_choices_frame.pack()

# Gumbi za odabir poteza (inicijalno onemogućeni)
papir_button = tk.Button(player_choices_frame, text="Papir", width=12, height=2, command=lambda: play_round('papir'))
papir_button.grid(row=0, column=0, padx=5, pady=5)
papir_button.config(state=tk.DISABLED) 

skare_button = tk.Button(player_choices_frame, text="Škare", width=12, height=2, command=lambda: play_round('škare'))
skare_button.grid(row=0, column=1, padx=5, pady=5)
skare_button.config(state=tk.DISABLED) 

kamen_button = tk.Button(player_choices_frame, text="Kamen", width=12, height=2, command=lambda: play_round('kamen'))
kamen_button.grid(row=0, column=2, padx=5, pady=5)
kamen_button.config(state=tk.DISABLED) 


# --- Simulirani terminalski prozor ---
terminal_frame = tk.Frame(root, bd=3, relief="sunken")
terminal_frame.pack(pady=15, padx=22, fill=tk.BOTH, expand=True)

terminal_output = tk.Text(terminal_frame, wrap="word", font=("Consolas", 11), bg="black", fg="lime green", insertbackground="white")
terminal_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(terminal_frame, command=terminal_output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

terminal_output.config(yscrollcommand=scrollbar.set)

# --- Opcije igre: Nova Igra, Kraj i Izlaz ---
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

new_game_button = tk.Button(options_frame, text="Nova Igra", width=12, height=2, command=new_game, bg="lightgreen")
new_game_button.grid(row=0, column=0, padx=5)

end_game_button = tk.Button(options_frame, text="Kraj", width=12, height=2, command=end_game, bg="orange")
end_game_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(options_frame, text="Izlaz", width=12, height=2, command=exit_application, bg="salmon")
exit_button.grid(row=0, column=2, padx=5)

# --- Proširena uvodna poruka ---
full_intro_message = """
============== * * * * * =============== 
          Dobrodošli u igru
                * * * 
         Kamen, papir, škare!        
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
    add_message_to_terminal(full_intro_message)
    update_score_display() # Prikaz početnog rezultata odmah

    # Pauza od 3 sekunde (3000 milisekundi)
    root.after(5000, clear_terminal_and_start_game)

def clear_terminal_and_end_game():
    """Briše terminalski ekran i prikazuje poruku za početak igre."""
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END) # Brisanje cijelog sadržaja
    terminal_output.config(state=tk.DISABLED)


def clear_terminal_and_start_game():
    """Briše terminalski ekran i prikazuje poruku za početak igre."""
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END) # Brisanje cijelog sadržaja
    terminal_output.config(state=tk.DISABLED)

    add_message_to_terminal("****************************************\n")
    add_message_to_terminal(" Spremni za igru! Odaberite svoj potez.\n")
    add_message_to_terminal("****************************************\n")
    enable_player_buttons() # Omogući gumbe nakon uvoda i čišćenja

# --- Pokretanje uvoda i igre pri startu aplikacije ---
start_intro_and_game()

# Pokretanje glavne petlje Tkinter aplikacije
root.mainloop()