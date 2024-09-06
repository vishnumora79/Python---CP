s1 = input("ENTER STRING1:")
s2 = input("Enter string2:")

# l1, l2 = len(s1), len(s2)

# yes = False
# if l1 == l2:
#     for i in s1.lower():
#         for j in s2.lower():
#             if i == j:
#                 yes = True
# else:
#     yes = False

# if yes == True:
#     print(f"The given strings {s1} and {s2} are matched")
# else:
#     print(f"The given strings {s1} and {s2} are not matched")    


def solve(s1,s2):
    a, b = len(s1),len(s2)
    if a == 0 and b == 0:
        return True
    if(a > 1 and s1[0] == "?" or (a != 0 and b != 0 and s1[0] == s2[0])):
        return solve(s1[1:],s2[1:])
    if a != 0 and s1[0] == '?':
        return solve(s1[1:],s2 or solve(s1,s2[1:]))    
# solve(s1,s2)    
if solve(s1,s2) == True:
    print(f"The given strings {s1} and {s2} are matched")
else:
    print(f"The given strings {s1} and {s2} are not matched")    

