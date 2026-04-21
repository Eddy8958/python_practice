# while 5 > 3:
#     print("bilal gandu")

#
# for i in range (1, 101):
#     if i % 3 == 0:
#         print("Fizz")
#         if i % 5 == 0:
#             print("FIZZBuzz")
#     else:
#      print(i)

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)