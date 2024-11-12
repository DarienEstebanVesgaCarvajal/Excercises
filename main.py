#Escribe un programa que determine el mayor de tres números usando if.

firstNumber = float(input("What's the first number?: "))
secondNumber = float(input("What's the second number?: "))
thirdNumber = float(input("What's the third number?: "))

if (secondNumber < firstNumber) and (thirdNumber < firstNumber):
    print(f"""The highest number is the first number: {firstNumber}.""")
elif (firstNumber < secondNumber) and (thirdNumber < secondNumber):
    print(f"""The highest number is the second number: {secondNumber}.""")
elif (firstNumber < thirdNumber) and (secondNumber < thirdNumber):
    print(f"""The highest number is the third number: {thirdNumber}.""")
else:
    print("Error: Highest numbers are identical.")