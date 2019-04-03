low = 0
high = 100
loop = True
while loop:
    mid = (low + high)//2
    answer = input("is {} your number?".format(mid))

    if answer == "c":
        print("bingo")
        loop = False
    elif answer == "l":
        high = mid
    elif answer == "s":
        low = mid