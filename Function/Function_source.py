#Built-in Function()
from math import ceil



print(len("Pyyhon"))


#Function from Libraries
Number = 4.2
print(ceil(Number)) #In build function from math libarary


#user defined function
def greet():
    print("Rupam Goswami")
greet()


#####################
name = "MariA   "

print(name.strip().lower())


def clean_text(name):
   print(name.strip().lower())


clean_text("MariA ")

def morning():
   print("Today date:20/08/2026")

morning()

Country =  { "IndiA    " , "NepaL   " , "BangladesH   " }

# for Country_data in Country:
#    print(Country_data.strip())


def Clean_data(Country_data):

 for Country_data in Country:
    Country_data = Country_data.strip().upper()
    print(Country_data)

Clean_data(Country)

