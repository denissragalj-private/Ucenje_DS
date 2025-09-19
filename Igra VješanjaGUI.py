import random
import time
import textwrap
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

# --- Klasa za boje i funkcije za poruke (Sada koriste Tkinter tagove) ---
class Collors:
    # Definiramo simbole boja koje ćemo mapirati na Tkinter tagove
    HEADER = 'purple'
    OKBLUE = 'blue'
    OKCYAN = 'cyan'
    OKGREEN = 'green'
    WARNING = 'orange'
    FAIL = 'red'
    ENDC = 'normal'
    BOLD = 'bold'
    UNDERLINE = 'underline'

# --- Glavna Tkinter Igra Klasa ---
class HangmanGame:
    LINE_WIDTH = 42 # Fiksna širina linije za formatiranje teksta
    MAX_ATTEMPTS = 6 # Maksimalan broj pogrešnih pokušaja (za crtež vješala)

    # ASCII ART za vješala (prošireno za sve korake)
    HANGMAN_PICS = [
        """
           -----
           |   |
               |
               |
               |
               -
        """,
        """
           -----
           |   |
           O   |
               |
               |
               -
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               -
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               -
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               -
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               -
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               -
        """
    ]

    def __init__(self, master):
        self.master = master
        self.master.title("Igra Vješala")
        self.master.geometry("600x850")
        self.master.resizable(False, False)
        self.master.config(bg="#2B2B2B")

        self.terminal_output = scrolledtext.ScrolledText(master, wrap='word', font=("Consolas", 11),
                                                         bg="#2B2B2B", fg="white", insertbackground="white",
                                                         border=0, highlightthickness=0)
        self.terminal_output.pack(padx=10, pady=10, fill='both', expand=True)
        self.terminal_output.config(state=tk.DISABLED)

        self._setup_tkinter_tags()

        self.progressbar_frame = tk.Frame(master, bg="#2B2B2B")
        self.progressbar_label = tk.Label(self.progressbar_frame, text="", font=("Consolas", 10), fg="white", bg="#2B2B2B")
        self.progressbar_label.pack(pady=(0, 2))
        self.progressbar = ttk.Progressbar(self.progressbar_frame, orient="horizontal", length=500, mode="determinate")
        self.progressbar.pack(fill='x', padx=5)
        self.progressbar_frame.pack_forget()

        # Okvir za unos slova i gumb za pogađanje
        self.input_frame = tk.Frame(master, bg="#2B2B2B")
        self.guess_label = tk.Label(self.input_frame, text="Unesite slovo:", font=("Arial", 12), fg="white", bg="#2B2B2B")
        self.guess_label.pack(side='left', padx=5)
        self.guess_entry = tk.Entry(self.input_frame, width=5, font=("Arial", 14), justify='center', bg="#3C3C3C", fg="white", insertbackground="white")
        self.guess_entry.pack(side='left', padx=5)
        self.guess_entry.bind("<Return>", lambda event: self._process_guess()) # Omogući Enter za unos
        self.guess_button = tk.Button(self.input_frame, text="Pogodi Slovo", command=self._process_guess,
                                        width=15, height=2, bg="#6A5ACD", fg="white", font=("Arial", 10, "bold"))
        self.guess_button.pack(side='left', padx=5)
        self.input_frame.pack_forget() # Sakrij na početku

        # Okvir za opcije "Igraj Još" / "Kraj Sesije"
        self.session_end_frame = tk.Frame(master, bg="#2B2B2B")
        self.play_another_round_button = tk.Button(self.session_end_frame, text="Igraj Još", 
                                                    command=self._start_new_game,
                                                    width=15, height=2, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.end_session_button = tk.Button(self.session_end_frame, text="Kraj Sesije", 
                                             command=self._show_session_results,
                                             width=15, height=2, bg="orange", fg="white", font=("Arial", 10, "bold"))
        self.play_another_round_button.pack(side='left', expand=True, padx=5, pady=5)
        self.end_session_button.pack(side='left', expand=True, padx=5, pady=5)
        self.session_end_frame.pack_forget()


        self.start_game_button = tk.Button(master, text="Započni Novu Igru", command=self._start_game_flow,
                                            height=2, bg='green', fg='white', font=("Arial", 10, "bold"))
        self.start_game_button.pack(fill='x', padx=10, pady=(0, 10))

        self.exit_button = tk.Button(master, text="Izlaz iz Igre", command=self._exit_game,
                                      height=2, bg='red', fg='white', font=("Arial", 10, "bold"))
        self.exit_button.pack(fill='x', padx=10, pady=(0, 10))

        # --- VARIJABLE STANJA IGRE VJEŠALA ---
        self.word_list = ["programiranje", "racunalo", "tipkovnica", "mis", "monitor", "algoritam", "varijabla", "funkcija", "petlja", "klasa", "internet", "softver", "hardver", "koder", "razvoj"]
        self.secret_word = ""
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.current_display_word = ""
        self.game_active = False # Zastavica za aktivnost runde

        # --- UKUPNI REZULTATI SESIJE ---
        self.total_wins = 0
        self.total_losses = 0

        self._print_to_terminal("Dobrodošli u igru Vješala!", Collors.OKCYAN, [Collors.BOLD])
        self._print_to_terminal("Kliknite 'Započni Novu Igru' za početak.", Collors.OKCYAN)

    # --- METODE ZA ISPIS, ČIŠĆENJE TERMINALA, PROGRESS BAR (ISTE KAO PRIJE) ---
    def _setup_tkinter_tags(self):
        self.terminal_output.tag_configure(Collors.HEADER, foreground="purple", font=("Consolas", 11, "bold"))
        self.terminal_output.tag_configure(Collors.OKBLUE, foreground="blue")
        self.terminal_output.tag_configure(Collors.OKCYAN, foreground="cyan")
        self.terminal_output.tag_configure(Collors.OKGREEN, foreground="green")
        self.terminal_output.tag_configure(Collors.WARNING, foreground="orange")
        self.terminal_output.tag_configure(Collors.FAIL, foreground="red")
        self.terminal_output.tag_configure(Collors.BOLD, font=("Consolas", 11, "bold"))
        self.terminal_output.tag_configure(Collors.UNDERLINE, underline=True)
        self.terminal_output.tag_configure(Collors.ENDC, foreground="white")

    def _print_to_terminal(self, message, color_tag=None, style_tags=None, end="\n"):
        self.terminal_output.config(state=tk.NORMAL)
        tags_to_apply = []
        if color_tag: tags_to_apply.append(color_tag)
        if style_tags: tags_to_apply.extend(style_tags)
        self.terminal_output.insert(tk.END, message + end, tags_to_apply)
        self.terminal_output.see(tk.END)
        self.terminal_output.config(state=tk.DISABLED)

    def _clear_terminal(self):
        self.terminal_output.config(state=tk.NORMAL)
        self.terminal_output.delete(1.0, tk.END)
        self.terminal_output.config(state=tk.DISABLED)

    def _display_progressbar(self, duration, message, next_step_callback=None):
        self.progressbar_frame.pack(fill='x', padx=10, pady=(0, 5))
        self.progressbar_label.config(text=message)
        self.progressbar['value'] = 0
        self.master.update_idletasks()

        start_time = time.time()
        def update_bar():
            elapsed_time = time.time() - start_time
            progress = (elapsed_time / duration) * 100
            if progress > 100: progress = 100
            self.progressbar['value'] = progress
            self.master.update_idletasks()
            if progress < 100:
                self.master.after(100, update_bar)
            else:
                self.progressbar_frame.pack_forget()
                self._print_to_terminal(f"\n{Collors.OKBLUE}{'=' * self.LINE_WIDTH}{Collors.ENDC}\n")
                if next_step_callback:
                    self.master.after(500, next_step_callback)
        self.master.after(100, update_bar)

    # --- LOGIKA IGRE VJEŠALA ---
    def _start_game_flow(self):
        """Pokreće sekvencu početka igre (progres bar -> pravila).
           Resetira ukupne rezultate ako je nova sesija.
        """
        self._clear_terminal()
        # Resetiraj ukupne rezultate samo ako se ponovno pokreće iz početnog stanja
        if self.start_game_button['text'] == "Započni Novu Igru":
            self.total_wins = 0
            self.total_losses = 0
        
        self.start_game_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.DISABLED)
        self._display_progressbar(3, "Pripremam igru Vješala...", self._start_new_game)

    def _start_new_game(self):
        """Resetira stanje za novu rundu i započinje igru."""
        self.session_end_frame.pack_forget() # Sakrij gumbe "Igraj Još" / "Kraj Sesije"
        
        self.secret_word = random.choice(self.word_list).lower()
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.game_active = True # Oznaka da je runda aktivna
        self._update_display()
        self.input_frame.pack(pady=10)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END) # Očisti prethodni unos
        self.guess_entry.focus_set() # Postavi fokus na input polje
        self.exit_button.config(state=tk.NORMAL)
        self.start_game_button.config(state=tk.DISABLED) # Onemogući start gumb tijekom runde


    def _update_display(self):
        """Ažurira prikaz riječi, pogođenih/promašenih slova i vješala."""
        self._clear_terminal()

        # Prikaz ukupnih rezultata
        self._print_to_terminal(f"Ukupne pobjede: {self.total_wins} | Ukupni porazi: {self.total_losses}", Collors.OKBLUE, [Collors.BOLD])
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKBLUE)
        
        # Prikaz vješala
        self._print_to_terminal(self.HANGMAN_PICS[self.wrong_guesses], Collors.OKBLUE)
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)

        # Prikaz skrivene riječi
        self.current_display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                self.current_display_word += letter + " "
            else:
                self.current_display_word += "_ "
        self._print_to_terminal(f"Riječ: {self.current_display_word.strip()}", Collors.HEADER, [Collors.BOLD])
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)

        # Prikaz pokušanih slova
        tried_letters_str = ", ".join(sorted(self.guessed_letters)) if self.guessed_letters else "Nijedno"
        self._print_to_terminal(f"Pokušana slova: {tried_letters_str}", Collors.OKCYAN)
        self._print_to_terminal(f"Preostalih pokušaja: {self.MAX_ATTEMPTS - self.wrong_guesses}", Collors.OKCYAN)
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)

    def _process_guess(self):
        """Obrađuje unos slova od strane igrača."""
        if not self.game_active: return

        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END) # Očisti input polje nakon unosa

        if not guess.isalpha() or len(guess) != 1:
            self._print_to_terminal("Molimo unesite samo jedno slovo.", Collors.WARNING)
            return
        
        if guess in self.guessed_letters:
            self._print_to_terminal(f"Već ste pokušali slovo '{guess}'.", Collors.WARNING)
            return

        self.guessed_letters.append(guess)
        
        if guess in self.secret_word:
            self._print_to_terminal(f"'{guess}' je točno!", Collors.OKGREEN)
        else:
            self.wrong_guesses += 1
            self._print_to_terminal(f"'{guess}' nije u riječi. Izgubili ste jedan pokušaj.", Collors.FAIL)
        
        self.master.after(500, self._check_game_status) # Provjeri status igre nakon kratke pauze

    def _check_game_status(self):
        """Provjerava je li runda završena (pobjeda ili gubitak)."""
        self._update_display() # Ažuriraj prikaz nakon pokušaja

        # Provjeri pobjedu
        if "_" not in self.current_display_word:
            self._print_to_terminal(f"\n🎉 Čestitam! Pogodili ste riječ: '{self.secret_word.upper()}' 🎉", Collors.OKGREEN, [Collors.BOLD])
            self.total_wins += 1 # Ažuriraj ukupne pobjede
            self._end_round_options()
            return

        # Provjeri gubitak
        if self.wrong_guesses >= self.MAX_ATTEMPTS:
            self._print_to_terminal(f"\n😔 Žao mi je, ponestalo vam je pokušaja!", Collors.FAIL, [Collors.BOLD])
            self._print_to_terminal(f"Tajne riječi je bila: '{self.secret_word.upper()}'", Collors.FAIL, [Collors.BOLD])
            self.total_losses += 1 # Ažuriraj ukupne poraze
            self._end_round_options()
            return

        # Ako runda nije gotova, omogući ponovno unos
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.guess_entry.focus_set()


    def _end_round_options(self):
        """Prikazuje opcije "Igraj Još" i "Kraj Sesije" nakon završene runde."""
        self.game_active = False # Runda je gotova
        self.input_frame.pack_forget() # Sakrij input polje i gumb za pogađanje
        
        self._print_to_terminal("\nŽelite li igrati još jednu rundu ili završiti sesiju?", Collors.OKCYAN, [Collors.BOLD])
        self.session_end_frame.pack(fill='x', padx=10, pady=(0, 10))
        self.exit_button.config(state=tk.NORMAL) # Omogući izlaz

    def _show_session_results(self):
        """Prikazuje konačne rezultate cijele sesije."""
        self._clear_terminal()
        self.session_end_frame.pack_forget() # Sakrij gumbe za sesiju
        
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Igra Vješala':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Ukupni Rezultati Sesije:':^{self.LINE_WIDTH}}\n", Collors.HEADER)
        
        label_part_width_final = 20
        score_part_width_final = self.LINE_WIDTH - label_part_width_final - 4

        self._print_to_terminal(f"  Ukupne Pobjede:{self.total_wins:>{score_part_width_final}}", Collors.OKGREEN, [Collors.BOLD])
        self._print_to_terminal(f"  Ukupni Porazi:{self.total_losses:>{score_part_width_final}}\n", Collors.FAIL, [Collors.BOLD])
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)

        if self.total_wins > self.total_losses:
            self._print_to_terminal(f"{'Čestitam na ukupnoj pobjedi!':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
        elif self.total_losses > self.total_wins:
            self._print_to_terminal(f"{'Ukupno je više poraza. Bolje sreće sljedeći put!':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
        else:
            self._print_to_terminal(f"{'Sesija je završila neriješeno!':^{self.LINE_WIDTH}}", Collors.OKCYAN, [Collors.BOLD])

        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Hvala na igranju !!':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        
        # Sada nudimo opcije za novu igru (resetirajući ukupne rezultate) ili izlaz
        self.start_game_button.config(state=tk.NORMAL, text="Započni Novu Igru") # Ovo će resetirati total_wins/losses
        self.exit_button.config(state=tk.NORMAL)


    def _final_exit_sequence(self):
        """Zadnji koraci prije izlaska iz aplikacije."""
        self._clear_terminal()
        self._display_progressbar(5, "Izlazim iz programa...", self._destroy_app)

    def _destroy_app(self):
        """Zatvara Tkinter prozor."""
        self.master.destroy()

    def _exit_game(self):
        """Izlazak iz igre putem Tkinter gumba."""
        if messagebox.askyesno("Izlaz", "Želite li napustiti igru?"):
            self.game_active = False # Prekini trenutnu rundu ako je bila aktivna
            self._final_exit_sequence()


# --- Glavno pokretanje igre ---
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()