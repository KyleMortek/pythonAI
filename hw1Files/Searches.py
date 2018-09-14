# -*- coding: utf-8 -*-
"""

"""
from SlideProblem import *
# qList = queue.Queue(maxSize= 9)
from queue import *
qList = Queue()
newList = []
# qList.put(1)
# qList.put(12)
# qList.put(100)
#visited nodes list 
# visited = []
# visited.append()
# visited.append()
# visited.append()

# print(qList.get())
# print(qList.get())
class Searches:    
    
    def graphBFS(self,problem):
        print(node.nodeCount)
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        print("I am an empty shell of a function.")        

        #what i need
        # list of visited nodes: if not visited, add to queue, add to visited list 
        # queue of children nodes to explore 
        fNode = problem.initialState
        nodeAtt = node(None,None,0,fNode)
        # qList.put(problem.initialState) #initialze fronti
        fList = Queue()
        # fList.append(problem.initialState)
        # fList.put(fNode)
        fList.put(nodeAtt)
        # qList.put(node)
        # newList.append(problem.initialState)
        visited = [] #explored set to empty.
        # if qList.empty():
        #     return solution == {}
        #get node from qlist and remove from qList 
        #while qlist is not empty explore currNodes children
        while fList.not_empty:
          
            #qList.not_empty:
            # newNode = fList.__getitem__(0)
            newNode = fList.get()

            visited.append(newNode.state)
            for move in problem.applicable(newNode.state):
                # node.parent = newNode
                # node.action = move
                # node.cost = 0
                # node.state = newNode
                # node.nodeID = node.nodeCount
                # print('about to perform child node')
                child = childNode(newNode,move,problem)
               

                y=0
                if not visited.__contains__(child.state):
                    # add to qList
                    if problem.goalTest(child.state):
                        # print('parent')
                        return solution(child)        
                    fList.put(child)
                    # newList.append(child.state)
                    # pass
               

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

    
    ''' 
    The sultion, should basically be the reverse order
    of backward moves above: RUULL
    '''
    
    print('=== Bfs  ===')
    startTime=time.clock()
    node.nodeCount=0
    
    res=search.graphBFS(p)

    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
 
    print('=== ID-Depth Limited Search ===')
    startTime=time.clock()
    node.nodeCount=0
    
    res=search.idDFS(p)
    print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))

    # print("this is what i get")
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
