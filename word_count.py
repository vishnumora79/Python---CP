n = int(input("Enter number:"))

for i in range(n):
    x = input("Enter word:")
    words = x.split(" ")
    length = len(words)
    print(f"Length of {i+1} person is {length}")
    if(length <= 2):
        score = 2
    elif(length > 2 and length <= 5):
        score = 3
    elif(length > 5 and length <= 7):
        score = 4
    elif(length > 7 and length <= 9):
        score = 5       
    print("The score is :", score)         
    
    
