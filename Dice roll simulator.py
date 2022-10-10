import random
while True:
    print("1.Roll the dice 2.exit")
    a=int(input("What you want to do:"))
    if a==1:
        b=random.randint(1,11)
        print(b)
    else:
        break
