 #Update
letters =['a','b','c']
letters[0] ='x'
letters[1]='y'
# letters ='z' #Don't do this it's change the whole variables data types

matrix = [
    ['a','b','c'], #Row 0
    ['d','e','f'], #Row 1
    ['g','h','i'], #Row 2
]

matrix[-1] =[ 'X','Y','z']
print(matrix)
matrix[0][0] ='-'
print(matrix)

#How to sort?
# Rank by 
#Sorting 
letter =['e', 'a', 'f']
letter.sort()
print(letter) #lowest to Highest
# letter.sort(reverse = True)
new_list = sorted(letters,reverse = True)
print('Original List:',letter)
print('Sorted List:',new_list)
print(letter)