n = int(input())
arr = list(int(i) for i in input().split()[:n])
for i in range(n+1):
    if arr[i]>arr[i+1]:
        c = arr[i]
        break
print(c)  
