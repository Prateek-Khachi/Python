import random

options = ["rock","paper" ,"scissors"]
user = 0
pc = 0

print("Welcome to Rock, Paper, Scissors!!")
while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit. " ).lower()
    
    if user_input == 'q':
        break
    
    elif user_input not in options:
        print("Enter a valid option. ")
        continue
    
    else:
        pc_choice=random.choice(options)

        if user_input==pc_choice:
            print("It's a Draw.")

        elif user_input=="rock" and pc_choice=="scissors":
            print("You Win!")
            user += 1    

        elif user_input=="paper" and pc_choice=="rock":
            print("You Win!")
            user += 1    

        elif user_input=="scissors" and pc_choice=="paper":
            print("You Win!")
            user += 1    

        else:
            print("You Lost!")
            pc+=1

print("You won ",user, "times.")
print("Computer won ",pc, "times.")
print("Goodbye!")                