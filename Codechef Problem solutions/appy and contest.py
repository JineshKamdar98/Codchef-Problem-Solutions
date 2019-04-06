def count(x,y,k):
    if(x%k==0):
        return (y/k)-(x/k)+1
    else:
        return (y/k)-(x/k)

def gcd(a,b):
    if(a==0 or b==0):
        return 0
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
    
def lcm(a,b):
    return (a*b)/gcd(a,b)
    

for t in range(int(input())):
    n,a,b,k=input().split()
    n,a,b,k=[int(n),int(a),int(b),int(k)]
    l=lcm(a,b)
    appy=count(1,n,a)
    chef=count(1,n,b)
    both=count(1,n,c)
    if((appy+chef-(2*both))>=k):
        print("Win")
    else:
        print("Lose")
            
