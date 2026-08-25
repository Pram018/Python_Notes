def classify_price(price):
    if price < 8:
        return "Good!"
    elif price > 12:
        return "Bad!"
    return "Ok"

# print(classify_price(7))
# print(classify_price(9))
# print(classify_price(14))

def classify_price_no_shenanigans(price):
    if price == 4:
        return 'Really Bad!'
    return classify_price(price)

print(classify_price_no_shenanigans(6))