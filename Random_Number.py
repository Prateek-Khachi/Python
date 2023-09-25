import random

print("Enter the range of the numbers to choose from: ")
a = input()
b= input()

if ((a.isdigit()==True and b.isdigit()==True) or ((a[0]=='-' and a[1:].isdigit()==True) and (b[0]=='-' and b[1:].isdigit()==True)) or ((a[0]=='-' and a[1:].isdigit()==True) and (b.isdigit()==True)) or ((a.isdigit()==True)and (b[0]=='-' and b[1:].isdigit()==True))):
    
    start=int(a)
    end=int(b)

else:  
    print("Please Enter a valid number next time.")
    quit()

if start > end:
    start, end = end, start

random_number = random.randint(start,end)
guesses=1
while True:
    

    guess=(input("Guess a number: "))

    if ((guess.isdigit()) or (guess.startswith('-') and guess[1:].isdigit())):
        guess= int(guess)
        
    else:
        print("Please enter a number next time.")
        continue

    if (guess < random_number):
        print("Try a bigger number.")
        guesses+= 1
        

    elif (guess > random_number):
        print("Try a smaller number.")   
        guesses+=1       

    else:    
        print("Congrats!!.")
        print("You got it in", guesses ,"guesses!!")
        quit()