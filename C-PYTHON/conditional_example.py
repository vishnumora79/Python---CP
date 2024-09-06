n = int(input("Enter N:"))
a = n % 2
if a != 0:
    print("weird")
elif a == 0 and n in range(2,6):
    print("Not Weird")
elif a == 0 and n in range(6,21):
    print("Weird")
elif a == 0 and n > 20:
    print("Not Weird")        