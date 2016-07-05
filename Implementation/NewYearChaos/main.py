#!/bin/python

import sys


T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    
    aux = []
    for i in range(n):
        aux.append([q[i],i])
    def getKey(item):
        return item[0]
    aux1 = sorted( aux, key=getKey )
    
    Loc = []
    for a in aux1:
        Loc.append(a[1])

    Flag = False
    p = 0
    
    for i in range(n-1,0,-1):
        k = 0
        while q[i]!= i+1 : #(muat be a while)
            ll = int( Loc[i]  )      # last in subarray location
            lv = int( q[Loc[i]])
            pl = int( Loc[i]+1 )
            pv = int( q[Loc[i]+1] )
            #            print i, lv, ll, pv, pl

            q[pl] = lv
            q[ll] = pv

            Loc[pv-1] -= 1
            Loc[lv-1] += 1

            p += 1
            k += 1

            if k >= 3:
                Flag = True

    if Flag:
        print "Too chaotic"
    else:
        print p
