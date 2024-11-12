#Escribe un programa que determine si un año es bisiesto o no.

year = int(input("What's the year to check?: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year isn't a leap year.")