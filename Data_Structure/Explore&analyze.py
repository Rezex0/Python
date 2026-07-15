Numbers = [1,2,3,4,5,5]
Numbers2  = [1,2,3,0,5]
print(max(Numbers))
print(min(Numbers))
print(len(Numbers))
print(sum(Numbers))
print('All:',all(Numbers))
print('All:',all(Numbers2))


Numbers12 = [1,2,3,4,5] 
print("All:",all(Numbers12))


print("Any:",all([1,0,2]))
print("Any:",any([1,0,0]))
print("Any:",any(['A','','B']))

print("Count:",Numbers.count(5))

print("Index:",Numbers.index(5))

#Analytics & Chcek 
Number23 = [1,2,3,4,5,5]
print(4 in Number23)
print(8 not in Number23)

#Comparison
list1 =[1,2,3]
list2 = [1,82,3]
print(list1 < list2)
print(list1 < list2)

# Using same value
print(list1 is list2)

#Comparison
# The First elements are Compared, 
# If they are equal,Python moves to the next elements 
