t=int(input())
while(t!=0):
    a=list(map(int,input().split()))
    a.remove(len(a)-1)
    print(max(a))
    t=t-1
    
