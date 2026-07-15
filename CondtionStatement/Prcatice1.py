input_number = int(input("Enter a Number: "))
if input_number < 0:
    print("Negative Number")
elif input_number == 0:
    print("Zero")
else:
    print("Positive Number")


#Practice question:take a input from user and Found out user eligible for vote or not
input_age = int(input("Enter your age: "))
if input_age >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")


#Chcek the number is even or odd
input_number1 =int(input("Enter a number: "))
if input_number1 % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Print grater numbe from two number 
user_input = int(input("Enter first number:"))
user_input1 = int(input("Enter secound number:"))
user_input2 = int(input("Enter Third number:"))

if user_input >  user_input1 and user_input > user_input2:
    print("First number is grater than secound number")
elif user_input1 > user_input and user_input1 > user_input2:
    print("Secound number is grater than first number")
elif user_input2 > user_input and user_input2 > user_input1:
    print ("Third number is grater than first and secound number")
elif user_input == user_input1 and user_input == user_input2:
    print("All numbers are equal")
else:
    print("all number are equal")
 

number1 = int(input("ente first number:"))
number2 = int(input("Enter secound  number:"))

if number1 > number2:
    if number1 == number2:


