# Lists

# Lists are kinda like arrays, but better
mylist = ['string123',1,2,3,4,32.7,True,'asf',[1,2,3]]

# Lists have no problem printing different types
print(mylist)

print(len(mylist))


# Lists are immutable
print("After Reassignment:")
mylist[0] = 'New Item'
print(mylist)

# Can also append to lists
mylist.append("ANOTHER NEW ITEM")
print(mylist)

# To add two lists together, use extend NOT append
listTwo = ['x', 'y', 'z']
mylist.extend(listTwo)
print(mylist)

# Pop works like a queue, removing the last (or indexed) variable
tempItem = mylist.pop(3)
print(tempItem)

# Now we'll demonstrate a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

first_col = [row[0] for row in matrix]
print(first_col)
