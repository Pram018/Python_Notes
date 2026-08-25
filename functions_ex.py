def classify_price(price, good_level = 8, bad_level = 12):
    if price < good_level:
        return "Good!"
    elif price > bad_level:
        return "Bad!"
    return "Ok"

print(classify_price(7))
print(classify_price(9))
print(classify_price(14))