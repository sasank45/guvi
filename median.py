n = int(input())
x = list(map(int,input().split()[:n]))
y = sorted(x)
length = len(y)
if n%2!=0:
    b = n // 2 
print(y[b])
    
