nums = [10,21,31]
b = []
for i in nums:
    if i < 10:
        pass
    else:
        j = list(map(int,str(i)))
        maxi = max(j)
        for x in range(len(j)):
            if j[x] != maxi:
                j[x] = maxi
        i = int("".join(map(str,j)))
        b.append(i)
print(b)        
total = sum(b)
print(total)


# class Solution:
#     def sumOfEncryptedInt(self, nums: List[int]) -> int:
#         b = []
#         for i in nums:
#             if i < 10:
#                 b.append(i)
#             else:
#                 j = list(map(int,str(i)))
#                 maxi = max(j)
#                 for x in range(len(j)):
#                     if j[x] != maxi:
#                         j[x] = maxi
#                 i = int("".join(map(str,j)))
#                 b.append(i)
        
#         total = sum(b)
#         return total
                