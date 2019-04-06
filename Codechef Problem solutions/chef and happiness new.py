for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    a.sort()
    index=[]
    value=[]
    f=0
    for i in range(n-1,-1,-1):
        if((a[i]-1) in index):
            f=0
            break
        else:
            index.append(a[i]-1)
            value.append(a[i])
            if(value.count(a[i])>1):
                f=1
    if(f==1):
        print("Truly Happy")
    else:
        print("Poor Chef")
