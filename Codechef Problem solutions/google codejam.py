def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

for t in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    la=get_all_substrings(a)
    lb=get_all_substrings(b)
    lb=list(set(lb))
    #j=len(lb)
    j=0
    c=0
    #la.sort()
    #lb.sort()
    #print(la)
    #print(lb)
    for i in range(2*n):
        while(j<len(lb)):
            #print(i,j)
            if(sorted(la[i])==sorted(lb[j])):
                #print(lb[j])
                #print(la[i])
                c+=1
                break
            j+=1
    print("Case #"+str(t+1)+": "+str(c))
