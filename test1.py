import random
ans = random.randint (0,10)

# if block
while True:
    que = int(input("Guess number (1 to 10): "))
    if ans == que:
        print("Correct answer is ", ans)
        break
    elif ans > que:
        print("Answer is bigger")
    else:
        print("Answer is lower")
