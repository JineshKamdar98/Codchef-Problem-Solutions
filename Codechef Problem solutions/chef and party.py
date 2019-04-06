for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    a.sort()
    c=0
    enter=0
    for i in range(len(a)):
        if(a[i]==0):
            enter+=1
            c+=1
            continue
        elif(a[i]<c):
            enter+=1
            c+=1
        
    print(enter)
