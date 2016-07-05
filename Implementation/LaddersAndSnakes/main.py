N = 20 # board size, number of blocks
M = 10  # To print AdjList

Ones = [1 for i in range(N)]
Zeros= [0 for i in range(N)]

# T: number of test cases
T = int(raw_input().strip())
#print T
for t in range(T):
    # L: number of ladders
    L = int(raw_input().strip())
    Ladders = []
    for l in range(L):
        n,m = raw_input().strip().split(' ')
        n,m = int(n), int(m)
        Ladders.append([n,m])
    # S: number of snakes on the board
    S = int(raw_input().strip())
    Snakes = []
    for s in range(S):
        n,m = raw_input().strip().split(' ')
        n,m = int(n), int(m)
        Snakes.append([n,m])
    
    AdjList = []  # Adjacency List
    for i in range(N):
        aux = []
        for j in range(N):
            if ((j-i)>0) & ((j-i)<=6) :
                aux.append(1)
            else:
                aux.append(0)
        AdjList.append(aux)
    
    def PrintAdjList(x):
        print "AdjList for %s" %x
        for i in range(M):
            print AdjList[x][10*i:10*(i+1)]
        print " "

    for l in range(L):   # Include Ladders
        k = Ladders[l][0]-1
        m = Ladders[l][1]-1
        for i in range(N):
            AdjList[i][k]=0
            AdjList[k][i]=0
        for j in range(6):
            if ( k-j-1>=0 ):
                AdjList[k-j-1][m]=1
            if ( m+j<N  ):
                AdjList[k][m+j]=1
                
    for s in range(S):   # Include Snakes
        k = Snakes[s][0]-1
        m = Snakes[s][1]-1
        for i in range(N):
            AdjList[i][k] = 0
            AdjList[k][i] = 0
        for j in range(6):
            if ( k-j>=0):
                AdjList[k-j][m]=1
            if ( m+j < N ):
                AdjList[k][m+j]=1

#    for i in range(N): print AdjList[i], i+1
        
    Rem = []

    # Assign a level to each node
   
    Level     = [0 for i in range(N)]
    Visited   = [False for i in range(N)]
    Flag      = [False for i in range(N)]
    Visited[0]= True # Origin, start
    for i in range(len(Rem)):
        Flag[Rem[i]]=True
    
    Lvl = []
    
    def PrintLevel():
        for i in range(M):
            print i, Level[10*i:10*(i+1)]
        print "\n"
        return
    
    #Find the level 1 nodes
    aux = []
    Lvl_aux = max(Level)
    for j in range(N):
        aux.append(abs(AdjList[0][j]+1-Ones[j]))
        print AdjList[j], j

    for j in range(N):
        if aux[j]==1:
            if Visited[j]==False:
                Level[j]+= Lvl_aux+1
                Visited[j]=True
    
    # find the level 2-N nodes
    for l in range(1,N):
        Level1 = []
        for i in range(N):
            if Level[i]==l:
                Level1.append(i)
            
        Lvl_aux = max(Level)
        aux1 = list(Zeros)
        for j in range(N):
            for k in Level1:
                aux1[j] += AdjList[k][j]
            for i in range(N):
                aux1[i] = bool(aux1[i])&(Visited[i]==False)
                if aux1[i]:
                    Level[i]=Lvl_aux+1
                    Visited[i]=True
        if Visited[N-1]==True:
            break
    for i in range(N):
        if Flag[i]==True:
            Level[i]=-1
        
    print "\nLevel" , Level,"\n",[ int(Visited[i]) for i in range(N)]
    #print "\n"
    if Visited[N-1]==False:
        Level[-1]=-1

    print Level[-1]
