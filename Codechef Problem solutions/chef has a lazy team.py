for t in range(int(input())):
    n,r=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    a.sort()
    x=n
    c=0
    for i in range(n):
        if(a[i]<=r):
            c+=1
        elif(a[i]>r):
            break
    print(str(x)+" "+str(c)+" "+str(c))
    
