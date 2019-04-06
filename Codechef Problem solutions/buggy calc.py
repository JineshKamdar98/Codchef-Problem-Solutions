t=int(input())
while(t!=0):
    a,b=input().split()
    a,b=[int(a),int(b)]
    c=[0]*30
    i=0
    while(a>0 or b>0):
        r1=a%10
        a=a//10
        r2=b%10
        b=b//10
        if(r1+r2>9):
            c[i]=(r1+r2)%10
        else:
            c[i]=r1+r2
        i+=1
    for k in range(i-1,-1,-1):
        print(c[k],end='')
    print()
    t=t-1
    
