tajna_rijec="python"

pokusaj = ""

broj_pokusaja = 0
max_broj_pokusaja = 5
kraj_igre = False


while pokusaj != tajna_rijec and not(kraj_igre):
    if broj_pokusaja < max_broj_pokusaja:
        pokusaj = input("Unesi tajnu rijeć:")
        broj_pokusaja += 1
    else:
        kraj_igre = True    
if kraj_igre:
    print("Iskoristili ste sve pokušaje. ")
else:
    print("Čestitam pogodili ste, koristili ste "+ str(broj_pokusaja)+" pokušaja.")
