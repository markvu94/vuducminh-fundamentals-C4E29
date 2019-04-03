x = int(input("nhap 1 so = "))
count = 0

for i in range (2,x):
    if (x%i) == 0:
        count +=1
       
if count == 0:
    print ("day la SNT")
if count >= 1:
    print ("day khong phai la SNT")           
        

    