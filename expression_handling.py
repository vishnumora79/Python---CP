a = "5*6+8-2/4"
result = 0
for c in a:
    if c == '+':
         result += int(a[(a.index(c)-1)]) + int(a[(a.index(c) + 1)])
    elif(c == '-'):
        result += int(a[(a.index(c)-1)]) - int(a[(a.index(c) + 1)]) 
         
    elif(c == '*'):
        result += int(a[(a.index(c)-1)]) * int(a[(a.index(c) + 1)])
    elif(c == '/'):
        result += int(a[(a.index(c)-1)]) // int(a[(a.index(c) + 1)])
        

print(result)        




