# Linux Osnovne Komande - Kompletni Vodič

## Sadržaj
1. [tar - Arhiviranje](#tar-komanda)
2. [mv - Preimenovanje i premještanje](#mv-komanda)
3. [rm - Brisanje](#rm-komanda)
4. [cp - Kopiranje](#cp-komanda)
5. [mkdir - Stvaranje direktorija](#mkdir-komanda)
6. [touch - Stvaranje datoteka](#touch-komanda)
7. [cat, less, head, tail - Čitanje datoteka](#citanje-datoteka)
8. [find - Pronalaženje datoteka](#find-komanda)
9. [grep - Pretraživanje sadržaja](#grep-komanda)
10. [chmod - Dozvole datoteka](#chmod-komanda)

---

# tar komanda - Arhiviranje {#tar-komanda}

## Što je `tar`?

`tar` (Tape Archive) je alat za arhiviranje datoteka u Linuxu i Unix sustavima. Koristi se za pakiranje više datoteka i direktorija u jednu arhivsku datoteku, često s kompresijom.

## Osnovna sintaksa

```bash
tar [opcije] [arhiva] [datoteke/direktoriji]
```

## Najvažnije opcije

- `c` - **create** - stvara novu arhivu
- `x` - **extract** - izvlači datoteke iz arhive
- `t` - **list** - prikazuje sadržaj arhive
- `v` - **verbose** - prikazuje detalje o procesu
- `f` - **file** - specificira ime arhivske datoteke
- `z` - kompresija gzip (.tar.gz ili .tgz)
- `j` - kompresija bzip2 (.tar.bz2)
- `J` - kompresija xz (.tar.xz)

## Detaljno objašnjenje sintakse

```bash
tar -cvf print_formati.tar .
```

### Razrada svake opcije:

**`-c`** (create) - Stvara novu arhivu

**`-v`** (verbose) - Prikazuje detalje - ispisuje imena datoteka dok se arhiviraju

**`-f`** (file) - Specificira ime arhivske datoteke koja slijedi
- **VAŽNO**: `-f` mora biti ZADNJA opcija jer se odmah nakon nje navodi ime arhive!

**`print_formati.tar`** - Ovo je **IME arhivske datoteke** koja će biti stvorena

**`.`** (točka) - Ovo je **IZVOR** - što želiš arhivirati
- `.` znači "trenutni direktorij i SVE u njemu"

### Razlika između "dva mjesta":

```bash
tar -cvf print_formati.tar .
        ↑                  ↑
        |                  |
   IME ARHIVE          ŠTO ARHIVIRATI
```

### Specijalni direktoriji:
- `.` = trenutni direktorij
- `..` = parent direktorij
- `/` = root direktorij
- `~` = home direktorij

## Primjeri

### Stvaranje arhive

```bash
# Osnovna arhiva bez kompresije
tar -cvf arhiva.tar datoteke/

# Arhiva trenutnog direktorija
tar -cvf arhiva.tar .

# Arhiva s gzip kompresijom (preporučeno)
tar -czvf arhiva.tar.gz datoteke/

# Arhiva s bzip2 kompresijom (bolja kompresija)
tar -cjvf arhiva.tar.bz2 datoteke/

# Backup s datumom
tar -czvf backup-$(date +%Y%m%d).tar.gz ~/projekti/
```

### Izvlačenje arhive

```bash
# Izvlačenje tar arhive
tar -xvf arhiva.tar

# Izvlačenje gzip arhive
tar -xzvf arhiva.tar.gz

# Izvlačenje u specifičan direktorij
tar -xzvf arhiva.tar.gz -C /putanja/do/direktorija/

# Automatsko detektiranje kompresije
tar -xavf arhiva.tar.gz
```

### Pregled sadržaja arhive

```bash
tar -tvf arhiva.tar
tar -tzvf arhiva.tar.gz
```

### Arhiviranje s isključivanjem datoteka

```bash
# Isključi određene datoteke
tar -czvf arhiva.tar.gz --exclude='*.log' datoteke/

# Isključi više pattern-a
tar -czvf projekt.tar.gz \
  --exclude='node_modules' \
  --exclude='*.log' \
  --exclude='.git' \
  projekt/
```

---

# mv komanda - Preimenovanje i premještanje {#mv-komanda}

## Osnovna sintaksa

```bash
mv izvor odrediste
```

## Opcije

- `-i` - pita za potvrdu prije prepisivanja
- `-f` - force, prepisuje bez pitanja
- `-n` - ne prepisuje postojeće datoteke
- `-v` - verbose, prikazuje što se radi
- `-u` - premješta samo ako je izvorna datoteka novija

## Primjeri

### Preimenovanje

```bash
# Preimenovanje jedne datoteke
mv staro_ime.txt novo_ime.txt

# Preimenovanje s potvrdom
mv -i staro.txt novo.txt

# Preimenovanje više datoteka (uklanjanje _sw)
for file in *_sw.json; do 
    mv "$file" "${file/_sw/}"
done

# Zamjena ekstenzije
for file in *.txt; do 
    mv "$file" "${file%.txt}.md"
done
```

### Premještanje

```bash
# Premjesti datoteku u direktorij
mv datoteka.txt ~/dokumenti/

# Premjesti više datoteka
mv *.json ~/backup/

# Premjesti i preimenuj
mv stara.txt ~/dokumenti/nova.txt

# Premjesti direktorij
mv stari_dir/ ~/novi_dir/
```

---

# rm komanda - Brisanje {#rm-komanda}

## Osnovna sintaksa

```bash
rm [opcije] datoteka
```

## Opcije

- `-i` - pita za potvrdu prije brisanja
- `-f` - force, briše bez pitanja
- `-r` ili `-R` - rekurzivno briše direktorije
- `-v` - verbose, prikazuje što se briše
- `-d` - briše prazne direktorije

## Primjeri

```bash
# Brisanje jedne datoteke
rm datoteka.txt

# Brisanje s potvrdom
rm -i datoteka.txt

# Brisanje više datoteka
rm file1.txt file2.txt file3.txt

# Brisanje svih .log datoteka
rm *.log

# Brisanje direktorija s sadržajem
rm -r direktorij/

# Brisanje direktorija bez potvrde (OPASNO!)
rm -rf direktorij/

# Brisanje svih datoteka u direktoriju
rm -rf direktorij/*
```

## ⚠️ VAŽNA UPOZORENJA

```bash
# ❌ NIKAD OVO:
rm -rf /           # Briše cijeli sustav!
rm -rf /*          # Također katastrofa!

# ✅ UVIJEK PROVJERI:
ls direktorij/     # Prvo vidi što brišeš
rm -i *.txt        # Koristi -i za potvrdu
```

---

# cp komanda - Kopiranje {#cp-komanda}

## Osnovna sintaksa

```bash
cp izvor odrediste
```

## Opcije

- `-r` ili `-R` - kopira direktorije rekurzivno
- `-i` - pita za potvrdu prije prepisivanja
- `-f` - force, prepisuje bez pitanja
- `-v` - verbose, prikazuje što se kopira
- `-p` - čuva атрибуте (dozvole, vrijeme)
- `-u` - kopira samo novije datoteke
- `-a` - arhivski mod (čuva sve, rekurzivno)

## Primjeri

```bash
# Kopiranje datoteke
cp datoteka.txt kopija.txt

# Kopiranje u drugi direktorij
cp datoteka.txt ~/backup/

# Kopiranje s novim imenom
cp stara.txt ~/backup/nova.txt

# Kopiranje direktorija
cp -r direktorij/ kopija_direktorija/

# Kopiranje s očuvanjem atributa
cp -p datoteka.txt backup.txt

# Arhivsko kopiranje (najbolje za backupe)
cp -a projekt/ backup_projekt/

# Kopiranje više datoteka
cp file1.txt file2.txt file3.txt ~/backup/

# Kopiranje samo novijih datoteka
cp -u *.txt ~/backup/

# Verbose kopiranje
cp -rv direktorij/ backup/
```

### Razlika cp vs mv

```bash
# cp - KOPIRA (original ostaje)
cp datoteka.txt kopija.txt    # Sad imaš OBE datoteke

# mv - PREMJEŠTA (original nestaje)
mv datoteka.txt nova.txt      # Imaš samo nova.txt
```

---

# mkdir komanda - Stvaranje direktorija {#mkdir-komanda}

## Osnovna sintaksa

```bash
mkdir ime_direktorija
```

## Opcije

- `-p` - stvara parent direktorije ako ne postoje
- `-v` - verbose, prikazuje što se stvara
- `-m` - postavlja dozvole odmah

## Primjeri

```bash
# Stvaranje jednog direktorija
mkdir novi_direktorij

# Stvaranje više direktorija odjednom
mkdir dir1 dir2 dir3

# Stvaranje ugniježđenih direktorija
mkdir -p projekti/web/frontend/src

# Bez -p bi dalo grešku ako 'projekti' ne postoji
# Sa -p stvara sve direktorije u putu

# Stvaranje s specifičnim dozvolama
mkdir -m 755 javni_direktorij

# Verbose stvaranje
mkdir -pv projekti/backup/2025/01

# Organizacija projekta
mkdir -p projekt/{src,docs,tests,config}

# Stvaranje strukture po datumima
mkdir -p backup/$(date +%Y)/$(date +%m)
```

### Praktični primjeri

```bash
# Struktura za web projekt
mkdir -p projekt/{frontend/{src,public,components},backend/{api,db,middleware},docs}

# Mjesečni backupi
mkdir -p backup/{Januar,Februar,Mart,April,Maj,Jun,Jul,Avgust,Septembar,Oktobar,Novembar,Decembar}

# Organizacija dokumenata
mkdir -p ~/Dokumenti/{Posao,Licno,Projekti,Racuni}
```

---

# touch komanda - Stvaranje datoteka {#touch-komanda}

## Osnovna sintaksa

```bash
touch ime_datoteke
```

## Što radi `touch`?

1. **Stvara praznu datoteku** ako ne postoji
2. **Ažurira timestamp** postojeće datoteke

## Primjeri

```bash
# Stvaranje jedne prazne datoteke
touch nova_datoteka.txt

# Stvaranje više datoteka odjednom
touch file1.txt file2.txt file3.txt

# Stvaranje datoteka s ekstenzijama
touch index.html style.css script.js

# Stvaranje u drugom direktoriju
touch ~/projekti/notes.txt

# Ažuriranje timestampa postojeće datoteke
touch postojeca_datoteka.txt

# Stvaranje skrivene datoteke
touch .gitignore

# Stvaranje više datoteka s pattern-om
touch test{1..10}.txt    # Stvara test1.txt do test10.txt

# Stvaranje datoteka po danima
touch backup-$(date +%Y-%m-%d).tar.gz
```

### Praktični primjeri

```bash
# Priprema strukture projekta
mkdir -p projekt/{src,tests,docs}
touch projekt/src/{main.py,utils.py,config.py}
touch projekt/tests/{test_main.py,test_utils.py}
touch projekt/docs/README.md

# Stvaranje log datoteka po danima
touch log-$(date +%Y-%m-%d).log

# Placeholder datoteke
touch TODO.txt NOTES.txt IDEAS.txt
```

---

# Čitanje datoteka {#citanje-datoteka}

## cat - Prikaz cijele datoteke

```bash
# Prikaz jedne datoteke
cat datoteka.txt

# Prikaz više datoteka
cat file1.txt file2.txt

# Prikaz s brojevima linija
cat -n datoteka.txt

# Spajanje datoteka u novu
cat file1.txt file2.txt > spojeno.txt

# Dodavanje u postojeću datoteku
cat dodatak.txt >> postojeca.txt
```

## less - Interaktivni prikaz

```bash
# Otvara datoteku za čitanje
less datoteka.txt

# Kontrole u less-u:
# Space - sljedeća stranica
# b - prethodna stranica
# / - pretraživanje
# n - sljedeći rezultat pretrage
# q - izlaz
# G - idi na kraj
# g - idi na početak

# Prikaz s brojevima linija
less -N datoteka.txt
```

## head - Prvih N linija

```bash
# Prvih 10 linija (default)
head datoteka.txt

# Prvih 20 linija
head -n 20 datoteka.txt

# Prva 3 reda
head -n 3 datoteka.txt

# Prvih 100 bajtova
head -c 100 datoteka.txt
```

## tail - Zadnjih N linija

```bash
# Zadnjih 10 linija (default)
tail datoteka.txt

# Zadnjih 20 linija
tail -n 20 datoteka.txt

# Praćenje datoteke u realnom vremenu (log files)
tail -f /var/log/syslog

# Praćenje s brojem linija
tail -f -n 50 logfile.log

# Praćenje više datoteka
tail -f file1.log file2.log
```

### Praktični primjeri

```bash
# Brza provjera CSV datoteke
head -n 5 data.csv

# Provjera loga
tail -n 50 error.log

# Praćenje log-a uživo
tail -f /var/log/apache2/access.log

# Prikaz s pagination
cat dugacka_datoteka.txt | less

# Brojanje linija u datoteci
cat datoteka.txt | wc -l

# Prikaz samo određenih linija (npr. 10-20)
sed -n '10,20p' datoteka.txt
```

---

# find komanda - Pronalaženje datoteka {#find-komanda}

## Osnovna sintaksa

```bash
find [putanja] [kriteriji] [akcije]
```

## Primjeri

### Pronalaženje po imenu

```bash
# Pronađi datoteke po imenu
find . -name "datoteka.txt"

# Pronađi bez obzira na velika/mala slova
find . -iname "datoteka.txt"

# Pronađi sve .txt datoteke
find . -name "*.txt"

# Pronađi sve .json datoteke
find . -name "*.json"

# Pronađi datoteke koje počinju s "test"
find . -name "test*"
```

### Pronalaženje po tipu

```bash
# Samo datoteke
find . -type f

# Samo direktoriji
find . -type d

# Samo symbolic linkovi
find . -type l
```

### Pronalaženje po veličini

```bash
# Datoteke veće od 100MB
find . -size +100M

# Datoteke manje od 1KB
find . -size -1k

# Datoteke točno 50MB
find . -size 50M

# Prazne datoteke
find . -type f -empty

# Prazni direktoriji
find . -type d -empty
```

### Pronalaženje po vremenu

```bash
# Izmijenjeno u zadnjih 7 dana
find . -mtime -7

# Izmijenjeno prije više od 30 dana
find . -mtime +30

# Izmijenjeno u zadnjih 24 sata
find . -mtime 0

# Pristupljeno u zadnja 2 dana
find . -atime -2
```

### Pronalaženje s akcijama

```bash
# Pronađi i obriši
find . -name "*.tmp" -delete

# Pronađi i prikaži s detaljima
find . -name "*.log" -ls

# Pronađi i izvrši naredbu
find . -name "*.txt" -exec cat {} \;

# Pronađi i prebaci u backup
find . -name "*.old" -exec mv {} ~/backup/ \;

# Pronađi i kopiraj
find . -name "*.conf" -exec cp {} ~/backup/ \;
```

### Kombiniranje kriterija

```bash
# .txt datoteke veće od 1MB
find . -name "*.txt" -size +1M

# .log datoteke starije od 7 dana
find . -name "*.log" -mtime +7

# Datoteke između 1MB i 10MB
find . -size +1M -size -10M

# .txt ILI .md datoteke
find . -name "*.txt" -o -name "*.md"

# .log datoteke I starije od 30 dana
find . -name "*.log" -and -mtime +30
```

### Praktični primjeri

```bash
# Pronađi i obriši log datoteke starije od 30 dana
find /var/log -name "*.log" -mtime +30 -delete

# Pronađi sve Python datoteke u projektu
find ~/projekti -name "*.py"

# Pronađi i arhiviraj stare datoteke
find . -name "*.old" -exec tar -czvf old_files.tar.gz {} +

# Pronađi najveće datoteke
find . -type f -exec du -h {} + | sort -rh | head -10

# Pronađi prazne direktorije i obriši
find . -type d -empty -delete

# Pronađi datoteke s dozvolama 777
find . -type f -perm 0777
```

---

# grep komanda - Pretraživanje sadržaja {#grep-komanda}

## Osnovna sintaksa

```bash
grep [opcije] pattern [datoteka]
```

## Opcije

- `-i` - ignoriraj velika/mala slova
- `-r` ili `-R` - rekurzivno pretraživanje
- `-n` - prikaži broj linije
- `-v` - invertiraj (prikaži što NE sadrži pattern)
- `-c` - broji pojavljivanja
- `-l` - prikaži samo imena datoteka
- `-w` - cijela riječ
- `-A n` - prikaži n linija nakon
- `-B n` - prikaži n linija prije
- `-C n` - prikaži n linija prije i nakon

## Primjeri

### Osnovno pretraživanje

```bash
# Traži riječ u datoteci
grep "error" logfile.log

# Ignoriraj velika/mala slova
grep -i "error" logfile.log

# Prikaži broj linije
grep -n "error" logfile.log

# Traži u više datoteka
grep "TODO" *.py

# Rekurzivno pretraži sve datoteke
grep -r "config" .
```

### Naprednije pretraživanje

```bash
# Prikaži samo imena datoteka
grep -l "error" *.log

# Broji pojavljivanja
grep -c "error" logfile.log

# Invertirano (sve osim pattern-a)
grep -v "debug" logfile.log

# Cijela riječ (ne dio riječi)
grep -w "test" file.txt

# Kontekst - 3 linije prije i nakon
grep -C 3 "error" logfile.log

# 2 linije nakon
grep -A 2 "error" logfile.log

# 2 linije prije
grep -B 2 "error" logfile.log
```

### Regular expressions

```bash
# Linije koje počinju s "Error"
grep "^Error" logfile.log

# Linije koje završavaju s ".json"
grep "\.json$" files.txt

# Bilo koji broj
grep "[0-9]" data.txt

# Email pattern
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" contacts.txt

# IP adresa pattern
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" log.txt
```

### Kombinacije s drugim komandama

```bash
# Pretraži output druge komande
ps aux | grep "python"

# Traži u tar arhivi bez izvlačenja
tar -tzf arhiva.tar.gz | grep "config"

# Pretraži history
history | grep "git"

# Broj linija koda u Python projektima
find . -name "*.py" | xargs grep -c "def" | awk -F: '{sum+=$2} END {print sum}'

# Pronađi datoteke koje sadrže određeni tekst
grep -rl "database_config" .
```

### Praktični primjeri

```bash
# Pronađi sve TODO komentare u kodu
grep -rn "TODO" --include="*.py" .

# Pronađi ERROR u log datotekama
grep -i "error" /var/log/*.log

# Filtriraj samo IP adrese iz loga
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log

# Pronađi datoteke s specifičnim tekstom i prikaži 5 linija konteksta
grep -rn -C 5 "database connection" .

# Pretraži sve osim komentara
grep -v "^#" config.conf

# Brzo pronalaženje funkcija u kodu
grep -rn "def funkcija" --include="*.py" .
```

---

# chmod komanda - Dozvole datoteka {#chmod-komanda}

## Što su dozvole?

Svaka datoteka/direktorij ima tri vrste dozvola za tri kategorije korisnika:
- **r** (read) - čitanje - 4
- **w** (write) - pisanje - 2  
- **x** (execute) - izvršavanje - 1

Kategorije:
- **u** (user) - vlasnik
- **g** (group) - grupa
- **o** (others) - ostali
- **a** (all) - svi

## Prikaz dozvola

```bash
ls -l datoteka.txt
# Primjer outputa:
# -rw-r--r-- 1 denis denis 1024 Jan 15 10:30 datoteka.txt
# ↓
# -rw-r--r--
#  ↑↑↑ ↑↑↑ ↑↑↑
#  │   │   └── ostali (r--)
#  │   └────── grupa (r--)
#  └────────── vlasnik (rw-)
```

## Dva načina postavljanja dozvola

### 1. Simbolički način

```bash
# Dodaj execute dozvolu vlasniku
chmod u+x script.sh

# Ukloni write dozvolu ostalima
chmod o-w datoteka.txt

# Dodaj read svima
chmod a+r datoteka.txt

# Postavi read i write vlasniku
chmod u=rw datoteka.txt

# Dodaj execute svima
chmod +x script.sh

# Kombinacije
chmod u+rwx,g+rx,o+r datoteka.txt
```

### 2. Numerički način (octalni)

```bash
# 755 = rwxr-xr-x (najčešće za skripte)
chmod 755 script.sh

# 644 = rw-r--r-- (najčešće za datoteke)
chmod 644 datoteka.txt

# 777 = rwxrwxrwx (OPASNO - sve dozvole svima!)
chmod 777 datoteka.txt

# 600 = rw------- (samo vlasnik može čitati/pisati)
chmod 600 private.key

# 700 = rwx------ (samo vlasnik sve dozvole)
chmod 700 ~/.ssh
```

## Brojevi i dozvole

| Broj | Binarne | Dozvole | Opis |
|------|---------|---------|------|
| 0 | 000 | --- | bez dozvola |
| 1 | 001 | --x | samo izvršavanje |
| 2 | 010 | -w- | samo pisanje |
| 3 | 011 | -wx | pisanje + izvršavanje |
| 4 | 100 | r-- | samo čitanje |
| 5 | 101 | r-x | čitanje + izvršavanje |
| 6 | 110 | rw- | čitanje + pisanje |
| 7 | 111 | rwx | sve dozvole |

## Primjeri

```bash
# Napravi skriptu izvršnom
chmod +x script.sh

# Standardne dozvole za web datoteke
chmod 644 index.html

# Standardne dozvole za web direktorije
chmod 755 public_html/

# Rekurzivno postavi dozvole
chmod -R 755 direktorij/

# Privatni SSH ključ
chmod 600 ~/.ssh/id_rsa

# Javni SSH ključ
chmod 644 ~/.ssh/id_rsa.pub

# SSH direktorij
chmod 700 ~/.ssh/

# Skripte u projektu
find . -name "*.sh" -exec chmod +x {} \;

# Ukloni execute svima
chmod a-x datoteka.txt
```

## Česte kombinacije

```bash
# Direktoriji obično
chmod 755 direktorij/

# Datoteke obično
chmod 644 datoteka.txt

# Izvršne datoteke/skripte
chmod 755 script.sh

# Privatni podaci
chmod 600 sensitive.txt

# Web content
chmod -R 755 ~/public_html/
find ~/public_html -type f -exec chmod 644 {} \;
find ~/public_html -type d -exec chmod 755 {} \;
```

## chown - Promjena vlasnika (bonus)

```bash
# Promjena vlasnika
sudo chown korisnik datoteka.txt

# Promjena vlasnika i grupe
sudo chown korisnik:grupa datoteka.txt

# Rekurzivno
sudo chown -R korisnik:grupa direktorij/

# Samo grupa
sudo chown :grupa datoteka.txt
```

---

## Praktični primjeri za exported_print_formats

```bash
# 1. Stvaranje backup strukture
mkdir -p ~/backups/print_formats

# 2. Arhiviranje
tar -czvf ~/backups/print_formats/backup-$(date +%Y%m%d).tar.gz .

# 3. Kopiranje prije promjena
cp -r ~/exported_print_formats ~/exported_print_formats.backup

# 4. Preimenovanje datoteka
cd ~/exported_print_formats
for file in *_sw.json; do 
    mv "$file" "${file/_sw/}"
done

# 5. Provjera sadržaja
cat ispis_ponude.json | less

# 6. Pronalaženje specifičnog teksta u JSON-ima
grep -r "print_format" *.json

# 7. Postavljanje ispravnih dozvola
chmod 644 *.json
chmod 644 *.png

# 8. Stvaranje nove prazne konfiguracije
touch config.json

# 9. Pronalaženje velikih datoteka
find . -type f -size +1M -ls

# 10. Provjera структуре
tree
```

---

## Brzi cheat sheet

```bash
# ARHIVIRANJE
tar -czvf arhiva.tar.gz direktorij/    # Stvori
tar -xzvf arhiva.tar.gz                # Izvuci
tar -tvf arhiva.tar.gz                 # Pregled

# DATOTEKE
mv staro.txt novo.txt                  # Preimenuj
cp datoteka.txt kopija.txt             # Kopiraj
rm datoteka.txt                        # Obriši
touch nova.txt                         # Stvori praznu

# DIREKTORIJI
mkdir novi_dir                         # Stvori
mkdir -p putanja/do/dir                # Stvori s parent-ima
rm -r direktorij/                      # Obriši direktorij

# ČITANJE
cat datoteka.txt                       # Prikaži sve
less datoteka.txt                      # Interaktivno
head -n 20 datoteka.txt                # Prvih 20 linija
tail -f logfile.log                    # Prati log

# PRETRAŽIVANJE
find . -name "*.txt"                   # Po imenu
find . -size +10M                      # Po veličini
grep -r "error" .                      # U sadržaju
grep -i "todo" *.py                    # Ignoriraj case

# DOZVOLE
chmod 755 script.sh                    # Izvršna skripta
chmod 644 datoteka.txt                 # Obična datoteka
chmod +x script.sh                     # Dodaj execute
```

---

## Sigurnosni savjeti

⚠️ **OPASNE KOMANDE - NIKAD:**
```bash
rm -rf /          # Briše cijeli sistem
chmod 777 -R /    # Otvara sve dozvole (opasno)
chown -R user /   # Mijenja vlasništvo cijelog sistema
```

✅ **SIGURNE PRAKSE:**
```bash
# Uvijek koristi -i za potvrdu
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'

# Prvo provjeri što brišeš
ls *.log
rm -i *.log

# Pravi redovne backupe
tar -czvf backup-$(date +%Y%m%d).tar.gz važni_podaci/

# Testiraj komande prije izvršavanja
echo rm -rf direktorij/  # Vidi što bi se izvršilo
```

---

## Korisni alias-i za .bashrc

Dodaj u `~/.bashrc` za lakši rad:

```bash
# Sigurnost
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Boje i prikaz
alias ls='ls --color=auto'
alias ll='ls -lAh'
alias la='ls -A'
alias l='ls -CF'

# Brzo arhiviranje
alias tarc='tar -czvf'
alias tarx='tar -xzvf'
alias tart='tar -tvf'

# Navigacija
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

# Grep s bojama
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# Brzi pregled
alias h='history'
alias j='jobs -l'
alias df='df -h'
alias du='du -h'

# Git shortcuts (ako koristiš git)
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'

# Brzo čišćenje
alias clean='find . -name "*~" -delete'
```

Nakon dodavanja:
```bash
source ~/.bashrc  # Učitaj promjene
```

---

## Napredne kombinacije komandi

### Pipes i redirekcija

```bash
# Pipe | - output jedne komande u drugu
ls -l | grep ".txt"
cat datoteka.txt | grep "error" | wc -l

# Preusmjeravanje > (prepisuje)
echo "Hello" > datoteka.txt
ls -l > lista.txt

# Dodavanje >> (appendanje)
echo "World" >> datoteka.txt

# Preusmjeravanje grešaka 2>
command 2> errors.log

# I output i errors
command > output.log 2>&1

# Ignoriraj output
command > /dev/null

# Ignoriraj errors
command 2> /dev/null
```

### Kombinacije za obradu datoteka

```bash
# Brojanje linija
wc -l datoteka.txt
cat datoteka.txt | wc -l

# Brojanje riječi
wc -w datoteka.txt

# Brojanje znakova
wc -c datoteka.txt

# Sortiranje
sort datoteka.txt
sort -r datoteka.txt  # Obrnuti redoslijed
sort -n brojevi.txt   # Numeričko sortiranje

# Unique linije
sort datoteka.txt | uniq
sort datoteka.txt | uniq -c  # S brojem ponavljanja

# Pronađi i zamijeni u datoteci
sed 's/staro/novo/g' datoteka.txt
sed -i 's/staro/novo/g' datoteka.txt  # In-place

# Specifične kolone (tab-separated)
cut -f1,3 data.tsv
cut -d',' -f2 data.csv  # CSV
```

### Petlje i automatizacija

```bash
# For petlja - operacije na više datoteka
for file in *.txt; do
    echo "Processing $file"
    wc -l "$file"
done

# Masovno preimenovanje
for file in *.jpeg; do
    mv "$file" "${file%.jpeg}.jpg"
done

# Backup svih konfiguracijskih datoteka
for config in *.conf; do
    cp "$config" "$config.backup-$(date +%Y%m%d)"
done

# Kompresija svih log datoteka starijih od 7 dana
find . -name "*.log" -mtime +7 -exec gzip {} \;

# Batch konverzija (primjer)
for img in *.png; do
    convert "$img" "${img%.png}.jpg"
done
```

---

## Upravljanje procesima (bonus)

```bash
# Vidi sve procese
ps aux

# Vidi procese trenutnog korisnika
ps ux

# Traži specifičan proces
ps aux | grep "python"

# Top - interaktivni prikaz procesa
top
htop  # Ako je instaliran

# Ubij proces po PID-u
kill 1234
kill -9 1234  # Force kill

# Ubij proces po imenu
pkill python
killall python

# Pokreni u pozadini
comando &

# Vidi background procese
jobs

# Vrati proces u foreground
fg %1

# Zaustavi trenutni proces
Ctrl+Z

# Nastavi proces u pozadini
bg %1
```

---

## Disk i memorija

```bash
# Prostor na disku
df -h

# Veličina direktorija
du -sh direktorij/
du -h --max-depth=1 .

# Top 10 najvećih datoteka/direktorija
du -ah . | sort -rh | head -10

# Memorija
free -h

# Disk usage - interaktivno (ako je instaliran)
ncdu
```

---

## Network komande (bonus)

```bash
# Provjera konekcije
ping google.com
ping -c 4 google.com  # 4 pokušaja

# Download datoteke
wget https://example.com/file.zip
curl -O https://example.com/file.zip

# Provjera porta
netstat -tuln
ss -tuln

# Whois informacije
whois example.com

# DNS lookup
nslookup example.com
dig example.com
```

---

## System informacije

```bash
# Verzija OS-a
cat /etc/os-release
lsb_release -a

# Kernel verzija
uname -r
uname -a

# Uptime
uptime

# Hostname
hostname

# Trenutni korisnik
whoami
id

# Prijavljeni korisnici
who
w

# Datum i vrijeme
date
date +%Y-%m-%d
date +%H:%M:%S

# Kalendar
cal
cal 2025
```

---

## Kompletni praktični primjer - Backup skripta

Stvori datoteku `backup.sh`:

```bash
#!/bin/bash

# Backup skripta za print formats

# Varijable
SOURCE_DIR="$HOME/exported_print_formats"
BACKUP_DIR="$HOME/backups/print_formats"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_$DATE.tar.gz"

# Stvori backup direktorij ako ne postoji
mkdir -p "$BACKUP_DIR"

# Napravi backup
echo "Stvaram backup: $BACKUP_FILE"
tar -czvf "$BACKUP_DIR/$BACKUP_FILE" -C "$SOURCE_DIR" .

# Provjeri uspjeh
if [ $? -eq 0 ]; then
    echo "✓ Backup uspješno stvoren: $BACKUP_DIR/$BACKUP_FILE"
    
    # Prikaži veličinu
    ls -lh "$BACKUP_DIR/$BACKUP_FILE"
    
    # Obriši backupe starije od 30 dana
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +30 -delete
    echo "✓ Stari backupi obrisani"
else
    echo "✗ Greška pri stvaranju backupa!"
    exit 1
fi
```

Napravi izvršnom i pokreni:

```bash
chmod +x backup.sh
./backup.sh
```

---

## Još korisnih trikova

```bash
# Zadnja komanda
!!

# Pokreni zadnju komandu s sudo
sudo !!

# Argumenti zadnje komande
!$
!*

# Brza zamjena u zadnjoj komandi
^staro^novo

# History pretraga
Ctrl+R  # Pa tipkaj za pretragu

# Clear screen
clear
Ctrl+L

# Zaustavi trenutni proces
Ctrl+C

# EOF (end of input)
Ctrl+D

# Autocomplete
Tab  # Jednom
Tab Tab  # Dvaput za opcije

# Wildcards
*       # Bilo što
?       # Jedan znak
[abc]   # a, b, ili c
[0-9]   # Bilo koji broj
{a,b}   # a ili b

# Primjeri wildcards
ls *.txt           # Sve txt datoteke
ls test?.txt       # test1.txt, test2.txt, ...
ls [a-c]*.txt      # Počinje s a, b, ili c
cp file.{txt,bak}  # cp file.txt file.bak
```

---

## Debugging i troubleshooting

```bash
# Detaljni output komande
bash -x script.sh

# Provjeri sintaksu bez izvršavanja
bash -n script.sh

# Verbalni mod
set -v

# Exit on error
set -e

# Tracing
set -x

# Provjeri postoji li datoteka
test -f datoteka.txt && echo "Postoji"
[ -f datoteka.txt ] && echo "Postoji"

# Provjeri postoji li direktorij
test -d direktorij && echo "Postoji"
[ -d direktorij ] && echo "Postoji"

# Provjeri je li izvršno
[ -x script.sh ] && echo "Izvršno"

# Provjeri je li prazna datoteka
[ -s datoteka.txt ] || echo "Prazna je"
```

---

## Man pages i pomoć

```bash
# Manual stranica za komandu
man ls
man tar
man grep

# Kratka pomoć
ls --help
tar --help

# Info stranice (detaljnije od man)
info coreutils

# Koja verzija komande
which python
whereis python

# Tip komande
type ls
type cd

# Apropos - traži u man stranicama
apropos search
man -k search
```

---

## Zaključak

Ovo su najvažnije Linux komande koje pokrivaju:
- ✓ Upravljanje datotekama (cp, mv, rm, touch)
- ✓ Direktoriji (mkdir)
- ✓ Arhiviranje (tar)
- ✓ Čitanje datoteka (cat, less, head, tail)
- ✓ Pretraživanje (find, grep)
- ✓ Dozvole (chmod)

**Zapamti:**
1. Uvijek koristi `-i` za potvrdu
2. Pravi redovne backupe
3. Testiraj opasne komande s `echo` prvo
4. Koristi `man` kad si nesiguran
5. Tab completion je tvoj prijatelj

**Vježbaj:**
```bash
mkdir test_dir
cd test_dir
touch file1.txt file2.txt
echo "Hello World" > file1.txt
cat file1.txt
cp file1.txt file1_backup.txt
tar -czvf backup.tar.gz *.txt
ls -lh
rm -i file2.txt
cd ..
rm -r test_dir
```

---

**Autor:** Linux Command Line Guide  
**Verzija:** 2.0  
**Zadnje ažurirano:** Oktobar 2025