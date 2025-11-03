<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Print naredba u Bash skriptama

**Bash nema ugrađenu `print` naredbu!** Umjesto toga koriste se **`echo`** i **`printf`** naredbe za ispis teksta.

## Printf naredba - napredna alternativa

`printf` je moćnija zamjena za `echo` koja omogućava precizno formatiranje:

### Osnovna sintaksa

```bash
printf "format_string" argumenti...
```


### Razlika između echo i printf

| Echo | Printf |
| :-- | :-- |
| Automatski dodaje novi red | Ne dodaje novi red osim ako se eksplicitno ne zatraži |
| Jednostavan za korištenje | Kompleksniji ali precizniji |
| Ograničene opcije formatiranja | Napredne opcije formatiranja |

## Printf format specifikatori

**Osnovni specifikatori:**

```bash
printf "%s\n" "tekst"        # %s = string
printf "%d\n" 42             # %d = cijeli broj
printf "%f\n" 3.14159        # %f = decimalni broj
printf "%c\n" 65             # %c = karakter (A)
```

**Preciznost i širina:**

```bash
printf "%10s\n" "tekst"      # Desno poravnano, širina 10
printf "%-10s\n" "tekst"     # Lijevo poravnano, širina 10
printf "%.2f\n" 3.14159      # 2 decimale: 3.14
printf "%05d\n" 42           # Popuni nulama: 00042
```


## Praktični primjeri printf

### Formatiranje brojeva

```bash
#!/bin/bash

BROJ=42
DECIMALA=3.14159

printf "Cijeli broj: %d\n" $BROJ
printf "Decimalni broj: %.2f\n" $DECIMALA
printf "Heksadecimalni: %x\n" $BROJ
printf "Oktal: %o\n" $BROJ

# Izlaz:
# Cijeli broj: 42
# Decimalni broj: 3.14
# Heksadecimalni: 2a
# Oktal: 52
```


### Formatiranje tablica

```bash
#!/bin/bash

printf "%-15s %-10s %8s\n" "IME" "GODINE" "PLAĆA"
printf "%-15s %-10s %8s\n" "───" "──────" "─────"
printf "%-15s %-10d %8.2f\n" "Marko Petrović" 30 5000.50
printf "%-15s %-10d %8.2f\n" "Ana Kovač" 25 4500.00
printf "%-15s %-10d %8.2f\n" "Ivo Horvat" 35 6200.75

# Izlaz:
# IME             GODINE      PLAĆA
# ───             ──────      ─────
# Marko Petrović  30        5000.50
# Ana Kovač       25        4500.00
# Ivo Horvat      35        6200.75
```


## Printf vs Echo primjer

```bash
#!/bin/bash

# Echo način
echo "Ime: $USER"
echo "Datum: $(date)"
echo ""

# Printf način
printf "Ime: %s\n" "$USER"
printf "Datum: %s\n" "$(date)"
printf "\n"

# Printf s formatiranjem
printf "Korisnik: %-20s | Datum: %s\n" "$USER" "$(date '+%d.%m.%Y')"
```


## Print u AWK skriptama

Ako koristite AWK unutar bash skripte, tada **postoji `print` naredba**:

```bash
#!/bin/bash

# AWK print naredba
awk '{print $1, $2}' file.txt

# Ili u heredoc
awk '
BEGIN { 
    print "Početak programa" 
}
{ 
    print "Linija:", NR, "Sadržaj:", $0 
}
END { 
    print "Kraj programa" 
}
' input.txt
```


## Kombiniranje printf s bojama

```bash
#!/bin/bash

# Definiranje boja
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

printf "${RED}Greška:${NC} %s\n" "Nešto je pošlo po zlu"
printf "${GREEN}Uspjeh:${NC} %s\n" "Operacija završena"
printf "${YELLOW}Upozorenje:${NC} %s\n" "Provjerite postavke"
```


## Kompletan primjer s printf

```bash
#!/bin/bash

clear

printf "\n"
printf "╔═══════════════════════════════════════════════════════╗\n"
printf "║                 SISTEMSKI IZVJEŠTAJ                  ║\n"
printf "╚═══════════════════════════════════════════════════════╝\n"
printf "\n"

printf "%-20s: %s\n" "Datum" "$(date '+%d.%m.%Y')"
printf "%-20s: %s\n" "Vrijeme" "$(date '+%H:%M:%S')"
printf "%-20s: %s\n" "Korisnik" "$USER"
printf "%-20s: %s\n" "Hostname" "$(hostname)"
printf "%-20s: %s\n" "Uptime" "$(uptime -p)"

printf "\n"
printf "Memorija korištena: %6.1f%%\n" "$(free | awk 'NR==2{printf "%.1f", $3*100/$2 }')"
printf "Disk korišten:      %6.1f%%\n" "$(df . | awk 'NR==2{print $5}' | tr -d '%')"

printf "\n"
```

**Ključno:** U bash skriptama koristite **`printf`** za precizno formatiranje umjesto nepostojeće `print` naredbe!

