#Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la semana usando match.

numberDay = input("What's the day's number?: ")

match numberDay:
    case "1":
        print("The day is Monday.")
    case "2":
        print("The day is Tuesday.")
    case "3":
        print("The day is Wednesday.")
    case "4":
        print("The day is Thursday.")
    case "5":
        print("The day is Friday.")
    case "6":
        print("The day is Saturday.")
    case "7":
        print("The day is Sunday.")
    case _:
        print("Error: Invalid number.")