# string_1 = input("Enter one string:")

# length = len(string_1)

# print(length)
# dict = {}

# for char in string_1:
#     if char not in dict:
#         dict[char] = 1
#     else:
#         dict[char] += 1    

# print(dict)      



n = int(input("Enter number:"))
primes = []

def isprime(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,n//2 + 1):
            if(n % i == 0):
                return False
                
        return True  
    
for i in range(n):
    if isprime(i):
       primes.append(i)
print(primes)
print(f"The maximum prime number below {n} is: {max(primes)} ")       

       