for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    b=[]
    a.sort()
    b.append(abs(a[0]-a[n-1]))
    for i in range(1,n):
        b.append(abs(a[i]-a[i-1]))
    print(min(b))
