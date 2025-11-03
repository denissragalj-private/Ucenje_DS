<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## "Grab" naredba - dohvaćanje podataka u Bash-u

**Bash nema ugrađenu `grab` naredbu**, ali termin "grab" znači **dohvaćanje podataka** iz različitih izvora. Evo načina kako možete "grabiti" informacije kombiniranjem postojećih naredbi.

## Dohvaćanje iz fajlova

### Korištenje `cat` za dohvaćanje sadržaja

```bash
# Grab cijeli sadržaj fajla
sadrzaj=$(cat fajl.txt)
echo "Dohvaćeni sadržaj: $sadrzaj"

# Grab i spremi u novi fajl
cat izvorni.txt > odredisni.txt
```


### Korištenje `grep` za selektivno dohvaćanje

```bash
# Grab linije koje sadrže određeni pattern
grep "Linux" welcome.txt > rezultati.txt

# Grab linije s brojem linije
grep -n "error" logovi.txt

# Grab određene kolone iz CSV fajla
grep "." podaci.csv | cut -d',' -f2,4 > kolone.txt
```


## Dohvaćanje informacija o fajlovima

### Kombiniranje `stat` s formatiranjem

```bash
#!/bin/bash

fajl="dokument.txt"

# Grab datum kreiranja
datum_kreiranja=$(stat -c %w "$fajl" 2>/dev/null)
echo "Kreiran: $datum_kreiranja" > info.txt

# Grab veličinu fajla
velicina=$(stat -c %s "$fajl")
printf "Veličina: %d bytes\n" "$velicina" >> info.txt

# Grab vlasnika
vlasnik=$(stat -c %U "$fajl")
echo "Vlasnik: $vlasnik" >> info.txt
```


## Dohvaćanje argumenata iz command line

### Grabiranje flagova s `getopts`

```bash
#!/bin/bash

# Grab command line argumente
while getopts "u:a:f:" flag; do
    case "${flag}" in
        u) username=${OPTARG};;
        a) age=${OPTARG};;
        f) fullname=${OPTARG};;
    esac
done

# Spremi grab-ane podatke u fajl
cat > korisnik.txt << EOF
Username: $username
Age: $age
Full Name: $fullname
Datum: $(date)
EOF
```


## Kompletan "grab" sistem

```bash
#!/bin/bash

# Definiranje fajlova
SOURCE_FILE="izvor.txt"
OUTPUT_FILE="grabbed_data.txt"

# Provjeri postojanje source fajla
if [ ! -f "$SOURCE_FILE" ]; then
    echo "❌ Izvorni fajl ne postoji: $SOURCE_FILE"
    exit 1
fi

# Kreiranje header-a u output fajlu
echo "╔═══════════════════════════════════════════════════════╗" > $OUTPUT_FILE
echo "║                  GRABBED DATA REPORT                  ║" >> $OUTPUT_FILE
echo "╚═══════════════════════════════════════════════════════╝" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Grab osnovnih informacija o fajlu
echo "📁 INFORMACIJE O FAJLU:" >> $OUTPUT_FILE
printf "   Ime fajla: %s\n" "$(basename $SOURCE_FILE)" >> $OUTPUT_FILE
printf "   Veličina: %s bytes\n" "$(stat -c %s $SOURCE_FILE)" >> $OUTPUT_FILE
printf "   Zadnja izmjena: %s\n" "$(stat -c %y $SOURCE_FILE | cut -d'.' -f1)" >> $OUTPUT_FILE

# Grab sadržaja fajla
echo "" >> $OUTPUT_FILE
echo "📄 SADRŽAJ FAJLA:" >> $OUTPUT_FILE
echo "────────────────────────────────────────────────────────" >> $OUTPUT_FILE
cat "$SOURCE_FILE" >> $OUTPUT_FILE

# Grab statistika
echo "" >> $OUTPUT_FILE
echo "📊 STATISTIKE:" >> $OUTPUT_FILE
printf "   Broj linija: %d\n" "$(wc -l < $SOURCE_FILE)" >> $OUTPUT_FILE
printf "   Broj riječi: %d\n" "$(wc -w < $SOURCE_FILE)" >> $OUTPUT_FILE
printf "   Broj znakova: %d\n" "$(wc -c < $SOURCE_FILE)" >> $OUTPUT_FILE

# Grab sistemskih informacija
echo "" >> $OUTPUT_FILE
echo "💻 SISTEMSKE INFORMACIJE:" >> $OUTPUT_FILE
printf "   Datum grab-a: %s\n" "$(date '+%d.%m.%Y %H:%M:%S')" >> $OUTPUT_FILE
printf "   Korisnik: %s\n" "$USER" >> $OUTPUT_FILE
printf "   Hostname: %s\n" "$(hostname)" >> $OUTPUT_FILE

echo "✅ Podaci uspješno grab-ani u: $OUTPUT_FILE"
```


## Grab iz pipe i kombinacije naredbi

```bash
#!/bin/bash

# Grab procesa i spremi u fajl
echo "🔍 GRAB SISTEMSKIH PROCESA:" > procesi.txt
ps aux | head -20 >> procesi.txt

# Grab network informacija
echo "" >> procesi.txt
echo "🌐 GRAB NETWORK INFORMACIJA:" >> procesi.txt
ifconfig | grep -A 4 "inet " >> procesi.txt

# Grab memorije i formatiraj s printf
mem_total=$(free -m | awk 'NR==2{print $2}')
mem_used=$(free -m | awk 'NR==2{print $3}')

echo "" >> procesi.txt
printf "💾 GRAB MEMORIJSKE INFORMACIJE:\n" >> procesi.txt
printf "   Ukupno: %8d MB\n" "$mem_total" >> procesi.txt
printf "   Koristi: %8d MB\n" "$mem_used" >> procesi.txt
printf "   Postotak: %6.1f%%\n" "$(echo "scale=1; $mem_used*100/$mem_total" | bc)" >> procesi.txt
```


## Interaktivni grab sustav

```bash
#!/bin/bash

echo "🔍 INTERAKTIVNI GRAB SUSTAV"
echo "═══════════════════════════════════════"

# Grab korisničkih inputa
read -p "📁 Unesite ime fajla za grab: " target_file
read -p "💾 Unesite ime output fajla: " output_file

if [ -f "$target_file" ]; then
    # Grab i formatiraj podatke
    {
        echo "GRAB IZVJEŠTAJ za: $target_file"
        echo "Generirano: $(date)"
        echo "═══════════════════════════════════════"
        echo ""
        echo "SADRŽAJ:"
        cat "$target_file"
        echo ""
        echo "STAT INFORMACIJE:"
        stat "$target_file"
    } > "$output_file"
    
    echo "✅ Podaci grab-ani u: $output_file"
else
    echo "❌ Fajl ne postoji: $target_file"
fi
```

**Ključno:** "Grab" u bash kontekstu znači kombiniranje različitih naredbi (`cat`, `grep`, `stat`, `cut`, `awk`) za dohvaćanje specifičnih podataka i njihovo formatiranje pomoću `echo`, `printf` i redirection operatora za spremanje u fajlove.

<div style="text-align: center">⁂</div>

[^1]: https://www.unix.com/shell-programming-and-scripting/128633-grab-file-one-command.html

[^2]: https://www.digitalocean.com/community/tutorials/grep-command-in-linux-unix

[^3]: https://askubuntu.com/questions/806640/how-do-i-find-a-time-stamp-on-a-file-and-then-echo-it-into-the-contents-of-the-f

[^4]: https://gist.github.com/36152d413260beefa558ab677f712349

[^5]: https://stackoverflow.com/questions/14447406/bash-shell-script-check-for-a-flag-and-grab-its-value

[^6]: https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script

[^7]: https://unix.stackexchange.com/questions/156009/how-to-grab-output-from-command-in-shell-script

[^8]: https://stackoverflow.com/questions/43698601/read-the-contents-of-a-command-into-a-variable-and-grab-the-first-line

[^9]: https://www.redhat.com/en/blog/linux-script-command

[^10]: https://stackoverflow.com/questions/2297510/linux-shell-script-for-each-file-in-a-directory-grab-the-filename-and-execute-a

