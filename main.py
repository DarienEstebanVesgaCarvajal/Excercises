# Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos internos.

firstAngle = float(input("What's the first angle of the triangle? (in degrees): "))
secondAngle = float(input("What's the second angle of the triangle? (in degrees): "))
thirdAngle = float(input("What's the third angle of the triangle? (in degrees): "))

if firstAngle + secondAngle + thirdAngle == 180:
    if firstAngle < 90 and secondAngle < 90 and thirdAngle < 90:
        print("The triangle is acute.")
    elif firstAngle == 90 or secondAngle == 90 or thirdAngle == 90:
        print("The triangle is right.")
    elif firstAngle > 90 or secondAngle > 90 or thirdAngle > 90:
        print("The triangle is obtuse.")
else:
    print("Error: The angles do not form a valid triangle.")
