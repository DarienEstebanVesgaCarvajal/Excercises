#Escribe un programa que calcule el número de créditos totales de un estudiante en base a las materias cursadas y el puntaje obtenido en cada una. El puntaje debe ser evaluado como aprobado o no aprobado.

numSubjects = int(input("How many school subjects have you completed?: "))
credits = 0

for x in range(numSubjects):
    score = float(input(f"""What's your score?: """))

    if score >= 60:
        credits += 3

print(f"""Total number of credits: {credits}.""")