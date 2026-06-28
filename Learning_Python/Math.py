password = "   1234556"
print(len(password))


if(len(password)) < 8:
    print("Your password is too short!")
 

 #replace()
Phone_No = "839-189-7457"
print(Phone_No.replace("-" , ""))

#python challenge :- Convert the messay phone number into a clean number format with only digits
Phone_No1 = "+49  (176) 123-4567"

print(Phone_No1.replace("  " ,"").replace("(", "").replace(")", "").replace("-" ,"").replace(" ",""))

#How to join string

first_Name = "Rupam"
last_Name = "Goswami"

last_Name = first_Name + "-" + last_Name
print(last_Name)

folder = "c:/users/rupam/"
file = "report.Csv"
full_file_path = folder + file 
print(full_file_path)

#use of Fstring
Name = "Rupam  Goswami"
age = 23 
is_student =  False
 
print(f"My name is {Name},I am {age} years old, and students status is {is_student}")

print(f"2+ 3 = {2+3}")

