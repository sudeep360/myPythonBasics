#storing user entered fruit items as a list 

fruit=list()
newFruitList=list()
def addFruits(items):
    for i in range(items):
        fruit=input(f"Enter fruit no{i}:\t")
    newFruitList=fruit
    return newFruitList

x=int(input("Enter a number of fruits that you want to add:\t"))
y=addFruits(x)
print(y)
#This code has an error for now so fix the bug after push