lst = []
SizeOfList= int(input('enter the size of list \t'))

for i in range(0,SizeOfList):
    i = int(input('enter the element \t'))
    lst.append(i)
print(lst)

SortLst=[]
for MinFound in range(0,SizeOfList):
         MinFound=min(lst)
         SortLst.append(MinFound)
         lst.remove(MinFound)

print(SortLst)
print(lst)