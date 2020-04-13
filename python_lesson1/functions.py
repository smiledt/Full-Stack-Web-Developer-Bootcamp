# In python we use the def keyword to define functions
# We also use snake case in function names


def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    We should include this in all of our code
    """
    print("my first python function! {}".format(param1))


my_func('test')


def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need Integers!"


result = addNum(2, 4)

# Lambda Expression
# filter(function, iterable)
mylist = [1, 2, 3, 4, 5, 6, 7, 8]


def even_bool(num):
    return num % 2 == 0


evens = filter(even_bool, mylist)
print(list(evens))
