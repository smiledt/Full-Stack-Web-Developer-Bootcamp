# Demonstrate Special Methods
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # Basically a toString() function
        return "Title: {}, Author: {}, Pages {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages


my_book = Book("Python", "Joese", 200)
print(my_book)  # The print function looks for a toString() (basically)

print("The book has", len(my_book), "pages!")
