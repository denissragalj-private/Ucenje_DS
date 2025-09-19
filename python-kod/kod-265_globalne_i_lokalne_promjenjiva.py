# def brojac(broj):
#     broj += 1
#     return broj

# print(brojac(3))  # vrati 4

# broj = 4  # globalna varijabla izvan funkcije

# def brojac(broj):
#     broj += 1
#     return broj

# print(brojac(2))                      # vrati               3
# print(broj)  # očekujem da se zbroji 4+1=5 ali ne , on vrača 4


# broj = 4       # globalna varijabla izvan funkcije
# broj_2 = 5     # globalna varijabla izvan funkcije
   
# def brojac(broj):
#     broj += 1
#     broj = broj + broj_2
#     return broj

# print(brojac(2))                 # vrati  (2+1)=3 i + 5   =  8
# print(broj)  # očekujem da se zbroji 4+1=5 ali ne , on vrača 4
# print(broj_2)                                   #  on vrača  5

broj = 6      # globalna varijabla izvan funkcije
   
def brojac():
    global broj

    broj += 1
    return broj

print(brojac())                 # vrati  6 +=1 == 7
print(broj)  # očekujem da vrati 6 ali ne, globalna varijabla je \
             #promjenila vrijednost i sada je 7 da ponovnog postavljanja \
             # ili ponovnog pokretanja programa.


