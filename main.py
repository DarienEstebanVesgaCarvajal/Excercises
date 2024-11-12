#Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.

distanceToCover = float(input("What's the distance to be covered? (in km): "))
averageSpeed = float(input("What's the average speed? (in km/h): "))

if averageSpeed > 0 and averageSpeed < 120:
    travelTime = (distanceToCover/averageSpeed)

    hours = int(travelTime)
    minutes = int((travelTime -  hours) * 60)

    if hours == 0:
        print(f"""Travel time is {minutes} minutes approx.""")
    elif minutes == 0:
        print(f"""Travel time is {hours} hours approx.""")
    else:
        print(f"""Travel time is {hours} hours and {minutes} minutes approx.""")
elif averageSpeed > 120:
    print("Warning: Overspeed.")
else:
    print("Error: Negative speed or zero.")