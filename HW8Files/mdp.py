import numpy as np
from markov import *
from drawprob import pList,pShow,robotShow


class MDPmaze:
    def __init__(self,maze,stateReward):

        self.maze = maze
        self.stateReward = stateReward
        self.stateSize = maze.stateSize
        self.stateReward.resize(self.stateSize)
               
        self.epsA = 0.01
        self.gamma = 0.9

        self.rewardM = np.ones(self.stateSize)*(-1)

        #Transition Matrices
        self.Arandom=self.ARandomWalk()
        self.Aup= self.Au(0)*(1-self.epsA) + self.epsA*self.Arandom
        self.Aleft= self.Al(0)*(1-self.epsA) + self.epsA*self.Arandom
        self.Adown= self.Ad(0)*(1-self.epsA) + self.epsA*self.Arandom
        self.Aright= self.Ar(0)*(1-self.epsA) + self.epsA*self.Arandom
        self.Astop = self.As()
        
        self.actions=['up','left','down','right','stop']        
        self.transDict={'up':self.Aup , 'left':self.Aleft, 'down':self.Adown, 
                        'right':self.Aright, 'stop':self.Astop}
        
        self.value=np.zeros(self.stateSize)
        self.policy=None 
        
        
    def ARandomWalk(self):
        A=np.zeros((self.stateSize,self.stateSize))
    
        for col in range(self.stateSize):
            nbrs=self.maze.nbrList(col)
            p=1/(len(nbrs)+1)       
            A[col,col]=p
            for r in nbrs:
                A[r,col]=p  
        return A
                
        
    def As(self):
        return np.identity(self.stateSize)

    def Au(self,eps):
        #eps is the probability the the motion does not succeed
        
        A=np.identity(self.stateSize) * eps
     
        for s in range(self.stateSize):
            r,c=self.maze.state2coord(s)
            if r==0 or self.maze.world[r-1,c]>0:
                A[s,s]+=1-eps
            else:
                A[self.maze.coord2state((r-1,c)),s]=1-eps
        return A

    def Al(self,eps):
        # eps is the probability that motion does not succeed

        A=np.identity(self.stateSize) * eps
     
        for s in range(self.stateSize):
            r,c=self.maze.state2coord(s)

            if c==0 or self.maze.world[r,c-1]>0:
                A[s,s]+=1-eps
            else:
                A[self.maze.coord2state((r,c-1)),s]=1-eps

        return A

    def Ad(self,eps):
        # eps is th probability that motion does not succeed

        A=np.identity(self.stateSize) * eps
     
        for s in range(self.stateSize):
            r,c=self.maze.state2coord(s)

            if r==self.maze.worldShape[0]-1 or self.maze.world[r+1,c]>0:
                A[s,s]+=1-eps
            else:
                A[self.maze.coord2state((r+1,c)),s]=1-eps

        return A

    def Ar(self,eps):
        # eps is th probability that motion does not succeed
        A=np.identity(self.stateSize) * eps
     
        for s in range(self.stateSize):
            r,c=self.maze.state2coord(s)

            if c==(self.maze.worldShape[1]-1) or self.maze.world[r,c+1]>0:
                A[s,s]+=1-eps
            else:
                A[self.maze.coord2state((r,c+1)),s]=1-eps
        return A


    def valIter(self):

        vu=np.zeros(self.stateSize)
        vr=np.zeros(self.stateSize)
        vd=np.zeros(self.stateSize)
        vl=np.zeros(self.stateSize)
        vs=np.zeros(self.stateSize)

        for s in range(self.stateSize):
            vu[s]=self.stateReward[s] + self.rewardM[s] + self.gamma*np.dot(self.Aup[:,s],self.value)
            vl[s]=self.stateReward[s] + self.rewardM[s] + self.gamma*np.dot(self.Aleft[:,s],self.value)
            vd[s]=self.stateReward[s] + self.rewardM[s] + self.gamma*np.dot(self.Adown[:,s],self.value)
            vr[s]=self.stateReward[s] + self.rewardM[s] + self.gamma*np.dot(self.Aright[:,s],self.value)
            vs[s]=self.stateReward[s] + self.gamma*self.value[s]
        
        self.value=np.max([vs,vu,vl,vd,vr],axis=0)
        return self.value
        
    def computePolicy(self):

        self.policy=[]
        minv=min(self.value)-100
        
        for s in range(self.stateSize):
            vnext=minv
            anext=''
            for a in self.actions:
                vtry=self.stateReward[s]+self.rewardM[s] + self.gamma*np.dot(self.transDict[a][:,s],self.value)
                
                if a == 'stop':
                    vtry=vtry +1
                    
                if vtry > vnext:
                    vnext=vtry
                    anext=a
                    
            self.policy.append(anext)
        return self.policy

    def showPolicy(self):
        row,col=self.maze.worldShape
        cellstr='{!s: ^7}'
        
        policylist=self.policy.copy()
        policylist.reverse()

        for i in range(row):
            for j in range(col):
                element=policylist.pop()
                if not self.maze.world[i,j]==0:
                    element='#'
                print(cellstr.format(element),end='')          
            print('')
        
if __name__=="__main__":

    
    ''' MAZE MPD '''
    
    myMaze=maze(np.array([
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,1,0],
                [0,1,0,1,1,0,1,0,1,0],
                [0,1,0,1,0,0,1,0,1,0],
                [0,1,1,1,0,1,1,0,1,0],
                [0,1,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0,1,0]]))

    stateReward=np.array([
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,100,0,0,0,0,0],
                [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000]])

    mdp = MDPmaze(myMaze,stateReward)

    iterCount=1000

    printSkip=100
    v=np.zeros(mdp.stateSize)
    for i  in range(iterCount):
        v = mdp.valIter()
        if np.mod(i,printSkip)==0:
            print("Iteration ",i)   
    pShow(v,myMaze)
  
