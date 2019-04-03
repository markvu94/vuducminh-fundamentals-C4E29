x = int(input("dien x ="))
count = 0
loop = True
while loop:
    x = x//10
    count += 1
    if x == 0:
        loop = False
print (count)
    
