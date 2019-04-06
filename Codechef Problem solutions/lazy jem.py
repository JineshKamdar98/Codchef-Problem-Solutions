t=int(input())
while(t!=0):
    n,b,m=input().split()
    n,b,m=[int(n),int(b),int(m)]
    tim=0
    bt=0
    while(n>0):
        if(n%2!=0):
            tim=tim+((n+1)//2)*m
            n=n-(n+1)//2
        else:
            n=n//2
            tim=tim+(n*m)

        if(n!=0):
            bt+=b
            m*=2
    print(tim+bt)
    t=t-1
    
