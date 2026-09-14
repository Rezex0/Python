my_dict = {
    'a' : 10,
    'b' : 20, 
    'c' : 30,
     'a':40
}
print(my_dict); #ordered 
#keys are Unique
#valus allow duplicates

print(my_dict['a']) #Not Indexed, but key based acces

my_dict['a'] = 100 #Mutable, can be chnaged

#Methods

User = {
    "id" :1, 
    "age": 30,
    "city": "berlin"

    }

#Access
print(User['city'])
print(User.get('name', "Unknown")) #get method will return None if key is not present, instead of throwing error

#Checks
print("age" in User)
print("name" in User)

#View Objects
print(User.keys())
print(User.values())
print(User.items())
print(User)

#Looping
for u in User:
    print(u , User[u])
for key, value in User.items():
    print(key,value)


#Update keys value 
User.update({"age" : 45, "City": "New york"})
print(User)

age = User.pop("city") #
print(User)
print("Remove itme:", age)

#Ignore the error
City = User.pop("location", "Not Found")
print(City)