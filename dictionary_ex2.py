def mystery_box_value(products, valuations):
    total_values = {}
    for product in products:
        stock = products[product]
        value = valuations[product]
        total_values[product] = stock*value
    return total_values

products = {'banana': 200, 'shell': 300, 'coconut': 100}
valuations = {'banana': 8, 'shell': 4, 'coconut': 13}

print(mystery_box_value(products, valuations))