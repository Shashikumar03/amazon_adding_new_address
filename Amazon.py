from faker import Faker


import random

fake = Faker('en_IN')  # Specify Indian locale
list=[845305,110001,530068,600001,211001,400001,147301,826124]



for _ in range(3):
    first_digit = fake.random_element(elements=('1', '2', '3', '4', '5', '6', '7', '8', '9'))
    remaining_digits = fake.random_number(digits=9)  #
    phone_number = f"{first_digit}{remaining_digits}"
    a = fake.address()

    if(a.__contains__("-")):
     print("if ",a.split("-")[0])

    else:
        print("else : ",a[0:-5])



    print("---------------")
