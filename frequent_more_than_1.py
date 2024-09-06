a = int(input("Enter the length of list:"))
mylist1 = []
print("Enter the elements:")
for _ in range(a):
    x = int(input())
    mylist1.append(x)

# Method - 1:
# mylist2 = set([x for x in mylist1 if mylist1.count(x) > 1])

# Method - 2:
dict1 = {}

for i in mylist1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1    
mylist2 = set([x for x in mylist1 if dict1[x] > 1])

print(list(mylist2))