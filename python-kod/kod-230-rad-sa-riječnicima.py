# riječnici  {}   - dictionaries
# {kljuc1: vrijednostq1, kljuc2:vrijednost2}     # Ključevi moraju biti različiti, a vrijednosti nemoraju.

# prazan_rijecnik = {}                   
# print ( prazan_rijecnik )                # {}
# print(type(prazan_rijecnik))               #  <class 'dict'>

karakteri_planete = {"Goku": "Vegeta", \
                     "Picolo": "Namek", "Krilin": "Zemlja"}  # '\' daje prelazak u novi red

print(karakteri_planete)     #   {'Goku': 'Vegeta', 'Picolo': 'Namek', 'Krilin': 'Zemlja'}

karakteri_planete["Bulma"] = "Zemlja"   #   dodaje u riječnik novu riječ i vrijednost
print(karakteri_planete)     #   {'Goku': 'Vegeta', 'Picolo': 'Namek', 'Krilin': 'Zemlja', 'Bulma': 'Zemlja'}

karakteri_planete["Goku"] = "Nemek"   # mjenjamo vrijednost za "Goku"
print(karakteri_planete)     #   {'Goku': 'Nemek', 'Picolo': 'Namek', 'Krilin': 'Zemlja', 'Bulma': 'Zemlja'}

del(karakteri_planete["Krilin"])   # Briše podatak "Krilin zajedno sa njegovom vrijednosti" (ovo je metoda del)
print(karakteri_planete)     #   {'Goku': 'Nemek', 'Picolo': 'Namek', 'Bulma': 'Zemlja'}

#metode is, keys 

print(karakteri_planete.keys())         #   dict_keys(['Goku', 'Picolo', 'Bulma'])
print(karakteri_planete.values())       #   dict_values(['Nemek', 'Namek', 'Zemlja'])
print(karakteri_planete.items())        #   dict_items([('Goku', 'Nemek'), ('Picolo', 'Namek'), ('Bulma', 'Zemlja')])

print(karakteri_planete.get("Goku"))                    # Nemek
print(karakteri_planete.get("Bula"))                    # None
print(karakteri_planete.get("Bula",'Nema karaktera'))   # Nema karaktera

karakteri_planete.setdefault('Master Roschi', 'Zemlja') # dodaje novi ključ i njegovu vrijednost 
print(karakteri_planete)                #   {'Goku': 'Nemek', 'Picolo': 'Namek', 'Bulma': 'Zemlja', 'Master Roschi': 'Zemlja'}


obrisan_karakter = karakteri_planete.pop('Goku')

print(obrisan_karakter)                 #    Nemek
print(karakteri_planete)                #   {'Picolo': 'Namek', 'Bulma': 'Zemlja', 'Master Roschi': 'Zemlja'}  
# ova .pop metoda za zadani key uhvati njegov Value i sprema 

karakteri_planete2 = {'Bulma':"NovaZemlja", "Chi-chi": 'Zemlja'}
print(karakteri_planete2)     #   {'Bulma': 'Zemlja', 'Chi-chi': 'Zemlja'}

karakteri_planete.update(karakteri_planete2) # dodaje i/ili  mjenja vrijednost !!!

print(karakteri_planete)   #    {'Picolo': 'Namek', 'Bulma': 'NovaZemlja', 'Master Roschi': 'Zemlja', 'Chi-chi': 'Zemlja'}
print(len(karakteri_planete))   #    4     riječnik ima 4 podatka u obliku 'kljuć': 'vrijednost'

