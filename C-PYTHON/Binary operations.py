# Binary operations
input_string = input("Enter string:")
characters = list(input_string)

def function(characters):
    a = int(characters[0])
    op = characters[1]
    for _ in characters:
        if op == 'A':
           return a and characters[2]
        elif op == 'B':
           return a or characters[2]
        elif op == 'C':
           return a ^ characters[2]
    return function

# print(inter)        
          
        

        


