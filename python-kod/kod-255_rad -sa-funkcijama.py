# def naziv_funkcije():
#   print("Zdravo")

def pozdrav():
    print("/" * 30)
    print("Zdravo svijete")
    print("x" * 30)

print("*" * 30)

print('Prije poziva funkcije')
pozdrav()
pozdrav()
pozdrav()
print('Nakon poziva funkcije')

def pozdrav_sa_parametrom(ime):   # parametar funkcije
    print("$ * %" * 6)
    print("pozdravi dragi  moj " + ime)
    print("# ° ~" * 6)


pozdrav_sa_parametrom("goku")   # vrijednost za parametar ime = "goku"
pozdrav_sa_parametrom("Krilin")
pozdrav_sa_parametrom("Bulma")

#  ili ako želimo da parametar bude unesen iz varijable, možemo napraviti sljedeće


uneseni_parametar = input("Unesi ime za test sa funkcijom pozdrav_sa_parametrom: ")

#pozivamo funkciju:
pozdrav_sa_parametrom(uneseni_parametar)
print("proba funkcije sa dva parametra")
print()

uneseno_ime = input("Unesi ime za probu funkcije sa dva parametra: ")
unesene_godine = input("Unesi godine kao drugi parametar: ")    
def pozdrav_sa_dva_parametra(ime, godine):
    print()
    print("Pozdrav " + ime)
    print(ime + " ima " + str(godine))
    print("=" * 30)
pozdrav_sa_dva_parametra("Denis Šragalj",43)
pozdrav_sa_dva_parametra(uneseno_ime,unesene_godine)