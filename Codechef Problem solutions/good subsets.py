def gcd(p,q):
    if(q==0):
        return p
    return gcd(q,p%q)

t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split(' ')[:n]))
    div=0
    for i in a:
        div=gcd(div,i)
    if(div==1):
        print('YES')
    else:
        print('NO')
    t=t-1
