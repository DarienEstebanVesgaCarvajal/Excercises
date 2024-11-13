#Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un sistema de calificación específico, usando  match.

grade = int(input("What's the grade?: "))

match grade:
    case grade if 90 <= grade <= 100:
        letterGrade = "A"
        print(f"""Your grade is: {letterGrade}.""")
    case grade if 80 <= grade <= 89:
        letterGrade = "B"
        print(f"""Your grade is: {letterGrade}.""")
    case grade if 70 <= grade <= 79:
        letterGrade = "C"
        print(f"""Your grade is: {letterGrade}.""")
    case grade if 60 <= grade <= 69:
        letterGrade = "D"
        print(f"""Your grade is: {letterGrade}.""")
    case grade if 0 <= grade <= 59:
        letterGrade = "F"
        print(f"""Your grade is: {letterGrade}.""")
    case _:
        print("Error: Invalid grade.")