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

