t=int(input())
for i in range(t):
    n=int(input())
    if n==0:
        print('Draw')
        continue
    a=input()
    b=''
    c=''
    c1=1
    c2=0
    for j in range(1,n):
        b=input()
        if(b==a):
            c1+=1
        if(b!=a):
            c=b
            c2+=1
    if(c1>c2):
        print(a)
    elif(c1<c2):
        print(c)
    else:
        print('Draw')
    
    
        
        
    
