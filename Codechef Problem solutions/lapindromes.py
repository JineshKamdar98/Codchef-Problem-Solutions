t=int(input())
while(t!=0):
    s=input()
    p=list(s[:len(s)//2])
    q=list(s[-(len(s)//2):])
    if(sorted(p)==sorted(q)):
        print('YES')
    else:
        print('NO')
    t-=1
