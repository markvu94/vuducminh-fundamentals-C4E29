table = [
    {"name": "Hai",
    "muc luong": 50000,
    "ngay": 25,
    "gio": 8},
    {"name": "Duc",
    "muc luong": 25000,
    "ngay": 20,
    "gio": 6},
    {"name": "Minh",
    "muc luong": 20000,
    "ngay": 27,
    "gio": 5},
    {"name": "Long",
    "muc luong": 10000,
    "ngay": 30,
    "gio": 3}]
while True:
    answer = input("dien ten")
    for i in table:        
            if answer == i["name"]:
                x1 = i["muc luong"]
                x2 = i["ngay"]
                x3 = i["gio"]
                y = x1 * x2 * x3
                print("{}:{}".format(answer,y))
                break
            else:
                pass

        


