# Spremite ovaj kod kao datoteku "importer.py"
import my_module
import duck_typing_module

print("Uvozimo 'my_module' i 'duck_typing_module'...")

# Pozivanje funkcije iz "my_module.py"
my_module.pozdravi("Ana")

# Pozivanje klase iz "my_module.py"
generator = my_module.GreetingGenerator("Ivana")
generator.say_hello()

# Sada pozivamo "patke" iz "duck_typing_module.py"
duck = duck_typing_module.Duck()
duck_typing_module.make_it_quack(duck)

# Stvaramo instancu klase koja oponaša patku iz "duck_typing_module.py"
person = duck_typing_module.Person()
duck_typing_module.make_it_quack(person) # Radi iako je Person klasa, jer ima metodu quack()