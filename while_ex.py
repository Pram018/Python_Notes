def stack_total(num_crates):
    total = 0
    while num_crates > 0:
        # print('num_crates:', num_crates)
        total+=num_crates
        # print('total:', total)
        num_crates -= 1
    return total

print(stack_total(6))