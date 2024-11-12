#Escribe un programa que determine si un número es positivo, negativo o cero usando if.

number = float(input("What's the number?: "))

if number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
elif number > 0:
    print("The number is positive.")