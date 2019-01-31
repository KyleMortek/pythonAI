# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:14:54 2017

@author: nnapp
"""


import numpy as np
import pickle 
from markov import maze
from mdp import MDPmaze
import os.path


'''
Class that models agent intractions with the environment

It also contains the associated MPD which can be used to compute
the optimal actions. To speed up loading time the optimal policy is 
stored in the file "policyFileName". If and of the parameters for the MDP 
change the optimal soultion should be re-computed using solveMDP 
'''

policyFileName='mdpPolicy.pkl'

class AgentInteraction:
    def __init__ (self):
         
        '''use the mdp class for action and maze defintions'''
        self.mdp=MDPmaze( maze(np.array([
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,1,0],
                [0,1,0,1,1,0,1,0,1,0],
                [0,1,0,1,0,0,1,0,1,0],
                [0,1,1,1,0,1,1,0,1,0],
                [0,1,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0,1,0]])),
    
                np.array([
                [0,0,0,-10,-10,-10,-10,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,100,0,0,0,0,0],
                [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000]]))
        
        self.computedOptimalPolicy=False
          
        '''
        setup computes:
            optimal policy
            statey state distribution pss
        '''
        self._setup()
        

        '''
        initialize the state of the system
        '''
        self.state=None
        self.reset()
        
        
    def reset(self):
        '''
        reset the agent to a random position in the maze
        according to the steady state distribution
        '''
        
        self.state=np.random.choice(self.mdp.stateSize,p=self.pss)
    
    def takeAction(self,a):  
        '''
        choose next state according to the transition matrix according
        to action a and the current state (self.state)
        
        return the next state and the reward for executing the action
        '''
        
        nextState=np.random.choice(self.mdp.stateSize,p=self.mdp.transDict[a][:,self.state])
        
        reward = self.mdp.stateReward[self.state]
        if not a == 'stop':
            reward = reward -1
        
        self.state=nextState
        
        return nextState, reward
 
    
    
    def applicableActions(self):
        '''
        return the list of applicable actions
        '''
        actionList=self.mdp.maze.actionList(self.state)
        actionList.append('stop')
        return actionList
        
    
    def solveMDP(self):
        
        for i in range(750):
            self.mdp.valIter()
        self.computedOptimalPolicy=True
        self.mdpSolved=True
        self.mdp.computePolicy()
        self.optimalPolicy=self.mdp.policy
        
        with open(policyFileName,'wb') as fh:
            pickle.dump(self.optimalPolicy,fh)

        return self.optimalPolicy
    
    def getoOtimalPolicy(self): 
        
        '''return policy, solve MDP if neccesary'''
        if self.mdpSolved:
            return self.optimalPolicy
        else: 
            return self.solveMDP()
    

    def _setup(self):
        
        '''
        compute steady state distribution of random motion
        
        This approach uses eigenvectors instead of 
        multiplying Arandom overand over again
        '''
        
        eigvals,eigvecs=np.linalg.eig(self.mdp.Arandom)
        idx=np.argmax(eigvals)
        assert abs(eigvals[idx]-1)<1e-6 # The maximum eigenvector should be 1
        self.pss=eigvecs[:,idx]
        self.pss=self.pss/sum(self.pss)
        
        '''
        get optimal policy, either by reading a cached version
        from the one stored in 'policyFileName' or by computing it
        '''
        if(os.path.isfile(policyFileName)):
            
            with open(policyFileName,'rb') as fh:    
                self.optimalPolicy=pickle.load(fh,encoding='bytes')
            
            self.computedOptimalPolicy=True

            # write back to mdp for visualizetion        
            self.mdp.policy = self.optimalPolicy

        else:
        
            self.solveMDP()
        
    
if __name__ == '__main__':
    
    agent=AgentInteraction()
    agent.mdp.showPolicy()
    