import numpy as np
from markov import *
from drawprob import pList,pShow,robotShow


class MDPSillyGame:
    def __init__(self):
        self.domsize = 160
        self.reward = self._mkreward()

        self.eps = 0.05 #<--- CHANGE ME

        self.A = self.transitionMatrix(self.eps)
        self.value = self._mkreward()
        
        
        ''' 
        Change this answer 
        You shoul play if you have equal or more than this amount
        '''
        self.cutoff= 81 # <--- your anwer here
        
        
    def _mkreward(self):
        reward = np.arange(self.domsize)
        for i in range(100,self.domsize):
            reward[i]=reward[i] + 50
        return reward

    def transitionMatrix(self,eps):
        print(eps, 'this is eps')
        '''put code here to compute the transition matrix '''
        A = np.zeros([self.domsize,self.domsize]) # so the transition matrix is 160x160 
        A[0][0]=1
        A[159][159]=.5# 50 chance of breaking even  
        A[158][159]=.5#50 chance of losing 

        for x in range(160):
            if x == 0:
                A[0][0]=1 ###this is given
            elif x == 159:
                A[159][159]=.5# 50 chance of breaking even  ### this is given 
                A[158][159]=.5# 50 chance of  
            else:
                A[x][x] = self.eps
                A[x-1][x] = .5
                A[x+1][x] = .5 -self.eps
            pass

        # print(A, "this is A")
        # print(self.domsize)
        return A

    def valIter(self):
        
        '''
        These are the two options 
        When you stop, you can cash out the reward
        when you plan, the you can win or lose 
        '''

        vstop = self.reward
        vplay = np.zeros(self.domsize)
        # print(vplay, 'this is vplay')
        # print(self.value, "this is self.value")
        for i in range(self.domsize):
            vplay[i] = np.dot(self.A[:,i],self.value)  #<--Note how this is computed
        
        self.value=np.amax(np.array([vstop,vplay]),axis=0)
        return vplay,self.value


        
#Actions of Maze problem        
actions=['up','left','down','right','stop']
        
class MDPMaze:
    def __init__(self,maze,stateReward):

        self.maze = maze
        self.stateReward = stateReward
        self.stateSize = maze.stateSize
        self.stateReward.resize(self.stateSize)
               
        self.eps = 0.30
        self.gamma = 0.9
        self.rewardM = np.ones(self.stateSize)*(-1)

        
        #place holders for computing transition matrices
        self.Aup=None
        self.Aleft=None
        self.Adown= None
        self.Aright=None
        self.Astop =None

        # computeTransitionMatrices function should compute self.Aup, self.Aleft, self.Adown, self.Aright and self.Astop
        # update the 5 matrices inside computeTransitionMatrices()
        self.computeTransitionMatrices() 

        
        self.value=np.zeros(self.stateSize)
        self.policy=None 
        
        
    # You can use this to construct the noisy matrices    
    def ARandomWalk(self):
        A=np.zeros((self.stateSize,self.stateSize))
    
        for col in range(self.stateSize):
            nbrs=self.maze.nbrList(col)
            p=1/(len(nbrs)+1)       
            A[col,col]=p
            for r in nbrs:
                A[r,col]=p  
        return A

    def computeTransitionMatrices(self):
        '''put code here to initialize the matrices '''

        A  = self.ARandomWalk()
        # initialize here. 
        self.Aup= np.zeros((self.stateSize,self.stateSize))
        self.Aleft= np.zeros((self.stateSize,self.stateSize))
        self.Adown= np.zeros((self.stateSize,self.stateSize))
        self.Aright= np.zeros((self.stateSize,self.stateSize))
        self.Astop = np.zeros((self.stateSize,self.stateSize))

        for j in range(self.stateSize): # this code is only for Aup
            aList = self.maze.actionList(j)
            nList = self.maze.nbrList(j)
            self.Astop[j][j]=1
            if 'U' in aList: #
                #set U postion to 1
                # (r,c) = self.maze.state2coord(nList[0])
                column = j 

                row = nList[aList.index('U')]
                self.Aup[row][j]=1
            else:#cant move up? set 1 to current position. 
                self.Aup[j][j]=1
            if 'D' in aList: #
                #set U postion to 1
                # (r,c) = self.maze.state2coord(nList[0])
                column = j 

                row = nList[aList.index('D')]
                self.Adown[row][j]=1
            else:#cant move up? set 1 to current position. 
                self.Adown[j][j]=1
            if 'L' in aList: #
                #set U postion to 1
                # (r,c) = self.maze.state2coord(nList[0])
                column = j 

                row = nList[aList.index('L')]
                self.Aleft[row][j]=1
            else:#cant move up? set 1 to current position. 
                self.Aleft[j][j]=1
            if 'R' in aList: #
                #set U postion to 1
                # (r,c) = self.maze.state2coord(nList[0])
                column = j 

                row = nList[aList.index('R')]
                self.Aright[row][j]=1
            else:#cant move up? set 1 to current position. 
                self.Aright[j][j]=1

        self.Aup = (1-self.eps)*self.Aup+self.eps*self.ARandomWalk()
        self.Adown = (1-self.eps)*self.Adown+self.eps*self.ARandomWalk()
        self.Aleft = (1-self.eps)*self.Aleft+self.eps*self.ARandomWalk()
        self.Aright =(1-self.eps)*self.Aright+self.eps*self.ARandomWalk()       
        
    def valIter(self):
        ''' This should update self.value'''
        #   vstop = self.reward
        # vplay = np.zeros(self.domsize)
        # # print(vplay, 'this is vplay')
        # # print(self.value, "this is self.value")
        # for i in range(self.domsize):
        #     vplay[i] = np.dot(self.A[:,i],self.value)  #<--Note how this is computed
        
        # self.value=np.amax(np.array([vstop,vplay]),axis=0)
        # return vplay,self.value
        #just like above make sure you initialize the vupand suh
        Vx = self.stateReward
        vup= np.zeros(self.stateSize)
        vdown= np.zeros(self.stateSize)
        vleft= np.zeros(self.stateSize)
        vright= np.zeros(self.stateSize)
        vstop= np.zeros(self.stateSize)
        for s in range(self.stateSize):
            vup[s] = self.stateReward[s]+ self.gamma*np.dot(self.Aup[:,s],self.value)-1
            vdown[s] = self.stateReward[s]+ self.gamma*np.dot(self.Adown[:,s],self.value)-1
            vleft[s] = self.stateReward[s]+ self.gamma*np.dot(self.Aleft[:,s],self.value)-1
            vright[s] = self.stateReward[s]+ self.gamma*np.dot(self.Aright[:,s],self.value)-1
            vstop[s] =  self.stateReward[s]+self.gamma*np.dot(self.Astop[:,s],self.value)
        self.value=np.amax(np.array([vstop,vup, vdown,vright,vleft]),axis=0)#np.argmax(self.stateReward())
        #     np.dot
        # # print(self.value, "value")
        # print(self.stateReward, "reward")
        pass

        
    def computePolity(self):
        '''write some code here'''
        self.policy=['']*80 #This shoule be a list so 
                         #that each location corresponds to a state and
                         #holds one of the 5 ossible actions
        vup= np.zeros(self.stateSize)
        vdown= np.zeros(self.stateSize)
        vleft= np.zeros(self.stateSize)
        vright= np.zeros(self.stateSize)
        vstop= np.zeros(self.stateSize)
        for s in range(self.stateSize):
            vup[s] = self.stateReward[s]+ self.gamma*np.dot(self.Aup[:,s],self.value)-1
            vdown[s] = self.stateReward[s]+ self.gamma*np.dot(self.Adown[:,s],self.value)-1
            vleft[s] = self.stateReward[s]+ self.gamma*np.dot(self.Aleft[:,s],self.value)-1
            vright[s] = self.stateReward[s]+ self.gamma*np.dot(self.Aright[:,s],self.value)-1
            vstop[s] =  self.stateReward[s]+self.gamma*np.dot(self.Astop[:,s],self.value)
        self.policy=np.argmax(np.array([vstop,vup, vdown,vright,vleft]),axis=0)#np.argmax
        print(self.policy, "hehehehehehe")
        # self.policy = self.valIter()
        # prin
             
        
if __name__=="__main__":

    
    ''' silly game '''    
    N = 1 # <-change me to get convergence
    
    gambling = MDPSillyGame()
    for i in range(N):
        vplay,vn = gambling.valIter()    
    print('V_stop\tV_play\tmax_u V_n')
    for i in range(60,110):
        print(gambling.reward[i],'\t', vplay[i],'\t', vn[i])

    
    ''' MAZE MDP '''
    
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

    mdp = MDPMaze(myMaze,stateReward)

    iterCount=100
    printSkip=10
    
    for i  in range(iterCount):
        mdp.valIter()
        if np.mod(i,printSkip)==0:
            print("Iteration ",i) 
            pShow(mdp.value,myMaze)

    
