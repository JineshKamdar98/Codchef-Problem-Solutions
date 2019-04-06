n=int(input())
while(n!=0):
    a=list(map(int,input().split()[:5]))
    c=a.count(1)
    if(c==0):
        print("Beginner")
    elif(c==1):
        print("Junior Developer")
    elif(c==2):
        print("Middle Developer")
    elif(c==3):
        print("Senior Developer")
    elif(c==4):
        print("Hacker")
    elif(c==5):
        print("Jeff Dean")
    n=n-1
