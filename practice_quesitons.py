string_1 = input("Enter one string:")

length = len(string_1)

print(length)
dict = {}

for char in string_1:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1    

print(dict)      
