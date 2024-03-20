a,b,c = map(int,input().split())

d = []
for i in range(a, b, c):
    d.append(i)
print(sorted(d, reverse=True))
