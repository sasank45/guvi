x=list(map(str,input()))
count=0
for k in x:
     if((k=='a')or(k=='e')or(k=='i')or(k=='o')or(k=='u')):
         count=count+1
if(count==0):
   print("no")
else:
    print("yes")
