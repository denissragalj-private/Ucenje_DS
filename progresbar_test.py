# import time
# from tqdm import tqdm
# import sys

# # print("\nPrimjer progress bara s opisom i ručnim ažuriranjem:")

# # # Kreiranje progress bara s ukupnim brojem iteracija i opisom
# # with tqdm(total=200, desc="Obrada podataka") as pbar:
# #     for i in range(200):
# #         # Simulacija obrade
# #         time.sleep(0.02)
# #         # Ažuriranje progress bara za 1 korak
# #         pbar.update(1)

# # print("\nSimulacija drugog primjera je završena!")

# # time.sleep(2)

import time
from tqdm import tqdm

print("Primjer jednostavnog progress bara:")

# Iteriranje kroz listu s tqdm
for i in tqdm(range(100), desc="Preuzimanje datoteka"):
    # Simulacija neke operacije koja traje kratko
    time.sleep(0.05) # Pauza od 50 milisekundi

print("\nSimulacija prvog primjera je završena!")

# # import time
# # import sys

# def jednostavni_progres_bar(trajanje_sekunde, poruka, duljina_bara_znakova=20):
#     """
#     Prikazuje osnovni progres bar u terminalu.
#     Fokus je na matematici i logici napretka.

#     Args:
#         trajanje_sekunde (float): Ukupno trajanje operacije u sekundama.
#         poruka (str): Tekstualna poruka koja se prikazuje iznad bara.
#         duljina_bara_znakova (int): Željena duljina progres bara u broju znakova.
#     """
    
#     # Znakovi za popunjeni i prazan dio bara
#     # popunjeni_znak = '█'
#     # prazan_znak = '░'
    
#     popunjeni_znak = '#'
#     prazan_znak = '.'
    


#     pocetno_vrijeme = time.time() # Bilježimo kada je operacija počela

#     # print(f"{poruka}\n") # Ispisujemo poruku iznad bara
    
#     while True:
#         # Izračunavamo koliko je vremena prošlo od početka
#         proslo_vrijeme = time.time() - pocetno_vrijeme
        
#         # Izračunavamo napredak kao decimalni broj između 0.0 i 1.0
#         # (npr. 0.5 znači 50% završeno)
#         postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

#         # Osiguravamo da postotak napretka ne pređe 1.0 (100%)
#         if postotak_napretka_decimalni >= 1.0:
#             postotak_napretka_decimalni = 1.0

#         # Izračunavamo koliko popunjenih znakova treba biti u baru
#         # npr. ako je 50% i bar je dug 20 znakova, 0.5 * 20 = 10 popunjenih znakova
#         broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
        
#         # Izračunavamo koliko praznih znakova treba biti u baru
#         # npr. ako je bar dug 20 i 10 je popunjenih, onda je 20 - 10 = 10 praznih
#         broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

#         # Sastavljamo sam progres bar: prvo popunjeni, pa prazni znakovi
#         bar_string = popunjeni_znak * broj_popunjenih_znakova + \
#                      prazan_znak * broj_praznih_znakova
        
#         # Izračunavamo postotak u cijelim brojevima za prikaz (npr. 50 umjesto 0.5)
#         postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
#         # Sastavljamo cijelu liniju za prikaz (npr. "[██████░░░░] 50%")
#         #linija_za_prikaz = f"{poruka}  [{bar_string}] {postotak_prikaz}%"
#         linija_za_prikaz = f" [{bar_string}] {postotak_prikaz} %  {poruka} "

#         # Ispisujemo liniju u terminal.
#         # '\r' vraća kursor na početak linije, tako da se prethodni ispis prepiše.
#         # 'end=''' sprječava prelazak u novi red.
#         # 'flush=True' osigurava da se ispis odmah vidi.
#         sys.stdout.write(f"\r{linija_za_prikaz}")
#         sys.stdout.flush()

#         # Ako je napredak 100%, izlazimo iz petlje
#         if postotak_napretka_decimalni >= 1.0:
#             break

#         time.sleep(0.1) # Pauza od 0.1 sekunde prije sljedećeg ažuriranja

#     sys.stdout.write('\n') # Nakon što bar završi, prelazimo u novi red
#     time.sleep(0.5) # Kratka pauza za kraj

# # --- Primjer korištenja ---
# print("--- Početak pojednostavljene simulacije ---")
# jednostavni_progres_bar(trajanje_sekunde=8, poruka="Obrada datoteka...", duljina_bara_znakova=30)
# time.sleep(2)
# jednostavni_progres_bar(trajanje_sekunde=3, poruka="Spremanje podataka...", duljina_bara_znakova=15)
# print("--- Kraj pojednostavljene simulacije ---")

# import time
# import sys

# # Klasa za ANSI escape kodove boja
# class Boje:
#     ZELENA = '\033[92m'  # Svijetlo zelena
#     PLAVA = '\033[94m'   # Svijetlo plava
#     CRVENA = '\033[91m'  # Crvena
#     ZUTA = '\033[93m'    # Žuta
#     KRAJ = '\033[0m'     # Resetira boju na zadanu terminalsku (vrlo važno!)

# def jednostavni_progres_bar(trajanje_sekunde, poruka, duljina_bara_znakova=20, boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA):
#     """
#     Prikazuje osnovni progres bar u terminalu s dodanim bojama.

#     Args:
#         trajanje_sekunde (float): Ukupno trajanje operacije u sekundama.
#         poruka (str): Tekstualna poruka koja se prikazuje uz bar.
#         duljina_bara_znakova (int): Željena duljina progres bara u broju znakova.
#         boja_bara (str): ANSI escape kod za boju popunjenog dijela bara.
#         boja_poruke (str): ANSI escape kod za boju poruke.
#     """
    
#     # popunjeni_znak = '#'
#     # prazan_znak = '.'
#     popunjeni_znak = '█'
#     prazan_znak = '░'


#     pocetno_vrijeme = time.time() 
    
#     while True:
#         proslo_vrijeme = time.time() - pocetno_vrijeme
#         postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

#         if postotak_napretka_decimalni >= 1.0:
#             postotak_napretka_decimalni = 1.0

#         broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
#         broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

#         # Bar sada ima boju! Dodajemo boju_bara na početak, i KRAJ na kraj bara
#         bar_string = boja_bara + popunjeni_znak * broj_popunjenih_znakova + \
#                      prazan_znak * broj_praznih_znakova + Boje.KRAJ
        
#         postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
#         # Poruka također ima boju!
#         linija_za_prikaz = f" [{bar_string}] {postotak_prikaz} %  {boja_poruke}{poruka}{Boje.KRAJ} "

#         sys.stdout.write(f"\r{linija_za_prikaz}")
#         sys.stdout.flush()

#         if postotak_napretka_decimalni >= 1.0:
#             break

#         time.sleep(0.1) 

#     sys.stdout.write('\n')
#     time.sleep(0.5)

# # --- Primjer korištenja s bojama ---
# print("--- Početak simulacije s bojama ---")
# jednostavni_progres_bar(trajanje_sekunde=8, poruka="Instalacija programa...", duljina_bara_znakova=30, boja_bara=Boje.ZUTA, boja_poruke=Boje.CRVENA)
# time.sleep(1) 
# jednostavni_progres_bar(trajanje_sekunde=5, poruka="Provjera ažuriranja...", duljina_bara_znakova=25, boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA)
# time.sleep(1)
# jednostavni_progres_bar(trajanje_sekunde=3, poruka="Pokretanje sustava...", duljina_bara_znakova=15, boja_bara=Boje.CRVENA, boja_poruke=Boje.ZUTA)

# print("--- Kraj simulacije s bojama ---")

# import time
# import sys

# # Klasa za ANSI escape kodove boja
# class Boje:
#     ZELENA = '\033[92m'  # Svijetlo zelena
#     PLAVA = '\033[94m'   # Svijetlo plava
#     CRVENA = '\033[91m'  # Crvena
#     ZUTA = '\033[93m'    # Žuta
#     KRAJ = '\033[0m'     # Resetira boju na zadanu terminalsku (vrlo važno!)

# # ANSI escape kod za brisanje od kursora do kraja ekrana
# CLEAR_SCREEN_FROM_CURSOR = '\033[0J'
# # ANSI escape kod za brisanje trenutne linije
# CLEAR_LINE = '\033[2K'
# # ANSI escape kod za pomicanje kursora gore za N linija
# CURSOR_UP_N = '\033[1A' 

# def napredniji_progres_bar(trajanje_sekunde, poruka, duljina_bara_znakova=20, 
#                            boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA, 
#                            tekst_ispod_bara="Dodatne informacije..."):
#     """
#     Prikazuje progres bar s tekstom ispod njega.

#     Args:
#         trajanje_sekunde (float): Ukupno trajanje operacije u sekundama.
#         poruka (str): Tekstualna poruka koja se prikazuje uz bar (prva linija).
#         duljina_bara_znakova (int): Željena duljina progres bara u broju znakova.
#         boja_bara (str): ANSI escape kod za boju popunjenog dijela bara.
#         boja_poruke (str): ANSI escape kod za boju poruke.
#         tekst_ispod_bara (str): Tekst koji se prikazuje ispod progres bara.
#                                  Može se mijenjati dinamički.
#     """
    
#     popunjeni_znak = '#'
#     prazan_znak = '.'
    
#     pocetno_vrijeme = time.time() 

#     # Početni ispis praznih linija kako bismo osigurali prostor za buduća ažuriranja
#     # Ovo je važno da se ne bi prebrisao tekst iznad bara u terminalu
#     print("\n\n") # 2 nova reda: 1 za bar, 1 za tekst ispod bara

#     while True:
#         proslo_vrijeme = time.time() - pocetno_vrijeme
#         postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

#         if postotak_napretka_decimalni >= 1.0:
#             postotak_napretka_decimalni = 1.0

#         broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
#         broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

#         bar_string = boja_bara + popunjeni_znak * broj_popunjenih_znakova + \
#                      prazan_znak * broj_praznih_znakova + Boje.KRAJ
        
#         postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
#         # Sastavljamo gornju liniju: bar + postotak + poruka
#         gornja_linija = f" [{bar_string}] {postotak_prikaz} %  {boja_poruke}{poruka}{Boje.KRAJ} "
        
#         # Sastavljamo donju liniju: dodatni tekst ispod bara
#         donja_linija = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}" # Dodajemo boju i za ovaj tekst

#         # --- Ažuriranje prikaza ---
#         # 1. Pomakni kursor 2 linije gore (jer imamo 2 linije za bar i tekst ispod)
#         sys.stdout.write(CURSOR_UP_N * 2) 
#         # 2. Obriši gornju liniju i ispiši novu gornju liniju
#         sys.stdout.write(CLEAR_LINE + gornja_linija + '\n') 
#         # 3. Obriši donju liniju i ispiši novu donju liniju
#         sys.stdout.write(CLEAR_LINE + donja_linija + '\n') 
#         sys.stdout.flush()

#         if postotak_napretka_decimalni >= 1.0:
#             break

#         time.sleep(0.1) 

#     # Nakon završetka, osiguraj da je kursor na novoj liniji i ispiši "Završeno!"
#     sys.stdout.write(f"Operacija '{poruka}' završena!\n")
#     sys.stdout.flush() # ISPRAVLJENO: time.stdout.flush() -> sys.stdout.flush()
#     time.sleep(0.5)

# # --- Primjer korištenja s tekstom ispod bara ---
# print("--- Početak simulacije s dodatnim tekstom ---")

# napredniji_progres_bar(trajanje_sekunde=10, 
#                        poruka="Preuzimanje datoteke A", 
#                        duljina_bara_znakova=40, 
#                        boja_bara=Boje.CRVENA, 
#                        boja_poruke=Boje.ZELENA,
#                        tekst_ispod_bara="Provjeravam vezu...")
# time.sleep(1)

# # Možeš čak i dinamički mijenjati tekst ispod bara u petlji ako želiš
# print("\n--- Pokretanje složene obrade ---")
# for korak in range(1, 4):
#     trenutni_tekst = f"Procesiranje koraka {korak}/3... Pripremam podatke."
#     if korak == 2:
#         trenutni_tekst = f"Procesiranje koraka {korak}/3... Izračunavam algoritam."
#     elif korak == 3:
#         trenutni_tekst = f"Procesiranje koraka {korak}/3... Optimiziram rezultate."

#     napredniji_progres_bar(trajanje_sekunde=3, # Kraće trajanje po koraku
#                            poruka=f"Složena obrada - Korak {korak}", 
#                            duljina_bara_znakova=30, 
#                            boja_bara=Boje.PLAVA, 
#                            boja_poruke=Boje.ZUTA,
#                            tekst_ispod_bara=trenutni_tekst)
#     time.sleep(0.5) # Kratka pauza između "koraka"

# print("--- Kraj simulacije s dodatnim tekstom ---")

# import time
# import sys

# # Klasa za ANSI escape kodove boja (prethodno definirana)
# class Boje:
#     ZELENA = '\033[92m'
#     PLAVA = '\033[94m'
#     CRVENA = '\033[91m'
#     ZUTA = '\033[93m'
#     KRAJ = '\033[0m'

# CLEAR_LINE = '\033[2K'
# CURSOR_UP_N = '\033[1A' 

# def napredniji_progres_bar(trajanje_sekunde, poruka, duljina_bara_znakova=20, 
#                            boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA, 
#                            tekst_ispod_bara=""): # Postavi default prazan string ako nema teksta
    
#     popunjeni_znak = '#'
#     prazan_znak = '.'
    
#     pocetno_vrijeme = time.time() 

#     # Osiguraj dovoljno praznih linija na početku za cijeli widget
#     sys.stdout.write("\n\n") 
#     sys.stdout.flush()

#     while True:
#         proslo_vrijeme = time.time() - pocetno_vrijeme
#         postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

#         if postotak_napretka_decimalni >= 1.0:
#             postotak_napretka_decimalni = 1.0

#         broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
#         broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

#         bar_string = boja_bara + popunjeni_znak * broj_popunjenih_znakova + \
#                      prazan_znak * broj_praznih_znakova + Boje.KRAJ
        
#         postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
#         gornja_linija = f" [{bar_string}] {postotak_prikaz} %  {boja_poruke}{poruka}{Boje.KRAJ} "
        
#         # Donja linija sada koristi direktno vrijednost iz parametra
#         donja_linija = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}"

#         # --- Ažuriranje prikaza ---
#         sys.stdout.write(CURSOR_UP_N * 2) 
#         sys.stdout.write(CLEAR_LINE + gornja_linija + '\n') 
#         sys.stdout.write(CLEAR_LINE + donja_linija + '\n') 
#         sys.stdout.flush()

#         if postotak_napretka_decimalni >= 1.0:
#             break

#         time.sleep(0.1) 

#     sys.stdout.write(f"Operacija '{poruka}' završena!\n")
#     sys.stdout.flush()
#     time.sleep(0.5)

# # --- Primjer korištenja s razdvojenim tekstom ---
# print("--- Početak simulacije s razdvojenim tekstom ---")

# napredniji_progres_bar(trajanje_sekunde=5, 
#                        poruka="Preuzimanje datoteka", 
#                        duljina_bara_znakova=40, 
#                        boja_bara=Boje.CRVENA, 
#                        boja_poruke=Boje.ZELENA,
#                        tekst_ispod_bara="Provjeravam vezu i zauzeće mreže...")
# time.sleep(1)

# print("\n--- Pokretanje složene obrade (koraci u dva reda) ---")

# for korak in range(1, 4):
#     # Definiramo tekst za prvi red (poruku)
#     poruka_za_bar = f"Korak {korak}/3"
    
#     # Definiramo tekst za drugi red (tekst ispod bara)
#     tekst_za_ispod_bara = ""
#     if korak == 1:
#         tekst_za_ispod_bara = "Pripremam podatke."
#     elif korak == 2:
#         tekst_za_ispod_bara = "Izračunavam algoritam."
#     elif korak == 3:
#         tekst_za_ispod_bara = "Optimiziram rezultate."

#     napredniji_progres_bar(trajanje_sekunde=3, 
#                            poruka=poruka_za_bar, # Sada šaljemo samo "Korak X/3"
#                            duljina_bara_znakova=30, 
#                            boja_bara=Boje.PLAVA, 
#                            boja_poruke=Boje.ZUTA,
#                            tekst_ispod_bara=tekst_za_ispod_bara) # Ovdje ide detaljan opis koraka
#     time.sleep(0.5) 

# print("--- Kraj simulacije s razdvojenim tekstom ---")

# import time
# import sys

# # Klasa za ANSI escape kodove boja
# class Boje:
#     ZELENA = '\033[92m'
#     PLAVA = '\033[94m'
#     CRVENA = '\033[91m'
#     ZUTA = '\033[93m'
#     KRAJ = '\033[0m'

# CLEAR_LINE = '\033[2K'
# CURSOR_UP_N = '\033[1A' 

# def napredniji_progres_bar_integrirano(trajanje_sekunde, poruka, duljina_bara_znakova=20, 
#                                      boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA, 
#                                      tekst_ispod_bara="", finalna_poruka=""): # Dodan novi parametar
#     """
#     Prikazuje progres bar s tekstom ispod njega i integriranom finalnom porukom
#     koja se ažurira na istom mjestu.
#     """
    
#     popunjeni_znak = '#'
#     prazan_znak = '.'
    
#     pocetno_vrijeme = time.time() 

#     # Inicijalni ispis praznih linija za cijeli blok: bar, tekst ispod, i finalna poruka.
#     # Ako je finalna poruka uvijek prisutna nakon bara, treba nam 3 linije prostora.
#     # Ako se finalna poruka pojavljuje SAMO na kraju, onda 2 linije.
#     # Za ovu verziju, pretpostavit ćemo 3 linije (bar, tekst ispod, finalna poruka).
#     sys.stdout.write("\n\n\n") 
#     sys.stdout.flush()

#     while True:
#         proslo_vrijeme = time.time() - pocetno_vrijeme
#         postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

#         if postotak_napretka_decimalni >= 1.0:
#             postotak_napretka_decimalni = 1.0

#         broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
#         broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

#         bar_string = boja_bara + popunjeni_znak * broj_popunjenih_znakova + \
#                      prazan_znak * broj_praznih_znakova + Boje.KRAJ
        
#         postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
#         gornja_linija = f" [{bar_string}] {postotak_prikaz} %  {boja_poruke}{poruka}{Boje.KRAJ} "
#         donja_linija = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}"

#         # Finalna poruka se prikazuje samo kada je korak 100% završen
#         # Inace je prazna linija ili neka placeholder poruka.
#         # Ako je finalna_poruka proslijeđena, koristimo nju.
#         linija_finalne_poruke = ""
#         if postotak_napretka_decimalni >= 1.0:
#             linija_finalne_poruke = f"{Boje.ZELENA}{finalna_poruka}{Boje.KRAJ}"
#         else:
#             # Možemo ispisati prazan string ili neku "..." animaciju dok se ne završi
#             linija_finalne_poruke = "" # Prazna linija dok se ne završi
        
#         # --- Ažuriranje prikaza ---
#         # Pomaknemo kursor 3 linije gore (bar, tekst ispod, finalna poruka)
#         sys.stdout.write(CURSOR_UP_N * 3) 
#         sys.stdout.write(CLEAR_LINE + gornja_linija + '\n') 
#         sys.stdout.write(CLEAR_LINE + donja_linija + '\n') 
#         sys.stdout.write(CLEAR_LINE + linija_finalne_poruke + '\n') # Nova linija za finalnu poruku
#         sys.stdout.flush()

#         if postotak_napretka_decimalni >= 1.0:
#             break

#         time.sleep(0.1) 

#     # Nakon završetka bara, zadržavamo finalnu poruku na ekranu.
#     # Nema potrebe za dodatnim printom jer je već ispisana u zadnjoj iteraciji.
#     time.sleep(0.5)

# # --- Primjer korištenja s integriranom finalnom porukom ---
# print("--- Početak simulacije s razdvojenim tekstom ---")

# napredniji_progres_bar_integrirano(trajanje_sekunde=5, 
#                                    poruka="Preuzimanje datoteka", 
#                                    duljina_bara_znakova=40, 
#                                    boja_bara=Boje.CRVENA, 
#                                    boja_poruke=Boje.ZELENA,
#                                    tekst_ispod_bara="Provjeravam vezu i zauzeće mreže...",
#                                    finalna_poruka="Preuzimanje završeno!") # Dodana finalna poruka
# time.sleep(1)

# print("\n--- Pokretanje složene obrade (koraci u dva reda, obriši sve) ---")

# # Treba nam malo praznog prostora prije nego krenemo s novim blokom koraka
# # jer prethodni blok za "Preuzimanje" ima 3 linije, a print("\n---") zauzima jednu.
# # Ako ne dodamo dodatni '\n' ovdje, sljedeći blok bi se mogao preklopiti
# # s "Preuzimanje završeno!" porukom.
# print("\n") 

# for korak in range(1, 4):
#     poruka_za_bar = f"Korak {korak}/3"
    
#     tekst_za_ispod_bara = ""
#     finalna_poruka_za_korak = ""

#     if korak == 1:
#         tekst_za_ispod_bara = "Pripremam podatke."
#         finalna_poruka_za_korak = f"Korak 1/3 završen!"
#     elif korak == 2:
#         tekst_za_ispod_bara = "Izračunavam algoritam."
#         finalna_poruka_za_korak = f"Korak 2/3 završen!"
#     elif korak == 3:
#         tekst_za_ispod_bara = "Optimiziram rezultate."
#         finalna_poruka_za_korak = f"Korak 3/3 završen!"

#     napredniji_progres_bar_integrirano(trajanje_sekunde=3, 
#                                        poruka=poruka_za_bar, 
#                                        duljina_bara_znakova=30, 
#                                        boja_bara=Boje.PLAVA, 
#                                        boja_poruke=Boje.ZUTA,
#                                        tekst_ispod_bara=tekst_za_ispod_bara,
#                                        finalna_poruka=finalna_poruka_za_korak)
#     # Nema potrebe za time.sleep(0.5) ovdje, jer ga funkcija već ima na kraju

# print("--- Kraj simulacije s razdvojenim tekstom ---")


import time
import sys
import os

# Klasa za ANSI escape kodove boja
class Boje:
    ZELENA = '\033[92m'
    PLAVA = '\033[94m'
    CRVENA = '\033[91m'
    ZUTA = '\033[93m'
    KRAJ = '\033[0m'

CLEAR_LINE = '\033[2K'
CURSOR_UP_N = '\033[1A' 

def napredniji_progres_bar_integrirano(trajanje_sekunde, poruka, duljina_bara_znakova=20, 
                                     boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA, 
                                     tekst_ispod_bara="", finalna_poruka=""):
    """
    Prikazuje progres bar s tekstom ispod njega i integriranom finalnom porukom
    koja se ažurira na istom mjestu.
    Ova verzija osigurava da se kursor vrati na vrh bloka nakon završetka,
    omogućujući prebrisavanje sljedećim pozivima.
    """
    
    popunjeni_znak = '#'
    prazan_znak = '.'
    
    pocetno_vrijeme = time.time() 

    # Inicijalni ispis bloka (3 linije: bar, tekst ispod, finalna poruka).
    # Ovo se ispisuje jednom na početku funkcije.
    # Kursor će biti na dnu ove 3 linije nakon inicijalnog ispisa.
    gornja_linija_initial = f" [{boja_bara}{popunjeni_znak * 0}{prazan_znak * duljina_bara_znakova}{Boje.KRAJ}] 0 %  {boja_poruke}{poruka}{Boje.KRAJ} "
    donja_linija_initial = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}"
    linija_finalne_poruke_initial = "" # U početku prazno
    
    sys.stdout.write(gornja_linija_initial + '\n')
    sys.stdout.write(donja_linija_initial + '\n')
    sys.stdout.write(linija_finalne_poruke_initial + '\n')
    sys.stdout.flush()

    while True:
        proslo_vrijeme = time.time() - pocetno_vrijeme
        postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

        if postotak_napretka_decimalni >= 1.0:
            postotak_napretka_decimalni = 1.0

        broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
        broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

        bar_string = boja_bara + popunjeni_znak * broj_popunjenih_znakova + \
                     prazan_znak * broj_praznih_znakova + Boje.KRAJ
        
        postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
        gornja_linija = f" [{bar_string}] {postotak_prikaz} %  {boja_poruke}{poruka}{Boje.KRAJ} "
        donja_linija = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}"

        linija_finalne_poruke = ""
        if postotak_napretka_decimalni >= 1.0:
            linija_finalne_poruke = f" {Boje.ZELENA}{finalna_poruka}{Boje.KRAJ}"
        else:
            linija_finalne_poruke = ""
        
        # --- Ažuriranje prikaza ---
        # Pomakni kursor 3 linije gore da prebrišeš prethodno stanje ovog bara
        sys.stdout.write(CURSOR_UP_N * 3) 
        sys.stdout.write(CLEAR_LINE + gornja_linija + '\n') 
        sys.stdout.write(CLEAR_LINE + donja_linija + '\n') 
        sys.stdout.write(CLEAR_LINE + linija_finalne_poruke + '\n')
        sys.stdout.flush()

        if postotak_napretka_decimalni >= 1.0:
            break

        time.sleep(0.1) 

    # Nakon što bar završi, kursor je na dnu bloka od 3 linije.
    # Pomakni ga natrag gore za 3 linije, tako da sljedeća print naredba
    # ili poziv funkcije prebriše ovaj trenutni blok.
    sys.stdout.write(CURSOR_UP_N * 3) 
    sys.stdout.flush() # Osiguraj da se pozicija kursora odmah ažurira

    # Nema time.sleep(0.5) ovdje, jer će ga pozivajuća petlja obraditi između barova.

# --- Glavni blok izvršavanja ---
print("--- Početak simulacije s razdvojenim tekstom ---")

# Osigurajmo 3 prazne linije za prvi bar da se ne preklapa s zaglavljem.
sys.stdout.write('\n' * 3) 

# napredniji_progres_bar_integrirano(trajanje_sekunde=5, 
                                #    poruka="Preuzimanje datoteka", 
                                #    duljina_bara_znakova=40, 
                                #    boja_bara=Boje.CRVENA, 
                                #    boja_poruke=Boje.ZELENA,
                                #    tekst_ispod_bara="Provjeravam vezu i zauzeće mreže...",
                                #    finalna_poruka="Preuzimanje završeno!")

# Nakon što prvi bar završi, njegov sadržaj ostaje na ekranu, a kursor je na vrhu njegovog bloka.
# Moramo pomaknuti kursor ispod tog bloka da bismo ispisali sljedeće zaglavlje.
sys.stdout.write('\n' * 3) # Pomakni kursor ispod upravo završenog bara (3 linije sadržaja)
print("--- Pokretanje složene obrade (koraci u dva reda, obriši sve) ---")
sys.stdout.write('\n' * 3) # Osiguraj početni prostor za prvi bar u ovoj petlji (3 linije)

# Za petlju, svaka iteracija će prebrisati prethodnu.
broj_koraka = 5
# čišćenje ekrana
def isprazni_ekran(): ## Funkcija za čišćenje ekrana
    """
    Briše sadržaj terminala.
    Radi na Windows ('nt') i Unix/Linux/macOS sustavima.
    """
    if os.name == 'nt': # Za Windows
        _ = os.system('cls')
    else:          # Za Unix/Linux/macOS
        _ = os.system('clear')

isprazni_ekran()

for korak in range(1, broj_koraka+1):
    poruka_za_bar = f" Korak {korak}/{broj_koraka}"
    
    tekst_za_ispod_bara = ""
    finalna_poruka_za_korak = f"Korak: {korak}/{broj_koraka} uspješno dovršen! "

    if korak == 1:
        tekst_za_ispod_bara = "Pripremam podatke."
        #finalna_poruka_za_korak = f"Korak 1/3 završen!"
    elif korak == 2:
        tekst_za_ispod_bara = "Izračunavam algoritam."
        #finalna_poruka_za_korak = f"Korak 2/3 završen!"
    elif korak == 3:
        tekst_za_ispod_bara = "Optimiziram rezultate."
        #finalna_poruka_za_korak = f"Korak 3/3 završen!"
    elif korak> 3 and korak<broj_koraka:
        tekst_za_ispod_bara = f"Provodim {korak}. korak ..."
    else:
        tekst_za_ispod_bara = f"Završno zapisivanje podataka .."

    napredniji_progres_bar_integrirano(trajanje_sekunde=3, 
                                       poruka=poruka_za_bar, 
                                       duljina_bara_znakova=30,     
                                       boja_bara=Boje.PLAVA, 
                                       boja_poruke=Boje.ZUTA,
                                       tekst_ispod_bara=tekst_za_ispod_bara,
                                       finalna_poruka=finalna_poruka_za_korak)
    # Kratka pauza NAKON što bar završi, prije nego što počne sljedeći
    time.sleep(1) 

# Nakon petlje, sadržaj zadnjeg bara je na ekranu, a kursor je na vrhu njegovog bloka.
# Ispiši nove linije kako bi se završna poruka pojavila ispod zadnjeg bara.
sys.stdout.write('\n' * 3) # Pomakni kursor ispod sadržaja zadnjeg bara
print(f"\n {Boje.PLAVA}Obrada uspješno završena,{Boje.ZELENA} odrađeno koraka: {Boje.ZUTA}{korak}/{broj_koraka}.{Boje.KRAJ} ")  
print(f"\n{Boje.PLAVA}--- Kraj simulacije s razdvojenim tekstom ---{Boje.KRAJ}")
input(f"\n--- pritisni{Boje.PLAVA} enter {Boje.ZELENA} za {Boje.ZUTA}kraj{Boje.KRAJ}.\n ")

# import time
# import sys
# import os

# # Klasa za ANSI escape kodove boja
# class Boje:
#     ZELENA = '\033[92m'
#     PLAVA = '\033[94m'
#     CRVENA = '\033[91m'
#     ZUTA = '\033[93m'
#     KRAJ = '\033[0m'

# CLEAR_LINE = '\033[2K'
# CURSOR_UP_N = '\033[1A' 

# def napredniji_progres_bar_integrirano(trajanje_sekunde, poruka, duljina_bara_znakova=20, 
#                                      boja_bara=Boje.ZELENA, boja_poruke=Boje.PLAVA, 
#                                      tekst_ispod_bara="", finalna_poruka=""):
#     """
#     Prikazuje progres bar s tekstom ispod njega i integriranom finalnom porukom
#     koja se ažurira na istom mjestu.
#     Ova verzija osigurava da se kursor vrati na vrh bloka nakon završetka,
#     omogućujući prebrisavanje sljedećim pozivima.
#     """
    
#     popunjeni_znak = '#'
#     prazan_znak = '.'
    
#     pocetno_vrijeme = time.time() 

#     # Inicijalni ispis bloka (3 linije: bar, tekst ispod, finalna poruka).
#     # Ovo se ispisuje jednom na početku funkcije.
#     # Kursor će biti na dnu ove 3 linije nakon inicijalnog ispisa.
#     gornja_linija_initial = f" [{boja_bara}{popunjeni_znak * 0}{prazan_znak * duljina_bara_znakova}{Boje.KRAJ}] 0 %  {boja_poruke}{poruka}{Boje.KRAJ} "
#     donja_linija_initial = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}"
#     linija_finalne_poruke_initial = "" # U početku prazno
    
#     sys.stdout.write(gornja_linija_initial + '\n')
#     sys.stdout.write(donja_linija_initial + '\n')
#     sys.stdout.write(linija_finalne_poruke_initial + '\n')
#     sys.stdout.flush()

#     while True:
#         proslo_vrijeme = time.time() - pocetno_vrijeme
#         postotak_napretka_decimalni = proslo_vrijeme / trajanje_sekunde

#         if postotak_napretka_decimalni >= 1.0:
#             postotak_napretka_decimalni = 1.0

#         broj_popunjenih_znakova = int(duljina_bara_znakova * postotak_napretka_decimalni)
#         broj_praznih_znakova = duljina_bara_znakova - broj_popunjenih_znakova

#         bar_string = boja_bara + popunjeni_znak * broj_popunjenih_znakova + \
#                      prazan_znak * broj_praznih_znakova + Boje.KRAJ
        
#         postotak_prikaz = int(postotak_napretka_decimalni * 100)
        
#         gornja_linija = f" [{bar_string}] {postotak_prikaz} %  {boja_poruke}{poruka}{Boje.KRAJ} "
#         donja_linija = f" {Boje.ZUTA}{tekst_ispod_bara}{Boje.KRAJ}"

#         linija_finalne_poruke = ""
#         if postotak_napretka_decimalni >= 1.0:
#             linija_finalne_poruke = f" {Boje.ZELENA}{finalna_poruka}{Boje.KRAJ}"
#         else:
#             linija_finalne_poruke = ""
        
#         # --- Ažuriranje prikaza ---
#         # Pomakni kursor 3 linije gore da prebrišeš prethodno stanje ovog bara
#         sys.stdout.write(CURSOR_UP_N * 3) 
#         sys.stdout.write(CLEAR_LINE + gornja_linija + '\n') 
#         sys.stdout.write(CLEAR_LINE + donja_linija + '\n') 
#         sys.stdout.write(CLEAR_LINE + linija_finalne_poruke + '\n')
#         sys.stdout.flush()

#         if postotak_napretka_decimalni >= 1.0:
#             break

#         time.sleep(0.1) 

#     # Nakon što bar završi, kursor je na dnu bloka od 3 linije.
#     # Pomakni ga natrag gore za 3 linije, tako da sljedeća print naredba
#     # ili poziv funkcije prebriše ovaj trenutni blok.
#     sys.stdout.write(CURSOR_UP_N * 3) 
#     sys.stdout.flush() # Osiguraj da se pozicija kursora odmah ažurira

# # Funkcija za čišćenje ekrana
# def isprazni_ekran():
#     """
#     Briše sadržaj terminala.
#     Radi na Windows ('nt') i Unix/Linux/macOS sustavima.
#     """
#     if os.name == 'nt': # Za Windows
#         _ = os.system('cls')
#     else:                # Za Unix/Linux/macOS
#         _ = os.system('clear')

# # --- Glavni blok izvršavanja ---

# isprazni_ekran()

# print("--- Početak simulacije s razdvojenim tekstom ---")

# print("\n--- Pokretanje složene obrade (koraci u dva reda, obriši sve) ---\n")

# # Osiguraj 3 početne prazne linije *nakon* zaglavlja za prvi bar koji će se iscrtati.
# sys.stdout.write('\n' * 3)
# sys.stdout.flush() 

# broj_koraka = 5

# for korak in range(1, broj_koraka + 1):
#     poruka_za_bar = f" Korak {korak}/{broj_koraka}"
    
#     tekst_za_ispod_bara = "" # Ovo je varijabla koju definiraš
#     # finalna_poruka_za_korak je već dobro definirana s korak/broj_koraka
#     finalna_poruka_za_korak = f"Korak: {korak}/{broj_koraka} uspješno dovršen!"

#     if korak == 1:
#         tekst_za_ispod_bara = "Pripremam podatke."
#     elif korak == 2:
#         tekst_za_ispod_bara = "Izračunavam algoritam."
#     elif korak == 3:
#         tekst_za_ispod_bara = "Optimiziram rezultate."
#     elif korak > 3 and korak < broj_koraka: 
#         tekst_za_ispod_bara = f"Provodim {korak}. korak ..."
#     else: 
#         tekst_za_ispod_bara = f"Završno zapisivanje podataka .."

#     napredniji_progres_bar_integrirano(trajanje_sekunde=3, # Trajanje po koraku
#                                        poruka=poruka_za_bar, 
#                                        duljina_bara_znakova=30, 
#                                        boja_bara=Boje.PLAVA, 
#                                        boja_poruke=Boje.ZUTA,
#                                        tekst_ispod_bara=tekst_za_ispod_bara, # ISPRAVLJENO OVDJE!
#                                        finalna_poruka=finalna_poruka_za_korak)
#     time.sleep(1) 

# # Nakon petlje, kursor je na vrhu zadnjeg iscrtanog bloka.
# # Ispiši nove linije kako bi se završna poruka pojavila ispod zadnjeg bara.
# sys.stdout.write('\n' * 3) # Pomakni kursor ispod sadržaja zadnjeg bara
# sys.stdout.flush() # Osiguraj da se pozicija kursora ažurira prije završnih printova

# # Ispravljene završne poruke
# print(f"\n {Boje.PLAVA}Obrada uspješno završena,{Boje.ZELENA} odrađeno koraka: {Boje.ZUTA}{korak}/{broj_koraka}{Boje.KRAJ}.")
# print(f"\n{Boje.PLAVA}--- Kraj simulacije s razdvojenim tekstom ---{Boje.KRAJ}")
# input(f"\n--- pritisni{Boje.PLAVA} enter {Boje.ZELENA}za {Boje.ZUTA}kraj{Boje.KRAJ}.\n ")
