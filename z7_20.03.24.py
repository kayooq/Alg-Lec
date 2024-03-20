a = int(input())
b = []
max = 0
while a !=0:
    b.append(a)
    a = int(input())
b = sorted(b)
for i in set(b):
    if max < b.count(i):
        max = b.count(i)
print(max)
