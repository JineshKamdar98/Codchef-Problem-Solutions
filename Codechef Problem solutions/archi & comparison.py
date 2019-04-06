t=int(input())
while(t!=0):
    a,b,n=input().split()
    a,b,n=[int(a),int(b),int(n)]
    if n%2==0:
        if abs(a)>abs(b):
            print("1")
        elif abs(a)<abs(b):
            print("2")
        else:
            print("0")
    else:
        if a>b:
            print("1")
        elif b>a:
            print("2")
        else:
            print("0")
    t=t-1


