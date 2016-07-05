T = int(raw_input())

for t in range(T):
    s = "{0:b}".format( int(raw_input()) )
    
    LS = len(s)
    r=""
    for i in range(32-LS):
        r+="0"
        
    r+=s
    r = list(r)
    
    N = [1]
    for b in r:
        if int(b)==1:
            N.append(0)
        else:
            N.append(1)

    s = ""
    for n in range(1,33):
        s+=str(N[n])
        
    
    print int(s,2)
