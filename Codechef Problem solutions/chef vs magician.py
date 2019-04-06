for t in range(int(input())):
    n,x,s=input().split()
    n,x,s=[int(n),int(x),int(s)]
    p=x
    for i in range(s):
        f=0
        a,b=map(int,input().split())
        if(a==p):
            p=b
            f=1
        elif(b==p and f==0):
            p=a
    print(p)
