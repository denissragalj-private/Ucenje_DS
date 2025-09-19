# Spremite ovaj kod kao datoteku "my_module.py"

def pozdravi(ime="svijete"):
    """
    Jednostavna funkcija koja ispisuje pozdrav.
    Argument 'ime' ima zadanu vrijednost 'svijete' ako nije proslijeđen.
    """
    print(f"Pozdrav, {ime}!")

class GreetingGenerator:
    """
    Jednostavna klasa za generiranje pozdrava.
    Sadrži metodu koja koristi ime spremljeno u objektu.
    """
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Pozdrav od klase, {self.name}!")

# Ova linija koda će se izvršiti KADA GOD se datoteka pokrene ili uvozi.
print("Ovo se uvijek ispisuje.")

# Ovaj blok koda se pokreće SAMO kada se skripta izvršava IZRAVNO.
# Kada se skripta uvozi kao modul, ovaj se kod PRESKAČE.
if __name__ == "__main__":
    print("Ovaj kod se pokreće samo ako je 'my_module.py' pokrenut direktno.")
    pozdravi("Marko")
    pozdravi() # Koristi zadanu vrijednost

    # Ovdje demonstriramo upotrebu nove klase kada se skripta pokreće izravno.
    # Stvaramo instancu klase i pozivamo njezinu metodu.
    generator = GreetingGenerator("Ana")
    generator.say_hello()
