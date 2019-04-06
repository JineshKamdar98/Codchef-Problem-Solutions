def isSorted(r):
    flag=1
    for j in range(1,len(r)):
        if(r[j]<r[j-1]):
            flag=0
            break
    return flag

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    b=a
    f=0
    for i in range(n-1):
        tem=b.pop(0)
        b.append(tem)
        if(isSorted(b)==1):
            f=1
            break
    if(f==1):
        print('YES')
    else:
        print('NO')
        
