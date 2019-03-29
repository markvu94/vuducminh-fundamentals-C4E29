a = float(input("Dien a "))
b = float(input("Dien b "))
c = float (input("Dien c "))

delta = b**2  - 4*a*c
if delta >0:
    print("co 2 nghiem")
    x1 = (-b+ delta**0.5)/(2*a)
    x2 = (-b- delta**0.5)/(2*a)
    print ("x1 =", x1)
    print ("x2 =", x2)
elif delta == 0:
    print("co nghiem kep")
    x1 = (-b)/(2*a)
    print ("x =",x1)
else:
    print("vo nghiem")    