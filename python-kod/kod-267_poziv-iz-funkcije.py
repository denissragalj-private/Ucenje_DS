def kub(broj):
    return broj * broj * broj


def ispis_kubnog_broja(broj):
    '''Funkcija izračunava kub braja po formuli 
    broj * broj * broj
    Korištenje funkcije: ispis_kubnog_broja(neki_broj)
    '''
    kubni_broj = kub(broj)

    print("Kubna vrijednost broja " + str(broj) + \
          " je " + str(kubni_broj))

ispis_kubnog_broja(2)
help(ispis_kubnog_broja)


