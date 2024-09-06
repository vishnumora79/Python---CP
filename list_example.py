a = [20,30,50,[5,6],3,10]
for i in a:
    if type(i) is list:
        for j in i:
            a.append(j) 
        a.remove(i)  
a.sort()
print(a)
