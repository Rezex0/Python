#Skip weekends in Calender Loop
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekeends = ['sat', 'sun']

for day in days:
    if day in weekeends:
        continue
    print(f'workday: {day}')