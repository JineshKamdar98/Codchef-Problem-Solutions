for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    total=0
    count=0
    for i in a:
        #print(total,count,i)
        if(total>=i):
            count+=1
            total+=1
    print(count)
