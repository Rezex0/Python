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


#Matrix Copy data
# Copying matrix
matrix =[
    ['a','b','c'], #Row 0
    ['c','d'] #Row 1
]

matrix_copy = matrix.copy()
# matrix.pop()
print('matrix:',matrix)
# matrix_copy[0].append('x')
print('original matrix:',matrix)
print('copy:     ',matrix_copy)


#import copy module to create a deep copy of the matrix

import copy
matrix_deepcopy = copy.deepcopy(matrix)
matrix.pop()
print('matrix:',matrix)
matrix_deepcopy[0].append('x')
print('New matrix:',matrix_deepcopy)