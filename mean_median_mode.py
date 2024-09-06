#declare a list
list1 = []
for i in range(5):
    a = int(input("enter number:"))
    list1.append(a)
frequency = {}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i] += 1    
frequent = max(frequency.values())
for i,j in frequency.items():
    if j == frequent:
        mode = i
mean = sum(list1) / len(list1)
list1.sort()
if len(list1) % 2 == 0:
   m1 = list1[len(list1) // 2]
   m2 = list1[len(list1) // 2 - 1]        
   median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]
print("mean:",mean)
print("median:",median)
print("mode:",mode)       