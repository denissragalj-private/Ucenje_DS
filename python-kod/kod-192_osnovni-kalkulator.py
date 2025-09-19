broj_1 = float(input("Unesite vrijednost prvog broja: "))    # tražimo unos koji pretvaramo u decimalni zbog računanja
broj_2 = float(input("Unesite vrijednost drugog broja: " ))

print(type(broj_1))      #  provjeravamo tip podatka
print(type(broj_2))

zbir = broj_1 + broj_2
razlika = broj_1 - broj_2
mnozenje = broj_1 * broj_2
djeljenje = broj_1 / broj_2

print("Zbir unesenih brojeva: " + str(zbir))         # zbog kombiniranog ispisa vračamo podatak u string
print("Razlika unesenih brojeva: " + str(razlika))
print("Množenje unesenih brojeva: " + str(mnozenje))
print("Djeljenje unesenih brojeva: " + str(djeljenje))