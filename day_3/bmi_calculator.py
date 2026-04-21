weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight // (height ** 2)

print("Your BMI is:", int(bmi))

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("You are normal")
else:
    print("You are bhees")