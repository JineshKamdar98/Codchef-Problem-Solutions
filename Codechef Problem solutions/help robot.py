t=int(input())
for _ in range(t):
    s1,s2=input().split()
    flag=0
    for i in set(s1):
        if(i in s2):
            if not(s1.count(i)<=s2.count(i)):
                flag=1
                break
        else:
            flag=1
            break
    if(flag):
        print("No")
    else:
        print("Yes")
