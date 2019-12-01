A=10
B=11
C=A
print(A ,'=', id(A) ,'\t', B ,'=' ,id(B),' \t', C ,'=',id(C))
C=float(A)
C=complex(A,B)
print(type(A),'\t',type(C))

if A>B | A<B :
    print('A is grater than B').format(A,B)
else:
    print(A,'IS GRT THAN',B)

    if A>B:
        A=10;
    elif A==10:
        A=5;
    else:
        print('not in range')

        print(A)

