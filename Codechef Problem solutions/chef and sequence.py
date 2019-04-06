for t in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    c=0
    for i in range(n):
        if(a[i]!=1):
            c+=1
    if(c<=k):
        print("YES")
    else:
        print("NO")
