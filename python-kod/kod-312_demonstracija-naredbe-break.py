karakter_opis = {}
brojac = 0
limit = 4


while brojac < limit:
    karakter_naziv = input("Unesite ime: ")
    karagter_godine = input("Unesite godine: ")

    if int(karagter_godine) <= 1:
        print("Godine ne mogu biti manje od 1! ")
        break
    elif int(karagter_godine) > 100:
        print("zombi haha !")
        continue
    else:
        karakter_opis[(karakter_naziv)]=karagter_godine
        brojac += 1
else:
    print("izvršavam se samo jednom ! ")

print(karakter_opis)