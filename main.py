#Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de dicho número n! = 1 \* 2 \* 3 \* ... \* n ). Usa un ciclo for para realizar el cálculo.

numberFactorial = int(input("What's the positive integer you'd like to calculate the factorial of?: "))
factorial = 1

for number in range(1, numberFactorial + 1):
    factorial *= number

print(f"The factorial of {numberFactorial} is: {factorial}.")
