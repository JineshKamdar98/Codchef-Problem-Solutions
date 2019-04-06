t=int(input())

while(t!=0):
    n=int(input())
    q=(10**n)-(10**(n-1))
    l=10**(n-1)
    u=(10**n)-1
    p=0
    for a in range(l,u+1):
        c=str(a)
        for i in range(0,int(len(c)/2)):
            if c[i]==c[len(c)-i-1]:
                p+=1
    t=t-1

    print(p,q)

    
            
            
        
