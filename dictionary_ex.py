def should_buy(product, price, valuations):
    if product not in valuations:
        return False

    value = valuations[product]
    # if price < value:
    #     return True
    # return False
    return price < value


valuations = {'banana':8, 'shell':4, 'coconut':13}
print(should_buy('banana', 7, valuations))
