for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    f=0
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]!=a[j]):
                if(a[a[i]-1]==a[a[j]-1]):
                    f=1
                    break
        if(f==1):
            break
    if(f==0):
        print("Poor Chef")
    else:
        print("Truly Happy")
    
    
