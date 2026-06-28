files = [
    'data1.csv', 
    'report.pdf',
    'data2.txt',
    'report2.csv' 

]

for file in files:
    if not file.endswith('.csv'):
        print(f'Not all files are CSV')
        break
else:
     print(f'all files are csv')

