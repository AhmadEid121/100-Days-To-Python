weight = float(input("Enter your Weight in kg: "))
height = float(input("Enter your Height in m: "))
BMI= round (weight /(height) ** 2)
print(f"Your BMI is {BMI}")
if BMI <= 18.5:
    print("Underweight")
elif BMI <=25:
    print("Normal Weight")
elif BMI <= 30:
    print("OverWeight")
elif BMI <= 35:
    print("Obese")
else:
    print("Clinically Obese")
    