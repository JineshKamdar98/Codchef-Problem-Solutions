for t in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        temp=[]
        st=input()
        temp=list(st)
        a=a+temp
    #print(a)
    #print(a[0])
    #print(a[m-1])
    #print(a[(n*m)-m])
    #print(a[(n*m)-1])
    if(n*m==4):
        print('NO')
    elif(a[0]=='#' or a[m-1]=='#'):
        print('YES')
    elif()
    elif('#' not in a):
        print('YES')
    else:
        print('NO')
    
