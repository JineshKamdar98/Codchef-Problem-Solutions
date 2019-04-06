def isSorted(a):
    i=1
    l=len(a)
    while(i<l):
        if(a[i]<a[i-1]):
            return False
        i+=1
    return True
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s=[]
    s.append(l[0])
    i=1
    while(i<n):
        if(l[i]>=l[i-1]):
            s.append(l[i])
        else:
            break
        i+=1
    b=l[i:]
    b.extend(s)
    if(isSorted(b)):
        print("YES")
    else:
        print("NO")
