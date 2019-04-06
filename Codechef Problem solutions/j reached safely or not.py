t=int(input())
for i in range(1,t+1):
    m,n=map(int,input().split())
    rx,ry=map(int,input().split())
    l=int(input())
    s=input()
    x=0
    y=0
    for a in list(s):
            if a=='U':y+=1
            elif a=='D':y-=1
            elif a=='R':x+=1
            elif a=='L':x-=1
    if x<0 or x>m or y<0 or y>n:
            print("Case {:d}: DANGER".format(i))
    elif x==rx and y==ry:
            print("Case {:d}: REACHED".format(i))
    else:print("Case {:d}: SOMEWHERE".format(i))
