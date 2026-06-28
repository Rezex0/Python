# Python Learning Guide - Lesson 1: Basics
# ==================================================

# 1. PRINTING OUTPUT
# -----------------
print("Hello, Python!")  # This prints text to the screen
print(42)               # You can print numbers too
print("My age:", 25)    # You can print multiple things

# 2. VARIABLES (Containers for storing data)
# -------------------------------------------
name = "Alice"           # String (text)
age = 25                 # Integer (whole number)
height = 5.7             # Float (decimal number)
is_student = True        # Boolean (True or False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# 3. VARIABLE NAMING RULES
# -------------------------
# Use lowercase with underscores for variable names
my_favorite_color = "blue"  # Good
MyFavoriteColor = "blue"    # Works but not preferred
# my-favorite-color = "blue"  # This doesn't work (dash not allowed)

# 4. MATH OPERATIONS
# -------------------
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Integer Division:", a // b)  # 3
print("Remainder:", a % b)       # 1
print("Power:", a ** b)          # 1000

# 5. COMBINING STRINGS (Concatenation)
# -------------------------------------
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# 6. INPUT FROM USER
# ------------------
# Uncomment the line below to ask for user input
# user_name = input("What is your name? ")
# print("Hello,", user_name)

# QUICK EXERCISES
# ================
# Try these in a new file or edit this one:

# 1. Create variables for your name, age, and favorite food
# 2. Print them in a sentence like "My name is X, I am Y years old, and I like Z"
# 3. Create two numbers and calculate their sum, difference, and product
# 4. (Bonus) Use input() to ask someone their favorite color and print it back

print("\n" + "="*50)
print("Congratulations on your first Python lesson!")
print("="*50)
