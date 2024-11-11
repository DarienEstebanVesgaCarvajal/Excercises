#Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando if .

note = float(input("What's the note?: "))

if 60 <= note <= 100:
    print("The grade is a pass.")
elif 0 <= note < 60:
    print("The grade is a fail.")
else:
    print("The note is invalid.")