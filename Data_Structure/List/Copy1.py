import copy

original = [
    ['a','b'],  # Row 0
    ['c','d']   #Row 1

]
#Assigment of original list to copy1
copy1 = original
print('same object:', original is copy1,"\n")

#shallow copy
copy2 = original.copy()
print('same object:', original is copy2, "\n")
print("shared Lists?",original[0] is copy2[0], "\n")


#Deep Copy
copy3 = copy.deepcopy(original)
print('same object:', original is copy3, "\n")
print("shared Lists?",original[0] is copy3[0], "\n")  