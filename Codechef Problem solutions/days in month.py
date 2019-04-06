a=['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
t=int(input())
while(t!=0):
    b=[4,4,4,4,4,4,4]
    w,s=input().split()
    w=int(w)
    if(w==28):
        print("4 4 4 4 4 4 4")
    else:
        strt=a.index(s)
        r=w-28
        for i in range(0,r):
            b[(i+strt)%7]=5
        print(b[0], b[1], b[2], b[3], b[4], b[5], b[6])
    t=t-1
