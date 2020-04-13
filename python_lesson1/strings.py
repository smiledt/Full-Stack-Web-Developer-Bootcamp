# STRINGS

mystring = 'abcdefg'

print(mystring)

# Python supports both indexing and negative (from the end) indexing
print(mystring[3])
print(mystring[-1])

# Slicing
print(mystring[2:])  # Everything from the second char onwards

x = mystring.split("c")

print(x)

# Print formatting
newString = "Item One: {x} Item Two: {y}".format(x="dog", y="cat")
print(newString)
