dictionary = {
    "hc" : "hoc",
    "eny" : "em nguoi yeu",
}
for key, value in dictionary.items():
    print(key, end = "    ")
print()

loop = True
while loop:
    x = input ("dien key: ")
    if x in dictionary.keys():
        print(dictionary[x])
    else:
        answer1 = input("do you want to add new key? (Y/N)").upper()
        if answer1 == "Y":
            answer2 = input("add translation: ")
            dictionary[x] = answer2
            print(dictionary)
        else:
            loop = False