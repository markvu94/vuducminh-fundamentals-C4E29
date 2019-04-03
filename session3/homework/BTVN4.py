menu = [5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my ship sizes {}".format(menu))
count = 0

for time in range (3):        
        for index in range(len(menu)):    #test cach thay doi item thay vi index
                menu[index] +=50
        print ("Month {}: ".format(time + 1))
        print("one month has passed, and here is my flock {}".format(menu))
        m = max (menu)
        print("now my biggest sheep has size {}, let's sheer it".format(m))
        for i in range (len(menu)):
                if menu[i] == m:
                        count = i
                        default = 8
                        menu [count] = default
                        print("after sheering, here is my flock: {}".format(menu))
                else:
                        pass
s = sum(menu)
print("my flock has size in total: {}".format(s))
price = s * 2
print ("I would get {}$".format(price))
