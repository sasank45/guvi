N = int(input())
s = list(map(str,input()[:N]))
for i in s:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        s.remove(i)
s.reverse()        
for i in s:
    print(i,end="")
