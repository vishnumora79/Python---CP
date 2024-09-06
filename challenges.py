
# Problem - 1

# a, b, c = map(int,input().split())
# x = []
# x.append(a)
# x.append(b)
# x.append(c)
# d, e, f = map(int,input().split())
# y = []
# y.append(d)
# y.append(e)
# y.append(f)

# person1, person2 = 0,0 

# for i in range(len(x)):
#     if(x[i] > y[i]):
#         person1 += 1
#     elif(x[i] == y[i]):
#         person1    
#     else:
#         person2 += 1    
 

# print(person1,person2)                     


# Problem - 2

a = []
for _ in range(5):
    x = int(input())
    a.append(x)
    

b = [0] * len(a) 

for i in range(len(a)):
    sum = 0
    for j in range(len(a)):
        if j == i:
           continue
        else:
           sum += a[j]
    b[i] = sum
    i += 1
print(b)    

max = min = b[0]
for i in range(len(b)):
    if(b[i] > max):
        max = b[i]
    if(b[i] < min):
        min = b[i]

print("Maximum value:",max,"Minimum value:",min)            

