naziv_karaktera = "Goku"
# #                 0123

# for slovo in naziv_karaktera:
#   print(slovo)
# # odziv:
# G
# o
# k
# u


karakteri = ["Goku", "Bulma", "Krilin", "Yamcha"]
#               1       2         3         4

# for karakter in karakteri:
#     print(karakter)


# for broj in range(10):
#     print(broj)

# # # odziv:
# # Goku
# # Bulma
# # Krilin
# # Yamcha
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9

# # novi primjer: 
# print(len(karakteri))

# for indeks in range(len(karakteri)):
#     print(karakteri[indeks])

# loto_brojevi = [1,4,7,13,54,32]
# brojevi_po_redu = sorted(loto_brojevi)
# for broj in brojevi_po_redu:
#     print(broj)

# for broj in range(4):
#     print(broj)
# # # Odziv:
# # 0
# # 1
# # 2
# # 3

# # novi test

# for karakter in karakteri:
#     if karakter == "Krilin":
#         print("u if petlji prije break naredbe")
#         print(karakter + " je jači od mene! ")
#         print("sada napoštam for i idem dalje")
#         break
#     else:
#         print("u else dijelu for petlje.. ")
#         print(karakter)

# print("\nizvan petlje ")

# # odziv:
# u else dijelu for petlje.. 
# Goku
# u else dijelu for petlje..     
# Bulma
# u if petlji prije break naredbe
# Krilin je jači od mene!        
# sada napoštam for i idem dalje 

# izvan petlje

# enumerate

for indeks, naziv in enumerate(karakteri):
    print(type(indeks))
    print(type(naziv))
    print(str(indeks) + " " + naziv)