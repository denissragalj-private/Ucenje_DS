# 1. zadatak je da upišete vaše ime, a program ga odmah ispiše 5 puta u redu sa razmakom

ime = input("Unesite vaše ima: ")

print((ime + " ") * 5)
print()

#  2. zadatak je da upišete dvije riječi koje tada ispisuje u jednom redu sa 3 razmaka između

prva_rijec = input("Unesite prvu riječ: ") 
druga_rijec = input("Unesite drugu riječ: ")

print(f"{prva_rijec}   {druga_rijec}")
print()

#  3. zadatak program koji izračuna va aritmetičku sredinu 3 broja

prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))
treci_broj = int(input("Unesite treči broj: "))
 
# (a + b + c)/3

aritmeticka_sredina = ((prvi_broj+drugi_broj+treci_broj)/3)
print(f"Aritticka sredina je  {aritmeticka_sredina}")
print()

#  4. zadatak napisati program koji za uneseni karakter sa testature vrača ASCII kod

#  ord() / vrača ASCI i chr()/ vrača znak sa testature

karakter_sa_testature =input("Unesite znak sa testature: ")

ascii_karakter = ord(karakter_sa_testature)

print(f"Vrijednost unesenog karaktera, ima ASCII \
vrijednost {ascii_karakter}")
print()

#  5. zadatak  ispiši tekst koi če napisati //   Omiljena pjasma od 'Milana Sobića' - "Od druga do druga"!   //

# print(f"Omiljena pjesma od 'Milana Sobica' - "Od druga do druga" !")    # daje egrešku
print(f"Omiljena pjesma od 'Milana Sobica' - \"Od druga do druga\" !")    # za koristiti navodnike u textu treba \
print()