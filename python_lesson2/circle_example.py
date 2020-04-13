class Circle():
    pi = 3.14

    # By including a = in the declaration you can set a default parameter value
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius


my_circle = Circle(3)
print(my_circle.area())

my_circle.set_radius(100)
print(my_circle.area())
