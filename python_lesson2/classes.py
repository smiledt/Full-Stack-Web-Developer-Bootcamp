class Dog():

    # CLASS OBJECT Attribute
    species = "mammal"

    # init is the most basic of speicalized functions
    # It initializes an instance of the class
    # And specifies what arguments are needed
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog(breed="Lab", name="Tommy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
