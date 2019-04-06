t=int(input())

while(t!=0):
    a,b,n=input().split()
    a,b,n=[int(a),(b),int(n)]
    p1=True
    p2=False
    for i in range(n):
        if(p1==True):
            a=a*2
            p1=False
            p2=True
        elif(p2==True):
            b=b*2
            p2=False
            p1=True
    ans=max(a,b)//min(a,b)
    print(ans)
    t=t-1
