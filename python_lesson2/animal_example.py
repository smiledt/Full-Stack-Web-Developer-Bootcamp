class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


class Dog(Animal):

    def __init__(self):
        print("DOG CREATED")


my_animal = Animal()
my_animal.whoAmI()
my_animal.eat()

my_dog = Dog()
my_dog.eat()
my_dog.whoAmI()
