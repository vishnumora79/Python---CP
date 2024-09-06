# Armstrong number
n = int(input("Enter N:"))

sum = 0
s = list(str(n))
if len(s) == 2:
   for i in s:
    sum += int(i) ** 2
if len(s) == 3:
   for i in s:
    sum += int(i) ** 3
if len(s) == 4:
   for i in s:
    sum += int(i) ** 4       

if sum == n:
    print(f"{n} is armstrong number")    
else:
    print(f"{n} is not armstrong number")  