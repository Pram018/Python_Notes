price = 10

if price < 6 and price % 2 == 0:
    print("Really Good!")
elif price < 10:
    print("Good")
elif price > 14 or price % 2 == 1:
    print("Really Bad!")
else:
    print("Bad")