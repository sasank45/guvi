n,k = map(int,input().split())
arr = list(int(i) for i in input().split()[:n])
c = 0
for i in arr:
    c += 1
    if i==k:
        break
print(c)
