# items = [1,2,3,4,5]
# for item in items:
#     print(f"Round:{item}")



# Range  function()
items1 = "Rupam Goswami"
for items in range(1,10):
    print(f"{items} Round:{items1}")
    
for Name in items1:
    print(Name)


for i in range(len(items1)):
    print(f"{i}: {items1[i]}")


scores = [10, 40, 60 , 80]
total = 0
for score in scores:
    total += score
    print("Current total:", total)
print("Final Total:",total)
 




files = [' Report.csv', 'Data.csv', ' Final.Txt']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"processing {file}")

    