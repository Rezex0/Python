attempts = 0
while attempts < 3:
    answer = input("Do you agree?(Yes/No):")
    answer=answer.upper()
    if answer == "Yes":
        print("Glad we're on the same page")
        break
    attempts +=1 
else:
 print("3 strikes,You're out")


