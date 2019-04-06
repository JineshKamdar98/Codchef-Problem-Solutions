a=list(map(int,input().split()))
b=a[1:len(a)]
m=1000005
c=[]
for i in range(2,m+1):
    c[i]=pow(2,i-1)-c[i-1]
for j in range(len(b)):
    d=2**b[j]
    print(c[j],d,end=' ')
