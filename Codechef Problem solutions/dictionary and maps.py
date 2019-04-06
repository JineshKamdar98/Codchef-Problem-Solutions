import sys
n=int(input())
d={}
a=[]
for i in range(n):
    name,ph=input().split()
    name,ph=[str(name),int(ph)]
    d[name]=ph
while True:
    i=sys.stdin.readline()
    if i=='':
        break
    a.append(i)
for i in a:
    if(i in d.keys()):
        print(i+'='+d[i])
    else:
        print("Not found")
