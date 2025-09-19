#textualni (str)
#brojeve (int,float)
#logicke (istina/laz (True/False))

karakter_ime = "Goku"  # tip tekstualni (string)
karakter_godine = 15   # broj, cjelobrojni (integer/int)
karakter_visina = 165.7  #broj, decimalni(float)
karakter_osobina_dobar = True
karakter_osobina_los = False

print(karakter_ime)
print(karakter_godine)
print(karakter_visina)
print(karakter_osobina_dobar)
print(karakter_osobina_los)

#print(karakter_ime+karakter_godine)

print(type(karakter_ime))
print(type(karakter_godine))
print(type(karakter_visina))
print(type(karakter_osobina_dobar))
print(type(karakter_osobina_los))

print(karakter_ime +" "+ str(karakter_godine))
print(karakter_godine+karakter_visina)

print(karakter_godine)
print(type(str(karakter_godine))) # int je postao string

# primjer primjene

print(karakter_ime + " ima " + str(karakter_godine) + " godina")
print(karakter_ime + " ce imati " + str(karakter_godine+1)+" godina")
print("za godinu dana")

