from math import log, exp


class ComputeBF:

    def __init__(self):
        """
            The constructor exists only to initialize variables. You do not need to change it.
        """
        self.tolerance=0.000001  #Set the tolerance for computing b
                
    def branching_factor(self,S,N):
        """ 
            Write a runction that sets the objects string to your name
            This is as simple as you tink it is!
        """
        
        upperBound=exp(log(S)/N)
        lowerBound=1
        
        lowerBound, upperBound = self.computeB_R(lowerBound,upperBound,S,N)
        
        return (lowerBound+upperBound)/2
        
    def computeB_R(self,lowerBound,upperBound,S,N):    
        
        # print("[",lowerBound, ", ", upperBound, "]" )
        
        #compute mean
        
        #check stopping condition for recusion, stop on else
        if(upperBound-lowerBound) > self.tolerance:            
            #compute mean
            guess=(upperBound+lowerBound)/2
           
            #compute sum as if it were the real one    
            val=sum([guess**n for n in range(N+1)])-1
            
            #figure out if guess was too high or too low    
            if(val>=S):
                return self.computeB_R(lowerBound,guess,S,N)
            else:
                return self.computeB_R(guess,upperBound,S,N)      
        else:
            return lowerBound, upperBound    