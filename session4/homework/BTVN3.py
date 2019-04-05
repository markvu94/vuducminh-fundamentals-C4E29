price = {
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3,
}
stock = {
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15,
}
total_price = 0
for key in price:
    if key in stock:
        print(key)
        print("price: {}".format(price[key]))
        print("stock: {}".format(stock[key]))
        total_price += price[key]*stock[key]
print(total_price)