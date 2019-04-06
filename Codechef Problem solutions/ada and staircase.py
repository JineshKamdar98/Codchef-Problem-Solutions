for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    i=1
    total=0
    while(i<=n):
        t=a[i]-a[i-1]
        if(t>k):
            total+=t//k
            if(t%k==0):
                total-=1
        i+=1
    print(total)
