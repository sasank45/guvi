n = int(input())
c = 0
for i in range(0,n+1):
    if pow(2,i)==n:
        c+=1
if(c>0):
    print("yes")
else:
    print("no")
 
