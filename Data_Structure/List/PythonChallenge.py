#1 Python Challenge

Students = [
    ["Maria",85], 
    ['Kumar', 90],
    ['Max', 60]
]

print(Students[2][0].startswith('M'))

print(list(filter(lambda row:row[0].startswith('M'), Students)))
