#List
#index
menu = ["com","canh","thit"]
#print(menu[0])
#print(menu[-3])

#loop items
# for item in menu:
#     print (item)

#loop index
# for index in range(len(menu)):
#     print (index)

#loop items and index
# for index, item in enumerate(menu):
#     print (index,item)

#creat
# menu = ["com","canh","thit"]
# print(enumerate(menu))

#update
# menu[0] = "pho"
# print (menu)

#delete
# del menu[1]
menu.remove("canh")
print(menu)