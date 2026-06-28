items = [1,3,4,7]
for i in items:
    print(i)
else:
    print("Loop is Complete")


#Check for even Number
items = [1,2,3,4,7]
for i in items:
    if i % 2 == 0:
         print("Even Number Found :", i)
         break
else:
    print("All Number are odd")
