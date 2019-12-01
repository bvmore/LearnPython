#Data=[]
f=open('family_members','r')
Data=f.readlines()
#print(Data)
surname="Bharsakle"
try:

    for i in Data:
        i = i.replace('\n', '')
        if i == "Bhavana":
            print(i + " More")
        else:
            print(i+" "+surname)

           # print(surname)
          #  print('Bharsakle')
finally:
    f.close()



