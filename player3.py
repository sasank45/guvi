N = int(input())
num = 0
while(N!=0):
    rem = N%10
    num = num*10+rem
    N = int(N/10)
print(num)    
