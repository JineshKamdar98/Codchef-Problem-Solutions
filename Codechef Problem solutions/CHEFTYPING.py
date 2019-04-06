hand = {'d':'l','f':'l','j':'r','k':'r'}
for _ in range(int(input())):
    n = int(input())
    time=0
    words={}
    p=''
    while(n>0):
        t=0
        s=input()
        l=len(s)
        if(s in words):
            time+=words[s]/2
        else:
            i=1
            p=hand[s[0]]
            t+=0.2
            while(i<l):
                if(hand[s[i]]==p):
                    t+=0.4
                else:
                    t+=0.2
                p=hand[s[i]]
                i+=1
            words[s]=t
            time+=t
        n-=1
    print('{:.0f}'.format(time*10,2))
