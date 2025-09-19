# Spremite ovaj kod kao datoteku "duck_typing_module.py"

class Duck:
    def quack(self):
        print("Kvaka! Ja sam patka.")
    def walk(self):
        print("Hodam kao patka.")

class Person:
    def quack(self):
        print("Ja imitiram patku: Kvaka! Kvaka!")
    def walk(self):
        print("Hodam na dvije noge.")

def make_it_quack(animal):
    """
    Ova funkcija ne provjerava je li 'animal' klasa Duck.
    Ona samo pretpostavlja da 'animal' ima metodu 'quack'.
    To je srž duck typinga.
    """
    animal.quack()

if __name__ == "__main__":
    duck = Duck()
    make_it_quack(duck)

    person = Person()
    make_it_quack(person) # Radi iako je Person klasa, jer ima metodu quack()

    # Ali ovo bi izazvalo grešku jer Person nema metodu 'fly()'
    # person.fly()