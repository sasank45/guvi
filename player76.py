n = int(input())
a = list(int(i) for i in input().split())
for i in range(n-1):
    if a[i]+2!=a[i]+1:
        print(a[i+1])
        break
