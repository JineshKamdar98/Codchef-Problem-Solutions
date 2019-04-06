for t in range(int(input())):
    D=int(input())
    d=[0]*D
    p=[0]*D
    for i in range(D):
        d[i],p[i]=map(int,input().split())
    Q=int(input())
    for j in range(Q):
        dead,req=map(int,input().split())
        s=0
        for k in range(len(d)):
            if(d[k]<=dead):
                s=s+p[k]
            else:
                break
        if(s>=req):
            print("Go Camp")
        else:
            print("Go Sleep")
                
        
