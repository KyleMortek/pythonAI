import numpy as np

'''
If you want to implement additional drawing functions please do not 
submit them. The autograder will get upset if you are tyring to inlclude
matplotlib. 

The grader will replace drawprob funcitons with empty ones for grading
'''
#used to visualize robot and maze probability distributions
from drawprob import pList,pShow,robotShow

class maze:
    def __init__(self,world):
        self.world=world
        self.worldShape=world.shape
        self.stateSize=self.worldShape[0]*self.worldShape[1]
        self.flatWrold=world.reshape((self.stateSize))

    def isWall(self,s):
        return not self.flatWrold[s]==0
        
    #Functions for going between the two representations 
    def state2coord(self,s):
    	# transfer state to grid world coordinate (x,y)
    	row=int(s/self.worldShape[1])
    	col=np.mod(s,self.worldShape[1])
    	return row,col

    def coord2state(self,c):
    	# transfer grid world coordinate (x,y) to state 
    	return c[0]*self.worldShape[1] + c[1]

    def numNbrs(self,s):
        nbrs=0
        r,c=self.state2coord(s)
        if r>0 and self.world[r-1,c]==0:
            nbrs+=1
        if r< self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs+=1
        if c>0 and self.world[r,c-1]==0:
            nbrs+=1
        if c< self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs+=1
        return nbrs

    def nbrList(self,s):
    # returns neighbors index of a given state (0-79)
        nbrs=[]
        r,c=self.state2coord(s)
        if r > 0 and self.world[r-1,c]==0:
            nbrs.append(self.coord2state((r-1,c)))
        if r < self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs.append(self.coord2state((r+1,c)))
        if c > 0 and self.world[r,c-1]==0:
            nbrs.append(self.coord2state((r,c-1)))
        if c < self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs.append(self.coord2state((r,c+1)))
        return nbrs

    def actionList(self,s):
        nbrs=[]
        r,c=self.state2coord(s)
        if r > 0 and self.world[r-1,c]==0:
            nbrs.append('up')
        if r < self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs.append('down')
        if c > 0 and self.world[r,c-1]==0:
            nbrs.append('left')
        if c < self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs.append('right')
        return nbrs

    def observation(self,s):
        #returns: [up, left, down, right]
        wlist=np.zeros(4)
        r,c=self.state2coord(s)
        #up
        if r==0 or self.world[r-1,c]>0:
            wlist[0]=1
        #down
        if r==(self.worldShape[0]-1) or self.world[r+1,c]>0:
            wlist[2]=1
        #left
        if c==0 or self.world[r,c-1]>0:
            wlist[1]=1
        #right
        if c==(self.worldShape[1]-1) or self.world[r,c+1]>0:
            wlist[3]=1
        return wlist
        
        

        
        
''' 
robot class that contains 
 
 * maze model  
 * a random action model 
 * estiamte over the possible robot locatins in the maze

 You will implement Bayes filter for localizaiton in this class
 You can think of it as trying to figure our the robot location from
 a stream of sensor measuremtns of the form [0,1,1,] where the order is
 [up,left,down,right] and zero indicates free space and 1 indicates 
 a maze edge or a wall
'''    

class robot:
    def __init__(self,maze):
        self.maze=maze

        self.A=self.ARandomWalk()           #<--- Transition Matrix

        self.prob=np.zeros(maze.stateSize)  #<--- estimate of robot position        
        self.prob[0]=1                      #Assume you start out at location 0
    
        self.obsError=0.2
        
        '''------- Put your answeres here ---- '''
        self.loc1=None
        self.loc2=None
        self.errors1=None
        self.errors2=None
        '''----------------------------------- '''
        
    #matrix power
    def mpower(self,A,n):
        res=np.identity(A.shape[0])
        for i in range(n):
            res=np.dot(res,A)
        return res

    def randomize(self):
        #get initial condition after long wandering
        Asteady=self.mpower(self.A,1000)
        psteady=Asteady[:,1]
        self.prob=psteady
            
        
    def obsLiklihood(self,o):
        likelihood = None #Should be vector of appropriate length
        return likelihood

        
    def ARandomWalk(self):
        A=np.zeros((80,80)) #shold be matrix not zeros!
        return A
            
    def step(self):
        #this is how A should work
        pn=np.dot(self.A,self.prob)
        self.prob=pn

    def bayesFilter(self,obs):
        #update prob
        pass
        

# =======================================================================================

if __name__=="__main__":
	    
    # ------- Weather ------    
    
    
    weather=weatherModel()
    weather.computeTransitionMatirx(days)

    weather.prob=np.zeros(3)
    weather.prob[weather.type2idx['sun']]=1

    weather.predict()
    weather.prob #<--- you should report this value

    
    # ------- Robot Maze ------    
    
    myMaze=maze(np.array([
				[0,0,0,0,0,0,0,0,0,0],
				[0,1,0,0,0,0,0,0,1,0],
				[0,1,0,1,1,0,1,0,1,0],
				[0,1,0,1,0,0,1,0,1,0],
				[0,1,1,1,0,1,1,0,1,0],
				[0,0,0,0,0,1,0,0,0,0],
				[0,0,1,0,1,1,0,0,1,0],
				[0,0,0,0,0,0,0,0,1,0]]))
    
    # =============================
    # usage of showState(p):
    p=np.zeros(myMaze.stateSize)
    p[0] = 0.2
    p[2] = 0.3
    p[8] = 0.5

    pShow(p,myMaze) #Note that pShow scales the probability so that the 
                    #Maximum values is 1 this makes it helpful to visuzliaze
                    #probabilities that are thinly spread out
    # =============================
    
    rob=robot(myMaze)
    rob.prob=p 
    
    robotShow(rob)
    rob.step()
    rob.step()
    rob.step()
    robotShow(rob)    

    ''' Set rob.prob to the steady state'''     
    rob.randomize()
       
     
    #two input sequences both contain occasional sensor errors
    #in one of them the robot got kidnamped! The vile criminals 
    #left the poor confused robot in a different location. 
    
    #Can you tell by the behavior of bayes filter which sequence of 
    #observations comes from the kindmaped robot?
    
    obsA=[[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,1,0,1],[0,0,1,1],
          [1,1,0,0],[1,1,0,1],[0,0,1,1],[1,0,0,0],[0,0,0,1],
          [1,0,1,0],[0,0,0,0],[0,1,0,1],[0,0,0,1],[0,1,0,1],
          [0,0,0,1],[1,0,0,0]]
 
    
    obsB=[[0,0,0,1],[1,0,1,0],[0,0,0,0],[0,1,0,1],[0,1,0,1],
         [0,1,0,1],[0,0,0,1],[1,0,0,0],[1,0,1,0],[1,0,0,0],
         [0,0,0,0],[0,1,0,1],[0,0,1,1],[1,1,0,0],[0,1,0,1],
         [0,0,1,1],[1,0,0,0]]
              
         
    #try this for both input sequences     
    #you can run this to test bayes filter
    for o in obsA:
            rob.bayesFilter(o)
            robotShow(rob)
  
  