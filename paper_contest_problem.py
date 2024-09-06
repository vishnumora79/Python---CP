n = int(input("Enter number of participants:"))

dict = {}

for i in range(n):
    length = int(input("Enter length of words:"))
    score = int(input("score:"))
    dict[length] = score

remove_keys = [key for key in dict.keys() if key > 10]
for i in remove_keys:
        dict.pop(i)

maxi = max(dict.values())    
        # maxi = max(dict.values())
print(dict)
print("The winner is :", maxi)    
