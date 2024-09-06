# Find the odd longest word in a sentence
# user = input("Enter the string:")

# mylist = user.split()
# mydict = {}
# for i in mylist:
#     if (len(i) % 2) != 0:
#        mydict[i] = len(i)

# for i,j in mydict.items():
#     if j == max(mydict.values()):
#         print(i)
#         break 

# user = input().split()

# result = ""

# for word in user:
#     if((len(word) & 1) and (len(word) > len(result))):
#             result = word

# print(result)  

# Finding the maximum profit

# def fun(diff):
#     n = len(diff)
#     if(n == 0):
#         return 0
#     mx = max(diff)
#     if mx <= 0:
#         return 0
#     maxS = 0
#     cS = 0

#     for i in diff:
#         cS += i
#         # print(cS,end = " ")
#         if(cS <= 0):
#             cS = 0
#         maxS = max(cS,maxS)
#     return maxS        

# n = int(input("No of transactions:"))
# arr = []
# diff = []
# for i in range(n):
#    arr.append(int(input(f"Enter {i+1} transactions")))
# for i in range(n-1):   
#    diff.append(arr[i+1] - arr[i])
#    result = fun(diff)

# print(result)




# arr = [1,4,2,5,9]

# countp = 0
# result = ()
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if((i<j) and (arr[i] > arr[j])):
#             result = (arr[i],arr[j])
#             countp += 1

# print(result)
# print(countp)


# strs = ['flower','flow','flight','fapple']

# for word in strs:
#     if not word:
#         print("No prefix")
#     prefix = strs[0]
#     while not word.startswith(prefix):
#         prefix = prefix[:-1]
        
# print(prefix)    

# strs.sort()
# print(strs)
# first = strs[0]
# last = strs[-1]
# print(first,last)
# prefix = ''

# for i in range(len(first)):
#     if( (i < len(first)) and first[i] == last[i]):
#         prefix += first[i]

# print(prefix)  

def generate_parentheses(n):
    def backtrack(s = "",left = 0,right = 0):
        if(len(s) == 2*n):
            result.append(s)
        if(left < n):
            backtrack(s + "(" , left + 1,right)
        if(right < left):
            backtrack(s + ")",left,right + 1)
    result = []
    backtrack()
    return result

print(generate_parentheses(4))                











