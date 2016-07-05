N = int(raw_input())

for n in range(N):
    S = raw_input()
    L = len(S)

    T = ""
    for i in range(L):
        T += S[L-i-1]
    
    Flag = True

    for i in range(L-1):
        a = abs(ord(S[i]) - ord(S[i+1]))
        b = abs(ord(T[i]) - ord(T[i+1]))
        if a!=b:
            Flag = False

    if Flag:
        print "Funny"
    else:
        print "Not Funny"
