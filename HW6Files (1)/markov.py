import numpy as np
import json
import time
'''
If you want to implement additional drawing functions please do not 
submit them. The autograder will get upset if you are tyring to inlclude
matplotlib. 

The grader will replace drawprob funcitons with empty ones for grading
'''

#used to visualize robot and maze probability distributions
from drawprob import pList,pShow,robotShow,close_all

#Fake weather sequence to test the weather model
days=['rain', 'rain', 'rain', 'clouds', 'rain', 'sun', 'clouds', 'clouds', 
      'rain', 'sun', 'rain', 'rain', 'clouds', 'clouds', 'sun', 'sun', 
      'clouds', 'clouds', 'rain', 'clouds', 'sun', 'rain', 'rain', 'sun',
      'sun', 'clouds', 'clouds', 'rain', 'rain', 'sun', 'sun', 'rain', 
      'rain', 'sun', 'clouds', 'clouds', 'sun', 'sun', 'clouds', 'rain', 
      'rain', 'rain', 'rain', 'sun', 'sun', 'sun', 'sun', 'clouds', 'sun', 
      'clouds', 'clouds', 'sun', 'clouds', 'rain', 'sun', 'sun', 'sun', 
      'clouds', 'sun', 'rain', 'sun', 'sun', 'sun', 'sun', 'clouds', 
      'rain', 'clouds', 'clouds', 'sun', 'sun', 'sun', 'sun']

class weatherModel:
    
    def __init__(self):
        self.types=('sun','clouds','rain')
        
        self.counts=np.zeros((3,3))
        self.transitionMatrix=[]
        self.type2idx=dict(sun=0,clouds=1,rain=2)
 
        self.prob=np.zeros(3)
        
        #set today to cloudy
        self.prob[self.type2idx['clouds']]=1.0

        # mat[0][0] = mat[0][0] / sun 
        # mat[0][1] = mat[0][1] / clouds
        # mat[0][2] = mat[0][2] / rain
        # mat[1][0] = mat[1][0] / sun 
        # mat[1][1] = mat[1][1]/clouds
        # mat[1][2] = mat[1][2]/rain
        # mat[2][0]=mat[2][0]/sun
        # mat[2][1]= mat[2][1]/clouds
        # mat[2][2]=mat[2][2]/rain
        '''------- PUT YOUR ANSWERS HERE  ---- '''
        self.pTomorrow= [0.7191011235955056, 0.20786516853932585, 0.07303370786516854]    #Should be np.array([psun,pclouds,prain])
        self.predictionHorizon=1 #Should be integer
        '''----------------------------------- '''
        
        
    def read_weather_log(self,fname):
        with open(fname,'r') as fh:
            days=[]
            for line in fh:
                d=json.loads(line)
                #print(line)
                #print(str(d['weather'][0]['main']))
                days.append(d['weather'][0]['main'])
        print('Read %d days.'%(len(days),))
        print('Possible States: ' + str(set(days)))
        return days
    
    def convert_raw(self,raw_days):
        '''
        Convert from raw days (which include other descriptors) to sun-rain-coulds sequence
        You can also modify the "read_data" function to do this automatically.
        '''
        # Possible States: {'Clear', 'Mist', 'Rain', 'Fog', 'Haze', 'Thunderstorm', 'Snow', 'Clouds'}
        new_raw_days= []

        for w in raw_days:
            # print('rhis is WWWWWW ', w)
            if w == 'Clear': 
                new_raw_days.append('sun')
                # print(new_raw_days)
            elif w == 'Mist':
                new_raw_days.append('rain')
            elif w == 'Rain':
                new_raw_days.append('rain')
            elif w == 'Fog':
                new_raw_days.append('clouds')
            elif w == 'Haze':
                new_raw_days.append('clouds')
            elif w == 'Thunderstorm':
                new_raw_days.append('rain')
            elif w == 'Snow':
                new_raw_days.append('rain')
            elif w == 'Clouds':
                new_raw_days.append('clouds')
            # print(new_raw_days)
    
        # print(len(raw_days))
        return new_raw_days        
    def get_pairs(self, data):
        #new a list of tuples. 
        # print(data)
        # print(len(data))
        paired_days = []
        while(len(data)-1 !=0 ):
            # print(len(data))
            paired_days.append((data[0],data[1]))
            data.pop(0)
        # print(paired_days, 'HELLOOOOOO ')
        return paired_days       
    def computeTransitionMatirx(self,data):#need to write sometihng here. 
        '''put something here to comput self.transitionMatrix'''
        # print('im here computer transition matrix')
        mat = self.transitionMatrix=np.zeros((3,3))
        # paired_data = self.get_pairs(data)#gets paired data
        # print(paired_data)
        # print(sorted(data), 'sorted')
        sun  = 0 
        rain = 0 
        clouds = 0 
        while len(data)-1 != 0:
        # for (x,y) in data: 
            # i = data[0]
            x = data[0]
            y = data[1]
            #s|s (0,0) in transition matrix
            if x == 'sun':
                sun+=1.0
            if x == 'rain':
                rain+=1.0
            if x == 'clouds':
                clouds+=1.0
            if x == 'sun' and y == 'sun':
                mat[0][0]+=1.0
            #s|c
            if x == 'clouds' and y == 'sun':
                mat[0][1]+=1.0
            #s|r
            if x == 'rain' and y == 'sun':
                mat[0][2]+=1.0
                ###########################
            #c|s
            if x == 'sun' and y == 'clouds':
                mat[1][0]+=1.0
            #c|c
            if x == 'clouds' and y == 'clouds':
                mat[1][1]+=1.0
            #c|r
            if x == 'rain' and y == 'clouds':
                mat[1][2]+=1.0 
                
                ###########################
            #r|s
            if x == 'sun' and y == 'rain':
                mat[2][0]+=1.0
            #r|c
            if x == 'clouds' and y == 'rain':
                mat[2][1]+=1.0
            #r|r
            if x == 'rain' and y == 'rain':
                mat[2][2]+=1.0
            data.pop(0)
            # print(mat, "matrix")
        mat[0][0] = mat[0][0] / sun 
        mat[0][1] = mat[0][1] / clouds
        mat[0][2] = mat[0][2] / rain
        mat[1][0] = mat[1][0] / sun 
        mat[1][1] = mat[1][1]/clouds
        mat[1][2] = mat[1][2]/rain
        mat[2][0]= mat[2][0]/sun
        mat[2][1]= mat[2][1]/clouds
        mat[2][2]=mat[2][2]/rain
        self.pTomorrow = [mat[0][0],mat[1][0],mat[2][0]]

    #  print(self.pTomorrow, 'ptoimoemntewoirn')
        # upperL = self.transitionMatrix[0][0]
        # print(upperL,'upperl')
        # we need to get pairs to find the probabilietes 
        # go through new data and get the probabilites for ss sc sr.....cs cc cr......rs rc rr 
        # print(mat, "this is maat")
        # print(self.transitionMatrix)    
        self.transitionMatrix= mat
        # return mat
        return self.transitionMatrix
            
    def predict(self):
        ''' 
        Use current probabilyt to predict one day ahead
        This matrix multiplication means that the entry
        [row][col] is the transition probability from 
        state col to state row
        
        Note, that you need to use np.dot instead of np.mul 
        in order to get the correct matrix multiplication 
        '''
        
            # print(self.transitionMatrix,'i am here PREDICT')
            # print(self.prob, 'prob')

        pnext=np.dot(self.transitionMatrix,self.prob)
            # print(pnext, 'pnext')
            # pnext=np.dot(self.transitionMatrix, pnext)

            # print(pnext,'pnext')
        self.prob=pnext

        
class maze:
    def __init__(self,world):
        self.world=world
        self.worldShape=world.shape
        self.stateSize=self.worldShape[0]*self.worldShape[1]

    #Functions for going between the two representations 
    def state2coord(self,s):
    	# transfer state to grid world coordinate (x,y)
        row=int(s/self.worldShape[1])
        col=np.mod(s,self.worldShape[1])
        # print(row,col,s,'printinf ')
        # time.sleep(1)
        # print(self.worldShape[0])
        # print(self.worldShape[1])

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
            nbrs.append('U')
        if r < self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs.append('D')
        if c > 0 and self.world[r,c-1]==0:
            nbrs.append('L')
        if c < self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs.append('R')
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
        self.prob[0]=None      #Assume you start out at location 0
    
        self.obsError=0.2
        self.kidnapped = False
        
        '''------- Put your answeres here ---- '''
        self.loc1=53
        self.loc2 =53
        self.errors1=[6,8,9,10,11,12,13,16]
        self.errors2 = [10]
        '''---------------------self-------------- '''
        
    #matrix power
    def mpower(self,A,n):
        res=np.identity(A.shape[0])
        print(A.shape[0], 'shape')
        print(A, 'this is A')
        for i in range(n):
            res=np.dot(res,A)
        return res

    def randomize(self):
        #get initial condition after long wandering
        # print(self.A, "12345678908765432")
        Asteady=self.mpower(self.A,1000)
        # print(Asteady, 'asteady')
        psteady=Asteady[:,1]
        print(psteady,'pstewady')
        print(sum(psteady))
        self.prob=psteady
            
        
    def obsLiklihood(self,o):
        likelihood = np.zeros(self.maze.stateSize) #Should be vector of appropriate length
        # print(o,"this is o")
        # o=[1,1,0,0]
        o_true = o
        newList= []
        setLoc = (0.0, 0)
        nl=[]
        for i in range(80):#i is current state
            ob= self.maze.observation(i) #ids it equal to o? 
            # print(o_true,ob, 'o_true')
            # time.sleep(5)
            #compare o_true with o 
            first = 0
            second =0 
            third = 0 
            fourth = 0
            if o_true[0] == ob[0]: 
                first = .8
            else: 
                first= .2
            if o_true[1] == ob[1]: 
                second = .8
            else: 
                second= .2
            if o_true[2] == ob[2]: 
                third = .8
            else: 
                third= .2
            if o_true[3] == ob[3]: 
                fourth = .8
            else: 
                fourth= .2
                # setLoc = i
                # print(i, 'BEST LOCATION')
            p = first*second*third*fourth
            # print(p, 'this is p ')
            if p >= setLoc[0]:# manually look at BESTLOC to find beset location? 53 appears the most for loc1
                #update set loc
                setLoc = (p,i)
                nl.append(i)
                # print(i, 'BEST LOCATION')

            # print(p, 'this is p')
            # likelihood[i]=p
            newList.append(p)
        print(sum(newList))
        # print(setLoc, 'BEST LOC')
        # print(nl)
        likelihood=newList
        # print(likelihood, 'LIKELYHOOD', )       
        return likelihood

    def ARandomWalk(self):#creates trnasition matrix? or in other words creates self.A
        A=np.zeros((80,80)) #shold be matrix not zeros!
        
        counter = 0
        for i in range(80):
            # print(self.maze.state2coord(i), 'hello')
            n = self.maze.nbrList(i)#this is probably the noise that we are ust given 
            for j in n:
                # n = self.maze.nbrList(j)
                # print(j, 'jjjjjj')
                newans = 1/(len(n)+1) #1 being the total probability and len(n)+ 1 total number of possible spots i could be 
                # print(newans)
                # A[i][j]= newans #new stuff
                A[i][i]= newans
                A[j][i]=newans
                counter = counter+1
               
                # print(newans, 'newanswwereress', counter)
        # print(A)
        # print(sum(A[4]))
        # print(self.step(), "print()")
        self.A = A
        print(A,'Ass')
        print(self.A, "newASS")
        return A
            
    def step(self):
        #this is how A should work
        print(self.A,'heheheheheAAAA')
        pn=np.dot(self.A,self.prob)
        print(pn,"pnpnpn")
        self.prob=pn

    def bayesFilter(self,obs):
        #update prob
        transitionMatrix2  = self.A
        # print(self.step(), "print()")

        priorDist = self.prob
        # print(priorDist,'helolololeuisfgjzvrsk')
        # time.sleep(10)
        # print(sum(priorDist))
        # print(priorDist)
        bel_ = np.dot(transitionMatrix2, priorDist)
        # print(bel_)
        bel = self.obsLiklihood(obs) * bel_
        # print(sum(bel_), 'BELLLLL_______')
        # print(sum(bel),'BELLLL')
        total= sum(bel)
        # print(total, 'total')
        pb = []
        for i in bel:# used from previous hw thijkn is for normalizesinhg 
            x = (i/total) 
            pb.append(x)

        # print(pb)
        # print(sum(pb), 'herehereerherherherherehre')
        #update prob
    
        self.prob= pb 
        # print(pb)  
        # print('start' , transitionMatrix2, 'here')     
        pass
        

# =======================================================================================

if __name__=="__main__":
	    
       # ------- Weather ------    
    
    weather=weatherModel()
    
    raw_days=weather.read_weather_log('weather.log')
    
    '''
    Convert raw sequenc into sequcne of ['sun', 'rain', 'clouds']
    '''
    
    #Train first on fake data
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
    print(rob.prob,'hererererer')
    rob.step()
    rob.step()
    rob.step()
    robotShow(rob)    

    ''' Set rob.prob to the steady state'''     
    rob.randomize()
       
     
    #two input sequences both contain occasional sensor errors
    #in one of them the robot got kidnamped!
    
    #Can you tell by the behavior of bayes filter which sequence of 
    #observations comes from the kindnaped robot?

    
    obsA=[[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,1,0,1],[0,0,1,1],
          [1,1,0,0],[1,1,0,1],[0,0,1,1],[1,0,0,0],[0,0,0,1],
          [1,1,0,1],[0,0,0,0],[0,1,0,1],[0,0,0,1],[0,1,0,1],
          [0,0,0,1],[1,0,0,0]]
 
    
    
    obsB=[[0,0,0,1],[1,0,1,0],[0,0,0,0],[0,1,0,1],[0,1,0,1],
          [0,1,0,1],[0,0,0,1],[1,0,0,0],[1,0,1,0],[1,0,0,0],
          [0,0,0,0],[0,1,0,1],[0,0,1,1],[1,1,0,0],[0,1,0,1],
          [0,0,1,1],[1,0,0,0]]
    '''                   
    try this for both input sequences     
    you can run this to test bayes filter
    NOTE: This will show nothing since the functions are not implemented 
    but once you get the bayes filter running, it will show the probability 
    distribution converging over a few steps
    '''
    # count = 0
    for o in obsA:
            rob.bayesFilter(o)
            # print(o, count ,'+++++++++++++++++++++', max(rob.prob), rob.prob.index(max(rob.prob)))
            robotShow(rob)
            # count= count+1
    #This will pop up a lot of figures. 
    #You can close them with close_all()
    
    