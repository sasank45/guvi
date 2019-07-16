n1,n2 = map(int,input().split())
for i in range(n1,n2):
    temp = i
    s = 0
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
    if i == s:
        print(i,end=" ")
