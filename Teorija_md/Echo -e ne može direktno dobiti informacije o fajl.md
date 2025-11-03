<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Echo -e ne može direktno dobiti informacije o fajlovima

Echo -e **sama po sebi ne može dobiti informacije** poput datuma kreiranja fajla ili imena fajla. Ona služi samo za **formatiranje i interpretaciju escape sekvenci**. Međutim, možete je koristiti u kombinaciji s drugim naredbama za lijepo formatiranje njihovih izlaza.

## Kombiniranje echo -e s drugim naredbama

### Informacije o fajlovima pomoću `stat`

```bash
#!/bin/bash

FILE="demo.txt"

# Osnovne informacije pomoću stat naredbe
echo -e "═══════════════════════════════════════"
echo -e "📁 INFORMACIJE O FAJLU: $FILE"
echo -e "═══════════════════════════════════════"

# Datum kreiranja
BIRTH_TIME=$(stat -c %w "$FILE" 2>/dev/null)
if [ "$BIRTH_TIME" != "-" ] && [ -n "$BIRTH_TIME" ]; then
    echo -e "🕐 Datum kreiranja:\t$BIRTH_TIME"
else
    echo -e "⚠️  Datum kreiranja:\tNije dostupan"
fi

# Datum zadnje modifikacije
MOD_TIME=$(stat -c %y "$FILE")
echo -e "✏️  Zadnja izmjena:\t$MOD_TIME"

# Veličina fajla
SIZE=$(stat -c %s "$FILE")
echo -e "📏 Veličina:\t\t$SIZE bytes"

# Dozvole
PERMISSIONS=$(stat -c %A "$FILE")
echo -e "🔒 Dozvole:\t\t$PERMISSIONS"

# Vlasnik
OWNER=$(stat -c %U "$FILE")
echo -e "👤 Vlasnik:\t\t$OWNER"
```


### Informacije o trenutnoj skripti

```bash
#!/bin/bash

# Ime trenutne skripte
SCRIPT_NAME=$(basename "$0")
echo -e "📝 Ime skripte:\t\t$SCRIPT_NAME"

# Puni path skripte
SCRIPT_PATH=$(realpath "$0")
echo -e "📂 Lokacija:\t\t$SCRIPT_PATH"

# Datum pokretanja
echo -e "🕐 Pokrenuto:\t\t$(date '+%Y-%m-%d %H:%M:%S')"

# Korisnik koji je pokrenuo
echo -e "👤 Pokrenuo:\t\t$USER"

# Radni direktorij
echo -e "📁 Radni dir:\t\t$(pwd)"
```


### Sistemske informacije

```bash
#!/bin/bash

echo -e "💻 SISTEMSKE INFORMACIJE"
echo -e "═══════════════════════════════════════"

# Datum i vrijeme
echo -e "📅 Datum:\t\t$(date '+%A, %d %B %Y')"
echo -e "🕐 Vrijeme:\t\t$(date '+%H:%M:%S')"

# Uptime sistema
UPTIME=$(uptime -p)
echo -e "⏱️  Uptime:\t\t$UPTIME"

# Dostupan prostor
DISK_SPACE=$(df -h . | awk 'NR==2 {print $4}')
echo -e "💾 Slobodan prostor:\t$DISK_SPACE"

# Memorija
MEM_INFO=$(free -h | awk 'NR==2{printf "%.0f%% (%.1fG/%.1fG)", $3*100/$2, $3/1024, $2/1024}')
echo -e "🧠 Memorija:\t\t$MEM_INFO"
```


## Kompletan praktični primjer

```bash
#!/bin/bash

# Boje
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

clear

echo -e "${WHITE}╔═══════════════════════════════════════════════════════╗"
echo -e "║                  INFORMACIJSKI PANEL                 ║"
echo -e "╚═══════════════════════════════════════════════════════╝${NC}\n"

# Informacije o skripti
echo -e "${CYAN}🔧 SKRIPTA${NC}"
echo -e "   📝 Ime:\t\t$(basename "$0")"
echo -e "   📂 Lokacija:\t$(dirname "$(realpath "$0")")"
echo -e "   🕐 Pokrenuto:\t$(date '+%H:%M:%S')"

# Provjeri postojanje fajla
TEST_FILE="test.txt"
if [ -f "$TEST_FILE" ]; then
    echo -e "\n${GREEN}📄 FAJL: $TEST_FILE${NC}"
    
    # Stat informacije
    STAT_OUTPUT=$(stat "$TEST_FILE")
    
    # Izvuci specifične informacije
    SIZE=$(echo "$STAT_OUTPUT" | grep -o 'Size: [0-9]*' | cut -d' ' -f2)
    MODIFY=$(echo "$STAT_OUTPUT" | grep 'Modify:' | cut -d' ' -f2,3)
    OWNER=$(echo "$STAT_OUTPUT" | grep -o 'Uid: ([^)]*' | cut -d'(' -f2)
    
    echo -e "   📏 Veličina:\t$SIZE bytes"
    echo -e "   ✏️  Izmjena:\t$MODIFY"
    echo -e "   👤 Vlasnik:\t$OWNER"
else
    echo -e "\n${YELLOW}⚠️  Fajl '$TEST_FILE' ne postoji${NC}"
    echo -e "   🔧 Kreiram test fajl..."
    echo "Test sadržaj" > "$TEST_FILE"
    echo -e "   ✅ Fajl kreiran!"
fi

# Sistemske informacije
echo -e "\n${PURPLE}💻 SISTEM${NC}"
echo -e "   📅 Datum:\t\t$(date '+%d.%m.%Y')"
echo -e "   🕐 Vrijeme:\t$(date '+%H:%M:%S')"
echo -e "   👤 Korisnik:\t$USER"
echo -e "   📁 Dir:\t\t$(pwd | tail -c 30)"

echo -e "\n${WHITE}═══════════════════════════════════════════════════════${NC}"
```


## Ključne točke

**Echo -e može:**

- ✅ Formatirati izlaz drugih naredbi
- ✅ Dodati boje i emoji
- ✅ Organizirati informacije u tablice
- ✅ Kreirati lijepe korisničke sučelja

**Echo -e ne može:**

- ❌ Direktno čitati fajl informacije
- ❌ Pristupiti sistemskim podacima
- ❌ Izvršavati druge naredbe

Echo -e je **alat za formatiranje**, a informacije morate dobiti putem drugih naredbi poput `stat`, `date`, `basename`, `pwd`, itd., a zatim ih formatirati pomoću echo -e.

<div style="text-align: center">⁂</div>

[^1]: https://kodekloud.com/blog/file-creation-time-linux/

[^2]: https://www.baeldung.com/linux/find-bash-script-filename

[^3]: https://linuxhandbook.com/stat-command/

[^4]: https://gcore.com/learning/how-to-determine-file-creation-date-in-linux

[^5]: https://www.ubuntumint.com/find-file-creation-date/

[^6]: https://stackoverflow.com/questions/1819187/test-a-file-date-with-bash

[^7]: https://www.baeldung.com/linux/get-file-creation-date

[^8]: https://unix.stackexchange.com/questions/91197/how-can-get-the-creation-date-of-a-file

[^9]: https://askubuntu.com/questions/806640/how-do-i-find-a-time-stamp-on-a-file-and-then-echo-it-into-the-contents-of-the-f

[^10]: https://stackoverflow.com/questions/68470266/bash-echo-time-date-format

