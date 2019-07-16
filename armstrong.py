n = int(input())
temp = n
s = 0
while temp > 0:
   digit = temp % 10
   s += digit ** 3
   temp //= 10
if n == s:
   print("yes")
else:
   print("no")
