#Escribe un programa que calcule el IMC y determine el estado de peso.

weight = float(input("What's your weight? (In Kg): "))
height = float(input("What is your height? (In m): "))

bodyMassIndex = (weight / (height) ** 2)

if bodyMassIndex > 0 and bodyMassIndex < 18.5:
    print("You're underweight.")
elif bodyMassIndex >= 18.5 and bodyMassIndex <= 24.9:
    print("You're normal weight.")
elif bodyMassIndex >= 25 and bodyMassIndex <= 29.9:
    print("You're overweight.")
elif bodyMassIndex >= 30:
    print("You're obese.")
else:
    print("Error: Negative data.")