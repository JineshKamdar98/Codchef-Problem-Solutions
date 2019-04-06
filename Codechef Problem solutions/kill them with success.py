t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    a.sort(reverse=True)
    for i in range(1,n):
        s=0
        s+=(a[i]/2)+(a[i-1]/2)
        a[i]=s
    print(float(s))
    t-=1
        
            
