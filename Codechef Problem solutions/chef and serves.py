for t in range(int(input())):
    p1,p2,k=input().split()
    p1,p2,k=[int(p1),int(p2),int(k)]
    r=(p1+p2)//k
    if(r%2==0):
        print("CHEF")
    else:
        print("COOK")
    
