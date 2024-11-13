#Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario ingresa un número impar. Usa un ciclo while para lograr esto.

sumEvenNumbers = 0

print("What's the integer to add if it's even? (The program will stop if you enter an odd number):")

while True:
    number = int(input("What's the integer you'd like to enter?: "))
    
    if number % 2 == 0:
        sumEvenNumbers += number
        print(f"Current sum of even numbers is: {sumEvenNumbers}.")
    else:
        print("An odd number was entered.")
        break