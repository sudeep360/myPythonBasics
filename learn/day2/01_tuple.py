# this program removes enpty tuple(s) from a tuple 

myTuple=("Apple",["Samsung","HTC", "Pixel","One Plus"], [], [], [],(),{})
myTuple= [t for t in myTuple if t]
# EXPLANATION for the logic:
# for t in myTuple 
# if t is true, because empty tuple evaluates to false in Python
# return t 
print(myTuple)