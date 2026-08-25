d = {'a': 1, 'b': 2, 'c': 3}
d['z'] = 4
d['b'] = 32
print(d)
print('z' in d)
print('z' not in d)
print("------------------------------------")

# looping through dictionary
for i in d:
    print(i, d[i])

print("------------------------------------")

for var in d.items():
    print(var)

print("------------------------------------")

for var, value in d.items():
    print(var, value)