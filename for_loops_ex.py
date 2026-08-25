# def count_bananas(crates):
#     total = 0
#     for crate in crates:
#         for bunch in crate:
#             total+=bunch
#     return total

def biggest_banana(crates):
    biggest = 0
    for crate in crates:
        for bunch in crate:
            if bunch > biggest:
                biggest=bunch
                print(biggest)
    return biggest

print(biggest_banana([[25, 25, 25, 25], [34, 45, 45], [450],[]]))