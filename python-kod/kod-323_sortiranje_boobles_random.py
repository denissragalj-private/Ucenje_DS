
import random
niz_brojeva = []

for i in range(20):
    niz_brojeva.append(random.randint(1,20))


# niz_brojeva = [4,2,1,5,3,7,10,13]
#              0 1 2 3 4

# Podsjetnik !
# a = 1
# b = 2
# a,b,c = 1,2, 3

print(niz_brojeva)
zadnj_element_niza = (len(niz_brojeva)-1)     # vrijednost indexa 4 

zamjena_izvrsena = True

while zamjena_izvrsena:
    # pretpostavimo da je lista već sortirana
    zamjena_izvrsena = False

    for index, broj in enumerate(niz_brojeva[0:zadnj_element_niza]):
        if niz_brojeva[index] > niz_brojeva[index+1]:
            print(str(index) + " ima vrijednost " + \
                      str(broj))
            niz_brojeva[index], niz_brojeva[index+1] =\
            niz_brojeva[index+1],niz_brojeva[index]
            zamjena_izvrsena = True
            print(niz_brojeva)


else:
    print(niz_brojeva)
