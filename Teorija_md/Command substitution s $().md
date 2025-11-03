<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Command substitution s \$()

`$()` je **command substitution** sintaksa u Bash-u koja omogućava izvršavanje naredbi i korištenje njihovog izlaza kao dio stringa. Umjesto `date` možete staviti bilo koju naredbu koja vraća tekstualni izlaz.

## Sistemske informacije

**Datum i vrijeme:**

```bash
echo -e "Danas je: $(date '+%A, %d %B %Y')"
echo -e "Vrijeme: $(date '+%H:%M:%S')"
echo -e "Unix timestamp: $(date +%s)"
```

**Korisničke informacije:**

```bash
echo -e "Trenutni korisnik: $(whoami)"
echo -e "ID korisnika: $(id -u)"
echo -e "Grupa: $(id -gn)"
echo -e "Shell: $(echo $SHELL)"
```

**Direktoriji i lokacije:**

```bash
echo -e "Radni direktorij: $(pwd)"
echo -e "Home direktorij: $(echo $HOME)"
echo -e "Ime skripte: $(basename $0)"
echo -e "Puni path skripte: $(realpath $0)"
```


## Informacije o fajlovima

**Osnovne informacije:**

```bash
echo -e "Veličina fajla: $(stat -c %s filename.txt) bytes"
echo -e "Lista fajlova:\n$(ls -l)"
echo -e "Broj fajlova: $(ls -1 | wc -l)"
echo -e "Zadnja izmjena: $(stat -c %y filename.txt)"
```

**Sadržaj fajlova:**

```bash
echo -e "Prvi red fajla: $(head -n 1 config.txt)"
echo -e "Zadnji red fajla: $(tail -n 1 config.txt)"
echo -e "Broj linija: $(wc -l < file.txt)"
```


## Mrežne informacije

**IP adrese i mreža:**

```bash
echo -e "IP adresa: $(hostname -I)"
echo -e "Hostname: $(hostname)"
echo -e "DNS serveri: $(cat /etc/resolv.conf | grep nameserver)"
echo -e "Aktivne konekcije: $(netstat -an | wc -l)"
```


## Sistemski resursi

**Memorija i prostor:**

```bash
echo -e "Memorija: $(free -h | awk 'NR==2{print $3"/"$2}')"
echo -e "Uptime: $(uptime -p)"
echo -e "Broj procesa: $(ps aux | wc -l)"
echo -e "Slobodan prostor: $(df -h . | awk 'NR==2 {print $4}')"
```

**CPU informacije:**

```bash
echo -e "CPU model: $(cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d: -f2)"
echo -e "Broj CPU jezgara: $(nproc)"
echo -e "Load average: $(uptime | awk -F'load average:' '{ print $2 }')"
```


## Matematički izrazi

**Kalkulacije:**

```bash
echo -e "Rezultat: $((5 + 3)) = $(expr 5 + 3)"
echo -e "Random broj: $(shuf -i 1-100 -n 1)"
echo -e "Trenutni timestamp: $(date +%s)"
```


## Kompletan praktični primjer

```bash
#!/bin/bash

# Boje
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗"
echo -e "║                SISTEMSKI IZVJEŠTAJ                   ║"
echo -e "╚═══════════════════════════════════════════════════════╝${NC}\n"

echo -e "${GREEN}📅 DATUM I VRIJEME${NC}"
echo -e "   Danas je: $(date '+%A, %d %B %Y')"
echo -e "   Vrijeme: $(date '+%H:%M:%S')"
echo -e "   Timezone: $(date '+%Z')"

echo -e "\n${GREEN}👤 KORISNIK${NC}"
echo -e "   Ime: $(whoami)"
echo -e "   ID: $(id -u)"
echo -e "   Shell: $(basename $SHELL)"
echo -e "   Home: $(echo $HOME)"

echo -e "\n${GREEN}💻 SISTEM${NC}"
echo -e "   Hostname: $(hostname)"
echo -e "   OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2 | tr -d '\"')"
echo -e "   Kernel: $(uname -r)"
echo -e "   Uptime: $(uptime -p)"

echo -e "\n${GREEN}📁 DIREKTORIJ${NC}"
echo -e "   Trenutni: $(pwd)"
echo -e "   Broj fajlova: $(ls -1 2>/dev/null | wc -l)"
echo -e "   Veličina: $(du -sh . 2>/dev/null | cut -f1)"

echo -e "\n${GREEN}🔧 RESURSI${NC}"
echo -e "   CPU: $(nproc) jezgara"
echo -e "   Memorija: $(free -h | awk 'NR==2{print $3"/"$2" ("int($3/$2*100)"%)"}')"
echo -e "   Disk: $(df -h . | awk 'NR==2 {print $3"/"$2" ("$5")"}')"

echo -e "\n${GREEN}🌐 MREŽA${NC}"
echo -e "   IP: $(hostname -I | awk '{print $1}')"
echo -e "   Konekcije: $(netstat -an 2>/dev/null | wc -l)"

echo -e "\n${YELLOW}🎲 Random broj: $(shuf -i 1-1000 -n 1)${NC}"
```

**Ključno:** Unutar `$()` možete staviti **bilo koju bash naredbu** koja vraća tekstualni izlaz - od jednostavnih poput `whoami` do složenih pipe kombinacija poput `ps aux | grep something | wc -l`.

<div style="text-align: center">⁂</div>

