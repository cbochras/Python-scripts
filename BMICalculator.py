# BMI Calculator

# Get height and weight input from user
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print BMI
print("Your BMI is:", round(bmi, 2))
