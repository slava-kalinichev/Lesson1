from random import choice, randint
pack = [0,1]
flag = True
for i in range(10000):
    if flag:
        for j in range(10000):
            if randint(1, 100) == 25:
                print("Almost", end="")
            elif randint(1, 1000000) == 25:
                print()
                print("WHAT'S THE MATTER?")
                flag = False
                break
            else:
                print(choice(pack), end="")