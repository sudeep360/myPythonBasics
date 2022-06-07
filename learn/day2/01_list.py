#storing user entered fruit items as a list 

fruit=list()
newFruitList=list()
def addFruits(items):
    for i in range(items):
        oneAtATimeFruit=input(f"Enter fruit no{i}:\t")   
        newFruitList.insert(i,oneAtATimeFruit)
    return newFruitList
x=int(input("Enter a number of fruits that you want to add:\t"))
y=addFruits(x)
print("\nYour list of fruits are \n")
print(y)


#error is fixed and now takes input from users and prints out a list