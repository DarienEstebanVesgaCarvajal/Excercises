#Escribe un programa que permita al usuario adivinar una letra secreta usando match.

import random

letters = "aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNñÑoOóÓpPqQrRsStTuUúÚüÜvVwWxXyYzZ"

secretLetter = random.choice(letters)

while True:

    userGuess = input("Which letter do you think it is?: ")

    match userGuess:

        case _ if userGuess == secretLetter:
            print("Congrats! You guessed the letter.")
            break
        case _:
            print("'Nah'! Try again!")