t=int(input())
for _ in range(t):
    n=int(input())
    v=list(map(int,input().split()))
    v.sort()
    i=1
    Min=10000001
    while(i<len(v)):
        temp=v[i]-v[i-1]
        if(temp<Min):
            Min=temp
        i+=1
    print(Min)
