#Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con tarifas progresivas.

parkingHours = int(input("How many hours of parking will you pay?: "))

match parkingHours:
    case 1:
        value = 5
    case 2:
        value = 5 + 4
    case 3:
        value = 5 + (4 * 2)
    case 4:
        value = 5 + (4 * 3)
    case _ if parkingHours > 4:
        value = 5 + (4 * 3) + (3 * (parkingHours - 4))
    case _:
        print("Error: Invalid number of hours.")
        value = None

if value is not None:
    print(f"The value to be paid is: ${value}.")