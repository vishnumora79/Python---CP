s = "leetcode"
substrings = []
for i in range(len(s)-1):
    substrings.append(s[i:i+2])

print(substrings)
s1 = s[::-1]
reverse_str = []
for i in range(len(s1)-1):
    reverse_str.append(s1[i:i+2])

print(reverse_str)    

for i in substrings:
    if i in reverse_str:
        print(True)
        break    
else:
    print(False)