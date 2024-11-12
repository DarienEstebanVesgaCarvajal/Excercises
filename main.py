#Escribe un programa que asigne una calificación basada en una nota numérica.

grade = float(input("What's the grade in number?: "))

if grade >= 90 and grade <= 100:
    print("The grade is A.")
elif grade >= 80 and grade < 90:
    print("The grade is B.")
elif grade >= 70 and grade < 80:
    print("The grade is C.")
elif grade >= 60 and grade < 70:
    print("The grade is D.")
elif grade >= 0 and grade < 60:
    print("The grade is F.")
else:
    print("Error: Invalid grade.")