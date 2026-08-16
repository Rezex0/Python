# Combining
letter = ['a', 'b', 'c']
numbers = [1,2,3]
numbers.extend(letter)
print(letter)
print(numbers) #extends doees not create a new list; it expands the original one

# comb = letter  + numbers


#Multiplier operator
print(letter * 3)


#combining using
#Zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = list(zip(letters, numbers,"Hi"))
print(comb)

#Practical example of Zip()
ids = [101, 102, 103]
names = ['Ali', 'sara', 'John ']
print(list(zip(ids, names)))
