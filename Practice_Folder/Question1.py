email = "rupamgposwami.@gmail"
email = email.strip()
# email cannot be empty 
if email == "":
    print("email cannot be empty.")

elif not '.' in email or not '@' in email:
    print("Email must contain . and @ character in it ")
elif email.count('@') != 1:
    print("Email must contain exactly one @ character ")
#Email Must end with .com,.net,.org 
elif not email.endswith(('.com','org','.net')):
    print("Email musty end with '.com', '.org' or '.net' ")
elif  len(email) < 254:
    print("Email must not be longer than 254 characters")
elif not email[0].isalnum() and email[-1].isalnum():
    print("Email must start  and end with an alphanumeric character")
else:
    print("Email is valid")