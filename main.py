#Escribe un programa que determine el tipo de triángulo en función de sus lados usando if.

firstLeg = float(input("What's the first leg of a triangle?: "))
secondLeg = float(input("What's the second leg of a triangle?: "))
thirdLeg = float(input("What's the third leg of a triangle?: "))

if firstLeg == secondLeg == thirdLeg:
    print("The triangle is equilateral.")
elif (firstLeg == secondLeg) or (secondLeg == thirdLeg) or (firstLeg == thirdLeg):
    print("The triangle is isoceles.")
elif (firstLeg != secondLeg) and (secondLeg != thirdLeg) and (firstLeg != thirdLeg):
    print("The tiangle is scalene.")