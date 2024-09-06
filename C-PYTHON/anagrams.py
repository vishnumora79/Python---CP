s1,s2 = input(),input()

l1, l2 = len(s1), len(s2)

a1 = sorted(s1)
a2 = sorted(s2)

if a1 == a2:
    print(f"{s1} and {s2} are anagrams")
else:
    print(f"{s1} and {s2} are not anagrams")   