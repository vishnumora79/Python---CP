mylist = [1,9,5,1,7,9,1,24]

dict1 = {}

for i in mylist:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

result = [x for x in mylist if dict1[x] == 1]

print(result)