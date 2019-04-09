x = int(input("dien x: "))
y = int(input("dien y: "))
z = input("dien phep tinh: (+,-,*,:) ")

result = 0
if z == "+":
    result = x + y    
if z == "-":
    result = x - y
if z == "*":
    result = x * y
if z == ":":
    result = x / y

print ("{0} {1} {2} = {3}".format (x,z,y,result))