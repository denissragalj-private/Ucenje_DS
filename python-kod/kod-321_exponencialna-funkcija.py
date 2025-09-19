#  eksponencijalna funkcija kada neznamo exponent

def eksponent_broja(baza, eksponent):
    rezultat = 1

    for i in range(eksponent):
        # i ovdje predstavlja trenutni broj ponavljanja petlje (od 0 do eksponent-1).
        # Nije dio matematike množenja, već samo brojač.
        print(f"--- Početak ITERACIJE {i+1} ---") # Bolji opis iteracije
        print(f"Baza je {baza}, a ovo je {i}. korak ponavljanja petlje (brojeći od 0).")

        rezultat = rezultat * baza
        # rezultat sada sadrži bazu pomnoženu i+1 puta
        print(f"Međurezultat nakon {i+1}. množenja: {rezultat}")
        # odavdje se vrača iritacija za i dok ne dođe do kraja
    print("--- Petlja završena ---")
    return rezultat    # vrača konačno stanje rezultat

print(eksponent_broja(8,3))
