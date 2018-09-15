# -*- coding: utf-8 -*-
"""

"""
from SlideProblem import *
# qList = queue.Queue(maxSize= 9)
# print(qList.get())
class Searches:    
    #from slides and book. 
    def graphBFS(self,problem):
       
        nodeAtt = node(None,None,0,problem.initialState)
        fList = []
        fList.append(nodeAtt)
        visited = [] #explored set to empty.
        if problem.goalTest(problem.initialState):
            return solution(nodeAtt)
        # if(fList == []):
        #     return solution
        while True:
            if(fList == []):
                return 
            newNode = fList.pop(0)
            visited.append(state.toTuple(newNode.state))
            # print(visited)
            for move in problem.applicable(newNode.state):
                child = childNode(newNode,move,problem)
                if state.toTuple(child.state) not in visited:
                    if problem.goalTest(child.state):
                        return solution(child)        
                    fList.append(child)
    
    def rDFS(self,nodeAtt, problem, limit):#, visited):
        # print(limit)
            if limit == 0:

                if problem.goalTest(nodeAtt.state): 
                # print(nodeAtt)
                    return solution(nodeAtt) 
            else:
                if limit != 0:
                    for move in problem.applicable(nodeAtt.state):
                        child = childNode(nodeAtt, move,problem)
                        result = self.rDFS(child,problem, limit-1)#, visited)
                        # print(result)
                        if(result == None):
                            continue
                        return result
    def idDFS(self,problem):
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        limit = 0
        # print('whatt')
        nodeAtt = node(None,None,0,problem.initialState)
        while not limit < 0:
            result = self.rDFS(nodeAtt, problem, limit)# visited)
            if result == None:
                #increase depth level. 
                limit = limit +1 
                continue
            return result#result# visited)
        # print("Please Implement me!")
    
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
    # print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
