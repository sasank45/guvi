N = int(input())
if N<=20:
    if (N==0):
        print("1")
    else:
        f = 1
        for i in range(1,N+1):
            f = f*i
        print(f)    
