# # a * b * c

# def kub_braja(broj):
#     broj * broj * broj     # zadržat ču vrijednost za sebe unutar funkcije
#     print("ispis unutar funkcije")

# def kub_sa_return(broj):
#     return broj * broj * broj   # aha želim vratiti vrijednost koju sam izračunao
    
# print("               prezan red              ")
# print("prvi upit: kub_braja(3) ")
# kub_braja(3)
# print("               prezan red              ")
# print("drugi upit: print(kub_braja(3)) ")
# print(kub_braja(3))                             # None

# # nema rezultata za funkciju jel nije vračen podatak iz funkcije, \
# # fali return ili print unutar funkcije

# print("               prezan red              ")
# print("prvi upit: kub_sa_return(broj)) ")
# kub_sa_return(3)
# print("               prezan red              ")
# print("drugi upit: print(kub_braja(4)) ")
# print(kub_sa_return(4))                          # 64

def brojac(broj):   # <-  broj je parametar funkcije
    broj += 1
    return broj

brojac(3)   # <-  3 je argument koji dajemeo na mjesto parametra broj \
            #i prosljeđujemo ga funkciji

print(brojac)     # <function brojac at 0x000001CD4231B240>  lokacija u memoriji
print(brojac(5))  # vrijednost 6  (to je ustvari 5+=1 a to  iznosi 6)