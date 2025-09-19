
class Animal:
    def walk(self):
        print('walking...')

class Dog(Animal):  # classi Dog dodjeljujem argument izvan njene klase koji je kreiran u class Animal
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('woof!')

roger = Dog('Roger', 8)

print(roger.name)
print(roger.age)


# pozivam funkciju 
roger.bark()
roger.walk()