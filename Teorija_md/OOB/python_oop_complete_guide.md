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
14. [Abstract Base Classes](#abstract-classes)
15. [Praktični primjeri](#prakticni-primjeri)
16. [Napredni koncepti](#napredni-koncepti)

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

# Python interpreter (shebang)
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
(docstring)
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

# Upper/Lower/Title
ime.upper()  # "DENIS"
ime.lower()  # "denis"
ime.title()  # "Denis"

# Strip (uklanja whitespace)
tekst = "  hello  "
tekst.strip()  # "hello"
tekst.lstrip()  # "hello  "
tekst.rstrip()  # "  hello"

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
# F-string (Python 3.6+) - preporučeno
poruka = f"Ja sam {ime} i imam {godine} godina"
# Format metoda
poruka = "Ja sam {} i imam {} godina".format(ime, godine)
# Stariji način
poruka = "Ja sam %s i imam %d godina" % (ime, godine)

# String metode
tekst = "Python Programming"
tekst.startswith("Py")  # True
tekst.endswith("ing")  # True
tekst.find("on")  # 4
tekst.count("m")  # 2
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

# Inline if (ternary operator)
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

# For s indeksom od određenog broja
for i, ime in enumerate(imena, start=1):
    print(f"{i}. {ime}")

# For kroz dictionary
osoba = {"ime": "Denis", "godine": 30}
for kljuc in osoba:
    print(kljuc)

for vrijednost in osoba.values():
    print(vrijednost)

for kljuc, vrijednost in osoba.items():
    print(f"{kljuc}: {vrijednost}")

# List comprehension
kvadrati = [x**2 for x in range(10)]
parni = [x for x in range(10) if x % 2 == 0]
matrica = [[i*j for j in range(3)] for i in range(3)]
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

# While/else (izvršava se ako nije bio break)
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Petlja završena normalno")
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

# Korištenje s map, filter, sorted
brojevi = [1, 2, 3, 4, 5]
kvadrati = list(map(lambda x: x**2, brojevi))
parni = list(filter(lambda x: x % 2 == 0, brojevi))
ljudi = [("Ana", 25), ("Denis", 30), ("Ivan", 20)]
sortirano = sorted(ljudi, key=lambda x: x[1])  # Po godinama
```

## Type hints (Python 3.5+)

```python
def pozdrav(ime: str) -> str:
    return f"Hello {ime}"

def zbroj(a: int, b: int) -> int:
    return a + b

from typing import List, Dict, Optional, Union

def filtriraj_parne(brojevi: List[int]) -> List[int]:
    return [x for x in brojevi if x % 2 == 0]

def dohvati_korisnika(id: int) -> Optional[Dict[str, str]]:
    # Vraća dict ili None
    pass
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
slice_sa_korakom = lista[::2]  # [1, 3, 5]

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
lista.sort()  # Sortiraj (in-place)
lista.sort(reverse=True)  # Sortiraj silazno
sorted(lista)  # Nova sortirana lista
lista.reverse()  # Obrni (in-place)

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

# Tuple bez zagrada
tuple_bez = 1, 2, 3

# Korisno za vraćanje više vrijednosti
def min_max(lista):
    return min(lista), max(lista)

minimum, maksimum = min_max([1, 5, 3, 9, 2])
```

## Dictionary (Dict)

```python
# Stvaranje
osoba = {
    "ime": "Denis",
    "prezime": "Horvat",
    "godine": 30
}

# Drugi način
osoba2 = dict(ime="Ana", prezime="Kovač", godine=25)

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
osoba.popitem()  # Ukloni zadnji par (Python 3.7+)

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

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2

# Update
dict1.update(dict2)
```

## Set

```python
# Jedinstveni elementi, nesortirani
skup = {1, 2, 3, 4, 5}
skup2 = {4, 5, 6, 7, 8}

# Stvaranje praznog seta
prazan = set()  # NE {}! To je dict

# Dodavanje
skup.add(6)
skup.update([7, 8, 9])

# Uklanjanje
skup.remove(1)  # Greška ako ne postoji
skup.discard(1)  # Nema greške
skup.pop()  # Ukloni i vrati proizvoljan element

# Set operacije
unija = skup | skup2  # ili skup.union(skup2)
presjek = skup & skup2  # ili skup.intersection(skup2)
razlika = skup - skup2  # ili skup.difference(skup2)
simetricna = skup ^ skup2  # ili skup.symmetric_difference(skup2)

# Provjera
if 5 in skup:
    print("5 je u skupu")

# Set comprehension
kvadrati_set = {x**2 for x in range(10)}
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

# Dinamičko dodavanje atributa (ne preporučuje se)
osoba1.grad = "Zagreb"
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

# MRO - Method Resolution Order
print(C.mro())  # [C, A, B, object]
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
        return "Radi wheelie!" if self.brzina > 50 else "Presporo za wheelie"

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

# Name mangling - pristup private atributu (ne preporučuje se)
print(racun._BankovniRacun__pin)  # 1234
```

## Getteri i Setteri (klasičan način)

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
print([proizvod])  # [Proizvod('Laptop', 899.99)]
```

## Aritmetičke operacije

```python
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    # Zbrajanje
    def __add__(self, drugi):
        return Vektor(self.x + drugi.x, self.y + drugi.y)

    # Oduzimanje
    def __sub__(self, drugi):
        return Vektor(self.x - drugi.x, self.y - drugi.y)

    # Množenje skalarom
    def __mul__(self, skalar):
        return Vektor(self.x * skalar, self.y * skalar)

    # Dijeljenje
    def __truediv__(self, skalar):
        return Vektor(self.x / skalar, self.y / skalar)

    # Jednakost
    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    # Duljina vektora
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

# Korištenje
v1 = Vektor(2, 3)
v2 = Vektor(4, 1)

print(v1 + v2)  # Vektor(6, 4)
print(v1 - v2)  # Vektor(-2, 2)
print(v1 * 3)   # Vektor(6, 9)
print(v1 == v2)  # False
print(abs(v1))  # 3.605551275463989
```

## Usporedbe

```python
class Osoba:
    def __init__(self, ime, godine):
        self.ime = ime
        self.godine = godine

    def __lt__(self, druga):  # Less than <
        return self.godine < druga.godine

    def __le__(self, druga):  # Less or equal <=
        return self.godine <= druga.godine

    def __gt__(self, druga):  # Greater than >
        return self.godine > druga.godine

    def __ge__(self, druga):  # Greater or equal >=
        return self.godine >= druga.godine

    def __eq__(self, druga):  # Equal ==
        return self.godine == druga.godine

    def __str__(self):
        return f"{self.ime} ({self.godine})"

osoba1 = Osoba("Denis", 30)
osoba2 = Osoba("Ana", 25)

print(osoba1 > osoba2)  # True
print(osoba1 < osoba2)  # False

# Sortiranje
ljudi = [Osoba("Marko", 35), Osoba("Ana", 25), Osoba("Ivan", 30)]
ljudi_sortirano = sorted(ljudi)
for osoba in ljudi_sortirano:
    print(osoba)
```

## Container metode

```python
class KolekcijaBrojeva:
    def __init__(self):
        self.brojevi = []

    # Duljina - len()
    def __len__(self):
        return len(self.brojevi)

    # Pristup po indeksu - obj[i]
    def __getitem__(self, index):
        return self.brojevi[index]

    # Postavljanje po indeksu - obj[i] = value
    def __setitem__(self, index, value):
        self.brojevi[index] = value

    # Brisanje - del obj[i]
    def __delitem__(self, index):
        del self.brojevi[index]

    # Provjera - if x in obj
    def __contains__(self, item):
        return item in self.brojevi

    # Iteracija - for x in obj
    def __iter__(self):
        return iter(self.brojevi)

    def dodaj(self, broj):
        self.brojevi.append(broj)

# Korištenje
kolekcija = KolekcijaBrojeva()
kolekcija.dodaj(10)
kolekcija.dodaj(20)
kolekcija.dodaj(30)

print(len(kolekcija))  # 3
print(kolekcija[0])  # 10
print(20 in kolekcija)  # True

for broj in kolekcija:
    print(broj)
```

## Poziv kao funkcija - __call__

```python
class Pozdrav:
    def __init__(self, poruka):
        self.poruka = poruka

    def __call__(self, ime):
        return f"{self.poruka}, {ime}!"

pozdrav = Pozdrav("Hello")
print(pozdrav("Denis"))  # Hello, Denis!
print(pozdrav("Ana"))  # Hello, Ana!

# Objekt se ponaša kao funkcija

# Praktičan primjer - brojač
class Brojac:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

brojac = Brojac()
print(brojac())  # 1
print(brojac())  # 2
print(brojac())  # 3
```

## Context Manager - with statement

```python
class Datoteka:
    def __init__(self, naziv, mod):
        self.naziv = naziv
        self.mod = mod
        self.file = None

    def __enter__(self):
        print(f"Otvaranje datoteke {self.naziv}")
        self.file = open(self.naziv, self.mod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Zatvaranje datoteke {self.naziv}")
        if self.file:
            self.file.close()
        # Ako vraća True, iznimke se ignoriraju
        return False

# Korištenje
with Datoteka("test.txt", "w") as f:
    f.write("Hello World")
# Datoteka se automatski zatvara
```

---

# Dekoratori i Properties {#dekoratori}

## @property dekorator

```python
class Temperatura:
    def __init__(self, celzij):
        self._celzij = celzij

    @property
    def celzij(self):
        """Getter za celzije"""
        return self._celzij

    @celzij.setter
    def celzij(self, vrijednost):
        """Setter za celzije"""
        if vrijednost < -273.15:
            raise ValueError("Ispod apsolutne nule!")
        self._celzij = vrijednost

    @celzij.deleter
    def celzij(self):
        """Deleter za celzije"""
        del self._celzij

    @property
    def fahrenheit(self):
        """Getter za fahrenheit - automatski računato"""
        return (self._celzij * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, vrijednost):
        """Setter za fahrenheit - automatski pretvara"""
        self._celzij = (vrijednost - 32) * 5/9

# Korištenje - kao atribut, ne metoda!
temp = Temperatura(25)
print(temp.celzij)  # 25 (bez zagrada!)
print(temp.fahrenheit)  # 77.0

temp.celzij = 30  # Poziva setter
print(temp.celzij)  # 30
print(temp.fahrenheit)  # 86.0

temp.fahrenheit = 100  # Postavlja preko fahrenheit
print(temp.celzij)  # 37.77777777777778

del temp.celzij  # Poziva deleter
```

## Property s validacijom

```python
class Zaposlenik:
    def __init__(self, ime, placa):
        self._ime = ime
        self._placa = placa

    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, vrijednost):
        if not isinstance(vrijednost, str):
            raise TypeError("Ime mora biti string")
        if len(vrijednost) < 2:
            raise ValueError("Ime mora imati najmanje 2 znaka")
        self._ime = vrijednost

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, vrijednost):
        if vrijednost < 0:
            raise ValueError("Plaća ne može biti negativna")
        self._placa = vrijednost

    @property
    def godisnja_placa(self):
        return self._placa * 12

# Korištenje
zap = Zaposlenik("Denis", 5000)
print(zap.ime)  # Denis
print(zap.placa)  # 5000
print(zap.godisnja_placa)  # 60000

zap.placa = 5500  # OK
# zap.placa = -1000  # ERROR! ValueError
```

## Vlastiti dekoratori

```python
def debug(func):
    """Dekorator koji ispisuje detalje o pozivu funkcije"""
    def wrapper(*args, **kwargs):
        print(f"Pozivam: {func.__name__}")
        print(f"Argumenti: args={args}, kwargs={kwargs}")
        rezultat = func(*args, **kwargs)
        print(f"Rezultat: {rezultat}")
        return rezultat
    return wrapper

class Kalkulator:
    @debug
    def zbroj(self, a, b):
        return a + b

    @debug
    def produkt(self, a, b):
        return a * b

k = Kalkulator()
k.zbroj(5, 3)
# Pozivam: zbroj
# Argumenti: args=(<__main__.Kalkulator object>, 5, 3), kwargs={}
# Rezultat: 8

# Decorator s parametrima
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                rezultat = func(*args, **kwargs)
            return rezultat
        return wrapper
    return decorator

@repeat(3)
def pozdrav():
    print("Hello!")

pozdrav()
# Hello!
# Hello!
# Hello!
```

---

# Abstract Base Classes {#abstract-classes}

## Korištenje ABC

```python
from abc import ABC, abstractmethod

class Oblik(ABC):
    """Apstraktna bazna klasa za oblike"""

    @abstractmethod
    def povrsina(self):
        """Metoda za računanje površine"""
        pass

    @abstractmethod
    def opseg(self):
        """Metoda za računanje opsega"""
        pass

    def opis(self):
        """Konkretna metoda - ne mora se overrideati"""
        return f"Ovo je oblik s površinom {self.povrsina():.2f}"

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

# Ne možeš instancirati apstraktnu klasu
# oblik = Oblik()  # ERROR! TypeError

# Možeš instancirati klasu koja implementira sve apstraktne metode
pravokutnik = Pravokutnik(5, 10)
print(pravokutnik.povrsina())  # 50
print(pravokutnik.opis())  # Ovo je oblik s površinom 50.00

krug = Krug(7)
print(krug.povrsina())  # 153.93791
print(krug.opis())  # Ovo je oblik s površinom 153.94
```

## Abstract Properties

```python
from abc import ABC, abstractmethod

class Vozilo(ABC):
    @property
    @abstractmethod
    def max_brzina(self):
        pass

    @abstractmethod
    def kreni(self):
        pass

    @abstractmethod
    def zaustavi(self):
        pass

class Auto(Vozilo):
    def __init__(self, marka):
        self.marka = marka
        self._max_brzina = 200

    @property
    def max_brzina(self):
        return self._max_brzina

    def kreni(self):
        return f"{self.marka} kreće"

    def zaustavi(self):
        return f"{self.marka} zaustavlja"

auto = Auto("BMW")
print(auto.max_brzina)  # 200
print(auto.kreni())  # BMW kreće
```

---

# Praktični primjeri {#prakticni-primjeri}

## Primjer 1: Sustav za upravljanje knjižnicom

```python
class Knjiga:
    def __init__(self, naslov, autor, isbn):
        self.naslov = naslov
        self.autor = autor
        self.isbn = isbn
        self.dostupna = True

    def __str__(self):
        status = "Dostupna" if self.dostupna else "Posuđena"
        return f"{self.naslov} - {self.autor} ({status})"

class Clan:
    def __init__(self, ime, clan_id):
        self.ime = ime
        self.clan_id = clan_id
        self.posudene_knjige = []

    def posudi_knjigu(self, knjiga):
        if not knjiga.dostupna:
            return f"Knjiga '{knjiga.naslov}' nije dostupna"
        knjiga.dostupna = False
        self.posudene_knjige.append(knjiga)
        return f"{self.ime} je posudio/la '{knjiga.naslov}'"

    def vrati_knjigu(self, knjiga):
        if knjiga in self.posudene_knjige:
            knjiga.dostupna = True
            self.posudene_knjige.remove(knjiga)
            return f"{self.ime} je vratio/la '{knjiga.naslov}'"
        return f"{self.ime} nije posudio/la ovu knjigu"

class Knjiznica:
    def __init__(self, naziv):
        self.naziv = naziv
        self.knjige = []
        self.clanovi = []

    def dodaj_knjigu(self, knjiga):
        self.knjige.append(knjiga)
        return f"Dodana knjiga: {knjiga.naslov}"

    def registriraj_clana(self, clan):
        self.clanovi.append(clan)
        return f"Registriran član: {clan.ime}"

    def dostupne_knjige(self):
        return [knjiga for knjiga in self.knjige if knjiga.dostupna]

    def prikazi_knjige(self):
        print(f"\n=== Knjige u {self.naziv} ===")
        for knjiga in self.knjige:
            print(knjiga)

# Korištenje
knjiznica = Knjiznica("Gradska knjižnica")

# Dodaj knjige
k1 = Knjiga("Python programiranje", "Denis Horvat", "123-456")
k2 = Knjiga("OOP u Pythonu", "Ana Kovač", "789-012")
k3 = Knjiga("Algoritmi", "Marko Marić", "345-678")

knjiznica.dodaj_knjigu(k1)
knjiznica.dodaj_knjigu(k2)
knjiznica.dodaj_knjigu(k3)

# Registriraj članove
clan1 = Clan("Ivan Ivić", "C001")
clan2 = Clan("Petra Petrić", "C002")

knjiznica.registriraj_clana(clan1)
knjiznica.registriraj_clana(clan2)

# Posuđivanje
print(clan1.posudi_knjigu(k1))
print(clan1.posudi_knjigu(k2))
print(clan2.posudi_knjigu(k1))  # Nije dostupna

# Prikaz stanja
knjiznica.prikazi_knjige()

# Vraćanje
print(clan1.vrati_knjigu(k1))
knjiznica.prikazi_knjige()
```

## Primjer 2: E-commerce sustav

```python
class Proizvod:
    def __init__(self, naziv, cijena, kolicina_na_skladistu):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina_na_skladistu = kolicina_na_skladistu

    def __str__(self):
        return f"{self.naziv} - {self.cijena} EUR (skladište: {self.kolicina_na_skladistu})"

    def je_dostupan(self, kolicina):
        return self.kolicina_na_skladistu >= kolicina

    def smanji_skladiste(self, kolicina):
        if self.je_dostupan(kolicina):
            self.kolicina_na_skladistu -= kolicina
            return True
        return False

class StavkaNarudzbe:
    def __init__(self, proizvod, kolicina):
        self.proizvod = proizvod
        self.kolicina = kolicina

    @property
    def ukupna_cijena(self):
        return self.proizvod.cijena * self.kolicina

    def __str__(self):
        return f"{self.proizvod.naziv} x{self.kolicina} = {self.ukupna_cijena} EUR"

class Narudzba:
    broj_narudzbe = 0

    def __init__(self, kupac):
        Narudzba.broj_narudzbe += 1
        self.id = Narudzba.broj_narudzbe
        self.kupac = kupac
        self.stavke = []
        self.status = "Nova"

    def dodaj_stavku(self, proizvod, kolicina):
        if proizvod.je_dostupan(kolicina):
            stavka = StavkaNarudzbe(proizvod, kolicina)
            self.stavke.append(stavka)
            return f"Dodano: {stavka}"
        return f"Nedovoljna količina za {proizvod.naziv}"

    @property
    def ukupno(self):
        return sum(stavka.ukupna_cijena for stavka in self.stavke)

    def potvrdi(self):
        for stavka in self.stavke:
            if not stavka.proizvod.smanji_skladiste(stavka.kolicina):
                return "Greška: Proizvod više nije dostupan"
        self.status = "Potvrđena"
        return f"Narudžba #{self.id} potvrđena. Ukupno: {self.ukupno} EUR"

    def prikazi(self):
        print(f"\n=== Narudžba #{self.id} ===")
        print(f"Kupac: {self.kupac}")
        print(f"Status: {self.status}")
        print("\nStavke:")
        for stavka in self.stavke:
            print(f"  {stavka}")
        print(f"\nUkupno: {self.ukupno} EUR")

# Korištenje
p1 = Proizvod("Laptop", 899.99, 5)
p2 = Proizvod("Miš", 19.99, 50)
p3 = Proizvod("Tipkovnica", 49.99, 30)

narudzba = Narudzba("Denis Horvat")
print(narudzba.dodaj_stavku(p1, 1))
print(narudzba.dodaj_stavku(p2, 2))
print(narudzba.dodaj_stavku(p3, 1))

narudzba.prikazi()
print(narudzba.potvrdi())

# Provjera skladišta
print(f"\n{p1}")  # Laptop - 899.99 EUR (skladište: 4)
```

## Primjer 3: Bankovni račun s transakcijama

```python
from datetime import datetime

class Transakcija:
    def __init__(self, tip, iznos, opis=""):
        self.tip = tip  # "uplata" ili "isplata"
        self.iznos = iznos
        self.opis = opis
        self.datum = datetime.now()

    def __str__(self):
        znak = "+" if self.tip == "uplata" else "-"
        return f"{self.datum.strftime('%Y-%m-%d %H:%M')} | {znak}{self.iznos} EUR | {self.opis}"

class BankovniRacun:
    def __init__(self, vlasnik, pocetno_stanje=0):
        self._vlasnik = vlasnik
        self._stanje = pocetno_stanje
        self._transakcije = []
        if pocetno_stanje > 0:
            self._transakcije.append(Transakcija("uplata", pocetno_stanje, "Početno stanje"))

    @property
    def vlasnik(self):
        return self._vlasnik

    @property
    def stanje(self):
        return self._stanje

    def uplati(self, iznos, opis=""):
        if iznos <= 0:
            return "Iznos mora biti pozitivan"
        self._stanje += iznos
        self._transakcije.append(Transakcija("uplata", iznos, opis))
        return f"Uplaćeno: {iznos} EUR. Novo stanje: {self._stanje} EUR"

    def isplati(self, iznos, opis=""):
        if iznos <= 0:
            return "Iznos mora biti pozitivan"
        if iznos > self._stanje:
            return "Nedovoljno sredstava"
        self._stanje -= iznos
        self._transakcije.append(Transakcija("isplata", iznos, opis))
        return f"Isplaćeno: {iznos} EUR. Novo stanje: {self._stanje} EUR"

    def povijest(self, zadnjih_n=None):
        print(f"\n=== Transakcije: {self._vlasnik} ===")
        print(f"Trenutno stanje: {self._stanje} EUR\n")
        transakcije = self._transakcije[-zadnjih_n:] if zadnjih_n else self._transakcije
        for t in transakcije:
            print(t)

    def __str__(self):
        return f"Račun vlasnika {self._vlasnik}: {self._stanje} EUR"

class StedniRacun(BankovniRacun):
    def __init__(self, vlasnik, pocetno_stanje=0, kamatna_stopa=0.02):
        super().__init__(vlasnik, pocetno_stanje)
        self.kamatna_stopa = kamatna_stopa

    def obracunaj_kamatu(self):
        kamata = self._stanje * self.kamatna_stopa
        self.uplati(kamata, "Obračun kamate")
        return f"Obračunata kamata: {kamata:.2f} EUR"

# Korištenje
racun = BankovniRacun("Denis Horvat", 1000)
print(racun.uplati(500, "Plaća"))
print(racun.isplati(200, "Kupovina"))
print(racun.uplati(300, "Bonus"))
print(racun.isplati(100, "Benzin"))

racun.povijest()

# Štedni račun
stednja = StedniRacun("Ana Kovač", 5000, 0.03)
print(stednja.obracunaj_kamatu())
stednja.povijest()
```

---

# Napredni koncepti {#napredni-koncepti}

## Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Osoba:
    ime: str
    prezime: str
    godine: int
    email: str = ""  # Default vrijednost

    def puno_ime(self):
        return f"{self.ime} {self.prezime}"

@dataclass
class Proizvod:
    naziv: str
    cijena: float
    kategorija: str = "Ostalo"
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        # Poziva se nakon __init__
        if self.cijena < 0:
            raise ValueError("Cijena ne može biti negativna")

# Korištenje
osoba = Osoba("Denis", "Horvat", 30, "denis@example.com")
print(osoba)  # Automatski __repr__
print(osoba.puno_ime())

proizvod = Proizvod("Laptop", 899.99, "Elektronika", ["novo", "akcija"])
print(proizvod)
```

## Mixins

```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_string):
        import json
        data = json.loads(json_string)
        return cls(**data)

class PrintMixin:
    def print_info(self):
        print(f"{self.__class__.__name__}:")
        for key, value in self.__dict__.items():
            print(f"  {key}: {value}")

class Osoba(JsonMixin, PrintMixin):
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

# Korištenje
osoba = Osoba("Denis", "Horvat", 30)
osoba.print_info()

json_str = osoba.to_json()
print(json_str)  # {"ime": "Denis", "prezime": "Horvat", "godine": 30}
```

## Descriptors

```python
class ValidatedString:
    def __init__(self, min_length=0, max_length=100):
        self.min_length = min_length
        self.max_length = max_length
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, "")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Vrijednost mora biti string")
        if len(value) < self.min_length:
            raise ValueError(f"String mora imati najmanje {self.min_length} znakova")
        if len(value) > self.max_length:
            raise ValueError(f"String može imati maksimalno {self.max_length} znakova")
        self.data[instance] = value

class Osoba:
    ime = ValidatedString(min_length=2, max_length=50)
    prezime = ValidatedString(min_length=2, max_length=50)

    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

# Korištenje
osoba = Osoba("Denis", "Horvat")
print(osoba.ime)  # Denis

# osoba.ime = "D"  # ERROR! ValueError
# osoba.ime = 123  # ERROR! TypeError
```

## Singleton Pattern

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Korištenje
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True - isti objekt
```

---

# Vježbe za praksu

## Vježba 1: Biblioteka filmova

Napravi sustav za upravljanje bibliotekom filmova:
- `Film` klasa (naslov, režiser, godina, žanr)
- `Kolekcija` klasa koja sadrži filmove
- Mogućnost pretrage po žanru, režiseru, godini
- Ocjenjivanje filmova (1-5 zvjezdica)

## Vježba 2: Fitness tracker

Napravi aplikaciju za praćenje treninga:
- `Vjezba` klasa (naziv, trajanje, kalorije)
- `Trening` klasa koja sadrži vježbe
- `Korisnik` klasa s poviješću treninga
- Statistika (ukupno kalorija, najdulji trening, itd.)

## Vježba 3: Restoran narudžbe

Napravi sustav za naručivanje u restoranu:
- `Jelo` klasa (naziv, cijena, kategorija)
- `Narudzba` klasa sa stavkama
- `Stol` klasa koja prati narudžbe
- `Racun` klasa s mogućnošću podjele računa

## Vježba 4: Mini ERP sustav

Implementiraj jednostavan ERP sustav:
- `Artikl` klasa (šifra, naziv, cijena, stanje)
- `Partner` klasa (OIB, naziv, adresa)
- `Dokument` bazna klasa
- Izvedene klase: `Ponuda`, `Narudzbenica`, `Otpremnica`, `Racun`

---

# Brzi Cheat Sheet

```python
# KLASA
class MojaKlasa:
    class_attr = "Dijeljeno"  # Class atribut

    def __init__(self, param):
        self.instance_attr = param  # Instance atribut

    def metoda(self):  # Instance metoda
        return self.instance_attr

    @classmethod
    def class_metoda(cls):  # Class metoda
        return cls.class_attr

    @staticmethod
    def static_metoda():  # Static metoda
        return "Static"

# NASLJEĐIVANJE
class Child(Parent):
    def __init__(self, param):
        super().__init__(param)

# PROPERTY
@property
def attr(self):
    return self._attr

@attr.setter
def attr(self, value):
    self._attr = value

# SPECIJALNE METODE
__init__(self)  # Konstruktor
__str__(self)   # print()
__repr__(self)  # repr()
__len__(self)   # len()
__getitem__(self, key)  # obj[key]
__setitem__(self, key, value)  # obj[key] = value
__add__(self, other)  # +
__sub__(self, other)  # -
__mul__(self, other)  # *
__eq__(self, other)  # ==
__lt__(self, other)  # <
__gt__(self, other)  # >
__call__(self)  # obj()
__enter__(self)  # with statement
__exit__(self)  # with statement
```

---

# Najbolje prakse

1. **Imenovanje**:
   - Klase: `PascalCase`
   - Metode i atributi: `snake_case`
   - Konstante: `UPPER_CASE`
   - Private: `_single_underscore`
   - Name mangling: `__double_underscore`

2. **Dokumentacija**:
   - Koristi docstrings za sve klase i metode
   - Piši jasne komentare gdje je potrebno

3. **DRY princip**:
   - Don't Repeat Yourself
   - Koristi nasljeđivanje i kompoziciju

4. **SOLID principi**:
   - Single Responsibility
   - Open/Closed
   - Liskov Substitution
   - Interface Segregation
   - Dependency Inversion

5. **Type Hints**:
   - Koristi type hints za bolju čitljivost
   - Olakšava debugging i IDE podršku

---

# Korisni resursi

## Službena dokumentacija
- [Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)

## Online učenje
- Real Python
- Python.org tutorials
- W3Schools Python
- GeeksforGeeks Python

---

**Autor:** Python OOP Vodič 2025
**Verzija:** 1.0 - Kompletno izdanje
