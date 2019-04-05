# Bai 3: random answer

import random                         
number = random.randint(1,10)
print("if x = {}, then what is the value of 4*(x+3)".format(number))
a = 4*(number +3)
b = random.randint(30,40)
c = random.randint(30,40)
d = random.randint(30,40)
menu = [a,b,c,d]
random.shuffle(menu)
dictionary = {}
for i in range(4):
    dictionary[i+1] = menu[i]
for key,item in dictionary.items():
    print(key,item, sep = ".")

count = 0                               # Bien nay dung de xet xem user tra loi dung may cau trong bai 3 va bai 4

loop = True                             #vong lap khi dien answer khong phai int, dien lai toi khi dung
while loop:
    answer = input("your choice? ")     #cho phep user dien gi cung duoc
    if answer.isdigit() == True and int(answer) in dictionary:      # test type(answer)
        if dictionary[int(answer)] == a:
            print("bingo")
            count +=1
            loop = False
        else:
            print("wrong answer")
            loop = False               #tra loi sai khong cho dien lai, de chuyen qua bai 4
    else:
        print("You only can choose number 1 - 4")       #ket thuc bai 3

#bai 4: Mean (dung luon a,b,c,d o bai 3 do la random)

e = random.randint(30,40)
print("Jack scored these marks in 5 math tests: {}, {}, {}, {}, {}. What is the mean?".format(a,b,c,d,e))
average = (a+b+c+d+e)//5
a1 = random.randint(20,100)
a2 = random.randint(20,100)
a3 = random.randint(20,100)
menu1 = [average,a1,a2,a3]
random.shuffle(menu1)
for t in range (4):
    dictionary[t+1] = menu1[t]
for key, item in dictionary.items():
    print(key,item, sep = ". About ")
loop = True                             #vong lap khi dien answer1 khong phai int, dien lai toi khi dung
while loop:
    answer1 = input("your choice? ")     #cho phep user dien gi cung duoc
    if answer1.isdigit() == True and int(answer1) in dictionary:        # test type(answer1)
        if dictionary[int(answer1)] == average:
            print("bingo")
            count +=1
            loop = False
        else:
            print("wrong answer")
            loop = False               
    else:
        print("You only can choose number 1 - 4")       #ket thuc bai 4

if count == 0:                                              #test xem tra loi dung may cau
    print("You answer wrong both questions")
elif count == 1:
    print("You correctly answer 1 out of 2 questions")
else:
    print("You correctly answer both questions")

