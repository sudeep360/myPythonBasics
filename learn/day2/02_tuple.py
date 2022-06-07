# tuple sorted in descending order

sampleTuple=(('item1','12.20'),('item2','15.50'),('item3','16.65'))

# you cannot change/sort tuple so convet to list first and only sort in descending order

convertToList=list(sampleTuple)
convertToList.sort(reverse=True)
newTuple=tuple(convertToList)
print(newTuple)