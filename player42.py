n = int(input())
a = list(int(i) for i in input().split()[:n])
b = sorted(a)
if a==b:
    print("yes")
else:
    print("no")
