<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Pisanje u fajl u Bash skriptama

Bash **nema `print` naredbu**, ali imate nekoliko načina pisanja u fajlove koristeći `echo`, `printf`, `cat` i redirection operatore.

## Redirection operatori

### `>` operator (prepisuje fajl)

```bash
echo "Novi sadržaj" > fajl.txt
```


### `>>` operator (dodaje na kraj)

```bash
echo "Dodaje liniju" >> fajl.txt
```


## Echo naredba za pisanje u fajl

**Osnovni primjeri:**

```bash
# Jednostavan tekst
echo "Pozdrav svijetu" > pozdrav.txt

# S varijablama
korisnik="Marko"
echo "Korisnik: $korisnik" > info.txt

# Više linija odjednom
echo -e "Prva linija\nDruga linija\nTreća linija" > linije.txt

# Dodavanje na postojeći fajl
echo "Nova linija" >> postojeci.txt
```

**S bojama i formatiranjem:**

```bash
echo -e "\033[32m✓ Uspješno završeno\033[0m" > status.txt
echo -e "Datum: $(date)\nKorisnik: $USER" > izvjestaj.txt
```


## Printf za precizno pisanje

**Osnovni printf:**

```bash
printf "Ime: %s\nGodine: %d\n" "Ana" 25 > profil.txt
printf "%.2f HRK\n" 123.456 > cijena.txt
```

**Formatirana tablica:**

```bash
printf "%-15s | %8s | %6s\n" "PROIZVOD" "CIJENA" "KOL." > tablica.txt
printf "%-15s | %8.2f | %6d\n" "Jabuke" 12.50 100 >> tablica.txt
printf "%-15s | %8.2f | %6d\n" "Naranče" 15.75 85 >> tablica.txt
```


## Cat naredba s Heredoc

**Pisanje više linija:**

```bash
cat > dokument.txt << EOF
Ovo je naslov dokumenta
========================

Ovo je sadržaj dokumenta koji može
sadržavati više linija teksta.

Trenutni korisnik: $USER
Datum: $(date)
EOF
```

**Dodavanje s heredoc:**

```bash
cat >> dnevnik.txt << EOF
$(date): Nova aktivnost zabilježena
Korisnik: $USER
Status: Aktivan
EOF
```


## Praktični primjeri kombiniranja

### Kreiranje log fajla

```bash
#!/bin/bash

LOG_FILE="system.log"

# Kreiranje zaglavlja
echo "═══════════════════════════════════════" > $LOG_FILE
echo "        SISTEMSKI DNEVNIK" >> $LOG_FILE
echo "═══════════════════════════════════════" >> $LOG_FILE

# Dodavanje informacija s printf
printf "Datum pokretanja: %s\n" "$(date)" >> $LOG_FILE
printf "Korisnik: %s\n" "$USER" >> $LOG_FILE
printf "Hostname: %s\n" "$(hostname)" >> $LOG_FILE

# Dodavanje sistemskih informacija
echo "" >> $LOG_FILE
echo "📊 SISTEMSKI RESURSI:" >> $LOG_FILE
echo "────────────────────" >> $LOG_FILE

# Formatirana tablica s printf
printf "%-15s: %s\n" "Memorija ukupno" "$(free -h | awk 'NR==2{print $2}')" >> $LOG_FILE
printf "%-15s: %s\n" "Memorija koristi" "$(free -h | awk 'NR==2{print $3}')" >> $LOG_FILE
printf "%-15s: %s\n" "Disk prostor" "$(df -h . | awk 'NR==2{print $4}')" >> $LOG_FILE
```


### Kreiranje konfiguracijskog fajla

```bash
#!/bin/bash

CONFIG_FILE="app.conf"

cat > $CONFIG_FILE << EOF
# Aplikacijska konfiguracija
# Generirano: $(date)

[database]
host=localhost
port=5432
name=myapp_db

[application]
debug=false
log_level=info
max_connections=100

[paths]
data_dir=/var/lib/myapp
log_dir=/var/log/myapp
temp_dir=/tmp/myapp
EOF

echo "✅ Konfiguracija kreirana: $CONFIG_FILE"
```


## Stat naredba (za čitanje, ne pisanje)

`stat` se koristi za **čitanje informacija** o fajlu, ne za pisanje:

```bash
# Čitanje informacija o fajlu
stat dokument.txt

# Pisanje stat informacija u drugi fajl
stat dokument.txt > info_o_fajlu.txt

# Formatiranje stat izlaza
stat --format="Ime: %n, Veličina: %s bytes" dokument.txt > kratki_info.txt
```


## Sigurnosne napomene

**Sprječavanje prepisivanja:**

```bash
set -o noclobber              # Aktivira zaštitu
echo "test" > postojeci.txt   # Greška ako fajl postoji
echo "test" >| postojeci.txt  # Forsiraj prepisivanje
```

**Provjera dozvola:**

```bash
if [ -w "$HOME/moj_fajl.txt" ]; then
    echo "Podaci" > "$HOME/moj_fajl.txt"
else
    echo "Nema dozvola za pisanje!"
fi
```

Ključno je razumjeti da `echo`, `printf` i `cat` **rade u kombinaciji s redirection operatorima** (`>`, `>>`) za pisanje u fajlove, dok `stat` služi za čitanje informacija o fajlovima.

<div style="text-align: center">⁂</div>

[^1]: https://linuxize.com/post/bash-write-to-file/

[^2]: https://www.linode.com/docs/guides/write-to-a-file-from-the-shell/

[^3]: https://linuxconfig.org/stat-command-usage-and-examples

[^4]: https://www.baeldung.com/linux/write-bash-variable-to-file

[^5]: https://phoenixnap.com/kb/bash-write-to-file

[^6]: https://stackoverflow.com/questions/17189237/how-can-i-write-and-append-using-echo-command-to-a-file

[^7]: https://askubuntu.com/questions/1019942/echo-hello-0-file-txt-doesnt-write-to-file-txt

[^8]: https://unix.stackexchange.com/questions/776470/bash-script-echo-output-of-variable-and-write-to-file

[^9]: https://www.tutorialspoint.com/writing-text-to-file-using-linux-cat-command

[^10]: https://www.redhat.com/en/blog/redirect-shell-command-script-output

