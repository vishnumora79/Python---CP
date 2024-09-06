matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         x = input("Enter elements ")
#         row.append(x)
#     matrix.append(row)       
    
# for i in range(3):
#     for j in range(3):
#         if(i == j):
#             print(matrix[i][j]) 



# matrix2 = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(3):
#     for j in range(3):       
          
#                matrix2[i][j]= matrix[j][i]

# print(matrix) 

symmetric_matrix = [
    [0, 1, -2, 3, -4],
    [-1, 0, 5, -6, 7],
    [2, -5, 0, 8, -9],
    [-3, 6, -8, 0, 10],
    [4, -7, 9, -10, 0]
]
i,flag=0,1
while(i<len(symmetric_matrix)):
    for j in range(i,len(symmetric_matrix)):
        if(i!=j):
          symmetric_matrix[i][j] = symmetric_matrix[j][i]
            
    i+=1

print(symmetric_matrix)    
# if(flag==1):        
#    print("true")
# else:
#     print("false")





# flag = 1
# for i in range(3):
#     for j in range(3):
#         if (i != j and matrix[i][j] != matrix[j][i]):
#           flag = 0
#           break

# if flag == 1:
#    print('yes')
# else:
#    print('NO')              
              



