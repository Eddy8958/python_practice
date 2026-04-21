import random
lives = 6
word_list = ["aaardvark", "baboon", "camel"]
b= random.choice(word_list)
print(b)
lund = ""
choot = (len(b))
for k in range (choot):
    lund += "_"
print(lund)
game_over = False
correct_letter = []
while not game_over:
    guess= input("Guess a letter: ").lower()
    print(guess)
    tkm = ""
    for i in b:
        if guess == i:
            tkm += i
            correct_letter.append(guess)
        elif i in correct_letter:
            tkm += i
        else:
            tkm += "_"
    print(tkm)


    if guess not in b:
        lives -= 1
        if lives == 0:
         game_over = True
         print("You Lose! Teri gand mar gyi")



    if "_" not in tkm:
        game_over = True
        print("YOu win!!Jeet gya madarchod!!!")

