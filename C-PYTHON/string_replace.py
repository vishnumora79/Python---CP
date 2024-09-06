# Method - 1
n = int(input("Enter N:"))
n = str(n)
# exp = n.replace('0','1')
# a = int(exp)
# print(a)

# Method - 2
import re

exp = re.sub(r"[0]","1",n)

print(exp)

