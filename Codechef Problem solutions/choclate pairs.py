for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(i==n-1):
            break
        for j in range(i+1,n):
            if(a[i]+a[j]==k):
                c+=1
    print(c)
