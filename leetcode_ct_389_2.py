s1 = 'abada'
c = 'a'
count = 0
substrings = []

for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        substrings.append(s1[i:j])

for x in substrings:
    if x[0] == c and x[-1] == c:
        count +=1       
print(count)
print(substrings)        