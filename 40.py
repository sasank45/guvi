N = int(input())
a = 0
b = 1
for i in range(1,N+1):
    if i==1:
        print(a+b,end=" ")
    else:
        n = a+b
        print(n,end=" ")
        a = b
        b = n
