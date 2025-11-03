<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Printf naredba - detaljno objašnjenje

`printf` je **formatirana ispis naredba** u Bash-u koja omogućava preciznu kontrolu nad načinom prikazivanja teksta i brojeva.

## Osnovna sintaksa

```bash
printf "format_string" argument1 argument2 ...
```

**Format string** sadrži:

- Običan tekst koji se ispisuje doslovno
- **Format specifikatore** koji počinju s `%`
- **Escape sekvence** poput `\n`, `\t`


## Format specifikatori

### Osnovni tipovi

| Specifikator | Tip podatka | Primjer |
| :-- | :-- | :-- |
| `%s` | String (tekst) | `printf "%s\n" "Pozdrav"` |
| `%d` | Decimalni broj (integer) | `printf "%d\n" 42` |
| `%f` | Floating point broj | `printf "%f\n" 3.14` |
| `%c` | Jedan karakter | `printf "%c\n" 65` → A |
| `%x` | Heksadecimalni broj | `printf "%x\n" 255` → ff |
| `%o` | Oktalni broj | `printf "%o\n" 64` → 100 |

### Praktični primjeri osnovnih tipova

```bash
#!/bin/bash

ime="Marko"
godine=25
visina=1.78

printf "Ime: %s\n" "$ime"
printf "Godine: %d\n" "$godine"
printf "Visina: %.2f m\n" "$visina"

# Izlaz:
# Ime: Marko
# Godine: 25
# Visina: 1.78 m
```


## Kontrola širine i poravnanja

### Širina polja

```bash
printf "%10s\n" "tekst"      # Desno poravnano, širina 10
printf "%-10s\n" "tekst"     # Lijevo poravnano, širina 10
printf "%010d\n" 42          # Popuni nulama: 0000000042
```


### Primjer formatiranja tablice

```bash
#!/bin/bash

printf "+%-15s+%-8s+%-10s+\n" "───────────────" "────────" "──────────"
printf "|%-15s|%-8s|%-10s|\n" "PROIZVOD" "CIJENA" "KOLIČINA"
printf "+%-15s+%-8s+%-10s+\n" "───────────────" "────────" "──────────"
printf "|%-15s|%8.2f|%10d|\n" "Jabuke" 12.50 100
printf "|%-15s|%8.2f|%10d|\n" "Naranče" 15.75 85
printf "|%-15s|%8.2f|%10d|\n" "Banane" 8.30 120
printf "+%-15s+%-8s+%-10s+\n" "───────────────" "────────" "──────────"
```


## Preciznost brojeva

### Decimalni brojevi

```bash
broj=3.14159265

printf "%.2f\n" $broj    # 3.14 (2 decimale)
printf "%.4f\n" $broj    # 3.1416 (4 decimale)
printf "%8.2f\n" $broj   # "    3.14" (širina 8, 2 decimale)
printf "%08.2f\n" $broj  # "00003.14" (popuni nulama)
```


## Escape sekvence u printf

```bash
printf "Prva linija\nDruga linija\n"
printf "Tab\tseparator\n"
printf "Backslash: \\\n"
printf "Navodnik: \"\n"
printf "Postotak: %%\n"      # %% za literal %
```


## Razlika između printf i echo

| Printf | Echo |
| :-- | :-- |
| Ne dodaje automatski novi red | Automatski dodaje novi red |
| Precizno formatiranje | Jednostavan ispis |
| Format specifikatori | Osnovne escape sekvence |
| Portable između sistema | Ponašanje varira |

```bash
# Echo
echo "Broj: $broj"

# Printf ekvivalent
printf "Broj: %s\n" "$broj"
```


## Napredni primjeri

### Progress bar s printf

```bash
#!/bin/bash

ukupno=100
for i in $(seq 0 5 100); do
    procenat=$((i * 100 / ukupno))
    printf "\rProgress: [%-20s] %3d%%" \
           "$(printf "%*s" $((procenat/5)) "" | tr ' ' '█')" \
           "$procenat"
    sleep 0.1
done
printf "\n"
```


### Sistemski izvještaj

```bash
#!/bin/bash

printf "\n"
printf "╔═══════════════════════════════════════════════════════╗\n"
printf "║                 SISTEMSKI STATUS                     ║\n"
printf "╚═══════════════════════════════════════════════════════╝\n"
printf "\n"

# Formirane informacije
printf "%-18s: %-30s\n" "Hostname" "$(hostname)"
printf "%-18s: %-30s\n" "Korisnik" "$USER"
printf "%-18s: %-30s\n" "Datum" "$(date '+%d.%m.%Y %H:%M')"
printf "%-18s: %-30s\n" "Uptime" "$(uptime -p)"

# Numeričke informacije
cpu_cores=$(nproc)
mem_total=$(free -m | awk 'NR==2{print $2}')
mem_used=$(free -m | awk 'NR==2{print $3}')

printf "\n"
printf "%-18s: %8d jezgara\n" "CPU" "$cpu_cores"
printf "%-18s: %8d MB / %d MB\n" "Memorija" "$mem_used" "$mem_total"

printf "\n"
```


## Ključne prednosti printf

- **Preciznost:** Potpuna kontrola nad formatiranjem
- **Portabilnost:** Radi isto na svim Unix sustavima
- **Fleksibilnost:** Širok spektar opcija formatiranja
- **Sigurnost:** Manje sklon greškama od echo-a

Printf je profesionalni alat za formatiranje u bash skriptama i preporučuje se za sve kompleksnije ispise!

