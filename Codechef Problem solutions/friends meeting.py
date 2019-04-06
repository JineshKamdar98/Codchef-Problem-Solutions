t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split(' ')[:n]))
    b=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    f=0
    if 1 in a:
        f=1
    if(f==1):
        a.sort()
        r=a.count(1)
        for i in range(r,len(a)):
            if a[i] in b:
                print(a[i])
                break
        else:
            print('-1')
    else:
        print('-1')
    t=t-1
            
                
                    
    
