''' 
Nils Napp
Sliding Probelm for AI-Class
'''
#!/usr/bin/python
from slideproblem import * 

from slideproblem import child_node
from slideproblem import solution
from slideproblem import State
import time
from queue import PriorityQueue
import heapq
# pq = PriorityQueue()
## you likely need to inport some more modules to do the serach

class Searches:
    
    def tree_bfs(self, problem):
        #reset the node counter for profiling
        Node.nodeCount=0
        n=Node(None,None,0,problem.initialState)
        print(n)
        frontier=[n]
        while len(frontier) > 0:
            n = frontier.pop(0)
            for a in p.applicable(n.state):
                nc=child_node(n,a,p)
                if nc.state == p.goalState:
                    return solution(nc)
                else:
                    frontier.append(nc)
            
    def graph_bfs(self, problem):
        Node.nodeCount=0
        n=Node(None,None,0,problem.initialState)
        print(n)
        frontier=[n]

        explored=set()
        
        while len(frontier) > 0:
            n = frontier.pop(0)
            for a in p.applicable(n.state):
                nc=child_node(n,a,p)
                if nc.state == p.goalState:
                    return solution(nc)
                else:
                    childState=nc.state.toTuple()
                    if not(childState in explored):
                        frontier.append(nc)
                        explored.add(childState)    
        
    
    def recursiveDL_DFS(self, lim,problem):
        n=Node(None,None,0,problem.initialState)
        return self.depthLimitedDFS(n,lim,problem)
    
    def depthLimitedDFS(self, n, lim, problem):
    
        #reasons to cut off brnaches    
        if n.state == problem.goalState:
            return solution(n)
        elif lim == 0:
            return None
        
        cutoff=False    
        for a in p.applicable(n.state):
            nc=child_node(n,a,problem)
            result = self.depthLimitedDFS(nc,lim-1,problem)
    
            if not result==None:
                return result
    
        return None        
    
    def id_dfs(self,problem):
    
        Node.nodeCount=0
        
        maxLim=32
        for d in range(1,maxLim):
            result = self.recursiveDL_DFS(d,problem)
            if not result == None:
                return result
        print('Hit max limit of ' + str(maxLim))
        return None
        
        
    def h_1(self,s0: State,sf: State ) -> numbers.Real:
        # return the number of misplaced tiles.
        count = 0    
        s0Tuple = s0.toTuple()
        sfTuple = sf.toTuple()
        for x in range(0,2):
            for y in range(0,2):
                # print(s0Tuple[x][y])
                if(sfTuple[x][y] != s0Tuple[x][y]):
                    # print(sfTuple[x][y],s0Tuple[x][y])
                   
                    count = count+1
                # print("val  %s compared to val  %s total not equal %d" % (sfTuple[x][y],s0Tuple[x][y], count))
        if count == 0: 
            return count 
        return count-1
        
    def h_2(self,s0: State,sf: State ) -> numbers.Real:
        #manny distance 
        #count number of tiles away from goal position for each tile.
        dist = 0 
        s0Tuple = s0.toTuple()
        sfTuple = sf.toTuple()

        #check if in correct x axis 
        # check if in correct y axis
        for x in range(0,3):
            for y in range(0,3):
                sP= s0Tuple[x][y]
                fP= sfTuple[x][y]
                # print(s0Tuple[x][y])
                if(fP != sP):
                    # if sP == 0: 
                    #     dist = dist +x + y
                    if sP == 1:
                        dist = dist +abs(x-0)+abs(y-1)
                    elif(sP == 2):
                        dist =dist + abs(x-0)+abs(y-2)
                    elif(sP == 3):
                        dist =dist + abs(x-1)+abs(y-0)
                    elif(sP == 4):
                        dist = dist +abs(x-1)+abs(y-1)
                    elif(sP == 5):
                        dist = dist +abs(x-1)+abs(y-2)
                    elif(sP == 6):
                        dist =dist + abs(x-2)+abs(y-0)
                    elif(sP == 7):
                        dist =dist + abs(x-2)+abs(y-1)
                    elif(sP == 8):
                        # print(sP)
                        # print(8)
                        dist =dist + abs(x-2)+abs(y-2)
        return dist
        
    def a_star_tree(self,problem : Problem) -> tuple:
        pq = PriorityQueue()
        Node.nodeCount=0
        n=Node(None,None,0,problem.initialState)
        # frontier=[]
        missedTiles = self.h_1(n.state,problem.goalState)
        n.f = missedTiles + n.cost
        pq.put((n.f, n))
        while pq.qsize != 0:
            newN= pq.queue[0][1]
            # frontier.append(newN)
            pq.get()      
            for a in problem.applicable(newN.state):
                nc=child_node(newN,a,problem)
                if nc.state == problem.goalState:
                    print(nc)
                    return solution(nc)
                else:
                    # frontier.append(nc)
                    nc.f = nc.cost + self.h_1(nc.state, problem.goalState)
                    pq.put((nc.f,nc))
            # time.sleep(1)
            # p
            # print("missed tiles %d" %(pq.get().f))
        return "Totally fake return value"
        
    def a_star_graph(self,problem : Problem) -> tuple:
        Node.nodeCount=0
        n=Node(None,None,0,problem.initialState)
        n.f =  n.cost + self.h_2(n.state, problem.goalState)
        print(n)
        frontier=[(n.f, n)]
        heapq.heapify(frontier)
        explored=set()
        
        while len(frontier) > 0:
            # n = frontier.pop(0)
            print("im here")
            print(frontier[0])
            n = heapq.heappop(frontier)[1] #pq wasnt working trying this think i figured out why pq wasnt working but ill stick with this . 
            print(n)
            print( "im herer")
            # newN = n[1].state
            # print(newN)
            for a in problem.applicable(n.state):
                nc=child_node(n,a,problem)
                nc.f = nc.cost + self.h_2(nc.state, problem.goalState)
                if nc.state == problem.goalState:
                    return solution(nc)
                else:
                    childState=nc.state.toTuple()
                    print(childState)
                    print("childstate")
                    if not(childState in explored):
                        frontier.append((n.f,nc))
                        # heapq.heappush(frontier, nc)
                        explored.add(childState) 
                
                           
        return "Not really the right format for Solution"


import time

p=Problem()
s=State()
n=Node(None,None, 0, s)
n2=Node(n,None, 0, s)

searches = Searches()

p.goalState=State(s)

p.apply('R',s)
p.apply('R',s)
p.apply('D',s)
p.apply('D',s)
p.apply('L',s)

p.initialState=State(s)

print(p.initialState)

si=State(s)
# change the number of random moves appropriately
# If you are curious see if you get a solution >30 moves. The 
apply_rnd_moves(15,si,p)
p.initialState=si

startTime=time.clock()


print('=== Bfs*  ===')
startTime=time.clock()
res=searches.graph_bfs(p)
print(res)
print(time.clock()-startTime)
print(Node.nodeCount)

print('=== id DFS*  ===')
startTime=time.clock()
res=searches.id_dfs(p)
print(res)
print(time.clock()-startTime)
print(Node.nodeCount)

print('\n\n=== A*-Tree ===\n')
startTime=time.clock()
res=searches.a_star_tree(p)
print(time.clock()-startTime)
print(Node.nodeCount)
print(res)

print('\n\n=== A*-Graph ===\n')
startTime=time.clock()
res=searches.a_star_graph(p)
print(time.clock()-startTime)
print(Node.nodeCount)
print(res)

# p.goalState = State()

# si=State()
# apply_rnd_moves(50,si,p)
# p.initialState=si