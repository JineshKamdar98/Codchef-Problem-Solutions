def prime(n):
    f=0
    for i in range(2,n):
        if(n%i==0):
            f=1
    return f

for t in range(int(input())):
    x,y=map(int,input().split())
    n=x+y
    while(True):
        n+=1
        f=prime(n)
        if(f==0):
            break
    print(n-(x+y))

        
