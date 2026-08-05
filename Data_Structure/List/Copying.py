#Copying
letters = ['a','b','c']
letters_copy = letters
letters.pop()
print('original list:',letters)
letters_copy.append('z')
print('original list:',letters)


#Create a copy of the list 
letters_Copy1 = letters.copy()
print("New list:",letters_Copy1)
letters_Copy1.append('x')
print("New list:",letters_Copy1)
print(letters)
