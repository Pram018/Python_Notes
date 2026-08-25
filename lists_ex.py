def create_banana(bunches):
    i=0
    crates = []
    while i < len(bunches):
        crates.append(min(bunches[i], 20))
        # if bunches[i] > 20:
        #     crates.append(20)
        # else:
        #     crates.append(bunches[i])
        i+=1
    return crates

print(create_banana([100, 19, 20, 30000]))