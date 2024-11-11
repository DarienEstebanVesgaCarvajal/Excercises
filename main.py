#Utiliza  match para implementar una calculadora simple.

firstNumber = float(input("What's the first number?"))
operation = input("What's the operation? ( + | - | * | / ): ")
secondNumber = float(input("What's the second number?"))

match operation:
    case "+":
        result = firstNumber + secondNumber
        print(f"The result of sum at {firstNumber} and {secondNumber} is: {result}")
    case "-":
        result = firstNumber - secondNumber
        print(f"The result of subtraction at {firstNumber} and {secondNumber} is: {result}")
    case "*":
        result = firstNumber * secondNumber
        print(f"The result of multiplication at {firstNumber} and {secondNumber} is: {result}")
    case "/":
        if secondNumber != 0:
            result = firstNumber / secondNumber
            print(f"The result of division at {firstNumber} and {secondNumber} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operation.")