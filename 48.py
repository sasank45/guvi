 N = int(input())
a = list(map(int,input().split()[:N]))
avg = 0
for i in a:
    avg = i+avg
print(int(avg/N))    
