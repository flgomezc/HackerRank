N, K = map(int, raw_input().split())
A = map(int, raw_input().split())

Loc = []

aux1=[]
for j in range(N):
    aux1.append([ A[j], j ])

def getKey(item):
    return item[0]

aux = sorted(aux1, key=getKey)

for j in range(len(A)):
    Loc.append(aux[j][1])

aux =[]
aux1=[]
#print "A= ", A, "\nLoc =", Loc, "\n "
#print " i=",i,", k=", k, ", A=", A, ", Loc=", Loc

i = 0
k = 0
while k < K:
    if i==(N-1):
        break
    else:
        if ( (A[i]) != (N-i) ):
            #print A[i], "should be ", A[Loc[N-i-1]]

            #print "\t", A[i], "is in the", Loc[A[i]-1], "th place."
            #print "\t", A[Loc[N-i-1]], "is in the", Loc[N-i-1], "th place."

            #print "Change places!"
            a = int(Loc[N-i-1])
            b = int(Loc[A[i]-1])
            c = int(A[i])

            Loc[N-i-1]  = b
            Loc[A[i]-1] = a
            
            A[i] = N-i
            A[a] = c

            #print "\t", A, "\n", Loc
                    
            i += 1
            k += 1
        else:
            #print A[i], "is well placed"
            i+=1

for j in range(N):     print A[j],
print 
