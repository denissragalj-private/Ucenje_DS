def maksimalan_broj(broj1,broj2,broj3):
    if broj1 > broj2 > broj3:
        print("Broj " + str(broj1) + " je najveći")
    elif broj2 > broj1 and broj2 > broj3:
        print("Broj " + str(broj2) + " je najveći")
    else:
        print("Broj " + str(broj3) + " je najveći")

maksimalan_broj(5,7,4)
