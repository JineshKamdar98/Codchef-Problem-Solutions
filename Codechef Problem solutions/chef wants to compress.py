a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for t in range(int(input())):
    b=[]
    d,n=map(int,input().split())
    s=input()
    for i in range(d):
        b.append(a[i])
    for j in s:
        if(j in b):
            b.remove(j)
    r=''.join(str(k) for k in b)
    print(r*n)
    
