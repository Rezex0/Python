user = {
    "id" :1,
     "name": "John",
     "Country": "USA",
    "age":29, 
    "status": "active"

}

user_str = {
    #Expression
    k:v.upper()
    for k, v  in user.items() # loop
    if isinstance(v, str) # filter

}

print(user_str)