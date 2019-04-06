for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    l=len(a)
    temp=0
    attack=0
    for i in range(l):
        if(i==0):
            attack=a[1]+a[l-1]
            if(d[0]>attack and d[0]>temp):
                temp=d[0]
        elif(i==l-1):
            attack=a[0]+a[l-2]
            if(d[l-1]>attack and d[l-1]>temp):
                temp=d[l-1]
        else:
            attack=a[i-1]+a[i+1]
            if(d[i]>attack and d[i]>temp):
                temp=d[i]
    if(temp!=0):
        print(temp)
    else:
        print("-1")
                
