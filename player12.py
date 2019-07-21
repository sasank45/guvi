N,K = map(int,input().split())       
a = list(map(int,input().split()[:N])) 
for i in range(0, K):      
    last = a[len(a)-1]    
    for j in range(len(a)-1, -1, -1):       
        a[j] = a[j-1]     
    a[0] = last           
for i in range(0, len(a)):    
    print(a[i],end=" ")
