karakteri = ('Goku', 'Krilin')
print(karakteri)    #  ('Goku', 'Krilin')
print(type(karakteri))  #  <class 'tuple'>


karakteri_naziv = "Goku"
karakteri_naziv = tuple(karakteri_naziv) # pretvara podatak u tuple
print(karakteri_naziv)   # ('G', 'o', 'k', 'u')
print(type(karakteri_naziv))   # <class 'tuple'>

sretan_broj = 1234
# sretan_broj = tuple(sretan_broj)  #ispisuje grešku "TypeError: 'int' object is not iterable" \
# jel se integer (broj se ne može razbiti na znakove)
sretan_broj = tuple(str(sretan_broj))  # 
print(sretan_broj)    #  ('1', '2', '3', '4')

spojeni_tuple = karakteri_naziv + sretan_broj   # spajamo dva tuple u jedan tuple (nizovi)

print(spojeni_tuple)   # ('G', 'o', 'k', 'u', '1', '2', '3', '4')
print(f'tuple karakteri se sastoji od {len(karakteri)} elemenata')  # tuple karakteri se sastoji od 2 elemenata
print(karakteri)   # NameError: name 'karakteri' is not defined
print('Brišem karaktere')  
del(karakteri)  # briše cijeli niz.
try:
    print(karakteri)   # NameError: name 'karakteri' is not defined
except NameError:
    print('Varijabla karakteri je obrisana')  # Varijabla karakteri je obrisana 
print('Ispisujem spojeni tuple nakon brisanja karaktera')    
print(spojeni_tuple)   # ('G', 'o', 'k', 'u', '1', '2', '3', '4')

