# Python Osnove i OOP - Kompletni Vodič

## Sadržaj
1. [Python Osnove](#python-osnove)
2. [Varijable i Tipovi podataka](#varijable-i-tipovi)
3. [Kontrolne strukture](#kontrolne-strukture)
4. [Funkcije](#funkcije)
5. [Liste, Tuple, Dictionary, Set](#kolekcije)
6. [OOP - Klase i Objekti](#oop-klase)
7. [Atributi i Metode](#atributi-metode)
8. [Konstruktor i self](#konstruktor-self)
9. [Nasljeđivanje](#nasljedivanje)
10. [Enkapsulacija](#enkapsulacija)
11. [Polimorfizam](#polimorfizam)
12. [Specijalne metode (Magic methods)](#specijalne-metode)
13. [Dekoratori i Properties](#dekoratori)
14. [Praktični primjeri](#prakticni-primjeri)

---

# Python Osnove {#python-osnove}

## Pokretanje Python koda

```python
# Iz terminala
python script.py
python3 script.py

# Interaktivni mod
python
>>> print("Hello World")

# Python interpreter
#!/usr/bin/env python3
```

## Print i Input

```python
# Print
print("Hello World")
print("Ime:", "Denis", "Prezime:", "Horvat")
print(f"Ime: {ime}, Prezime: {prezime}")  # f-string (najbolji način)

# Input
ime = input("Unesi ime: ")
godine = int(input("Unesi godine: "))
cijena = float(input("Unesi cijenu: "))
```

## Komentari

```python
# Ovo je komentar u jednoj liniji

"""
Ovo je komentar
u više linija
"""

'''
I ovo je multi-line
komentar
'''
```

---

# Varijable i Tipovi podataka {#varijable-i-tipovi}

## Osnovni tipovi

```python
# Integer (cijeli brojevi)
x = 10
y = -5

# Float (decimalni brojevi)
cijena = 19.99
pi = 3.14159

# String (tekst)
ime = "Denis"
prezime = 'Horvat'
poruka = """Multi-line
string"""

# Boolean (True/False)
je_aktivan = True
je_admin = False

# None (null vrijednost)
rezultat = None
```

## Provjera tipa

```python
x = 10
print(type(x))  # <class 'int'>

ime = "Denis"
print(type(ime))  # <class 'str'>

# Provjera tipa
isinstance(x, int)  # True
isinstance(ime, str)  # True
```

## Konverzije tipova

```python
# String u broj
broj = int("123")
decimala = float("19.99")

# Broj u string
tekst = str(123)

# List u string
lista = [1, 2, 3]
tekst = str(lista)

# String u list
tekst = "Hello"
lista = list(tekst)  # ['H', 'e', 'l', 'l', 'o']
```

## String operacije

```python
ime = "Denis"

# Konkatenacija
puno_ime = ime + " " + "Horvat"

# Ponavljanje
tekst = "Ha" * 3  # "HaHaHa"

# Duljina
len(ime)  # 5

# Upper/Lower
ime.upper()  # "DENIS"
ime.lower()  # "denis"
ime.title()  # "Denis"

# Strip (uklanja whitespace)
tekst = "  hello  "
tekst.strip()  # "hello"

# Replace
tekst = "Hello World"
tekst.replace("World", "Python")  # "Hello Python"

# Split
tekst = "jedan,dva,tri"
lista = tekst.split(",")  # ['jedan', 'dva', 'tri']

# Join
lista = ['jedan', 'dva', 'tri']
tekst = ",".join(lista)  # "jedan,dva,tri"

# Formatiranje
ime = "Denis"
godine = 30
# F-string (Python 3.6+)
poruka = f"Ja sam {ime} i imam {godine} godina"
# Format metoda
poruka = "Ja sam {} i imam {} godina".format(ime, godine)
# Stariji način
poruka = "Ja sam %s i imam %d godina" % (ime, godine)
```

---

# Kontrolne strukture {#kontrolne-strukture}

## If/Elif/Else

```python
# Osnovno
godine = 18
if godine >= 18:
    print("Punoljetan")
else:
    print("Maloljetan")

# Elif
ocjena = 85
if ocjena >= 90:
    print("Odličan")
elif ocjena >= 75:
    print("Vrlo dobar")
elif ocjena >= 60:
    print("Dobar")
else:
    print("Nedovoljan")

# Inline if
status = "Aktivan" if je_aktivan else "Neaktivan"

# Multiple uvjeti
if godine >= 18 and ima_dozvolu:
    print("Može voziti")

if je_vikend or je_praznik:
    print("Slobodan dan")

# Not
if not je_obrađeno:
    print("Treba obraditi")
```

## For petlja

```python
# For kroz range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# For kroz listu
imena = ["Denis", "Ana", "Marko"]
for ime in imena:
    print(ime)

# For s indexom
for i, ime in enumerate(imena):
    print(f"{i}: {ime}")

# For kroz dictionary
osoba = {"ime": "Denis", "godine": 30}
for kljuc, vrijednost in osoba.items():
    print(f"{kljuc}: {vrijednost}")

# List comprehension
kvadrati = [x**2 for x in range(10)]
parni = [x for x in range(10) if x % 2 == 0]
```

## While petlja

```python
# Osnovno
i = 0
while i < 5:
    print(i)
    i += 1

# Sa break
while True:
    odgovor = input("Unesi 'quit' za izlaz: ")
    if odgovor == 'quit':
        break

# Sa continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)  # Ispisuje samo neparne
```

---

# Funkcije {#funkcije}

## Osnovna deklaracija

```python
# Jednostavna funkcija
def pozdrav():
    print("Hello World")

pozdrav()  # Poziv funkcije

# Funkcija s parametrima
def pozdrav_korisnik(ime):
    print(f"Hello {ime}")

pozdrav_korisnik("Denis")

# Funkcija s return
def zbroj(a, b):
    return a + b

rezultat = zbroj(5, 3)  # 8

# Više return vrijednosti
def operacije(a, b):
    return a + b, a - b, a * b, a / b

suma, razlika, produkt, kvocijent = operacije(10, 5)
```

## Default parametri

```python
def pozdrav(ime, poruka="Hello"):
    print(f"{poruka} {ime}")

pozdrav("Denis")  # Hello Denis
pozdrav("Denis", "Hi")  # Hi Denis

# Keyword argumenti
def info_osoba(ime, prezime, godine):
    print(f"{ime} {prezime}, {godine} godina")

info_osoba(ime="Denis", godine=30, prezime="Horvat")
```

## *args i **kwargs

```python
# *args - varijabilan broj argumenata
def suma(*brojevi):
    return sum(brojevi)

print(suma(1, 2, 3))  # 6
print(suma(1, 2, 3, 4, 5))  # 15

# **kwargs - keyword argumenti
def ispis_info(**info):
    for kljuc, vrijednost in info.items():
        print(f"{kljuc}: {vrijednost}")

ispis_info(ime="Denis", godine=30, grad="Zagreb")

# Kombinacija
def funkcija(obavezan, *args, default="test", **kwargs):
    print(obavezan)
    print(args)
    print(default)
    print(kwargs)

funkcija("prvi", "drugi", "treći", key1="value1", key2="value2")
```

## Lambda funkcije

```python
# Lambda - anonimna funkcija
kvadrat = lambda x: x**2
print(kvadrat(5))  # 25

suma = lambda a, b: a + b
print(suma(3, 4))  # 7

# Korištenje s map, filter
brojevi = [1, 2, 3, 4, 5]
kvadrati = list(map(lambda x: x**2, brojevi))
parni = list(filter(lambda x: x % 2 == 0, brojevi))
```

---

# Kolekcije {#kolekcije}

## Liste (List)

```python
# Stvaranje liste
lista = [1, 2, 3, 4, 5]
imena = ["Denis", "Ana", "Marko"]
mijesana = [1, "tekst", 3.14, True]
prazna = []

# Pristup elementima
prvi = lista[0]  # 1
zadnji = lista[-1]  # 5
slice = lista[1:3]  # [2, 3]

# Dodavanje
lista.append(6)  # Dodaj na kraj
lista.insert(0, 0)  # Dodaj na poziciju
lista.extend([7, 8, 9])  # Dodaj više elemenata

# Uklanjanje
lista.remove(3)  # Ukloni element
element = lista.pop()  # Ukloni i vrati zadnji
element = lista.pop(0)  # Ukloni i vrati na indeksu
lista.clear()  # Ukloni sve

# Ostale operacije
len(lista)  # Duljina
lista.count(2)  # Broji pojavljivanja
lista.index(3)  # Pronađi indeks
lista.sort()  # Sortiraj
lista.reverse()  # Obrni

# Provjera
if 5 in lista:
    print("5 je u listi")

# List comprehension
kvadrati = [x**2 for x in range(10)]
parni = [x for x in range(10) if x % 2 == 0]
```

## Tuple

```python
# Immutable lista
tuple_obj = (1, 2, 3)
koordinate = (10.5, 20.3)

# Pristup kao kod liste
prvi = tuple_obj[0]

# Unpacking
x, y = koordinate
a, b, c = tuple_obj

# Ne može se mijenjati
# tuple_obj[0] = 5  # ERROR!

# Tuple s jednim elementom
single = (1,)  # Zapazi zarez!
```

## Dictionary (Dict)

```python
# Stvaranje
osoba = {
    "ime": "Denis",
    "prezime": "Horvat",
    "godine": 30
}

# Pristup
ime = osoba["ime"]
ime = osoba.get("ime")  # Sigurniji način
ime = osoba.get("srednje_ime", "N/A")  # Default vrijednost

# Dodavanje/Izmjena
osoba["grad"] = "Zagreb"
osoba["godine"] = 31

# Uklanjanje
del osoba["grad"]
godine = osoba.pop("godine")

# Iteracija
for kljuc in osoba:
    print(kljuc)

for vrijednost in osoba.values():
    print(vrijednost)

for kljuc, vrijednost in osoba.items():
    print(f"{kljuc}: {vrijednost}")

# Provjera
if "ime" in osoba:
    print("Ime postoji")

# Dictionary comprehension
kvadrati = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Set

```python
# Jedinstveni elementi, nesortirani
skup = {1, 2, 3, 4, 5}
skup2 = {4, 5, 6, 7, 8}

# Dodavanje
skup.add(6)
skup.update([7, 8, 9])

# Uklanjanje
skup.remove(1)  # Greška ako ne postoji
skup.discard(1)  # Nema greške

# Set operacije
unija = skup | skup2
presjek = skup & skup2
razlika = skup - skup2
simetricna = skup ^ skup2

# Provjera
if 5 in skup:
    print("5 je u skupu")
```

---

# OOP - Klase i Objekti {#oop-klase}

## Što je OOP?

**Objektno Orijentirano Programiranje (OOP)** je paradigma koja organizira kod oko "objekata" koji sadrže podatke (atribute) i funkcije (metode).

### Četiri stupa OOP-a:
1. **Enkapsulacija** - Sakrivanje detalja implementacije
2. **Apstrakcija** - Fokus na bitno, sakrivanje kompleksnosti
3. **Nasljeđivanje** - Stvaranje novih klasa iz postojećih
4. **Polimorfizam** - Isti interface, različite implementacije

## Osnovna klasa

```python
# Definicija klase
class Osoba:
    pass  # Prazna klasa

# Stvaranje objekta (instanciranje)
osoba1 = Osoba()
osoba2 = Osoba()

print(type(osoba1))  # <class '__main__.Osoba'>
```

---

# Atributi i Metode {#atributi-metode}

## Atributi instance

```python
class Osoba:
    def __init__(self, ime, prezime, godine):
        # Atributi instance
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

# Stvaranje objekata
osoba1 = Osoba("Denis", "Horvat", 30)
osoba2 = Osoba("Ana", "Kovač", 25)

# Pristup atributima
print(osoba1.ime)  # Denis
print(osoba2.ime)  # Ana

# Izmjena atributa
osoba1.godine = 31
```

## Metode instance

```python
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
    
    def predstavi_se(self):
        return f"Ja sam {self.ime} {self.prezime}, imam {self.godine} godina"
    
    def je_punoljetan(self):
        return self.godine >= 18
    
    def rodjendan(self):
        self.godine += 1
        return f"Sretno {self.godine}!"

# Korištenje
osoba = Osoba("Denis", "Horvat", 30)
print(osoba.predstavi_se())  # Ja sam Denis Horvat, imam 30 godina
print(osoba.je_punoljetan())  # True
print(osoba.rodjendan())  # Sretno 31!
```

## Class atributi (dijeljeni)

```python
class Zaposlenik:
    # Class atribut - dijele svi objekti
    kompanija = "Moja Firma d.o.o."
    broj_zaposlenika = 0
    
    def __init__(self, ime, placa):
        self.ime = ime
        self.placa = placa
        Zaposlenik.broj_zaposlenika += 1
    
    def info(self):
        return f"{self.ime} radi u {Zaposlenik.kompanija}"

# Korištenje
z1 = Zaposlenik("Denis", 5000)
z2 = Zaposlenik("Ana", 6000)

print(z1.info())  # Denis radi u Moja Firma d.o.o.
print(Zaposlenik.broj_zaposlenika)  # 2

# Promjena class atributa
Zaposlenik.kompanija = "Nova Firma d.o.o."
print(z1.info())  # Denis radi u Nova Firma d.o.o.
print(z2.info())  # Ana radi u Nova Firma d.o.o.
```

## Class metode i Static metode

```python
class Kalkulator:
    pi = 3.14159
    
    def __init__(self, broj):
        self.broj = broj
    
    # Instance metoda
    def kvadrat(self):
        return self.broj ** 2
    
    # Class metoda - prima cls (klasu) kao prvi parametar
    @classmethod
    def iz_stringa(cls, string):
        broj = int(string)
        return cls(broj)
    
    # Static metoda - ne prima ni self ni cls
    @staticmethod
    def zbroj(a, b):
        return a + b
    
    @staticmethod
    def opseg_kruga(radijus):
        return 2 * Kalkulator.pi * radijus

# Korištenje
k1 = Kalkulator(5)
print(k1.kvadrat())  # 25

# Class metoda - alternativni konstruktor
k2 = Kalkulator.iz_stringa("10")
print(k2.kvadrat())  # 100

# Static metode
print(Kalkulator.zbroj(5, 3))  # 8
print(Kalkulator.opseg_kruga(10))  # 62.8318
```

---

# Konstruktor i self {#konstruktor-self}

## __init__ konstruktor

```python
class Automobil:
    def __init__(self, marka, model, godina):
        """
        Konstruktor - poziva se automatski pri stvaranju objekta
        self - referenca na trenutnu instancu
        """
        self.marka = marka
        self.model = model
        self.godina = godina
        self.kilometraza = 0  # Default vrijednost
    
    def vozi(self, km):
        self.kilometraza += km
        return f"Prešao {km} km. Ukupno: {self.kilometraza} km"

# Stvaranje
auto = Automobil("Toyota", "Corolla", 2020)
print(auto.marka)  # Toyota
print(auto.vozi(100))  # Prešao 100 km. Ukupno: 100 km
```

## Razumijevanje self

```python
class Primjer:
    def __init__(self, vrijednost):
        # self.vrijednost je atribut objekta
        self.vrijednost = vrijednost
    
    def ispis(self):
        # self koristi se za pristup atributima
        print(f"Vrijednost: {self.vrijednost}")
    
    def promijeni(self, nova):
        # self koristi se za izmjenu atributa
        self.vrijednost = nova

obj1 = Primjer(10)
obj2 = Primjer(20)

obj1.ispis()  # Vrijednost: 10
obj2.ispis()  # Vrijednost: 20

# Kada pozoveš obj1.ispis(), Python automatski šalje obj1 kao self
# Ekvivalentno je: Primjer.ispis(obj1)
```

---

# Nasljeđivanje {#nasljedivanje}

## Osnovno nasljeđivanje

```python
# Parent (bazna) klasa
class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    
    def predstavi_se(self):
        return f"Ja sam {self.ime} {self.prezime}"

# Child (izvedena) klasa
class Student(Osoba):
    def __init__(self, ime, prezime, indeks):
        super().__init__(ime, prezime)  # Pozovi konstruktor parent klase
        self.indeks = indeks
    
    def info(self):
        return f"{self.predstavi_se()}, indeks: {self.indeks}"

# Korištenje
student = Student("Denis", "Horvat", "12345")
print(student.predstavi_se())  # Ja sam Denis Horvat
print(student.info())  # Ja sam Denis Horvat, indeks: 12345
```

## Overriding metoda

```python
class Zaposlenik(Osoba):
    def __init__(self, ime, prezime, pozicija):
        super().__init__(ime, prezime)
        self.pozicija = pozicija
    
    # Override metode iz parent klase
    def predstavi_se(self):
        return f"Ja sam {self.ime} {self.prezime}, radim kao {self.pozicija}"

zaposlenik = Zaposlenik("Ana", "Kovač", "Developer")
print(zaposlenik.predstavi_se())  
# Ja sam Ana Kovač, radim kao Developer
```

## Višestruko nasljeđivanje

```python
class A:
    def metoda_a(self):
        return "Metoda iz A"

class B:
    def metoda_b(self):
        return "Metoda iz B"

class C(A, B):  # Nasljeđuje od A i B
    def metoda_c(self):
        return "Metoda iz C"

obj = C()
print(obj.metoda_a())  # Metoda iz A
print(obj.metoda_b())  # Metoda iz B
print(obj.metoda_c())  # Metoda iz C
```

## Praktičan primjer nasljeđivanja

```python
class Vozilo:
    def __init__(self, marka, brzina_max):
        self.marka = marka
        self.brzina_max = brzina_max
        self.brzina = 0
    
    def ubrzaj(self, iznos):
        self.brzina = min(self.brzina + iznos, self.brzina_max)
        return f"Brzina: {self.brzina} km/h"
    
    def zakoci(self):
        self.brzina = 0
        return "Vozilo zaustavljeno"

class Automobil(Vozilo):
    def __init__(self, marka, brzina_max, broj_vrata):
        super().__init__(marka, brzina_max)
        self.broj_vrata = broj_vrata
    
    def info(self):
        return f"{self.marka}, {self.broj_vrata} vrata, max {self.brzina_max} km/h"

class Motocikl(Vozilo):
    def __init__(self, marka, brzina_max, tip):
        super().__init__(marka, brzina_max)
        self.tip = tip
    
    def wheelie(self):
        return "Radi wheelie!" if self.brzina > 50 else "Prebrzo za wheelie"

# Korištenje
auto = Automobil("Toyota", 180, 4)
motor = Motocikl("Yamaha", 250, "Sport")

print(auto.info())  # Toyota, 4 vrata, max 180 km/h
print(auto.ubrzaj(50))  # Brzina: 50 km/h

print(motor.ubrzaj(100))  # Brzina: 100 km/h
print(motor.wheelie())  # Radi wheelie!
```

---

# Enkapsulacija {#enkapsulacija}

## Public, Protected, Private

```python
class BankovniRacun:
    def __init__(self, vlasnik, stanje):
        self.vlasnik = vlasnik  # Public
        self._stanje = stanje  # Protected (konvencija)
        self.__pin = "1234"  # Private (name mangling)
    
    # Public metoda
    def provjeri_stanje(self):
        return f"Stanje: {self._stanje} EUR"
    
    # Public metoda za pristup private atributu
    def provjeri_pin(self, pin):
        return self.__pin == pin
    
    def uplati(self, iznos):
        if iznos > 0:
            self._stanje += iznos
            return f"Uplaćeno: {iznos} EUR"
        return "Neispravan iznos"
    
    def podigni(self, iznos, pin):
        if not self.provjeri_pin(pin):
            return "Neispravan PIN"
        if iznos > self._stanje:
            return "Nedovoljno sredstava"
        self._stanje -= iznos
        return f"Podignuto: {iznos} EUR"

# Korištenje
racun = BankovniRacun("Denis", 1000)

print(racun.vlasnik)  # Denis (Public - OK)
print(racun._stanje)  # 1000 (Protected - može se, ali ne bi trebalo)
# print(racun.__pin)  # ERROR! Private atribut

print(racun.provjeri_stanje())  # Stanje: 1000 EUR
print(racun.uplati(500))  # Uplaćeno: 500 EUR
print(racun.podigni(200, "1234"))  # Podignuto: 200 EUR
print(racun.podigni(200, "0000"))  # Neispravan PIN
```

## Getteri i Setteri

```python
class Temperatura:
    def __init__(self, celzij):
        self._celzij = celzij
    
    # Getter
    def get_celzij(self):
        return self._celzij
    
    # Setter
    def set_celzij(self, vrijednost):
        if vrijednost < -273.15:
            raise ValueError("Temperatura ne može biti ispod apsolutne nule")
        self._celzij = vrijednost
    
    # Getter za Fahrenheit
    def get_fahrenheit(self):
        return (self._celzij * 9/5) + 32

# Korištenje
temp = Temperatura(25)
print(temp.get_celzij())  # 25
print(temp.get_fahrenheit())  # 77.0

temp.set_celzij(30)
print(temp.get_celzij())  # 30

# temp.set_celzij(-300)  # ERROR! ValueError
```

---

# Polimorfizam {#polimorfizam}

## Ista metoda, različito ponašanje

```python
class Pas:
    def zvuk(self):
        return "Vau vau!"
    
    def opis(self):
        return "Ovo je pas"

class Macka:
    def zvuk(self):
        return "Mijau!"
    
    def opis(self):
        return "Ovo je mačka"

class Krava:
    def zvuk(self):
        return "Muuu!"
    
    def opis(self):
        return "Ovo je krava"

# Polimorfizam - ista funkcija, različiti objekti
def zivotinja_zvuk(zivotinja):
    print(zivotinja.opis())
    print(zivotinja.zvuk())
    print()

# Korištenje
pas = Pas()
macka = Macka()
krava = Krava()

zivotinja_zvuk(pas)
zivotinja_zvuk(macka)
zivotinja_zvuk(krava)

# Lista različitih objekata
zivotinje = [Pas(), Macka(), Krava()]
for zivotinja in zivotinje:
    print(zivotinja.zvuk())
```

## Polimorfizam s nasljeđivanjem

```python
class Oblik:
    def povrsina(self):
        pass
    
    def opseg(self):
        pass

class Pravokutnik(Oblik):
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina
    
    def povrsina(self):
        return self.sirina * self.visina
    
    def opseg(self):
        return 2 * (self.sirina + self.visina)

class Krug(Oblik):
    def __init__(self, radijus):
        self.radijus = radijus
    
    def povrsina(self):
        return 3.14159 * self.radijus ** 2
    
    def opseg(self):
        return 2 * 3.14159 * self.radijus

# Polimorfizam
def ispis_info(oblik):
    print(f"Površina: {oblik.povrsina():.2f}")
    print(f"Opseg: {oblik.opseg():.2f}")
    print()

pravokutnik = Pravokutnik(5, 10)
krug = Krug(7)

ispis_info(pravokutnik)
ispis_info(krug)
```

---

# Specijalne metode (Magic methods) {#specijalne-metode}

## __str__ i __repr__

```python
class Proizvod:
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cijena = cijena
    
    def __str__(self):
        # Za print() - čitljivo za korisnika
        return f"{self.naziv} - {self.cijena} EUR"
    
    def __repr__(self):
        # Za debugiranje - nedvosmisleno
        return f"Proizvod('{self.naziv}', {self.cijena})"

proizvod = Proizvod("Laptop", 899.99)
print(proizvod)  # Laptop - 899.99 EUR
print(repr(proizvod))  # Proizvod('Laptop', 899.99)