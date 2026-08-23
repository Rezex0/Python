#Multipliction
multiple = lambda x: x*2
print(multiple(2))


#subtration
add = lambda x,y: x+y 
print(add(1,2))


check = lambda i: i in "python"
print(check('n'))


prices = ['$168.68' , '$567.98' , '$7848.23']
print(list(map(lambda p: print(float(p.replace('$', ''))), prices)))

p = '$12.50'
print(float(p.replace('$', '')))


p1= [120 , 30 , 300 , 80]
print(list(filter (lambda p: p >= 100, p1)))


#Experiment on string 

students = [['Maria', 85],
           ['Kumar', 90],
           ['Max', 60]]

print(list(filter(lambda row:row[ 1] > 70, students)))


print(students[0][1] > 70) 



