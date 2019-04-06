t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    flag=0
    amt=0
    for i in range(n):
        if(a[i]==0):
            amt+=1100
            flag+=1
        else:
            if(flag!=0):
                amt+=100
    print(amt)
    t=t-1
