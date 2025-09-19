import random
import time
import textwrap
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk # Importiramo ttk modul za modernije widgete

# --- Klasa za boje i funkcije za poruke (Sada koriste Tkinter tagove) ---
class Collors:
    # Definiramo simbole boja koje ćemo mapirati na Tkinter tagove
    HEADER = 'purple'
    OKBLUE = 'blue'
    OKCYAN = 'cyan'
    OKGREEN = 'green'
    WARNING = 'orange'
    FAIL = 'red'
    ENDC = 'normal' # Tag za reset boje
    BOLD = 'bold'   # Tag za bold stil
    UNDERLINE = 'underline' # Tag za podcrtano

# --- Klasa Card (Globalna klasa) ---
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # Vraća string bez ANSI kodova, Game klasa će primijeniti Tkinter tagove
        return f"{self.rank['rank']} od {self.suit}"

    def get_tkinter_tag(self):
        if self.suit in ['Herc', 'Karo']:
            return 'card_red'
        else:
            return 'card_blue'

# --- Klasa Deck (Globalna klasa) ---
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Herc', 'Karo', 'Pik', 'Tref']
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank)) # Poziva globalnu klasu Card

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

# --- Klasa Hand (Globalna klasa) ---
class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
        self.value=0 # Reset value when adding cards

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21 and len(self.cards) == 2

    def display(self, parent_game, show_all_dealer_cards=False): # Dodaj parent_game argument
        if self.dealer:
            parent_game._print_to_terminal("Djeliteljeva ruka:", Collors.OKCYAN)
        else:
            parent_game._print_to_terminal("Vaša ruka:", Collors.OKCYAN)

        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack():
                parent_game._print_to_terminal("skrivena karta", Collors.OKCYAN)
            else:
                # Koristimo card.get_tkinter_tag() za boju
                parent_game._print_to_terminal(str(card), card.get_tkinter_tag())

        if not self.dealer or show_all_dealer_cards:
            parent_game._print_to_terminal(f"Vrijednost: {self.get_value()}", Collors.OKCYAN, [Collors.BOLD])


# --- Glavna Tkinter Igra Klasa ---
class TerminalGame:
    LINE_WIDTH = 42 # Fiksna širina linije za formatiranje teksta
    
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack - Terminal Simulation")
        self.master.geometry("600x800") # Povećana veličina prozora
        self.master.resizable(False, False)

        # Tkinter Text widget kao simulirani terminal
        self.terminal_output = scrolledtext.ScrolledText(master, wrap='word', font=("Consolas", 11),
                                                         bg="#2B2B2B", fg="white", insertbackground="white")
        self.terminal_output.pack(padx=10, pady=10, fill='both', expand=True)
        self.terminal_output.config(state=tk.DISABLED) # Postavi na DISABLED dok ne pišemo

        # Definiranje Tkinter tagova za boje i stilove
        self._setup_tkinter_tags()

        # Progres bar (novi element)
        self.progressbar_frame = tk.Frame(master, bg="#2B2B2B")
        self.progressbar_frame.pack(fill='x', padx=10, pady=(0, 5))
        self.progressbar_label = tk.Label(self.progressbar_frame, text="", font=("Consolas", 10), fg="white", bg="#2B2B2B")
        self.progressbar_label.pack(pady=(0, 2))
        self.progressbar = ttk.Progressbar(self.progressbar_frame, orient="horizontal", length=500, mode="determinate")
        self.progressbar.pack(fill='x', padx=5)
        self.progressbar_frame.pack_forget() # Sakrij ga na početku


        # Okvir za unos broja rundi (umjesto input_entry)
        self.round_input_frame = tk.Frame(master, bg="#2B2B2B")
        self.round_buttons_label = tk.Label(self.round_input_frame, text="Odaberite broj rundi:",
                                             font=("Consolas", 11, "bold"), fg="white", bg="#2B2B2B")
        self.round_buttons_label.pack(pady=5)
        
        self.round_buttons_frame = tk.Frame(self.round_input_frame, bg="#2B2B2B")
        self.round_buttons_frame.pack(pady=5)

        self.round_buttons = []
        for num_rounds in [1, 3, 5, 10]:
            btn = tk.Button(self.round_buttons_frame, text=str(num_rounds), 
                            command=lambda r=num_rounds: self._process_games_to_play_button(r),
                            width=5, height=2, bg="#6A5ACD", fg="white", font=("Arial", 10, "bold"))
            btn.pack(side='left', padx=5, pady=5)
            self.round_buttons.append(btn)

        # Gumbi "Da" / "Ne" za ponovnu igru (također dinamički pakirani)
        self.play_again_frame = tk.Frame(master, bg="#2B2B2B")
        self.play_again_yes_button = tk.Button(self.play_again_frame, text="Da", 
                                                command=lambda: self._process_play_again_button("da"),
                                                width=10, height=2, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.play_again_no_button = tk.Button(self.play_again_frame, text="Ne", 
                                               command=lambda: self._process_play_again_button("ne"),
                                               width=10, height=2, bg="red", fg="white", font=("Arial", 10, "bold"))

        # Okvir za gumbe igre
        self.game_button_frame = tk.Frame(master, padx=10, pady=5)
        self.game_button_frame.pack(fill='x', pady=(0,10))

        self.start_button = tk.Button(self.game_button_frame, text="Započni Novu Igru", command=self._start_new_game,
                                       height=2, bg='green', fg='white', font=("Arial", 10, "bold"))
        self.start_button.pack(side='left', expand=True, fill='x', padx=5)

        self.hit_button = tk.Button(self.game_button_frame, text="Dalje (Vuci)", command=self._hit_player,
                                     height=2, state=tk.DISABLED, bg='blue', fg='white', font=("Arial", 10, "bold"))
        self.hit_button.pack(side='left', expand=True, fill='x', padx=5)

        self.stand_button = tk.Button(self.game_button_frame, text="Stati", command=self._stand_player,
                                       height=2, state=tk.DISABLED, bg='orange', fg='white', font=("Arial", 10, "bold"))
        self.stand_button.pack(side='left', expand=True, fill='x', padx=5)
        
        self.exit_button = tk.Button(self.game_button_frame, text="Izlaz iz Igre", command=self._exit_game,
                                      height=2, bg='red', fg='white', font=("Arial", 10, "bold"))
        self.exit_button.pack(side='left', expand=True, fill='x', padx=5)

        # Varijable stanja igre
        self.game_running = False
        self.deck = None
        self.player_hand = None
        self.dealer_hand = None

        self.game_number = 0
        self.games_to_play = 0
        self.player_score = 0
        self.dealer_score = 0
        self.push_score = 0

        # Početna poruka
        self._print_to_terminal("Dobrodošli u Blackjack! Kliknite 'Započni Novu Igru'.", Collors.OKCYAN, [Collors.BOLD])

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

        # Posebni tagovi za karte
        self.terminal_output.tag_configure('card_red', foreground="red")
        self.terminal_output.tag_configure('card_blue', foreground="blue")
        self.terminal_output.tag_configure('card_normal', foreground="white")


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

    def _display_progressbar(self, duration, message):
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
                self.master.after(500, self.start_round) # Start round after progress bar

        self.master.after(100, update_bar) # Pokreni prvu animaciju

    def _prikazi_zaglavlje_igre(self):
        """Prikazuje zaglavlje igre u simuliranom terminalu."""
        self._clear_terminal()
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{f'Igra {self.game_number} od {self.games_to_play}':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)

        self._print_to_terminal(f"{'Trenutni rezultat:':^{self.LINE_WIDTH}}", Collors.OKCYAN)

        label_part_width = 15
        score_part_width = self.LINE_WIDTH - label_part_width -6

        self._print_to_terminal(f"    {'Igrač:':<{label_part_width}}{self.player_score:>{score_part_width}}", Collors.OKCYAN, [Collors.BOLD, Collors.OKGREEN])
        self._print_to_terminal(f"    {'Djelitelj:':<{label_part_width}}{self.dealer_score:>{score_part_width}}", Collors.OKCYAN, [Collors.BOLD, Collors.FAIL])
        self._print_to_terminal(f"    {'Neriješeno:':<{label_part_width}}{self.push_score:>{score_part_width}}", Collors.OKCYAN, [Collors.BOLD, Collors.WARNING])
        self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.HEADER)


    def _start_new_game(self):
        """Resetira igru i pita za broj igara."""
        self.game_number = 0
        self.player_score = 0
        self.dealer_score = 0
        self.push_score = 0
        self.game_running = False 

        self._clear_terminal()
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(f"{'Dobrodošli u Blackjack!':^{self.LINE_WIDTH}}", Collors.HEADER)
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal("Pravila igre:", Collors.OKCYAN)
        rules = [
            "1. Cilj igre je dobiti ukupnu vrijednost karata što je moguće bliža 21.",
            "2. As može biti vrijedan 1 ili 11.",
            "3. Brojevi 2 do 10 imaju vrijednost po broju.",
            "4. J, Q i K imaju vrijednost 10.",
            "5. Djelitelj mora vući dok ne dostigne vrijednost od 17.",
            "6. Ako igrač ili djelitelj dobiju Blackjack (21 s točno dvije karte), to je instant pobjeda.",
            "7. Ako igrač ili djelitelj prekorače 21, to je instant poraz.",
            "8. Ako igrač i djelitelj imaju istu vrijednost, to je izjednačeno.",
            "9. Igrač može odabrati 'Dalje' (D) za vučenje dodatne karte ili 'Stati' (S) za zadržavanje trenutne ruke."
        ]

        for rule in rules:
            self._print_to_terminal(textwrap.fill(rule, width=self.LINE_WIDTH, subsequent_indent="    "), Collors.OKCYAN)

        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)

        # Onemogući gumbe za igru dok ne počne runda
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)

        # Prikaži gumbe za odabir broja rundi
        self.round_input_frame.pack(fill='x', padx=10, pady=(0, 10))


    def _process_games_to_play_button(self, num_rounds):
        """Callback za obradu unosa broja igara putem gumba."""
        self.games_to_play = num_rounds
        self.game_running = True
        
        # Sakrij gumbe za odabir broja rundi
        self.round_input_frame.pack_forget()

        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._display_progressbar(3, "Miješam karte i pokrećem igru.")
        # start_round će se pozvati nakon progress bara

    def start_round(self):
        """Inicijalizira novu rundu igre."""
        self.game_over = False
        self.game_number += 1
        
        if self.game_number > self.games_to_play:
            self._show_final_results()
            return # Kraj svih igara

        self.deck = Deck() # Poziva globalnu klasu Deck
        self.deck.shuffle()

        self.player_hand = Hand() # Poziva globalnu klasu Hand
        self.dealer_hand = Hand(dealer=True) # Poziva globalnu klasu Hand

        self.player_hand.add_card(self.deck.deal(2))
        self.dealer_hand.add_card(self.deck.deal(2))

        self._prikazi_zaglavlje_igre()

        self.player_hand.display(self) # Proslijedi self (Game instancu)
        self.dealer_hand.display(self) # Proslijedi self (Game instancu)

        self.master.after(1500, self._check_initial_blackjack) # Kratka pauza pa provjera

    def _check_initial_blackjack(self):
        """Provjerava početni Blackjack za igrača i djelitelja."""
        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.OKCYAN)
            self._print_to_terminal(f"{'Oba igrača imaju Blackjack!':^{self.LINE_WIDTH}}", Collors.OKCYAN)
            self._print_to_terminal(f"{'Izjednačeno! ! !':^{self.LINE_WIDTH}}", Collors.OKCYAN)
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKCYAN)
            self.push_score += 1
            self.game_over = True
        elif self.player_hand.is_blackjack():
            self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.OKGREEN, [Collors.BOLD])
            self._print_to_terminal(f"{'🎉 Imate Blackjack!':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
            self._print_to_terminal(f"{'      Pobjeđujete!      🎉':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKGREEN, [Collors.BOLD])
            self.player_score += 1
            self.game_over = True
        elif self.dealer_hand.is_blackjack():
            self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.FAIL, [Collors.BOLD])
            self._print_to_terminal(f"{'Djelitelj ima Blackjack!':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
            self._print_to_terminal(f"{'  Djelitelj pobjeđuje!  ':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.FAIL, [Collors.BOLD])
            self.dealer_score += 1
            self.game_over = True
        
        if self.game_over:
            self.master.after(2000, self._end_round_actions)
        else:
            self.hit_button.config(state=tk.NORMAL)
            self.stand_button.config(state=tk.NORMAL)
            self._print_to_terminal("\nVaš potez: Kliknite 'Dalje' ili 'Stati'.", Collors.OKCYAN, [Collors.BOLD])

    def _hit_player(self):
        """Funkcija za gumb 'Dalje'."""
        if self.game_over or not self.game_running: return

        self.player_hand.add_card(self.deck.deal(1))
        
        self._prikazi_zaglavlje_igre()
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)
        self._print_to_terminal(f"{'Odabrali ste Dalje...':^{self.LINE_WIDTH}}", Collors.OKCYAN)
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)
        self.player_hand.display(self)
        self.dealer_hand.display(self)
        self.master.after(1000, self._check_player_bust)

    def _check_player_bust(self):
        if self.player_hand.get_value() > 21:
            self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.FAIL, [Collors.BOLD])
            self._print_to_terminal(f"{'😫 Prekoračili ste 21!':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
            self._print_to_terminal(f"{'  Djelitelj pobjeđuje!  😫':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
            self.dealer_score += 1
            self.game_over = True
            self.master.after(2000, self._end_round_actions) # Završi rundu nakon busta
        else:
            self._print_to_terminal("\nVaš potez: Kliknite 'Dalje' ili 'Stati'.", Collors.OKCYAN, [Collors.BOLD])


    def _stand_player(self):
        """Funkcija za gumb 'Stati'."""
        if self.game_over or not self.game_running: return

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

        self._prikazi_zaglavlje_igre()
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)
        self._print_to_terminal(f"{'Odabrali ste Stati...':^{self.LINE_WIDTH}}", Collors.OKCYAN)
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)
        self.player_hand.display(self)
        self._print_to_terminal("-" * self.LINE_WIDTH, Collors.OKCYAN)
        self.master.after(2000, self._dealer_turn)


    def _dealer_turn(self):
        """Logika djeliteljevog poteza."""
        self._print_to_terminal(f"{'Potez djelitelja...':^{self.LINE_WIDTH}}", Collors.OKCYAN)
        self.dealer_hand.display(self, show_all_dealer_cards=True)
        self.master.after(2000, self._continue_dealer_turn)

    def _continue_dealer_turn(self):
        if self.dealer_hand.get_value() < 17:
            self._print_to_terminal(f"{'Djelitelj vuče kartu...':^{self.LINE_WIDTH}}", Collors.OKCYAN)
            self.master.after(1500, lambda: self._dealer_draw_card_and_continue())
        else:
            self._check_winner()

    def _dealer_draw_card_and_continue(self):
        self.dealer_hand.add_card(self.deck.deal(1))
        self.dealer_hand.display(self, show_all_dealer_cards=True)
        self.master.after(1500, self._continue_dealer_turn)


    def _check_winner(self):
        """Provjerava pobjednika nakon što djelitelj završi potez."""
        if self.dealer_hand.get_value() > 21:
            self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.OKGREEN, [Collors.BOLD])
            self._print_to_terminal(f"{'🎉 Djelitelj je prekoračio 21!':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
            self._print_to_terminal(f"{'Pobjeđujete! 🎉':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKGREEN, [Collors.BOLD])
            self.player_score += 1
        else:
            player_value = self.player_hand.get_value()
            dealer_value = self.dealer_hand.get_value()

            if player_value > dealer_value:
                self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.OKGREEN, [Collors.BOLD])
                self._print_to_terminal(f"{'🎉 Pobjeđujete! 🎉':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
                self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKGREEN, [Collors.BOLD])
                self.player_score += 1
            elif player_value < dealer_value:
                self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.FAIL, [Collors.BOLD])
                self._print_to_terminal(f"{'Djelitelj pobjeđuje!':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
                self._print_to_terminal("*" * self.LINE_WIDTH, Collors.FAIL, [Collors.BOLD])
                self.dealer_score += 1
            else:
                self._print_to_terminal("\n" + "*" * self.LINE_WIDTH, Collors.OKCYAN, [Collors.BOLD])
                self._print_to_terminal(f"{'Izjednačeno! ! !':^{self.LINE_WIDTH}}", Collors.OKCYAN, [Collors.BOLD])
                self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKCYAN, [Collors.BOLD])
                self.push_score += 1
        
        self.game_over = True # Označi rundu kao gotovu
        self.master.after(2000, self._end_round_actions)

    def _end_round_actions(self):
        """Prikazuje rezultate runde i pita za sljedeći korak."""
        self._print_to_terminal("\n" + "=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(f"{'KONAČNI REZULTATI RUNDE':^{self.LINE_WIDTH}}", Collors.HEADER)
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)
        self._print_to_terminal(f" Vaša ruka:              {self.player_hand.get_value()}", Collors.OKCYAN, [Collors.BOLD, Collors.OKGREEN])
        self._print_to_terminal(f" Djeliteljeva ruka:      {self.dealer_hand.get_value()}", Collors.OKCYAN, [Collors.BOLD, Collors.FAIL])
        self._print_to_terminal("=" * self.LINE_WIDTH, Collors.OKBLUE)

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL) # Omogući start gumb ako je sesija završila

        self.master.after(3000, self._check_next_round_or_final_results)

    def _check_next_round_or_final_results(self):
        if self.game_number < self.games_to_play:
            # Automatski nastavi ako nije posljednja runda
            self.start_round() 
        else:
            self.master.after(100, self._show_final_results)


    def _show_final_results(self):
        """Prikazuje konačne rezultate cijele sesije."""
        self._clear_terminal()
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'B l a c k j a c k !':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Konačan Rezultat:':^{self.LINE_WIDTH}}\n", Collors.HEADER)
        label_part_width_final = 20
        score_part_width_final = self.LINE_WIDTH - label_part_width_final - 4

        self._print_to_terminal(f"  Pobjede Vi:{self.player_score:>{score_part_width_final}}", Collors.OKCYAN, [Collors.BOLD, Collors.OKGREEN])
        self._print_to_terminal(f"  Djelitelj:{self.dealer_score:>{score_part_width_final}}", Collors.OKCYAN, [Collors.BOLD, Collors.FAIL])
        self._print_to_terminal(f"  Neriješeno:{self.push_score:>{score_part_width_final}}\n", Collors.OKCYAN, [Collors.BOLD, Collors.WARNING])
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)

        if self.player_score > self.dealer_score:
            self._print_to_terminal(f"{'Čestitam na pobjedi!':^{self.LINE_WIDTH}}", Collors.OKGREEN, [Collors.BOLD])
        elif self.dealer_score > self.player_score:
            self._print_to_terminal(f"{'Djelitelj je ukupno pobijedio.':^{self.LINE_WIDTH}}", Collors.FAIL, [Collors.BOLD])
        else:
            self._print_to_terminal(f"{'Ukupan rezultat je neriješen!':^{self.LINE_WIDTH}}", Collors.OKCYAN, [Collors.BOLD])

        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._print_to_terminal(f"{'Hvala na igranju !!':^{self.LINE_WIDTH}}", Collors.OKBLUE)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        
        self.game_running = False # Označi da je igra završena
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL) # Omogući ponovni start igre
        
        self.master.after(2000, self._ask_play_again)

    def _ask_play_again(self):
        """Pita korisnika želi li ponovo igrati putem gumba."""
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKCYAN)
        self._print_to_terminal(f"\n  Želite li igrati ponovo? \n ", Collors.OKCYAN)
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.OKCYAN)

        # Prikaži gumbe "Da" i "Ne"
        self.play_again_frame.pack(fill='x', padx=10, pady=(0, 10))
        self.play_again_yes_button.pack(side='left', expand=True, padx=5, pady=5)
        self.play_again_no_button.pack(side='left', expand=True, padx=5, pady=5)


    def _process_play_again_button(self, choice):
        """Callback za obradu odabira "Da"/"Ne" za ponovnu igru putem gumba."""
        # Sakrij gumbe "Da" i "Ne"
        self.play_again_frame.pack_forget()

        if choice == "da":
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
            self._print_to_terminal(f"{' 🎉 S u p e r 🎉 ':^{self.LINE_WIDTH}}", Collors.WARNING, [Collors.BOLD])
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
            self.master.after(1500, self._start_new_game) # Ponovno pokreni igru
        elif choice == "ne":
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
            self._display_progressbar(5, "Odjavljujem se ..") # Koristi ttk.Progressbar za odjavu
            self.master.after(5000, self._final_exit_message) # Pozovi finalnu poruku pa izlaz
    
    def _final_exit_message(self):
        self._print_to_terminal(f"{'Hvala na igranju !':^{self.LINE_WIDTH}}", Collors.WARNING, [Collors.BOLD])
        self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
        self._clear_terminal() # Očisti sve prije zatvaranja
        self.master.destroy() # Zatvori Tkinter prozor i cijeli program

    def _exit_game(self):
        """Izlazak iz igre putem Tkinter gumba."""
        if messagebox.askyesno("Izlaz", "Želite li napustiti igru?"):
            self._print_to_terminal("*" * self.LINE_WIDTH, Collors.HEADER)
            self._display_progressbar(5, "Odjavljujem se ..") # Koristi ttk.Progressbar za odjavu
            self.master.after(5000, self._final_exit_message) # Pozovi finalnu poruku pa izlaz


# --- Glavno pokretanje igre ---
if __name__ == "__main__":
    root = tk.Tk()
    game = TerminalGame(root)
    root.mainloop()