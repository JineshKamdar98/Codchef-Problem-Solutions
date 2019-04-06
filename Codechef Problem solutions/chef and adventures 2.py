for t in range(int(input())):
    n,m,x,y=input().split()
    n,m,x,y=[int(n),int(m),int(x),int(y)]
    k=n%x
    p=m%y
    k1=n//x
    p1=m//y
    if(k==p and k1==p1+1):
        print('Chefirnemo')
    else:
        print('Pofik')
