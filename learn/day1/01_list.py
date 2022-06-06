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
print("Your list of fruits are \n")
print(y)


#Fixed the input error now need to display each input by the user
