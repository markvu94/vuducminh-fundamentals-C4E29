table = [
    {
        "name": "Hai",
        "muc luong": 50000,
        "ngay": 25,
        "gio": 8
    },
    {
        "name": "Duc",
        "muc luong": 25000,
        "ngay": 20,
        "gio": 6
    },
    {
        "name": "Minh",
        "muc luong": 20000,
        "ngay": 27,
        "gio": 5
    },
    {
        "name": "Long",
        "muc luong": 10000,
        "ngay": 30,
        "gio": 3
    }]
name_input = input("name? ")
for person in table:
    if name_input == person["name"]:
        month_salary = person["muc luong"] * person["ngay"] * person["gio"]
        print(month_salary)
