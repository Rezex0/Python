import pandas


# List creation 
sales = [1200, 1500 , 1000 , 2000]

Total_salary = sum(sales)
print(Total_salary)


#

employee = ["Rahul" , "Pritya" , "Amit" , "Sourav"]
for i in range(len(employee)):
   print(employee[i])
    



employe2 = ["Rahul", 25, "Data Analyst", 45000]

monthly_sales = [12000, 15000, 18000, 14000, 21000, 25000]
# January = monthly_sales[0]
# february = monthly_sales[1]

# for sale in monthly_sales:
#    print(sale[])

first_quarter = monthly_sales[0:3]
print(first_quarter)


#Updating data
monthly_sales[1]= 16000
print(monthly_sales)


#Adding data 
monthly_sales.append(2000)
print(monthly_sales)


#Cobining the list

north_sales = [1200, 1500, 1800]
south_sales = [1300, 1600, 1900]

all_sales = north_sales + south_sales

print(all_sales)


kolkata = [12000, 15000, 18000]
delhi = [14000, 17000, 19000]

sales = kolkata + delhi
print(sum(sales))

#sorting

sales = [1500 , 800 , 200 , 1200]
sales.sort()
print(sales)


sales = [1500,800,200,1200]
sales.sort(reverse=True)

# In sales
original_sales =[1000,2000,3000]
cleaned_sales =original_sales.copy()

cleaned_sales.remove(2000)
print(cleaned_sales)
print(original_sales)

#Unpacking
employee = ["Rupam", "IBM" , "Data Analyst"]

name, company, salary = employee

print(salary)

numbers = [10,20,30,40]

result = list(map(lambda x: x * 2 , numbers))

print(result) 

formula1 = lambda x,y: x * y,numbers
print(formula1)

check = lambda i: i in "Java"
print(check('J'))

Check1 = lambda i: i in "Rupam "

# according to the Bodmas 
formula2 = lambda x,y,z: x + y * z 
print(formula2(10,20,40))

#use of sort here

students = [
    ("Rahul", 80),
    ("Priya", 95),
    ("Amit", 70)
]

students.sort(key=lambda x:x[1])  # use it because of it's reverse the defualt value.
print(students)


# Sorting = sorted(students)
# print(Sorting)
# sorting1 =students.sort()
# print(sorting1)

#Lambda with If

check = lambda x: "Even" if x % 2 == 0 else "odd"
print(check(10))

Marks = [2,3,4]
check1 = lambda x: "pass" if x >= 90 else "Fail"
print(check1(Marks[0]))
result = (list(map(check1,Marks)))
print(result)






#Iterable & iterator

sales = [1000, 2000, 3000]
sales_iterator = iter(sales)


print(next(sales_iterator))
print(next(sales_iterator))

