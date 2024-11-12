#Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando match.

temperature = float(input("What is the temperature?: "))
scale = input("What is the temperature scale? (C or F): ")

match scale:
    case "C":
        convertedTemperature = (((9 / 5) * temperature) + 32)
        convertedScale = "F"
        print(f"The temperature is {convertedTemperature:.2f}{convertedScale}.")
    case "F":
        convertedTemperature = ((5 / 9) * (temperature - 32))
        convertedScale = "C"
        print(f"The temperature is {convertedTemperature:.2f}{convertedScale}.")
    case _:
        print("Error: Invalid scale.")