t=int(input())
while(t!=0):
    a=list(map(int,input().split()[:30]))
    if a.count(1)==30:
        print("#coderlifematters")
        t=t-1
        continue
    if a.count(0)==30:
        print("#allcodersarefun")
        t=t-1
        continue
    c=0
    for i in a:
        if i==1:
            c+=1
            if(c>5):
                print("#coderlifematters")
                break
        if i==0:
            c=0
    else:
        print("#allcodersarefun")
    t-=1
