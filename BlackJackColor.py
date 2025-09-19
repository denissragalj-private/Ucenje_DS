import os
import random
import time
import textwrap

# --- Klasa za boje i funkcije za poruke ---
class Collors:
    HEADER = '\033[95m'    # ljubičasta boja
    OKBLUE = '\033[94m'    # plava boja
    OKCYAN = '\033[96m'    # cijan boja
    OKGREEN = '\033[92m'   # zelena boja
    WARNING = '\033[93m'   # žuta boja
    FAIL = '\033[91m'      # crvena boja
    ENDC = '\033[0m'       # reset boje
    BOLD = '\033[1m'       # bold boja
    UNDERLINE = '\033[4m'  # podcrtana boja

def info_msg(message):
    print(f"{Collors.OKCYAN}{message}{Collors.ENDC}")

def header_msg(message):
    print(f"{Collors.HEADER}{message}{Collors.ENDC}")

def header_blue(message):
    print(f"{Collors.OKBLUE}{message}{Collors.ENDC}")

def warning_msg(message):
    print(f"{Collors.WARNING}{message}{Collors.ENDC}")

def win_msg(message):
    print(f"{Collors.OKGREEN}{Collors.BOLD}{message}{Collors.ENDC}")

def lose_msg(message):
    print(f"{Collors.FAIL}{Collors.BOLD}{message}{Collors.ENDC}")

def isprazni_ekran(): ## Funkcija za čišćenje ekrana
    """
    Briše sadržaj terminala.
    Radi na Windows ('nt') i Unix/Linux/macOS sustavima.
    """
    if os.name == 'nt': # Za Windows
        _ = os.system('cls')
    else:          # Za Unix/Linux/macOS
        _ = os.system('clear')

def simple_progress_bar(duration, message, bar_length=None):
    """
    Prikazuje progres bar u terminalu koristeći ASCII kockice.
    Duljina bara se automatski prilagođava Game.LINE_WIDTH.

    Args:
        duration (float): Ukupno trajanje u sekundama za koje se prikazuje progres bar.
        message (str): Poruka koja se prikazuje iznad progres bara.
        bar_length (int, optional): Duljina progres bara u "kockicama".
                                    Ako nije definirano (None), automatski se postavlja
                                    na Game.LINE_WIDTH - 4.
    """
    filled_char = '█'
    empty_char = '░'

    if bar_length is None:
        bar_length = Game.LINE_WIDTH - 8 # Adjusted to match the new progres_bar_ds logic

    start_time = time.time()

    header_blue(f"{message:^{Game.LINE_WIDTH}}\n")

    while True:
        elapsed_time = time.time() - start_time
        progress = elapsed_time / duration

        if progress >= 1.0:
            progress = 1.0

        filled_count = int(bar_length * progress)
        bar = filled_char * filled_count + empty_char * (bar_length - filled_count)
        percentage = int(progress * 100)
        content_for_centering = f"[{bar}] {percentage}%"

        if len(content_for_centering) > Game.LINE_WIDTH:
            padding_needed = 0 # Changed from 1 to 0 for consistency
        else:
            padding_needed = (Game.LINE_WIDTH - len(content_for_centering)) // 2

        if padding_needed < 0:
            padding_needed = 0

        left_padding = " " * padding_needed
        right_padding = " " * (Game.LINE_WIDTH - len(left_padding + content_for_centering))

        print(f"\r{left_padding}{Collors.OKGREEN}{content_for_centering}{Collors.ENDC}{right_padding}", end='', flush=True)

        if progress >= 1.0:
            break

        time.sleep(0.1)
    print()
    time.sleep(0.5)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.suit in ['Herc', 'Karo']:
            return f"{Collors.FAIL}{self.rank['rank']} od {self.suit}{Collors.ENDC}"
        else:
            return f"{Collors.OKBLUE}{self.rank['rank']} od {self.suit}{Collors.ENDC}"


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
                self.cards.append(Card(suit, rank))

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

    def display(self, show_all_dealer_cards=False):
        if self.dealer:
            info_msg("Djeliteljeva ruka:")
        else:
            info_msg("Vaša ruka:")

        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack():
                info_msg("skrivena karta")
            else:
                print(card)

        if not self.dealer or show_all_dealer_cards:
            info_msg(f"Vrijednost: {Collors.BOLD}{self.get_value()}{Collors.ENDC}")

class Game:
    LINE_WIDTH = 42

    def prikazi_zaglavlje_igre(self, game_number, games_to_play, player_score, dealer_score, push_score):
        header_msg("*" * Game.LINE_WIDTH)
        header_blue(f"{f'Igra {game_number} od {games_to_play}':^{Game.LINE_WIDTH}}")
        header_msg("*" * Game.LINE_WIDTH)

        info_msg(f"{'Trenutni rezultat:':^{Game.LINE_WIDTH}}")

        label_part_width = 15
        score_part_width = Game.LINE_WIDTH - label_part_width -6

        print(f"    {Collors.OKCYAN}{f'Igrač:':<{label_part_width}}{Collors.OKGREEN}{Collors.BOLD}{player_score:>{score_part_width}}{Collors.ENDC}")
        print(f"    {Collors.OKCYAN}{f'Djelitelj:':<{label_part_width}}{Collors.FAIL}{Collors.BOLD}{dealer_score:>{score_part_width}}{Collors.ENDC}")
        print(f"    {Collors.OKCYAN}{f'Neriješeno:':<{label_part_width}}{Collors.WARNING}{Collors.BOLD}{push_score:>{score_part_width}}{Collors.ENDC}\n")

        header_msg("*" * Game.LINE_WIDTH)


    def play(self):
        while True:
            game_number = 0
            games_to_play = 0

            player_score = 0
            dealer_score = 0
            push_score = 0

            while games_to_play <= 0:
                isprazni_ekran()
                header_blue("=" * Game.LINE_WIDTH)
                header_msg(f"{'Dobrodošli u Blackjack!':^{Game.LINE_WIDTH}}")
                header_blue("=" * Game.LINE_WIDTH)
                info_msg("Pravila igre:")
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
                    info_msg(textwrap.fill(rule, width=Game.LINE_WIDTH, subsequent_indent="    "))

                header_blue("=" * Game.LINE_WIDTH)

                try:
                    print("\n" + "=" * Game.LINE_WIDTH)
                    header_msg(f"{'Koliko igara želite igrati?':^{Game.LINE_WIDTH}}")
                    print("=" * Game.LINE_WIDTH)
                    games_to_play_str = input(f"{Collors.OKCYAN}\nUnesite broj:{Collors.BOLD}{Collors.OKGREEN} ")
                    games_to_play = int(games_to_play_str)
                    print(Collors.ENDC, end='')

                    if games_to_play <= 0:
                        print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                        warning_msg(f"{'Morate unijeti broj igara za igranje.':^{Game.LINE_WIDTH}}")
                        print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                        time.sleep(2)
                    else: # <-- Dodaj 'else' blok ovdje
                        print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                        simple_progress_bar(3, "Mješam karte i pokrečem igru.")
                        print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                        time.sleep(2)
                except ValueError:
                    print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                    warning_msg(f"{'Morate unijeti broj!':^{Game.LINE_WIDTH}}")
                    print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                    games_to_play = 0
                    time.sleep(3)

            while game_number < games_to_play:
                game_number += 1
                deck = Deck()
                deck.shuffle()

                player_hand = Hand()
                dealer_hand = Hand(dealer=True)

                player_hand.add_card(deck.deal(2))
                dealer_hand.add_card(deck.deal(2))

                isprazni_ekran()
                self.prikazi_zaglavlje_igre(game_number, games_to_play, player_score, dealer_score, push_score)

                player_hand.display()
                dealer_hand.display()

                time.sleep(1.5)

                game_over = False

                if player_hand.is_blackjack() and dealer_hand.is_blackjack():
                    info_msg("\n" + "*" * Game.LINE_WIDTH)
                    info_msg(f"{'Oba igrača imaju Blackjack!':^{Game.LINE_WIDTH}}")
                    info_msg(f"{'Izjednačeno! ! !':^{Game.LINE_WIDTH}}")
                    info_msg("*" * Game.LINE_WIDTH)
                    push_score += 1
                    game_over = True
                elif player_hand.is_blackjack():
                    win_msg("\n" + "*" * Game.LINE_WIDTH)
                    win_msg(f"{'🎉 Imate Blackjack!':^{Game.LINE_WIDTH}}")
                    win_msg(f"{'     Pobjeđujete!  🎉':^{Game.LINE_WIDTH}}")
                    win_msg("*" * Game.LINE_WIDTH)
                    player_score += 1
                    game_over = True
                elif dealer_hand.is_blackjack():
                    lose_msg("\n" + "*" * Game.LINE_WIDTH)
                    lose_msg(f"{'Djelitelj ima Blackjack!':^{Game.LINE_WIDTH}}")
                    lose_msg(f"{' Djelitelj pobjeđuje!':^{Game.LINE_WIDTH}}")
                    lose_msg("*" * Game.LINE_WIDTH)
                    dealer_score += 1
                    game_over = True

                if not game_over:
                    while player_hand.get_value() < 21:
                        choice = input(f"{Collors.OKCYAN}\nŽelite li 'Dalje' (D) ili 'Stati' (S)? {Collors.BOLD}{Collors.OKGREEN}").lower()
                        print(Collors.ENDC, end='')
                        while choice not in ["d", "s", "dalje", "stati"]:
                            warning_msg(f"{'Pogrešan unos.':^{Game.LINE_WIDTH}}")
                            warning_msg(f"{'Unesite Dalje/Stati (D/S).':^{Game.LINE_WIDTH}}")
                            choice = input(f"{Collors.OKCYAN}\nŽelite li 'Dalje' (D) ili 'Stati' (S)? {Collors.BOLD}{Collors.OKGREEN}").lower()
                            print(Collors.ENDC, end='')

                        if choice in ["dalje", "d"]:
                            player_hand.add_card(deck.deal(1))
                            isprazni_ekran()
                            self.prikazi_zaglavlje_igre(game_number, games_to_play, player_score, dealer_score, push_score)
                            info_msg("-" * Game.LINE_WIDTH)
                            info_msg(f"{'Odabrali ste Dalje...':^{Game.LINE_WIDTH}}")
                            info_msg("-" * Game.LINE_WIDTH)
                            player_hand.display()
                            dealer_hand.display()
                            time.sleep(1)
                            if player_hand.get_value() > 21:
                                lose_msg("\n" + "*" * Game.LINE_WIDTH)
                                lose_msg(f"{'😫 Prekoračili ste 21!':^{Game.LINE_WIDTH}}")
                                lose_msg(f"{'   Djelitelj pobjeđuje! 😫':^{Game.LINE_WIDTH}}")
                                lose_msg("*" * Game.LINE_WIDTH)
                                dealer_score += 1
                                game_over = True
                                break
                        else:
                            break

                if not game_over:
                    isprazni_ekran()
                    self.prikazi_zaglavlje_igre(game_number, games_to_play, player_score, dealer_score, push_score)
                    info_msg("Vaša konačna ruka:")
                    player_hand.display()
                    info_msg("-" * Game.LINE_WIDTH)
                    time.sleep(2)

                    info_msg(f"{'Potez djelitelja...':^{Game.LINE_WIDTH}}")
                    dealer_hand.display(show_all_dealer_cards=True)
                    time.sleep(2)

                    while dealer_hand.get_value() < 17:
                        info_msg(f"{'Djelitelj vuče kartu...':^{Game.LINE_WIDTH}}")
                        time.sleep(1.5)
                        dealer_hand.add_card(deck.deal(1))
                        dealer_hand.display(show_all_dealer_cards=True)
                        time.sleep(1.5)

                    if dealer_hand.get_value() > 21:
                        win_msg("\n" + "*" * Game.LINE_WIDTH)
                        win_msg(f"{'🎉 Djelitelj je prekoračio 21!':^{Game.LINE_WIDTH}}")
                        win_msg(f"{'Pobjeđujete! 🎉':^{Game.LINE_WIDTH}}")
                        win_msg("*" * Game.LINE_WIDTH)
                        player_score += 1
                    else:
                        player_value = player_hand.get_value()
                        dealer_value = dealer_hand.get_value()

                        if player_value > dealer_value:
                            win_msg("\n" + "*" * Game.LINE_WIDTH)
                            win_msg(f"{'🎉 Pobjeđujete! 🎉':^{Game.LINE_WIDTH}}")
                            win_msg("*" * Game.LINE_WIDTH)
                            player_score += 1
                        elif player_value < dealer_value:
                            lose_msg("\n" + "*" * Game.LINE_WIDTH)
                            lose_msg(f"{'Djelitelj pobjeđuje!':^{Game.LINE_WIDTH}}")
                            lose_msg("*" * Game.LINE_WIDTH)
                            dealer_score += 1
                        else:
                            info_msg("\n" + "*" * Game.LINE_WIDTH)
                            info_msg(f"{'Izjednačeno! ! !':^{Game.LINE_WIDTH}}")
                            info_msg("*" * Game.LINE_WIDTH)
                            push_score += 1

                header_blue("\n" + "=" * Game.LINE_WIDTH)
                header_msg(f"{'KONAČNI REZULTATI RUNDE':^{Game.LINE_WIDTH}}")
                header_blue("=" * Game.LINE_WIDTH)
                info_msg(f" Vaša ruka:                  {Collors.OKGREEN}{Collors.BOLD}{player_hand.get_value()}{Collors.ENDC}")
                info_msg(f" Djeliteljeva ruka:          {Collors.FAIL}{Collors.BOLD}{dealer_hand.get_value()}{Collors.ENDC}")
                header_blue("=" * Game.LINE_WIDTH)

                time.sleep(3)

                info_msg("\nPritisnite Enter za sljedeće partije...")
                input()

            isprazni_ekran()
            header_msg("*" * Game.LINE_WIDTH)
            header_blue(f"{'B l a c k j a c k !':^{Game.LINE_WIDTH}}")
            header_msg("*" * Game.LINE_WIDTH)
            header_msg(f"{'Konačan Rezultat:':^{Game.LINE_WIDTH}}\n")
            label_part_width_final = 20
            score_part_width_final = Game.LINE_WIDTH - label_part_width_final - 4

            print(f"{Collors.OKCYAN}{f'  Pobjede Vi:':<{label_part_width_final}}{Collors.OKGREEN}{Collors.BOLD}{player_score:>{score_part_width_final}}{Collors.ENDC} ")
            print(f"{Collors.OKCYAN}{f'  Djelitelj:':<{label_part_width_final}}{Collors.FAIL}{Collors.BOLD}{dealer_score:>{score_part_width_final}}{Collors.ENDC} ")
            print(f"{Collors.OKCYAN}{f'  Neriješeno:':<{label_part_width_final}}{Collors.WARNING}{Collors.BOLD}{push_score:>{score_part_width_final}}{Collors.ENDC} \n")
            header_msg("*" * Game.LINE_WIDTH)

            if player_score > dealer_score:
                win_msg(f"{'Čestitam na pobjedi!':^{Game.LINE_WIDTH}}")
            elif dealer_score > player_score:
                lose_msg(f"{'Djelitelj je ukupno pobijedio.':^{Game.LINE_WIDTH}}")
            else:
                info_msg(f"{'Ukupan rezultat je neriješen!':^{Game.LINE_WIDTH}}")

            header_msg("*" * Game.LINE_WIDTH)
            header_blue(f"{'Hvala na igranju !!':^{Game.LINE_WIDTH}}")
            header_msg("*" * Game.LINE_WIDTH)

            time.sleep(2)
            info_msg("*" * Game.LINE_WIDTH)
            info_msg(f"\n  Želite li igrati ponovo? \n ")
            info_msg("*" * Game.LINE_WIDTH)

            while True:
                play_again = input(f"{Collors.OKGREEN}  Unesite 'da' ili 'ne':  ").strip().lower()
                print(Collors.ENDC, end='')

                if play_again in ["yes", "y", "da", "d"]:
                    header_msg("*" * Game.LINE_WIDTH)
                    warning_msg(f"{' 🎉 S u p e r 🎉 ':^{Game.LINE_WIDTH}}")
                    header_msg("*" * Game.LINE_WIDTH)
                    time.sleep(1.5)
                    break
                elif play_again in ["no", "n", "ne"]:
                    header_msg("*" * Game.LINE_WIDTH)
                    simple_progress_bar(5, "Odjavljujem se ..", )
                    print()    # Add a newline after the progress bar
                    warning_msg(f"{'Hvala na igranju !':^{Game.LINE_WIDTH}}")
                    header_msg("*" * Game.LINE_WIDTH)
                    time.sleep(1.5)
                    isprazni_ekran()
                    # Removed the problematic call to progres_bar_ds here
                    time.sleep(1)
                    #return # Exit the game loop
                    exit()     # Exit the program    
                    '''Exit komanda je dodana da se program ne vrati na početak, a funkcionira na Windowsu i Linuxu.'''
                                # Ako se želi da se program vrati na početak, onda se može koristiti 'return' komanda.
                                # Ako se želi da se program zatvori, onda se može koristiti 'exit()' komanda.                
                else:
                    print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                    warning_msg(f"{'Nevažeći unos. Molimo unesite (da) ili (ne).':^{Game.LINE_WIDTH}}")
                    print(f"{Collors.OKBLUE}{'=' * Game.LINE_WIDTH}{Collors.ENDC}")
                    time.sleep(2)
                    isprazni_ekran()
                    info_msg("*" * Game.LINE_WIDTH)
                    info_msg(f"\n  Želite li igrati ponovo? \n ")
                    info_msg("*" * Game.LINE_WIDTH)
                    time.sleep(1)


g = Game()
g.play()