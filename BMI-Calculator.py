# BMI = kilograms / (meters ** 2)

pounds = float(input("\nPounds: "))
height_feet = float(input("Height(feet): "))
height_inches = float(input("Height(inches): "))

kilograms = pounds / 2.205
meters = ((height_feet * 12) + height_inches) / 39.37

bmi = kilograms / (meters * meters)

print("\nBMI: " + str(round(bmi, 2)))

if bmi <= 18.5:
    print("Weight Status: Underweight\n")
if bmi >= 18.5 and bmi <= 24.9:
    print("Weight Status: Healthy\n")
if bmi >= 25.0 and bmi <= 29.9:
    print("Weight Status: Overweight.\n")
if bmi >= 30.0:
    print("Weight Status: Obese\n")
