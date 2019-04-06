try:
    t=int(input())
    while(t):
        n=int(input())
        st=['']*n
        temp=['']*200
        count=0
        for i in range(n):
            st[i]=input()
        for i in range(len(st[0])):
            for j in range(len(st[1])):
                if(st[0][i]==st[1][j]):
                    if(st[0][i] not in temp):
                        temp.append(st[0][i])
        for j in range(2,len(st)):
            for k in range(len(st[j])):
                if(st[j][k] in temp):
                    count+=1
        print(count)
        t-=1
except:
    pass
