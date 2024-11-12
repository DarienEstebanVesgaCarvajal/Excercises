#Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.

grossWage = float(input("What's your gross wage?: $"))
country = int(input("""What's your country?
    1. Austria.
    2. Belgium.
    3. Czech.
    0. Another Country.
( 1 | 2 | 3 | 0 ): """))

if country == 1:
    netSalary = grossWage - (0.20 * grossWage)
    print(f"""Your net wage is: ${netSalary:.2f}""")
elif country == 2:
    netSalary = grossWage - (0.15 * grossWage)
    print(f"""Your net wage is: ${netSalary:.2f}""")
elif country == 3:
    netSalary = grossWage - (0.10 * grossWage)
    print(f"""Your net wage is: ${netSalary:.2f}""")
elif country == 0:
    netSalary = grossWage - (0.25 * grossWage)
    print(f"""Your net wage is: ${netSalary:.2f}""")
else:
    print("Error: Incorrect Country.")