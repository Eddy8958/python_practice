import random
print("Welcome to the pypassword generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*','+']

# l = int(input("How many letters you want?"))
# n = int(input("How many number you want?"))
# s = int(input("How many symbols you want?"))
# password = ''
# # Easy Level
# password = ""
# for char in range(0, l):
#     password += random.choice(letters)
#
# for num in range(0, n):
#     password += random.choice(numbers)
#
# for sym in range(0, s):
#     password += random.choice(symbol)
#
# print("Your password is: " + random.shuffle(password))


# hard level

l = int(input("How many letters you want?"))
n = int(input("How many number you want?"))
s = int(input("How many symbols you want?"))
# password = ''
# Easy Level
password = []
for char in range(0, l):
    password.append (random.choice(letters))

for num in range(0, n):
    password.append(random.choice(numbers))

for sym in range(0, s):
    password.append(random.choice(symbol))

random.shuffle(password)
print(f"Your password is:  {password}")

passsword = ""

for char in password:
    passsword += char
print(f"Your password is:  {passsword}")

