from math import floor

N = int(raw_input())
A = map(int, raw_input().split())
p,q = map(int, raw_input().split())

A.sort()

#print N, A, p,q

a = 0
b = 0
mina = -1.*float('inf')
minA = 0
minq = float('inf')
minp = float('inf')
minlist =[]
minQ = []
minP = []

for i in range(N-1):
    aux1 = abs(A[i]-A[i+1])/2.
    aux = floor(aux1)
    aux0 = int(A[i]+aux)
    if (p<=aux0) &( aux0<= q):
        if aux > mina:
            minlist = []
            mina = aux
            minA = aux
        if aux == mina:
            minlist.append([A[i],A[i+1]])
            
if len(minlist) == 0:
    minlist.append([float('nan')])

for a in A:
    aux2 = abs(a-p)
    if aux2 == 0:
        aux2 = float('nan')
        minP = float('nan')
        minp = float('nan')
        break
    else: 
        if aux2 < minp :
            minp = aux2
            minP = a

for a in A:
    aux3 = abs(a-q)
    if aux3 == 0:
        aux3 = float('nan')
        minQ = float('nan')
        minq = float('nan')
        break
    else:
        if aux3 < minq :
            minq = aux3
            minQ = a
    

#print A, "\n", minlist, minA, minlist[0][0]+minA,"\n minp, p, minP", minp, p, minP, "\n minq, q, minQ", minq, q, minQ, "\nMins", minA,minp,minq


x = max(minA, minp, minq)


M = []

if (minA == x):
    M.append( minlist[0][0] + int( minA) )
if minp == x:
    M.append( p)
if minq == x:
    M.append( q)

print min(M)
