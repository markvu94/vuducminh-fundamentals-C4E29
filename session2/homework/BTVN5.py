n = int(input("dien n"))

if n % 2 == 0:
    for i in range (1,n,2):
        print ("x",end = "")
        print ("*", end = "")
else:
    for i in range (1,n,2):
        print ("x",end = "")
        print ("*", end = "")
    print("x")
