n,k = list(map(int,input().split()))
a = list(map(int,input().split()[:n]))
a.sort()
print(a[k-1])
