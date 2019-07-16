n,k = map(int,input().split())
if k-n>1:
    for i in range(n+1,k):
        if(i%2 != 0):
            print(i)
else:
    print("no numbers")
