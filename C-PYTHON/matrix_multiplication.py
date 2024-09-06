# Get user input for matrix dimensions
rows1, cols1 = map(int, input("Enter the number of rows and columns for first matrix (separated by space): ").split())
rows2, cols2 = map(int, input("Enter the number of rows and columns for second matrix (separated by space): ").split())

print(type(rows1))
# Input validation
if cols1 != rows2:
    raise ValueError("Incompatible dimensions for multiplication")

# Initialize matrices
matrix1 = []
matrix2 = []

# Read elements for matrix1
for _ in range(rows1):
    row = list(map(int, input("Enter row elements (separated by space): ").split()))
    matrix1.append(row)

# Read elements for matrix2
for _ in range(rows2):
    row = list(map(int, input("Enter row elements (separated by space): ").split()))
    matrix2.append(row)

# Initialize result matrix
result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]

# Perform multiplication
for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

# Print the result matrix
print("Result matrix:")
for row in result_matrix:
    for element in row:
        print(f"{element:.2f}", end=" ")
    print()
