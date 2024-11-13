 #Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i, o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.

textString = input("What's the text you'd like to analyze for vowels?: ")
vowelCount = 0

for character in textString:
    if character.lower() in 'aeiou':
        vowelCount += 1

print(f"The number of vowels in your text is: {vowelCount}.")