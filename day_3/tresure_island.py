print("Welcome to Tresure island \n Your mission is to find the treasure island")
a =input("where do you want to go left or right ?")

if a == "left":
    b =input("swim or wait")
    if b == "wait":
        c = input("Which door 'red', 'yellow' or 'blue'")
        if c == "yellow":
            print("laddo baat de")
        else:
            print("gand mar gyi")
    else:
        print("aukaat hai game khelne ki")
else:
    print("abe bot phlei kdm pe mar gya")