sajt_naziv = "programiranje.ba"   # string sastavljen od alpga + spec "." i " " razmak
#             0123456789.......(17)  
sajt_slogan = "besplatni online kursevi"
godine = "2020"    #string sastavljen od digit (brojeva)

print(sajt_naziv)
print(sajt_slogan)
print(sajt_naziv + " " + sajt_slogan)

print(sajt_naziv.upper())
print(sajt_slogan.upper())
print(sajt_naziv.upper() + " " + sajt_slogan.upper())
print(sajt_naziv * 3)

print(sajt_naziv[4])            #  r 
print(sajt_naziv[4:9])          #  ramir  
print(sajt_naziv[1:9])          # rogramir
print(sajt_naziv[0:-4])         #programiranje  (bez zadnja 4 znaka ".ba_")
print(sajt_naziv.index('a'))         # 5   "a" je na 5 mjestu
print(sajt_naziv.index('ranje'))     # 8   "ranje" pocinje na 8 mjestu
print(sajt_naziv.find('a'))          # 5   "a" pronalazi na 5 mjestu
#print(sajt_naziv.index('anja'))      # greška    "anja" ne postoji vec "anje" (moram zakomentirati jel inače program stane na tom redu)
print(sajt_naziv.find('anja'))       # -1	ne pronalazi ali ne daje grešku vec odgovara sa -1
print(sajt_naziv.replace("program","xxxx"))    # xxxxiranje.ba

print(sajt_naziv.isalpha())   # False     jel ima i specijalni znak "." i razmak " "
print(godine.isdigit())       # True      ima samo brojeve

# format()
print("{0} {1}".format(sajt_naziv, sajt_slogan)) # dao je programiranje.ba "razmak"kojije sada izmedju }" "{ i besplatni......"
print(f"{sajt_naziv} : {sajt_slogan}")         # programiranje.ba : besplatni online kursevi

# ord() i chr()
# ord prevodi u ASCI    chr prevodi nazad 

print(ord('a'))        # 97
print(ord('A'))        # 65
print(chr(98))         # b
print(chr(66))         # B