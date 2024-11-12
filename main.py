#Escribe un programa que clasifique a una persona en función de su edad.

age = int(input("What' the age?: "))

if age >= 0 and age <= 12:
    print("It's a child.")
elif age >= 13 and age <= 17:
    print("It's a teenager.")
elif age >= 18 and age <= 64:
    print("It's an adult.")
elif age >= 65:
    print("It's an old.")
else:
    print("Error: Invalid age.")