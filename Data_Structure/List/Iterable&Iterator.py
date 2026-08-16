letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
print(new_list)


#emuerate iterator object
print(list(enumerate(letters, start = 1)))
for index, value in enumerate(letters):
    print(index, value)

# reversed iterator
for l in reversed(letters):
    print(l)
# iterator zip
numbers = [1,2,3]
print(list(zip(letters, numbers)))

for l, n in zip(letters,numbers):
    print(l,n)

#iterator map
print(list(map(str.upper, letters)))


Names = ['  John', 'jane   ', ' Kumar']
print(list(map(str.strip, Names)))







students = ["Rahul", "Priya", "Amit"]
print(students.upper())