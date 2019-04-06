for t in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    tem=k
    s=''
    for i in range(0,len(a)):
        if(a[i]<=tem):
            s+='1'
            tem=tem-a[i]
        else:
            s+='0'
    print(s)
        
