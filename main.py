#Escribe un programa que verifique si un número es par o impar utilizando «if».

number = int(input("What's the number?: "))

if number % 2 == 0:
    print(f"The {number} number is even.")
else:
    print(f"The {number} number is odd.")