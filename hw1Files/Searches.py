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
        # print(problem.initialState)
        # print(state.toTuple(problem.goalState))
        # print(state.toTuple(problem.initialState))
        

        # node1 = problem.initialState()
        # node.cost=0
        # frontier = Queue()
        # frontier.put(node)
        # explored = []

        # while frontier.not_empty:
        #     if frontier.empty: 
        #         return solution == []
        #     node = frontier.get()
        #     explored.append(node.state)
        #     for move in problem.applicable(node.state):
        #         child = childNode(node,move,problem)
        #         if not explored.__contains__(child):
        #             if problem.goalTest(child.state):
        #                 return solution(child)
        #             frontier.put(child)
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
            print(newNode.state)
            print('state')
            print(newNode.cost)
            # currNode = qList.get()#node
            # cNode = newList.pop(0)
            #add currNode to visited
            # visited.append(currNode)
            visited.append(newNode.state)
            for move in problem.applicable(newNode.state):
                # node.parent = newNode
                # node.action = move
                # node.cost = 0
                # node.state = newNode
                # node.nodeID = node.nodeCount
                print('about to perform child node')
                child = childNode(newNode,move,problem)
               
                # print(child)
                # print(currNode)
                # print('parent')
                print('newList')
                print(child.state)
                y=0
                if not visited.__contains__(child.state):
                    # add to qList
                    if problem.goalTest(child.state):
                        print('parent')
                        return solution(child)        
                    fList.put(child)
                    # newList.append(child.state)
                    # pass
               
            

        # if currNode == problem.goalState:
        #     return solution(currNode) 
        #     # return current node as the answer.
        # #add node to visited list 
        # if not visited.__contains__(currNode):
        #     visited.append(currNode)
        #     print('appending node to visited')
        #     print(visited[0])
            


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
    # visited.append(p.goalState)
    # print(visited[0])
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
    # print(res)
    # print("res")
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
