#Escribe un programa que calcule la calificación final de un estudiante basándose en su calificación y si ha hecho tareas adicionales. Las tareas adicionales pueden darle un extra de puntos, pero el máximo de puntos no puede exceder 100.

grade = float(input("What's your grade?: "))
additionalTasks = input("""Have you done additional tasks?
    Y (Yes).
    N (Not).
( Y | N ): """)

additionalTasks = additionalTasks.upper()

while True:

    match additionalTasks:
        case "Y":
            finalGrade = grade + (0.05 * grade)
            if finalGrade > 100:
                finalGrade = 100
                print(f"""You have a grade of: {finalGrade:.2f}.""")
            else:
                print(f"""You have a grade of: {finalGrade:.2f}.""")
            break
        case "N":
            print(f"""You have a grade of: {grade:.2f}. """)
            break
        case _:
            print("Error: Wrong character.")
            additionalTasks = input("""Have you done additional tasks?
    Y (Yes).
    N (Not).
( Y | N ): """)
            additionalTasks = additionalTasks.upper()