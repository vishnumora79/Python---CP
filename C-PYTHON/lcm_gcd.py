a, b = int(input("Enter a:")), int(input("Enter b:"))

if a > b:
    smaller = b
else:
    smaller = a
for i in range(1,smaller+1):
    if a % i == 0 and b % i == 0:
        gcd = i
    else:
        gcd = 1

lcm = (a * b) // gcd

print(f"GCD of {a} and {b} is {gcd}")
print(f"LCM of {a} and {b} is {lcm}")


 
