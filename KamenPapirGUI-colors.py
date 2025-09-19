import tkinter as tk
import random

# --- Globalne varijable za bodove ---
player_score = 0
computer_score = 0
draw_count = 0
thinking_line_index = None

# --- Logika igre (nepromijenjena) ---
def get_computer_choice():
    return random.choice(['papir', 'škare', 'kamen'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Neriješeno!"
    elif (player_choice == 'papir' and computer_choice == 'kamen') or \
         (player_choice == 'škare' and computer_choice == 'papir') or \
         (player_choice == 'kamen' and computer_choice == 'škare'):
        return "Pobijedio si! 🎉"
    else:
        return "Računalo je pobjedilo! 💻"

# --- GUI pomoćne funkcije ---
def add_message_to_terminal(message, tag=None):
    terminal_output.config(state=tk.NORMAL)
    if tag:
        terminal_output.insert(tk.END, message, tag)
    else:
        terminal_output.insert(tk.END, message)
    terminal_output.config(state=tk.DISABLED)
    terminal_output.see(tk.END)

def update_score_display():
    if player_score > computer_score:
        score_label.config(fg="green")
    elif computer_score > player_score:
        score_label.config(fg="red")
    else:
        score_label.config(fg="darkblue")
    
    score_label.config(text=f"Rezultat:\n Igrač {player_score}      -      Računalo {computer_score}      -      Neriješeno {draw_count}")

def enable_player_buttons():
    papir_button.config(state=tk.NORMAL)
    skare_button.config(state=tk.NORMAL)
    kamen_button.config(state=tk.NORMAL)

def disable_player_buttons():
    papir_button.config(state=tk.DISABLED)
    skare_button.config(state=tk.DISABLED)
    kamen_button.config(state=tk.DISABLED)

# --- Glavna logika igre unutar GUI-ja ---
def play_round(player_choice):
    disable_player_buttons()

    add_message_to_terminal(f"Tvoj izbor:      {player_choice.capitalize()}\n")

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
            
            message_tag = None
            if "Pobijedio si" in result:
                player_score += 1
                message_tag = "pobjeda" 
            elif "Računalo je" in result:
                computer_score += 1
                message_tag = "poraz"   
            else:
                draw_count += 1
                message_tag = "nerijeseno" 

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

            add_message_to_terminal(f"Izbor računala: {computer_choice.capitalize()}\n", tag="info")
            add_message_to_terminal("-" * 40 + "\n")
            add_message_to_terminal(f"Ishod:      {result}\n", message_tag)
            add_message_to_terminal("-" * 40 + "\n")

            enable_player_buttons() 
            terminal_output.see(tk.END)
            thinking_line_index = None 

    animate_thinking(0)

def new_game():
    global player_score, computer_score, draw_count, thinking_line_index

    player_score = 0
    computer_score = 0
    draw_count = 0
    thinking_line_index = None 
    update_score_display()

    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END)
    terminal_output.config(state=tk.DISABLED)

    add_message_to_terminal("****************************************\n", tag="naslov")
    add_message_to_terminal(f"  Započeta je nova igra! Sretno!      \n", tag="naslov")
    add_message_to_terminal("****************************************\n", tag="naslov")
    add_message_to_terminal(f"  Odaberi svoj potez klikom na gumb.\n", tag="pobjeda")
    add_message_to_terminal("****************************************\n", tag="zelenibold12")

    enable_player_buttons() 

# --- Glavna funkcija za kraj igre, sada s unificiranim ispisom ---
def end_game():
    clear_terminal_and_end_game()
    add_message_to_terminal("\n" + "=" * 40 + "\n", tag="naslov")
    add_message_to_terminal(f"           Konačni rezultat:        \n", tag="naslov")
    add_message_to_terminal(f"-" * 40 + "\n", tag="naslov")
    add_message_to_terminal(f"  Igrač {player_score} - Računalo {computer_score} - Neriješeno {draw_count}\n", tag="naslov")
    add_message_to_terminal(f"*" * 40 + "\n", tag="naslov")

    # --- Logika za proglašenje pobjednika i UNIFICIRANI ISPIS ---
    winner_message_text = "" # Tekst koji ide između zvjezdica
    message_tag = ""         # Tag za taj tekst

    if player_score > computer_score:
        winner_message_text = "Čestitam! Pobjedili ste! :)"
        message_tag = "pobjeda" # Tag za zeleni tekst
    elif computer_score > player_score:
        winner_message_text = "Izgubili ste ! :("
        message_tag = "poraz"   # Tag za crveni tekst
    else: # Neriješeno
        winner_message_text = "Neriješeno je !    :| "
        message_tag = "nerijeseno" # Tag za svijetloplavi tekst

    # NOVO: Dinamičko određivanje paddinga (razmaka)
    # Ovo će osigurati da se tekst centirira unutar zvjezdica
    total_stars_line_length = 45 # Ukupna željena duljina linije sa zvjezdicama
    stars_on_side = 3 # Broj zvjezdica na svakoj strani (***)
    padding_length = total_stars_line_length - (2 * stars_on_side) - len(winner_message_text)
    # Podijelimo razmak na pola za lijevu i desnu stranu
    left_padding = " " * (padding_length // 2)
    right_padding = " " * (padding_length - (padding_length // 2))

    # Sada ispisujemo poruku dio po dio
    terminal_output.config(state=tk.NORMAL) # Omogući terminal
    terminal_output.insert(tk.END, "\n", "naslov") # Dodaj novi red za odmak

    # Prvi red sa zvjezdicama i praznim prostorom
    terminal_output.insert(tk.END, "*" * total_stars_line_length, "zute_zvjezdice")
    terminal_output.insert(tk.END, "\n")

    # Drugi red sa zvjezdicama, porukom i paddingom
    terminal_output.insert(tk.END, "*" * stars_on_side, "zute_zvjezdice")
    terminal_output.insert(tk.END, left_padding) # Lijevi razmak
    terminal_output.insert(tk.END, winner_message_text, message_tag) # Tekst poruke s tagom boje
    terminal_output.insert(tk.END, right_padding) # Desni razmak
    terminal_output.insert(tk.END, "*" * stars_on_side, "zute_zvjezdice")
    terminal_output.insert(tk.END, "\n")

    # Treći red sa zvjezdicama i praznim prostorom
    terminal_output.insert(tk.END, "*" * total_stars_line_length, "zute_zvjezdice")
    terminal_output.insert(tk.END, "\n")

    terminal_output.config(state=tk.DISABLED) # Onemogući terminal
    terminal_output.see(tk.END) # Pomakni prikaz na kraj

    add_message_to_terminal(f"*" * 40 + "\n", tag="naslov")
    add_message_to_terminal(f"            KRAJ IGRE!              \n", tag="zelenibold12")
    add_message_to_terminal(f"*" * 40 + "\n", tag="naslov")
    add_message_to_terminal(f"        Klikni 'Izlaz' za Kraj ili \n", tag="info")
    add_message_to_terminal(f"      'Nova Igra' za ponovni početak. \n", tag="info")
    add_message_to_terminal(f"=" * 40 + "\n", tag="naslov")
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
score_label = tk.Label(root, text="Rezultat: Igrač 0 - Računalo 0 - Neriješeno 0", 
                       font=("Arial", 12, "bold"), fg="darkblue")
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

# ************************************************************
# DEFINIRANJE TAGOVA ZA RAZLIČITE STILOVE TEKSTA U TERMINALU
# ************************************************************
terminal_output.tag_configure("pobjeda", foreground="green", font=("Consolas", 11, "bold")) # Zeleni, podebljani tekst za pobjedu
terminal_output.tag_configure("zelenibold12", foreground="green", font=("Consolas", 12, "bold")) # Zeleni, podebljani tekst za pobjedu
terminal_output.tag_configure("poraz", foreground="red", font=("Consolas", 11, "bold"))     # Crveni, podebljani tekst za poraz
terminal_output.tag_configure("nerijeseno", foreground="cyan", font=("Consolas", 11, "bold")) # Svijetloplavi, podebljani tekst za neriješeno
terminal_output.tag_configure("info", foreground="lightgray") # Svijetlosivi tekst za općenite informacije
terminal_output.tag_configure("naslov", foreground="gold", font=("Consolas", 12, "bold")) # Zlatni, veći i podebljani tekst za naslove/važne poruke
terminal_output.tag_configure("zute_zvjezdice", foreground="yellow", font=("Consolas", 11, "bold")) # Tag samo za žute, podebljane zvjezdice

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
    add_message_to_terminal(full_intro_message, tag="naslov") 
    update_score_display()

    root.after(5000, clear_terminal_and_start_game)

def clear_terminal_and_end_game():
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END)
    terminal_output.config(state=tk.DISABLED)

def clear_terminal_and_start_game():
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END)
    terminal_output.config(state=tk.DISABLED)

    add_message_to_terminal("****************************************\n", tag="naslov")
    add_message_to_terminal(" Spremni za igru! Odaberite svoj potez.\n", tag="naslov")
    add_message_to_terminal("****************************************\n", tag="naslov")
    enable_player_buttons()

# --- Pokretanje uvoda i igre pri startu aplikacije ---
start_intro_and_game()

# Pokretanje glavne petlje Tkinter aplikacije
root.mainloop()