# #Acess and read 
# lst = ['a', 'b' , 'c' , 'd', 'e' , 'f']
# print(lst[0]) 
# #first elements
# print(lst[-1])
#  #last elements
# print(lst[-2]) 
# #seceound last elements

#Metrix read&acess
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e' , 'f'],
    [1,2,3]
]
print(matrix[0][0]) #first row, first column
print(matrix[1][2]) 
print(matrix[2][2]) #second row, third column
print(matrix[-1][-1])

#Using slicing to read and access list 
lst  = ['a', 'b' , 'c' , 'd' , 'e' , 'f']
print(lst)
print(lst[0:-1])
print(lst[0:3])
print(lst[1:4])
print(lst[:2])
 