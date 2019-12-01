f=open('family_members','r')
Data = f.readlines()
Found=0
try:
    for i in Data:
        i = i.lower()
        i=i.replace("\n","")
        if i == 'mang':
            Found = 1
    if Found == 1:
        print('String Found')
    else:
        print('string not found')
finally:
    f.close()