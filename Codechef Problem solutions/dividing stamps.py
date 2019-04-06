n=int(input())
a=list(map(int,input().split()[:n]))
s1=sum(a)
s2=0
for i in range(1,n+1):
    s2+=i
if(s1==s2):
    print('YES')
else:
    print('NO')
