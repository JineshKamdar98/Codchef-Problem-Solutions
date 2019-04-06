t=int(input())
while(t!=0):
    c,d,l=input().split()
    c,d,l=[int(c),int(d),int(l)]
    m1=(4*c+4*d)
    if(c<=2*d):
        m2=4*d
    else:
        m2=4*(c-d)

    if(l%4==0 and l>=m2 and l<=m1):
        print('yes')
    else:
        print('no')
    t=t-1
