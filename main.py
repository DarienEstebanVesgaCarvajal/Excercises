#Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los primeros n números enteros. Utiliza un ciclo for para realizar la suma.

numberSum = int(input("What's the positive integer you'd like to sum up to?: "))

totalSum = 0
for number in range(1, numberSum + 1):
    totalSum += number

print(f"The sum of the first {numberSum} integers is: {totalSum}.")
