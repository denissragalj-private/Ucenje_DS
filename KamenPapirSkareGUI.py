import tkinter as tk
from tkinter import messagebox
import random

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
        return "Računalo je pobijedilo! 💻"

def play_game(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    
    player_choice_label.config(text=f"Tvoj izbor: {player_choice.capitalize()}")
    computer_choice_label.config(text=f"Izbor računala: {computer_choice.capitalize()}")
    result_label.config(text=result)

# Glavni prozor
root = tk.Tk()
root.title("Papir Škare Kamen")
root.geometry("400x300")
root.resizable(False, False) # Onemogući mijenjanje veličine prozora

# Naslov
title_label = tk.Label(root, text="Odaberi svoj potez:", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Labele za prikaz izbora i rezultata
player_choice_label = tk.Label(root, text="Tvoj izbor: ", font=("Arial", 12))
player_choice_label.pack()

computer_choice_label = tk.Label(root, text="Izbor računala: ", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "italic"), fg="blue")
result_label.pack(pady=20)

# Gumbi za odabir poteza
button_frame = tk.Frame(root)
button_frame.pack()

papir_button = tk.Button(button_frame, text="Papir", width=10, height=2, command=lambda: play_game('papir'))
papir_button.grid(row=0, column=0, padx=5, pady=5)

skare_button = tk.Button(button_frame, text="Škare", width=10, height=2, command=lambda: play_game('škare'))
skare_button.grid(row=0, column=1, padx=5, pady=5)

kamen_button = tk.Button(button_frame, text="Kamen", width=10, height=2, command=lambda: play_game('kamen'))
kamen_button.grid(row=0, column=2, padx=5, pady=5)

# Pokretanje aplikacije
root.mainloop()