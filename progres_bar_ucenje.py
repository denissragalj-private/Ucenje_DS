# Prije pokretanja, provjerite jeste li instalirali potrebne biblioteke:
# otvorite terminal/komandni redak i pokrenite:
# pip install tqdm rich

# import time
# import random
# from tqdm import tqdm
# from rich.progress import Progress

# print("--- Početak svih jednostavnih primjera progres barova ---")
# print("--------------------------------------------------\n")

# ### 1. Ugniježđeni Progres Barovi s 'tqdm'
# print("--- 1. Ugniježđeni progres barovi s 'tqdm' ---")

# # Glavna petlja (vanjski progres bar)
# for i in tqdm(range(3), desc="Ukupni proces"):
#     # Simulacija glavnog koraka
#     time.sleep(0.5) 
    
#     # Pod-petlja (unutarnji progres bar)
#     # 'leave=False' osigurava da se ovaj bar makne kada završi
#     for j in tqdm(range(5), desc=f"  Pod-proces korak {i+1}", leave=False):
#         # Simulacija pod-koraka
#         time.sleep(0.1)

# print("\nSvi ugniježđeni procesi završeni!")
# print("--------------------------------------------------\n")
# time.sleep(1) # Kratka pauza između primjera

### 2. Prilagođavanje prikaza s 'tqdm.set_postfix'
# print("--- 2. Prilagođavanje prikaza s 'tqdm.set_postfix' ---")

# total_items = 100
# processed_count = 0

# with tqdm(total=total_items, desc="Analiza podataka") as pbar:
#     for i in range(total_items):
#         # Simulacija obrade stavke
#         time.sleep(0.1)
#         processed_count += 1
        
#         # Simulacija nekog dinamičkog podatka (npr. 'brzina')
#         current_speed = random.randint(10, 50) # npr. stavki/sekundi

#         # Ažuriramo progres bar za 1 korak
#         pbar.update(1)
#         time.sleep(0.05)
#         # Ažuriramo dodatne informacije pored bara
#         pbar.set_postfix({"obradjeno": processed_count, "brzina (st/s)": current_speed})

# print("\nAnaliza podataka završena!")
# print("--------------------------------------------------\n")
# time.sleep(1) # Kratka pauza između primjera

# ### 3. Ispisivanje poruka bez ometanja bara s 'tqdm.write'
# print("--- 3. Ispisivanje poruka s 'tqdm.write' ---")

# # Standardni tqdm bar
# for i in tqdm(range(10), desc="Preuzimanje datoteke"):
#     time.sleep(0.5)
#     if i == 3:
#         # Poruka ispisana iznad bara, bez njegovog ometanja
#         tqdm.write("  --> Srednji dio preuzet (30%)...") 
#     if i == 7:
#         tqdm.write("  --> Blizu kraja, provjeravam vezu...") 
    
# print("\nPreuzimanje datoteke završeno!")
# print("--------------------------------------------------\n")
# time.sleep(1) # Kratka pauza između primjera

### 4. Jednostavan Progres Bar s 'Rich' bibliotekom
# print("--- 4. Jednostavan progress bar s 'Rich' bibliotekom ---")

# # Koristimo 'Progress' context manager za automatsko upravljanje Rich barom
# with Progress() as progress:
#     # Dodajemo "task" (zadatak) koji će predstavljati naš progres bar
#     # Možete koristiti Rich-ove tagove za boju, npr. [green]
#     task1 = progress.add_task("[green]Proračunavanje složenih podataka...", total=100)

#     for i in range(100):
#         # Ažuriramo napredak zadatka za 1 jedinicu
#         progress.update(task1, advance=1)
#         time.sleep(0.05)

# print("\nProračunavanje završeno!")
# print("--------------------------------------------------\n")

# print("--- Svi primjeri su uspješno prikazani! ---")
# input("\nPritisnite ENTER za kraj...")

# # ===============================================================


import time
import random
from tqdm import tqdm
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    MofNCompleteColumn,
    TimeElapsedColumn,   # Vraćamo TimeElapsedColumn
    TimeRemainingColumn, # Vraćamo TimeRemainingColumn
    SpinnerColumn,       
)
from rich.console import Console 

# Klasa za ANSI escape kodove boja (možete koristiti i iste kao u ranijim primjerima)
class Boje:
    ZELENA = '\033[92m'
    PLAVA = '\033[94m'
    CRVENA = '\033[91m'
    ZUTA = '\033[93m'
    MAGENTA = '\033[95m' 
    KRAJ = '\033[0m' 

print("--- Prilagođeni i obojeni progress bar s 'tqdm' i 'set_postfix' ---")

total_items = 100
processed_count = 0

with tqdm(total=total_items, 
          desc=f"{Boje.PLAVA}Analiza super-podataka{Boje.KRAJ}", 
          colour="green", 
          ascii=" #", 
          bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {percentage:3.0f}%|{postfix}", 
          ) as pbar:

    for i in range(total_items):
        time.sleep(0.1) 
        processed_count += 1
        
        current_speed = random.randint(10, 50) 

        pbar.update(1)
        
        pbar.set_postfix({
            "Obrađeno": f"{Boje.ZELENA}{processed_count}/{total_items}{Boje.KRAJ}", 
            "Brzina": f"{Boje.MAGENTA}{current_speed} st/s{Boje.KRAJ}"
        })

print(f"\n{Boje.ZELENA}Analiza podataka završena!{Boje.KRAJ}")
print("--------------------------------------------------\n")


console = Console()

def rich_napredni_primjer():
    console.print("[bold blue]--- Rich: Primjer s Višestrukim Progres Barovima i Prilagođenim Kolonama ---[/bold blue]\n")

    # --- VRAĆENA DEFINICIJA KOLONA, BEZ CUSTOM TIME KOLONE ---
    custom_progress_columns = [
        TextColumn("[progress.description]{task.description}"), 
        SpinnerColumn(),       
        BarColumn(),           
        MofNCompleteColumn(),  
        " • ",                 
        TimeElapsedColumn(),   # Ostavljamo ih ovdje, vidjet ćemo hoće li se prikazati
        "<",                   
        TimeRemainingColumn(), # Ostavljamo ih ovdje
    ]

    with Progress(
        *custom_progress_columns, 
        console=console,          
        refresh_per_second=10     
    ) as progress:
        download_task = progress.add_task(
            "[green]Preuzimanje datoteke A", 
            total=1024,                     
        )
        process_task = progress.add_task(
            "[cyan]Obrada redova podataka", 
            total=200,                      
        )
        # Spremamo originalni opis za wait_task
        original_wait_description = "[magenta]Provjera resursa (pozadinsko)..."
        wait_task = progress.add_task(
            original_wait_description, 
            total=None, 
        )
        
        # Zastavice za praćenje statusa zadataka
        download_finished = False
        process_finished = False
        wait_finished = False

        while not (download_finished and process_finished and wait_finished):
            # Ažuriranje Zadataka s Određenim Progresom
            if not download_finished: 
                download_advance = random.randint(5, 20)
                progress.update(
                    download_task, 
                    advance=download_advance, 
                )
                if progress.tasks[download_task].completed >= progress.tasks[download_task].total:
                    progress.stop_task(download_task)
                    download_finished = True 

            if not process_finished: 
                process_advance = random.randint(1, 5)
                progress.update(
                    process_task, 
                    advance=process_advance, 
                )
                if progress.tasks[process_task].completed >= progress.tasks[process_task].total:
                    progress.stop_task(process_task)
                    process_finished = True 

            # Ažuriranje Neodređenog Zadataka (Pozadinska Provjera)
            if not wait_finished: 
                elapsed_time = time.time() - progress.tasks[wait_task].start_time 
                
                # Formatiranje vremena za dodavanje u DESCRIPTION
                minutes, seconds = divmod(int(elapsed_time), 60)
                formatted_time = f"{minutes:02}:{seconds:02}"
                
                current_description = original_wait_description # Početni opis

                if elapsed_time > 3 and elapsed_time < 7:
                    current_description = "[magenta]Provjera resursa (Analiziram bazu podataka)..."
                elif elapsed_time >= 7 and elapsed_time < 10:
                    current_description = "[magenta]Provjera resursa (Provjeravam mrežnu povezanost)..."
                elif elapsed_time >= 10:
                    progress.update(wait_task, description="[bold green]Pozadinska provjera završena![/bold green]")
                    progress.stop_task(wait_task)
                    wait_finished = True 
                
                # Ažuriramo description zadatka s vremenom, ako nije završen
                if not wait_finished:
                    progress.update(wait_task, description=f"{current_description} ({formatted_time})")

            time.sleep(0.08) 

    console.print("\n[bold green]Svi glavni zadaci uspješno završeni![/bold green]")

# Poziv funkcije za pokretanje primjera
rich_napredni_primjer()

import time
import random
from tqdm import tqdm
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    MofNCompleteColumn,
    # TimeElapsedColumn,   # <-- UKLONJENO
    # TimeRemainingColumn, # <-- UKLONJENO
    SpinnerColumn,       
)
from rich.console import Console 

# Klasa za ANSI escape kodove boja
class Boje:
    ZELENA = '\033[92m'
    PLAVA = '\033[94m'
    CRVENA = '\033[91m'
    ZUTA = '\033[93m'
    MAGENTA = '\033[95m' 
    KRAJ = '\033[0m' 

print("--- Prilagođeni i obojeni progress bar s 'tqdm' i 'set_postfix' ---")

total_items = 100
processed_count = 0

with tqdm(total=total_items, 
          desc=f"{Boje.PLAVA}Analiza super-podataka{Boje.KRAJ}", 
          colour="green", 
          ascii=" #", 
          bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {percentage:3.0f}%|{postfix}", 
          ) as pbar:

    for i in range(total_items):
        time.sleep(0.1) 
        processed_count += 1
        
        current_speed = random.randint(10, 50) 

        pbar.update(1)
        
        pbar.set_postfix({
            "Obrađeno": f"{Boje.ZELENA}{processed_count}/{total_items}{Boje.KRAJ}", 
            "Brzina": f"{Boje.MAGENTA}{current_speed} st/s{Boje.KRAJ}"
        })

print(f"\n{Boje.ZELENA}Analiza podataka završena!{Boje.KRAJ}")
print("--------------------------------------------------\n")


console = Console()

def rich_napredni_primjer():
    console.print("[bold blue]--- Rich: Primjer s Višestrukim Progres Barovima i Prilagođenim Kolonama ---[/bold blue]\n")

    # --- NOVO: UKLONJENE NEPOUZDANE KOLONE ZA VRIJEME ---
    custom_progress_columns = [
        TextColumn("[progress.description]{task.description}"), 
        SpinnerColumn(),       
        BarColumn(),           
        MofNCompleteColumn(),  
        # TimeElapsedColumn i TimeRemainingColumn su uklonjeni zbog problema s rich 14.0.0
    ]

    with Progress(
        *custom_progress_columns, 
        console=console,          
        refresh_per_second=10     
    ) as progress:
        download_task = progress.add_task(
            "[green]Preuzimanje datoteke A", 
            total=1024,                     
        )
        process_task = progress.add_task(
            "[cyan]Obrada redova podataka", 
            total=200,                      
        )
        # Spremamo originalni opis za wait_task
        original_wait_description = "[magenta]Provjera resursa (pozadinsko)..."
        wait_task = progress.add_task(
            original_wait_description, 
            total=None, 
        )
        
        # Zastavice za praćenje statusa zadataka
        download_finished = False
        process_finished = False
        wait_finished = False

        while not (download_finished and process_finished and wait_finished):
            # Ažuriranje Zadataka s Određenim Progresom
            if not download_finished: 
                download_advance = random.randint(5, 20)
                progress.update(
                    download_task, 
                    advance=download_advance, 
                )
                if progress.tasks[download_task].completed >= progress.tasks[download_task].total:
                    progress.stop_task(download_task)
                    download_finished = True 

            if not process_finished: 
                process_advance = random.randint(1, 5)
                progress.update(
                    process_task, 
                    advance=process_advance, 
                )
                if progress.tasks[process_task].completed >= progress.tasks[process_task].total:
                    progress.stop_task(process_task)
                    process_finished = True 

            # Ažuriranje Neodređenog Zadataka (Pozadinska Provjera)
            if not wait_finished: 
                elapsed_time = time.time() - progress.tasks[wait_task].start_time 
                
                # Formatiranje vremena za dodavanje u DESCRIPTION
                minutes, seconds = divmod(int(elapsed_time), 60)
                formatted_time = f"{minutes:02}:{seconds:02}"
                
                current_description_base = original_wait_description # Početni opis ili ažurirani tijekom faze
                
                if elapsed_time > 3 and elapsed_time < 7:
                    current_description_base = "[magenta]Provjera resursa (Analiziram bazu podataka)..."
                elif elapsed_time >= 7 and elapsed_time < 10:
                    current_description_base = "[magenta]Provjera resursa (Provjeravam mrežnu povezanost)..."
                elif elapsed_time >= 10:
                    # Kad je zadatak gotov, promijeni opis i zaustavi
                    progress.update(wait_task, description="[bold green]Pozadinska provjera završena![/bold green]", refresh=True)
                    progress.stop_task(wait_task)
                    wait_finished = True 
                
                # Ažuriramo description zadatka s vremenom, samo ako zadatak još nije završen
                if not wait_finished:
                    progress.update(wait_task, description=f"{current_description_base} ({formatted_time})")

            time.sleep(0.08) 

    console.print("\n[bold green]Svi glavni zadaci uspješno završeni![/bold green]")

# Poziv funkcije za pokretanje primjera
rich_napredni_primjer()