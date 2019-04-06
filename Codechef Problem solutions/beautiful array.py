t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    if(a.count(1)>=1 and a.count(1)+a.count(0)+a.count(-1)==n)or(a.count(1)+a.count(0)>=n-1):
        print('yes')
    else:
        print('no')
    t=t-1
