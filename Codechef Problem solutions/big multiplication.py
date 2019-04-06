t=int(input())
while(t!=0):
    m,n=input().split()
    m,n=[int(m),int(n)]
    p=m*n
    print(p%3)
    t=t-1
