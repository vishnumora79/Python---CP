import random
if __name__ ==  '__main__':
 n = random.randrange(1,10)
 guess = int(input("Enter any number(1-10):"))
 while(n != guess):
    if (guess < n):
        print("Too Low")
        guess = int(input("Enter number again:"))
    elif (guess > n):
        print("Too high")
        guess = int(input("Enter number again:"))    
    else:
        break
 print("You guessed it right!! - it is:",guess)    