import random
import time
import textwrap
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk # Importiramo ttk modul za modernije widgete

# --- Klasa za boje i funkcije za poruke (Sada koriste Tkinter tagove) ---
class Collors:
    # Definiramo simbole boja koje ćemo mapirati na Tkinter tagove
    HEADER = 'purple'  # ROZA
    OKBLUE = 'blue'    # PLAVA
    OKCYAN = 'cyan'    # CIAN
    OKGREEN = 'green'  # ZELENA
    WARNING = 'orange' # ZUTA (za upozorenja)
    FAIL = 'red'       # CRVENA (za greške i gubitke)
    ENDC = 'normal'    # Tag za reset boje
    BOLD = 'bold'      # Tag za bold stil
    UNDERLINE = 'underline' # Tag za podcrtano

# --- Glavna Tkinter Igra Klasa ---
class RPSGame:
    LINE_WIDTH = 42 # Fiksna širina linije za formatiranje teksta
    
    def __init__(self, master):
        self.master = master
        self.master.title("Kamen, Papir, Škare")
        self.master.geometry("600x850") # Povećana veličina prozora
        self.master.resizable(False, False)
        self.master.config(bg="#2B2B2B") # Tamna pozadina

        # Tkinter Text widget kao simulirani terminal
        self.terminal_output = scrolledtext.ScrolledText(master, wrap='word', font=("Consolas", 11),
                                                         bg="#2B2B2B", fg="white", insertbackground="white",
                                                         border=0, highlightthickness=0) # Bez obruba
        self.terminal_output.pack(padx=10, pady=10, fill='both', expand=True)
        self.terminal_output.config(state=tk.DISABLED) # Postavi na DISABLED dok ne pišemo

        # Definiranje Tkinter tagova za boje i stilove
        self._setup_tkinter_tags()

        # Progres bar
        self.progressbar_frame = tk.Frame(master, bg="#2B2B2B")
        self.progressbar_label = tk.Label(self.progressbar_frame, text="", font=("Consolas", 10), fg="white", bg="#2B2B2B")
        self.progressbar_label.pack(pady=(0, 2))
        self.progressbar = ttk.Progressbar(self.progressbar_frame, orient="horizontal", length=500, mode="determinate")
        self.progressbar.pack(fill='x', padx=5)
        self.progressbar_frame.pack_forget() # Sakrij ga na početku

        # Okvir za gumbe za igranje (kamen, papir, škare, STOP)
        self.game_choices_frame = tk.Frame(master, bg="#2B2B2B")
        self.rock_button = tk.Button(self.game_choices_frame, text="Kamen", 
                                      command=lambda: self._process_player_choice("kamen"),
                                      width=10, height=3, bg="#6A5ACD", fg="white", font=("Arial", 11, "bold"))
        self.paper_button = tk.Button(self.game_choices_frame, text="Papir", 
                                       command=lambda: self._process_player_choice("papir"),
                                       width=10, height=3, bg="#6A5ACD", fg="white", font=("Arial", 11, "bold"))
        self.scissors_button = tk.Button(self.game_choices_frame, text="Škare", 
                                          command=lambda: self._process_player_choice("škare"),
                                          width=10, height=3, bg="#6A5ACD", fg="white", font=("Arial", 11, "bold"))
        self.stop_button = tk.Button(self.game_choices_frame, text="STOP",
                                     command=self._stop_playing,
                                     width=10, height=3, bg="darkred", fg="white", font=("Arial", 11, "bold"))
        
        # Rasporedi gumbe u okviru za odabir poteza
        self.rock_button.pack(side='left', padx=3, pady=10)
        self.paper_button.pack(side='left', padx=3, pady=10)
        self.scissors_button.pack(side='left', padx=3, pady=10)
        self.stop_button.pack(side='left', padx=3, pady=10)
        self.game_choices_frame.pack_forget() # Sakrij na početku

        # Gumb za početak nove igre (ili nastavak nakon uvoda)
        self.start_game_button = tk.Button(master, text="Započni Novu Igru", command=self._start_game_flow,
                                            height=2, bg='green', fg='white', font=("Arial", 10, "bold"))
        self.start_game_button.pack(fill='x', padx=10, pady=(0, 10))

        # Gumb za izlaz
        self.exit_button = tk.Button(master, text="Izlaz iz Igre", command=self._exit_game,
                                      height=2, bg='red', fg='white', font=("Arial", 10, "bold"))
        self.exit_button.pack(fill='x', padx=10, pady=(0, 10))

        # Varijable stanja igre
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.game_active = False # Je li glavna petlja igre aktivna (za automatsko ponavljanje)

        # Početna poruka
        self._print_to_terminal("Dobrodošli u igru Kamen, Papir, Škare!", Collors.OKCYAN, [Collors.BOLD])
        self._print_to_terminal("Kliknite 'Započni Novu Igru' za početak.", Collors.OKCYAN)

    def _setup_tkinter_tags(self):
        """Definira tagove za boje i stilove u tk.Text widgetu."""
        self.terminal_output.tag_configure(Collors.HEADER, foreground="purple", font=("Consolas", 11, "bold"))
        self.terminal_output.tag_configure(Collors.OKBLUE, foreground="blue")
        self.terminal_output.tag_configure(Collors.OKCYAN, foreground="cyan")
        self.terminal_output.tag_configure(Collors.OKGREEN, foreground="green")
        self.terminal_output.tag_configure(Collors.WARNING, foreground="orange")
        self.terminal_output.tag_configure(Collors.FAIL, foreground="red")
        self.terminal_output.tag_configure(Collors.BOLD, font=("Consolas", 11, "bold"))
        self.terminal_output.tag_configure(Collors.UNDERLINE, underline=True)
        self.terminal_output.tag_configure(Collors.ENDC, foreground="white") # Reset to default fg

    def _print_to_terminal(self, message, color_tag=None, style_tags=None, end="\n"):
        """
        Ispisuje poruku u simulirani terminal.
        """
        self.terminal_output.config(state=tk.NORMAL)
        
        tags_to_apply = []
        if color_tag:
            tags_to_apply.append(color_tag)
        if style_tags:
            tags_to_apply.extend(style_tags)
        
        self.terminal_output.insert(tk.END, message + end, tags_to_apply)
        self.terminal_output.see(tk.END) # Scroll to the bottom
        self.terminal_output.config(state=tk.DISABLED)

    def _clear_terminal(self):
        """Briše sadržaj simuliranog terminala."""
        self.terminal_output.config(state=tk.NORMAL)
        self.terminal_output.delete(1.0, tk.END)
        self.terminal_output.config(state=tk.DISABLED)

    def _display_progressbar(self, duration, message, next_step_callback=None):
        """Prikazuje i ažurira ttk.Progressbar."""
        self.progressbar_frame.pack(fill='x', padx=10, pady=(0, 5))
        self.progressbar_label.config(text=message)
        self.progressbar['value'] = 0
        self.master.update_idletasks() # Odmah ažuriraj GUI

        start_time = time.time()
        
        def update_bar():
            elapsed_time = time.time() - start_time
            progress = (elapsed_time / duration) * 100
            
            if progress > 100:
                progress = 100

            self.progressbar['value'] = progress
            self.master.update_idletasks() # Ažuriraj bar
            
            if progress < 100:
                self.master.after(100, update_bar) # Ponavljaj animaciju
            else:
                self.progressbar_frame.pack_forget() # Sakrij bar nakon završetka
                self._print_to_terminal(f"\n{Collors.OKBLUE}{'=' * self.LINE_WIDTH}{Collors.ENDC}\n")
                if next_step_callback:
                    self.master.after(500, next_step_callback) # Pozovi sljedeći korak

        self.master.after(100, update_bar) # Pokreni prvu animaciju

    def _display_rules(self):
        """Prikazuje pravila igre."""
        self._clear_terminal()
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(f"{'Dobrodošli u igru Kamen, Papir, Škare!':^{self.LINE_WIDTH}}", Collors.HEADER)
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal("Ovo je jednostavna igra u kojoj se možeš", Collors.OKCYAN)
        self._print_to_terminal("igrati protiv računala.", Collors.OKCYAN)
        self._print_to_terminal(f"----------------------------------------", Collors.OKCYAN)
        self._print_to_terminal("Bit će zatraženo da odabereš svoj potez ", Collors.OKCYAN)
        self._print_to_terminal("klikom na gumb 'Kamen', 'Papir' ili 'Škare'.", Collors.OKCYAN)
        self._print_to_terminal(f"----------------------------------------", Collors.OKCYAN)
        self._print_to_terminal("Računalo će odabrati jednu od tri opcije.", Collors.OKCYAN)
        self._print_to_terminal(f"----------------------------------------", Collors.OKCYAN)
        self._print_to_terminal("Pobjednik se određuje na temelju pravila.", Collors.OKCYAN)
        self._print_to_terminal(f"----------------------------------------", Collors.OKCYAN)
        self._print_to_terminal("Možeš igrati dok ne odlučiš izaći.", Collors.OKCYAN)
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(f"{'Pravila:':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(" 1.) Kamen udara škare,", Collors.OKCYAN)
        self._print_to_terminal(" 2.) Škare režu papir,", Collors.OKCYAN)
        self._print_to_terminal(" 3.) Papir pokriva kamen.", Collors.OKCYAN)
        self._print_to_terminal(f"----------------------------------------", Collors.OKCYAN)
        self._print_to_terminal(" 4.) Ako oba igrača odaberu istu opciju,", Collors.OKCYAN)
        self._print_to_terminal("     izjednačeno je.", Collors.OKCYAN)
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(f"{'Sretno!':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        
        self.start_game_button.config(text="Započni Rundu", command=self._start_round, state=tk.NORMAL)
        self._print_to_terminal("\nKliknite 'Započni Rundu' za početak prve runde.", Collors.OKCYAN)


    def _start_game_flow(self):
        """Pokreće sekvencu početka igre (progres bar -> pravila)."""
        self._clear_terminal()
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.game_active = True # Postavljamo da je igra aktivna
        self.start_game_button.config(state=tk.DISABLED) # Onemogući start gumb dok se ne završi uvod
        self.exit_button.config(state=tk.DISABLED) # Onemogući exit gumb

        self._display_progressbar(3, "Učitavam igru ...", self._display_rules)

    def _start_round(self):
        """Započinje novu rundu igre."""
        self._clear_terminal()
        self._update_score_display()
        self._print_to_terminal("Odaberite svoj potez:", Collors.HEADER)
        
        # Prikazivanje i omogućavanje gumba za odabir poteza i STOP
        self.game_choices_frame.pack(fill='x', padx=10, pady=5)
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL) # Omogući i STOP gumb

        # Onemogući gumb za start/nastavak dok se ne odabere potez
        self.start_game_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.NORMAL) # Omogući exit

    def _stop_playing(self):
        """Zaustavlja automatsko ponavljanje igre i prikazuje finalne rezultate."""
        self.game_active = False # Postavi da igra više nije aktivna
        self._print_to_terminal("\nOdabrali ste STOP. Prikazujem ukupne rezultate...", Collors.WARNING, [Collors.BOLD])
        
        # Onemogući sve gumbe za igru
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        self.game_choices_frame.pack_forget() # Sakrij gumbe

        self.master.after(2000, self._show_final_results)

    def _update_score_display(self):
        """Ažurira prikaz bodova."""
        self._clear_terminal()
        self._print_to_terminal(f"{'Vaši bodovi:':<{self.LINE_WIDTH//2}}{self.player_score:>{self.LINE_WIDTH//2}}", Collors.OKCYAN, [Collors.BOLD])
        self._print_to_terminal(f"{'Bodovi računala:':<{self.LINE_WIDTH//2}}{self.computer_score:>{self.LINE_WIDTH//2}}", Collors.OKCYAN, [Collors.BOLD])
        self._print_to_terminal(f"{'Neriješeno:':<{self.LINE_WIDTH//2}}{self.tie_score:>{self.LINE_WIDTH//2}}", Collors.OKCYAN, [Collors.BOLD]) # Dodano neriješeno
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)

    def _process_player_choice(self, player_choice):
        """Obrada odabira igrača i logika igre."""
        if not self.game_active: return # Ne radi ništa ako igra nije aktivna

        # Onemogući gumbe za odabir dok se ne obradi potez
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED) # Onemogući i STOP dok se ne obradi potez

        options = ["kamen", "papir", "škare"]
        computer_choice = random.choice(options)

        self._update_score_display()
        self._print_to_terminal(f"Vaš odabir: {player_choice.capitalize()}", Collors.OKBLUE)
        self._print_to_terminal(f"Računalo bira: {computer_choice.capitalize()}\n", Collors.OKBLUE)
        self.master.update_idletasks() # Odmah prikaži odabire

        result_message = self._check_win(player_choice, computer_choice)

        self.master.after(1500, lambda: self._display_result_and_continue(result_message))

    def _check_win(self, player, computer):
        """Provjerava pobjednika i ažurira bodove."""
        if player == computer:
            self.tie_score += 1
            return "Nerješeno !"
        elif player == "kamen":
            if computer == "škare":
                self.player_score += 1
                return "Kamen udara škare! Pobijedili ste!"
            else:
                self.computer_score += 1
                return "Papir pokriva kamen. Izgubili ste!"
        elif player == "papir":
            if computer == "kamen":
                self.player_score += 1
                return "Papir pokriva kamen! Pobijedili ste!"
            else:
                self.computer_score += 1
                return "Škare režu papir. Izgubili ste!"
        elif player == "škare":
            if computer == "papir":
                self.player_score += 1
                return "Škare režu papir! Pobijedili ste!"
            else:
                self.computer_score += 1
                return "Kamen udara škare. Izgubili ste!"
        return "Došlo je do pogreške u logici." # Nikada ne bi trebalo doći ovdje

    def _display_result_and_continue(self, result_message):
        """Prikazuje rezultat runde i priprema za sljedeću."""
        if "Pobijedili" in result_message:
            self._print_to_terminal(result_message, Collors.OKGREEN, [Collors.BOLD])
        elif "Izgubili" in result_message:
            self._print_to_terminal(result_message, Collors.FAIL, [Collors.BOLD])
        else:
            self._print_to_terminal(result_message, Collors.OKCYAN)

        # Ako je igra aktivna (nije kliknut STOP), automatski kreni novu rundu
        if self.game_active:
            self.master.after(2000, self._start_round)
        else:
            # Ako je igra zaustavljena, prikaži finalne rezultate
            self.master.after(2000, self._show_final_results)

    def _show_final_results(self):
        """Prikazuje konačne rezultate cijele sesije."""
        self._clear_terminal()
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Kamen, Papir, Škare':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Konačan Rezultat:':^{self.LINE_WIDTH}}\n", Collors.HEADER)
        
        label_part_width_final = 20
        score_part_width_final = self.LINE_WIDTH - label_part_width_final - 4

        self._print_to_terminal(f"  Pobjede Vi:{self.player_score:>{score_part_width_final}}", Collors.OKCYAN, [Collors.BOLD, Collors.OKGREEN])
        self._print_to_terminal(f"  Računalo:{self.computer_score:>{score_part_width_final}}", Collors.OKCYAN, [Collors.BOLD, Collors.FAIL])
        self._print_to_terminal(f"  Neriješeno:{self.tie_score:>{score_part_width_final}}\n", Collors.OKCYAN, [Collors.BOLD, Collors.WARNING])
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)

        if self.player_score > self.computer_score:
            self._print_to_terminal(f"{'Čestitam na pobjedi!':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
        elif self.computer_score > self.player_score:
            self._print_to_terminal(f"{'Računalo je ukupno pobijedilo.':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
        else:
            self._print_to_terminal(f"{'Ukupan rezultat je neriješen!':^{self.LINE_WIDTH}}", Collors.OKCYAN, [Collors.BOLD])

        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Hvala na igranju !!':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        
        self.start_game_button.config(state=tk.NORMAL, text="Započni Novu Igru") # Omogući ponovni start igre
        self.exit_button.config(state=tk.NORMAL) # Omogući izlaz

        # Više ne pozivamo _final_exit_sequence automatski ovdje
        # Korisnik mora kliknuti "Započni Novu Igru" ili "Izlaz iz Igre"

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
            self.game_active = False # Prekini igru ako je bila aktivna
            self._final_exit_sequence()


# --- Glavno pokretanje igre ---
if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()