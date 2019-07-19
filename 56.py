str = list(input())
c = 0
b = 0
for i in str:
    if i.isnumeric():
        c+=1
    elif i.isalpha():
        b+=1

if c>0 and b>0:
    print("yes")
else:
    print("no")
