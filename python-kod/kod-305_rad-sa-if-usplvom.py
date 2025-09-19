'''
# relacijski operatori
> - veće
< - manje
>= - veče ili jednako
<= - manje ili jednako
== - jednako
!= - nije jednako, različito

# logički ili bitski operatori
and - i
or - ili
not - ne, negacija
'''
print("="*50)

dobar = True         
zabavan = False
# opcije 11,
# opcija 10,
# opcija 01,
# opcija 00. 

print(type(dobar))        #     <class 'bool'>
print(type(zabavan))      #     <class 'bool'>

print("="*50)

dobar = True         
zabavan = True
print("dobar: " + str(dobar) + ", \nzabavan: " + str(zabavan))

if dobar and zabavan:                  #11  ulazi  u petlju ako je dobar i zabavan
    print("Goku je dobar i zabavan karakter.")  
elif dobar and not(zabavan):           #10  ulazi  u petlju ako je dobar i nije zabavan
    print("Picolo je dobar ali nije zabavan ! ")
elif not(dobar) and zabavan:           #01  ulazi  u petlju ako je nije dobar i je zabavan
    print("Bulma nije dobar ali je zabavan")
else:                                  #00  izvršava ako nije prethodno ništa točno tj. ne i ne
    print("Freza nije dobar ni zabavan karakter")
print("="*50)


dobar = True         
zabavan = False
print("dobar: " + str(dobar) + ", \nzabavan: " + str(zabavan))

if dobar and zabavan:                  #11  ulazi  u petlju ako je dobar i zabavan
    print("Goku je dobar i zabavan karakter.")  
elif dobar and not(zabavan):           #10  ulazi  u petlju ako je dobar i nije zabavan
    print("Picolo je dobar ali nije zabavan ! ")
elif not(dobar) and zabavan:           #01  ulazi  u petlju ako je nije dobar i je zabavan
    print("Bulma nije dobar ali je zabavan")
else:                                  #00  izvršava ako nije prethodno ništa točno tj. ne i ne
    print("Freza nije dobar ni zabavan karakter")
print("="*50)

dobar = False     
zabavan = True
print("dobar: " + str(dobar) + ", \nzabavan: " + str(zabavan))

if dobar and zabavan:                  #11  ulazi  u petlju ako je dobar i zabavan
    print("Goku je dobar i zabavan karakter.")  
elif dobar and not(zabavan):           #10  ulazi  u petlju ako je dobar i nije zabavan
    print("Picolo je dobar ali nije zabavan ! ")
elif not(dobar) and zabavan:           #01  ulazi  u petlju ako je nije dobar i je zabavan
    print("Bulma nije dobar ali je zabavan")
else:                                  #00  izvršava ako nije prethodno ništa točno tj. ne i ne
    print("Freza nije dobar ni zabavan karakter")
print("="*50)

dobar = True         
zabavan = True
print("dobar: " + str(dobar) + ", \nzabavan: " + str(zabavan))

if dobar and zabavan:                  #11  ulazi  u petlju ako je dobar i zabavan
    print("Goku je dobar i zabavan karakter.")  
elif dobar and not(zabavan):           #10  ulazi  u petlju ako je dobar i nije zabavan
    print("Picolo je dobar ali nije zabavan ! ")
elif not(dobar) and zabavan:           #01  ulazi  u petlju ako je nije dobar i je zabavan
    print("Bulma nije dobar ali je zabavan")
else:                                  #00  izvršava ako nije prethodno ništa točno tj. ne i ne
    print("Freza nije dobar ni zabavan karakter")
print("="*50)