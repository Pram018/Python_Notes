def add(x, y, z=0):
    print('X:', x, 'Y:', y, 'Z:', z)
    return x + y + z

ans1 = add(10, 45, z=1)
ans2 = add(45, 60, z=45)
print("Total:", ans1)
print("Total:", ans2)