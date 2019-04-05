answer = input("write a sample sentence: ").lower()
print(answer)                                                   
menu_answer = list(answer)
bangchucai = "abcdefghijklmnopqrstuvwxyz"
menu = list(bangchucai)

#cach 2: dictionary = {}

for i in range(len(menu)):
    count = 0
    for index in range(len(menu_answer)):
        if menu[i] == menu_answer[index]:
            count +=1
            #cach 2: dictionary[menu[i]] = count                
    if count != 0:
        print(menu[i],count)   
                    
#cach2: for letter,number in dictionary.items():
#cach2:     print(letter,number)

#dung get: dictionary = {}
#dung get:  for letter in answer:
#dung get:     dictionary[letter] = dictionary.get(letter,0)+1


