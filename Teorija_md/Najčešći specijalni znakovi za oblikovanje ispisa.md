<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Najčešći specijalni znakovi za oblikovanje ispisa u Bash-u

## ANSI escape sekvence za boje i stilove

**Struktura ANSI koda:**[^3]

```bash
\033[kod  # ili \x1b[kod
```


### Boje teksta

| Kod | Boja | Primjer |
| :-- | :-- | :-- |
| `30m` | Crna | `echo -e "\033[30mCrni tekst\033[0m"` |
| `31m` | Crvena | `echo -e "\033[31mCrveni tekst\033[0m"` |
| `32m` | Zelena | `echo -e "\033[32mZeleni tekst\033[0m"` |
| `33m` | Žuta | `echo -e "\033[33mŽuti tekst\033[0m"` |
| `34m` | Plava | `echo -e "\033[34mPlavi tekst\033[0m"` |
| `35m` | Magenta | `echo -e "\033[35mMagenta tekst\033[0m"` |
| `36m` | Cyan | `echo -e "\033[36mCyan tekst\033[0m"` |
| `37m` | Bijela | `echo -e "\033[37mBijeli tekst\033[0m"` |

### Stilovi teksta

| Kod | Stil | Primjer |
| :-- | :-- | :-- |
| `1m` | Bold (deblje) | `echo -e "\033[1mDebao tekst\033[0m"` |
| `2m` | Dim (tamnije) | `echo -e "\033[2mTaman tekst\033[0m"` |
| `3m` | Italic (koso) | `echo -e "\033[3mKoso tekst\033[0m"` |
| `4m` | Underline (podcrtano) | `echo -e "\033[4mPodcrtan tekst\033[0m"` |
| `5m` | Blink (treperi) | `echo -e "\033[5mTreperavi tekst\033[0m"` |
| `7m` | Reverse (obrnut) | `echo -e "\033[7mObrnut tekst\033[0m"` |
| `0m` | Reset (vraća na normal) | `echo -e "\033[31mCrveno\033[0mNormal"` |

## Osnovne escape sekvence za formatiranje

**Najčešće korišćene:**[^2]

```bash
\n  # Nova linija
\t  # Tab karakter
\r  # Carriage return
\b  # Backspace
\\  # Literal backslash
\"  # Literal navodnik
```


### Praktični primjeri:

```bash
echo -e "Prva linija\nDruga linija"
echo -e "Kolona1\tKolona2\tKolona3"
printf "Ime:\t%s\nGodine:\t%d\n" "Marko" 25
```


## Box Drawing znakovi za okvire

### Jednostruke linije

```bash
┌─┬─┐  # Gornji red
├─┼─┤  # Srednji red  
└─┴─┘  # Donji red
│      # Vertikalna linija
```


### Dvostruke linije

```bash
╔═╦═╗  # Gornji red
╠═╬═╣  # Srednji red
╚═╩═╝  # Donji red
║      # Vertikalna linija
```


## Kompletan praktični primjer

```bash
#!/bin/bash

# Definiranje boja
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
NC='\033[0m' # No Color

clear

# Box drawing okvir
echo -e "${WHITE}╔═══════════════════════════════════════════════════════╗"
echo -e "║              ${BOLD}DEMONSTRACIJA SPECIJALNIH ZNAKOVA${NC}${WHITE}         ║"
echo -e "╚═══════════════════════════════════════════════════════╝${NC}\n"

# Statusni indikatori s bojama
echo -e "${GREEN}✅ Uspješno izvršavanje${NC}"
echo -e "${RED}❌ Greška u sustavu${NC}"
echo -e "${YELLOW}⚠️  Upozorenje - provjeri postavke${NC}"
echo -e "${BLUE}ℹ️  Informacija: Proces je u tijeku${NC}\n"

# Formatiranje s Tab karakterima
echo -e "${CYAN}📊 SISTEMSKI PODACI:${NC}"
echo -e "Korisnik:\t${BOLD}$USER${NC}"
echo -e "Datum:\t\t${BOLD}$(date '+%d.%m.%Y')${NC}"
echo -e "Vrijeme:\t${BOLD}$(date '+%H:%M:%S')${NC}\n"

# Tablica s box drawing znakovima
echo -e "${PURPLE}┌─────────────────┬──────────┬──────────────┐${NC}"
echo -e "${PURPLE}│${NC} ${BOLD}KATEGORIJA${NC}      ${PURPLE}│${NC} ${BOLD}STATUS${NC}   ${PURPLE}│${NC} ${BOLD}VRIJEDNOST${NC}   ${PURPLE}│${NC}"
echo -e "${PURPLE}├─────────────────┼──────────┼──────────────┤${NC}"
echo -e "${PURPLE}│${NC} Memorija        ${PURPLE}│${NC} ${GREEN}✓ OK${NC}     ${PURPLE}│${NC} $(free -h | awk 'NR==2{print $3"/"$2}') ${PURPLE}│${NC}"
echo -e "${PURPLE}│${NC} Disk prostor    ${PURPLE}│${NC} ${GREEN}✓ OK${NC}     ${PURPLE}│${NC} $(df -h . | awk 'NR==2{print $4}') free ${PURPLE}│${NC}"
echo -e "${PURPLE}│${NC} Uptime          ${PURPLE}│${NC} ${GREEN}✓ OK${NC}     ${PURPLE}│${NC} $(uptime -p)     ${PURPLE}│${NC}"
echo -e "${PURPLE}└─────────────────┴──────────┴──────────────┘${NC}\n"

# Stilovi teksta
echo -e "${UNDERLINE}Različiti stilovi teksta:${NC}"
echo -e "${BOLD}• Debao tekst${NC}"
echo -e "${RED}${BOLD}• Crveno i debao${NC}"
echo -e "\033[3m• Italic tekst\033[0m"
echo -e "\033[4m• Podcrtan tekst\033[0m"
echo -e "\033[7m• Obrnut tekst\033[0m\n"

# Progress bar s specijalnim znakovima
echo -e "${CYAN}Progress:${NC}"
echo -e "████████████████████ 100%"
echo -e "▓▓▓▓▓▓▓▓░░░░░░░░░░░░  40%"
echo -e "██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒  30%\n"

# Strelice i simboli
echo -e "${WHITE}Navigacijski simboli:${NC}"
echo -e "→ Naprijed    ← Nazad    ↑ Gore    ↓ Dolje"
echo -e "➡️ Sljedeći korak    ⬅️ Prethodni korak"
echo -e "🔄 Refresh    🔍 Pretraži    ⚙️ Postavke\n"

echo -e "${GREEN}✨ Demonstracija završena uspješno!${NC}"
```


## Korisne varijable za česte boje

```bash
#!/bin/bash

# Standardne boje
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[1;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[1;37m'
export NC='\033[0m'

# Stilovi
export BOLD='\033[1m'
export DIM='\033[2m'
export UNDERLINE='\033[4m'
export BLINK='\033[5m'
export REVERSE='\033[7m'

# Funkcija za obojani ispis
colored_echo() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Korištenje
colored_echo "$GREEN" "✅ Uspješno"
colored_echo "$RED" "❌ Greška"
colored_echo "$YELLOW" "⚠️ Upozorenje"
```

Ovi specijalni znakovi omogućavaju stvaranje profesionalnih, čitljivih i vizualno privlačnih bash skripti koje pružaju bolje korisničko iskustvo.[^1][^5]

<div style="text-align: center">⁂</div>

[^1]: https://www.fer.unizg.hr/_download/repository/predavanje-01.pdf

[^2]: https://www.dhiwise.com/post/how-to-use-escape-html-in-bash-a-practical-guide

[^3]: https://www.youtube.com/watch?v=c5VNZTKY6Ys

[^4]: https://stackoverflow.com/questions/28012767/print-a-string-with-its-special-characters-printed-as-literal-escape-sequences

[^5]: https://www.fer.unizg.hr/_download/repository/shell_programiranjeB5_6.pdf

[^6]: https://unze.ba/am/cdp/pdf/Skripta PZI B5.pdf

[^7]: https://home.izum.si/izum/e-prirucnici/1_COBISS2_Katalogizacija/Ceo_1_COBISS2_Katalogizacija.pdf

[^8]: https://c2.etf.unsa.ba/file.php/300/OS_Skripta-zima2015.pdf

[^9]: https://www.scribd.com/document/553455894/Principi-Informatike-Latinovic-Nedim-2015-v-14102015-v1

[^10]: https://www.reddit.com/r/bash/comments/18ph0a5/bash_printf_formatting_accented_characters_ruin/

