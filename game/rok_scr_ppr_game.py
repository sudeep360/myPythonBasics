from operator import truediv
import random
from re import S, T

def gameWin(comp,user):
    if comp==user:
        return None
    elif comp=='s':
        if user=='p':
            return False
        elif user=='r':
            return True
    elif comp=='p':
        if user=='s':
            return True
        elif user=='r':
            return False
    elif comp=='r':
        if user=='s':
            return False
        elif user=='p':
            return True
        
    

randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
else:
    comp='r'

print("Pick one either Scissors(s)/Paper(p)/Rock(r)\n")
user=input("Type 's' or 'p' or 'r':")

if user=='s' or user=='p' or user=='r': 
    print(f"you have choosen {user}")
    print(f"Computer has choosen {comp}")
    a=gameWin(comp,user)
    if a==None:
        print("Game tie!")
    elif a==True:
        print("YOU WON!! HURRAH !!!")
    else:
        print("YOU LOST !! SORRY :( ")
else:
    print("PLEASE CHOOSE THE CORRECT STRING AMONG s, p or r !!")

 


