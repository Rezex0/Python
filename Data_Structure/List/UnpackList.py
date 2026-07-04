Person=  ['Maria' , 29 , 'Data Engineer' , 'Spain']
name = Person[0]
age = Person[1]
role = Person[2]
country = Person[3]


name,age,role,country = Person
#Order of Variables should be same as the list elements
print(name)
print(age)

name,*details, country = Person
print(name) 
print(details)
