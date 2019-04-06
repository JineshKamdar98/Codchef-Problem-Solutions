t=int(input())
while(t!=0):
    s1=input()
    s2=input()
    for i in range(0,len(s1)):
        if s1[i]==s2[i]=='B':
            print('W',end='')
        else:
            print('B',end='')
    print()
    t=t-1
