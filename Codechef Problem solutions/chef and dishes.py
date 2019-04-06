for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    c=0
    for i in a:
        if(i>=x):
            c+=1
            break
    if(c==1):
        print('YES')
    elif(c==0):
        print('NO')

    

