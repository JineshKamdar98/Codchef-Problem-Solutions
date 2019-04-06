n=int(input())
a=[0]*n
m=int(input())
while(m!=0):
    l,r=map(int,input().split())
    for i in range(l,r+1):
        a[i-1]+=1
    m=m-1
a.sort(reverse=True)
q=int(input())
while(q!=0):
    k=int(input())
    c=0
    for i in a:
        if(i>=k):
            c+=1
        else:
            break
    print(c)
    q=q-1
