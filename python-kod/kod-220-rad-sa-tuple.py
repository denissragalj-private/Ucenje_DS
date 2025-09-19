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

del(karakteri)  # briše cijeli niz.
print(karakteri)   # NameError: name 'karakteri' is not defined



