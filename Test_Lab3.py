import Lab3

print("Test_Lab3")


def calculate_bmi(height, weight):
    bmi = weight / (height * height)
    if bmi < 18.5:
        return bmi, -1  # Under weight
    elif bmi >= 18.5 and bmi < 25:
        return bmi, 0   # Normal weight
    else:
        return bmi, 1   # Over weight

# Get user input for height and weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Call the calculate_bmi function with user input
bmi, bmi_classification = calculate_bmi(height, weight)

# Print the calculated BMI and classification
print("BMI: {:.2f}".format(bmi))
if bmi_classification == -1:
    print("Under weight")
elif bmi_classification == 0:
    print("Normal weight")
else:
    print("Over weight")