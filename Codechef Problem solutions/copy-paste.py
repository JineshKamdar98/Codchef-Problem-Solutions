for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    a=set(a)
    print(len(a))
