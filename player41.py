n,k = map(int,input().split())
c = 0
for i in range(n):
    if (k**i==n):
        c+=1
        break
if c==1:
    print("yes")
else:
    print("no")
