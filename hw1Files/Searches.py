# -*- coding: utf-8 -*-
"""

"""
from SlideProblem import *
# qList = queue.Queue(maxSize= 9)
from queue import *
qList = Queue()
qList.put(1)
qList.put(12)
qList.put(100)
#visited nodes list 
visited = []
# visited.append()
# visited.append()
# visited.append()
print(visited)
print(qList.get())
print(qList.get())
class Searches:    
    
    def graphBFS(self,problem):
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        print("I am an empty shell of a function.")        
        

    def idDFS(self,problem):
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        print("Please Implement me!")
        
if __name__ == '__main__':

    import time

    search=Searches()
    
    ''' Set up the search problem '''
    p=problem()
    s=state()

    p.goalState=state(s)

    p.apply('R',s)
    p.apply('R',s)
    p.apply('D',s)
    p.apply('D',s)
    p.apply('L',s)
    
    p.initialState=state(s)
    visited.append(p.goalState)
    print(visited[0])
    # print(s)
    # print('hello im here')
    # # me testing 
    # print("initial state")
    # print(p.initialState)
    # print("initial state")
    
    ''' 
    The sultion, should basically be the reverse order
    of backward moves above: RUULL
    '''
    
    print('=== Bfs  ===')
    startTime=time.clock()
    node.nodeCount=0
    
    res=search.graphBFS(p)
    print(res)
    print("res")
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
 
    print('=== ID-Depth Limited Search ===')
    startTime=time.clock()
    node.nodeCount=0
    
    res=search.idDFS(p)
    print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))

    print("this is what i get")
    # print(p.goalState)
    # print('here')
    # print(p.applicable(s)) # what moves can the initial state do. 
    # print("above is the root nodes of the initial state?") # but what are the u l and right nodes numbers??
    #p.apply(p.applicable(s)[0],s)#apply the first idx from in this instance it move 0 up one. 
    # print(s)
    # print(p.applicable(s))
    # print(p.actions)
    # print(p.initialState)
    # print(p.goalState)
