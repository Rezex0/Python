Years = [1998,2027]
Months = ['Jan','Feb']
days = range(1,29)


for year in Years:
    for month in Months:
        for day in days:
            print(f"{year}_{month}_{day}.csv")