for t in range(int(input())):
    n,m=map(int,input().split())
    i=0
    invalid=0
    weak=0
    p=[]
    q=[]
    while(i<n):
        a,b=input().split()
        p.append(a)
        q.append(b)
        i+=1
    for i in range(n):
        if(p[i]=='correct' and q[i].count('0')!=0):
            print('INVALID')
            invalid=1
            break
        elif(p[i]=='wrong' and q[i].count('0')==0):
            weak=1
    if(weak==1 and invalid==0):
        print('WEAK')
    elif(invalid==0 and weak==0):
        print('FINE')
        
