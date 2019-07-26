n = int(input())
a = list(i for i in input().split())
c = 0
for i in range(n+1):
    for j in range(i+1,n):
        if (a[i]<a[j]):
            c+=1
print(c)  
