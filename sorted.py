n = int(input())
x = list(map(int,input().split()[:n]))
y = sorted(x)
for i in y:
    print(i,end=" ")
