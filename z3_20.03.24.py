a = [1, 7653,332,21,55,78,8,2,91,3]
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)
print(c, b)
