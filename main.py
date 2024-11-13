#Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el número.

import random

secretNumber = random.randint(1, 100)

while True:
    attempt = int(input("What number between 1 and 100 do you think it is?: "))

    if attempt == secretNumber:
        print("Congrats! You guessed the number.")
        break
    elif attempt > secretNumber:
        print("Try again! The number is lower.")
    elif attempt < secretNumber:
        print("Try again! The number is higher.")
    else:
        print("Error: Number out of range.")