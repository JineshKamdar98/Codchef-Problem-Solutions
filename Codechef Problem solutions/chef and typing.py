for t in range(int(input())):
    n=int(input())
    tot_time=0
    a=[]
    b=[]
    for i in range(n):
        s=input()
        if s in a:
            ind=a.index(s)
            tot_time+=(int(b[ind]))//2
            continue

        a.append(s)
        word_time=0
        char_time=0.2
        for j in range(1,len(s)):
            if((s[j]=='d'and(s[j-1]=='d' or s[j-1]=='f'))or(s[j]=='f'and(s[j-1]=='d' or s[j-1]=='f'))):
                char_time+=0.4
            elif((s[j]=='j'and(s[j-1]=='j' or s[j-1]=='k'))or(s[j]=='k'and(s[j-1]=='j' or s[j-1]=='k'))):
                char_time+=0.4
            else:
                char_time+=0.2
        word_time+=char_time
        b.append(word_time)
        tot_time+=word_time
    print(a)
    print(b)
    print(tot_time)
                
            
