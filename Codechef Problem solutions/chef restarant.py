import bisect
for _ in range(int(input())):
    n,m = map(int,input().split())
    start = []
    t = {}
    end_max = 0
    for i in range(n):
        p,q = map(int,input().split())
        start.append(p)
        t[p]=q
        if(q > end_max):
            end_max = q
    start.sort()
    for j in range(m):
        #a = list(map(int,input().split()))
        a = int(input())
        if(a >= end_max):
            print("-1")
        #elif(a in start):
            #print("0")
        else:
            temp = bisect.bisect_left(start,a)
            if(temp==0):
                print(start[0] - a)
                continue
            if(a < t[start[temp-1]]):
                print("0")
            else:
                print(start[temp] - a)
    
