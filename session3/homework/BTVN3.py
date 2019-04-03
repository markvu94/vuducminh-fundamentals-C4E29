menu = ["T-Shirt","Sweater"]

loop = True
for index, item in enumerate(menu):
    while loop:
        x = input("welcome to our shop, what do you want? (C,R,U,D or Exit) ")
        if x == "R":
            print("Our items: ", *menu)
        elif x == "C":
            y = input ("enter new item: ")
            menu = [*menu,y]
            print("Our items: ", *menu)
        elif x == "U":
            loopU = True
            while loopU:
                z = int(input ("Update new position? "))
                if z > len(menu):
                    print("position must not be larger than range")
                else:    
                    a = input("New item? ")
                    menu[z-1] = a
                    print("Our items: ", *menu)
                    loopU = False
        elif x == "D":
            b = int(input("Delete position: "))
            del menu[b-1]
            print("Our items: ", *menu)
        elif x == "Exit":
            loop = False
        else:
            print("Please write exact answer(C,R,U,D or Exit)")


        


