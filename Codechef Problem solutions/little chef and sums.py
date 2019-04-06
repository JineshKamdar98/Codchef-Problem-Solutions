t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split()))
    print(a.index(min(a))+1)
    t=t-1
