for t in range(int(input())):
    n=int(input())
    c=0
    for i in range(n):
        s,j=map(int,input().split())
        d=j-s
        if(d>5):
            c+=1
    print(c)
