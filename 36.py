n = list(map(str,input()))
count = 0
for i in n:
    if(i.isnumeric()==False):
        if(i.isalpha()==False):
            count+=1
print(count)  
