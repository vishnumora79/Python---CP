# Method - 1:
import re
n = int(input("Enter number of rows for pascal triangle:"))

triangle = [[1]]

for _ in range(1,n):
    current_row = [1]
    previous_row = triangle[-1]
    for i in range(1,len(previous_row)):
        current_row.append(previous_row[i-1] + previous_row[i])
    current_row.append(1)
    triangle.append(current_row)

for row in triangle:
     row = re.sub(r"[\[\]]","","".join(map(str,row)))
    
     print(row)


# Method - 2:
n = int(input("Enter the n value:"))
for i in range(1,n + 1):
    print(int(ascii(1)*i)**2)

    
    
