print("Welcome to the rolercoster park ticket system")
height = float(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coster")
    age = int(input("What is your age? "))
    if age >=18:
        bill = 15
        print("You can pay $15")
    elif age > 12 and age < 18:
        bill =10
        print("You can pay $10")
    elif age < 12:
        bill = 5
        print("You can pay $5")
    else:
       print("chala ja bhai")
    want_photo = input("you want photo? for 3$ type Y for yes and N for no")
    if want_photo == "y" or want_photo =="Y":
        bill += 3
        print(f"your total bill is  {bill}")




else:
    print("You can't ride the roller coster")