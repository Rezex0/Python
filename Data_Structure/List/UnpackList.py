Person=  ['Maria' , 29 , 'Data Engineer' , 'Spain']
# name = Person[0]
# age = Person[1]
# role = Person[2]
# country = Person[3]
# Address = Person[4]




name,age,role,country = Person
#Order of Variables should be same as the list elements
print(name)
print(age)
# print(Address23)

#Rest Collector Asterisk
name,*details, country = Person
print(name)     
print(details)
print(country)

#Unpack Rules with astersk(*)
numbers =[1]
word = 'Hi'
First, *last = word
print(First)
print(last)


first,  *rest = numbers

print(first)
print(rest)


#Skiping itme Underscrore(_) 
person_New = ['Rupam', 23 ,' Data Engineer', 'India']
name,_,role,_ = person_New

print(name)
print(role)


#Rest of the Item go to trash
Person_one = [' Rupal' , 22 , 'Software developer' ,'India']
name,*_, place = Person_one
print(name)
print(place)










