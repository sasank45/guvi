n,n1 = list(map(int,input().split()))
a = list(map(int,input().split()[:n]))
c = 0
for i in a:
    if n1==i:
        c+=1
if c>0:
    print("yes")
else:
    print("no")
        
