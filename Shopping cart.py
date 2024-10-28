items = []
prices = []
total = 0

while True :
    item = input('Enter the name of your item [##press "q" if you want to exit##] = ')
    if item == 'q':
        break
    else:
        price = float(input(f"ENTER the PRICE OF THE {item} : Rs."))
        items.append(item)
        prices.append(price)

print('----------YOUR CART----------')
for item in items:
    print(item)
for price in prices:
    total += price

print(f"Your total is Rs.{total}")
