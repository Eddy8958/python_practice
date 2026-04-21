print("Welcome to the Pizza Order")
size = input("What size pizza do you want? S, M OR L")
pepperoni = input("Do you want  pepporani on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else:
    print("Sorry your size is invalid")

if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

    if extra_cheese == "Y":
        bill +=1

print(f"Your bill is {bill}")





