lst=[3,3,1,5,4,3,1,1,4,1,3,5,5,5,5,5,3,3]
print(sorted(lst))
lst1 =sorted(lst)
D=[]
E=[]
newlst = []
for j in lst:
    maxFound=max(lst)
    count = lst.count(maxFound)
    newlst.append(maxFound)
    newlst.append(count)
    for i in lst:
        if count != 0:
            lst.remove(maxFound)
            count-=1
print(lst)
print(newlst)
SizeOfNewLst= len(newlst)
for z in range(1,SizeOfNewLst,2):
   a=newlst[z]
   D.append(a)
for y in range(0,SizeOfNewLst,2):
   a=newlst[y]
   E.append(a)

print(D)
print(E)
MaxInD=max(D)
IndexFound=D.index(MaxInD)
MaxCount= E[IndexFound]
print(MaxCount)
