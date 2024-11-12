#Escribe un programa que implemente un juego de adivinanza de números.

import random

randomNumber = random.randint(1, 10)

while True:
    attempt = int(input("What number between 1 and 10 do you think it is?: "))

    if attempt == randomNumber:
        print("Congrats! You guessed the number.")
        break
    elif attempt > randomNumber:
        print("Try again! The number is lower.")
    elif attempt < randomNumber:
        print("Try again! The number is higher.")
    else:
        print("Error: Number out of range.")