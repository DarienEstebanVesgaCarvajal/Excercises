#Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa un ciclo for para recorrer el rango.

startValue = int(input("What's the starting integer of your range?: "))
endValue = int(input("What's the ending integer of your range?: "))

print("The even numbers in your range are:")
for evenNumber in range(startValue, endValue + 1):
    if evenNumber % 2 == 0:
        print(evenNumber)