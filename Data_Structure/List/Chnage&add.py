letters = ['a' , 'b' , 'c']
print(letters)
letters.append('X')
print(letters)

#Specific postion and add the value
letters.insert(2,'e')
print( letters)


#Adding

Matrix = [
    ['a','b','c'], #Row ....0
    ['d','e','f'],#Row .....1
    ['f' ,'g','h'], #Row......2 

    ]

Matrix[1].append('X')
Matrix[0].append('W')
Matrix[2].insert(0,'E')
# Matrix.append(['x', 'y', 'z'])
# Matrix.insert(0,['E','F','L'])
print(Matrix)


#How to remove
Data = ['a' , 'b' , 'c','a']
# Data.clear()

# letters.remove('a')

Data.pop()
print(Data)



 
