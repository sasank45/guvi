n = list(map(str,input()))
count = 0
for i in n:
    if(i.isnumeric()==True):
        count+=1
print(count)    
