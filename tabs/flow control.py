age = int(input("how old are you?"))

#if (age >= 16) and (age <=65):
# if 16 <= age <= 65:
#     print("Have a good day at work")

if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print('Have a good day at work')