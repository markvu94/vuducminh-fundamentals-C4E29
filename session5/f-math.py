import random
import functions.calculate
loop = True
while loop:
    x = random.randint (1,10)
    y = random.randint (1,10)
    z = random.choice (["+","-","*","/"])

    # result = 0
    # if z == "+":
    #     result = x + y    
    # if z == "-":
    #     result = x - y
    # if z == "*":
    #     result = x * y
    # if z == "/":
    #     result = x / y
    result = functions.calculate.calc(x,y,z)
    q = random.choice ([result -1, result, result, result,result +1])

    print ("{0} {1} {2} = {3}".format (x,z,y,q))

    answer = input("Y/N? :").lower()
    if answer == "y":
        if q == result:
            print("hura")    
        else:
            print("sai roi")
            
    if answer == "n":
        if q != result:
            print ("hura")
            
        else:
            print("sai roi")
            
