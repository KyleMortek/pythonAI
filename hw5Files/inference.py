"""
Homework 5 CSE410 2017
Your Name <<---
"""
from bayesnets import (ProbDist, BayesNode, BayesNet)
import random
from time import sleep
class Inference:
    
    '''
    Class to generate inference algorithms on Bayesian Networks        

    * Enumeraiton (produce all the terms in the joing and then marginalize)

    * Rejection Sampling

    * Likeliehood Weighting
    '''            
    
    def __init__(self, bayesian_network, evidence = {}):
        self.net=bayesian_network
        self.evidence=evidence
        
    def sample(self) -> dict:
        """ Return sample from network"""
    
        """ 
        Sample should be a dictionary where the keyes are  
        variable names and elemnts of their sample sapce
        """

        samp = {}
        for node in self.net.nodes:
            samp[node.variable] = node.sample(samp)
        return samp

        
        
    def rejection_sampling(self,X :str, N :int, e :dict = None) -> ProbDist:#533
        """
        Estimate the probability distribution of variable X given using 
        N samples and evidence e.  If not evidence is given, use the default
        for the Inference object.
        """
        if e==None:
            e=self.evidence

        # Q = ProbDist(X) 
        
        """YOUR CODE"""        
        countV = ProbDist(X)

        for j in range(N): #N is the sample spaces. 
            x = self.sample()#   x←PRIOR-SAMPLE(bn)
            # px=ProbDist(x)  
            #new way. want to find if e is subset of x items. 
            setx = set(x.items())
            sete = set(e.items())
            if(sete.issubset(setx)):#yay
                if x[X] is True: 
                    countV[x[X]] = countV[x[X]]+1
                if(x[X] is False):
                    countV[x[X]] = countV[x[X]]+1
        # print(ProbDist.normalize(countV))
        return ProbDist.normalize(countV)#<-- fix this too

    def copy_assign(self,ev,X,xval):
        '''
        return a copy of the evidence dictionary with X:xval appended
        this is useful for recursive enumerations of all assignments since 
        otherwise changing the dictionary would have side effects outside 
        the call, though it is entierly optional
        '''
        e=ev.copy()
        e[X]=xval
        return e
                
    def enumeration_infer(self,X, e=None) -> ProbDist:#page 525-528
        """
        Return the conditional probability distribution of variable X
        given evidence e
        """    
        
        '''
        Use evidence passed to function call, otherwise use default
        '''
        if e==None:
             e=self.evidence
        
        assert X not in e, 'Query variable must be distinct from evidence'
        assert X in self.net.variables, 'Variable needs to be in network'
        
        """
        * Initialize a probability distribution 
        * For each outcome sum over all the hidden variables
        * Normalize
        """
        Q= ProbDist(X)
        # print(Q)
        # print('im here')
        # for each value xi of X do
        for xi in self.net.variable_values(X):
            # e[xi] = X
            exi= self.copy_assign(e,X,xi)
            # print(exi,'exiGHGHGHGHGHHGHGHGHGHGHG')
            # Q(xi)←ENUMERATE-ALL(bn.VARS, exi )
            Q[xi] = self.enumerate_all(self.net.variables, exi)
            # print(e)
        """YOUR CODE""" 
        # return NORMALIZE(Q(X))
        # print(Q, "this is Q")
        return Q.normalize()

    def enumerate_all(self, vars, e):
        # print(vars, 'this is vars')
        if vars == []: return 1.0
        # Y←FIRST(vars)
        # newVars = vars
        Y=vars[0]
        # print(Y,'=========================================')
        RESTY = []
        for i in range(1,len(vars)):# f
            RESTY.append(vars[i])
        # print(Y, 'YYYYYYYYYYYYY')
        # if Y has value y in e
        if Y in e: #if e conatins Y
            # then return P(y | parents(Y )) × ENUMERATE-ALL(REST(vars), e)
            # print(Y)
            # print(self.net.variable_node(Y).p(e[Y], e))
            # print(e)
            # print(vars)
            # print(RESTY,'RESTYYYYY')
            return self.net.variable_node(Y).p(e[Y], e) *self.enumerate_all(RESTY, e)

        else:#else return sum(y P(y | parents(Y )) × ENUMERATE-ALL(REST(vars), ey))
            findVals= []
            # print(self.net.variables,'Y vallluesss')
            # take sum of (
            for y in self.net.variable_values(Y):
                ey= self.copy_assign(e,Y,y) # where ey is e extended with Y = y 
                # print(ey,"this is ey")
                # print(findVals,'findvals')

                findVals.append(self.net.variable_node(Y).p(y, e) *self.enumerate_all(RESTY, ey)) # finds the numbers that needs to be summed 
                pass
            # take sum of )
            answer=sum(findVals)# finds sum of 
            return answer
                # where ey is e extended with Y = y
        ###############################
        ######################         
# Probability distribution

# Let  X be a random variable which takes values x.
# The probability that the random variable X takes the value x is defined as the probability distribution of X.  It is denoted by f(x)
            
# function LIKELIHOOD-WEIGHTING(X, e, bn,N) returns an estimate of P(X|e)
    # inputs: X, the query variable
    # e, observed values for variables E
    # bn, a Bayesian network specifying joint distribution P(X1, . . . , Xn)
    # N, the total number of samples to be generated
# local variables: W, a vector of weighted counts for each value of X, initially zero
    # for j = 1 to N do
    # x,w ←WEIGHTED-SAMPLE(bn, e)
    # W[x ]←W[x] + w where x is the value of X in x
# return NORMALIZE(W)      
    def likelihood_weighting(self, X :str, N:int, e : dict =None) -> ProbDist:#page 534
        """Estimate the probability distribution of variable X given
        evidence e
        """
        if e == None:
            e=self.evidence
        W = ProbDist(X)        
        for j in range(N):
            x,w = self.weighted_sample(e.copy())
            W[x[X]]=W[x[X]]+w
        return ProbDist.normalize(W)
        
    def weighted_sample(self,e :dict = None) -> (dict,float):#page 534
        """Sample an event from bn that's consistent with the evidence e;
        return the event and its weight, the likelihood that the event
        accords to the evidence."""

        """YOUR CODE""" 
        newe= e
        w= 1.0
        # print(newe)
    
        # print(x,'herererererer',e)
        # foreach variable Xi in X1, . . . , Xn or all variables in net do
        for Xi in self.net.nodes:
            Xi = Xi.variable
            # if Xi is an evidence variable with value xi in 
            if(Xi in newe):
                w= w*self.net.variable_node(Xi).p(newe[Xi],newe)
            else:
                
                #new random sample
               newe[Xi]= self.net.variable_node(Xi).sample(newe) # then w ←w × P
            # print(newe,w)
        return newe, w
        # return {}, 1.0


diagnoseNet=BayesNet([('Healthy','','',(0.8,0.2)),
                      ('FluShot','','',(0.6,0.4)),
                      ('Flu','','Healthy FluShot',{(True,True):(0,1.0),
                                                   (True,False):(0,1.0),
                                                   (False,True):(0.1,0.9),
                                                   (False,False):(0.4,0.6)}),
                      ('Lyme','', 'Healthy',{True: (0,1.0)  , False:(0.01,0.99)}),
                      ('Numbness','','Lyme',{True: (0.8,0.2), False:(0.3,0.7)}),
                      ('Fever','','Flu',{True:(0.9,0.1), False:(0.2,0.8)}),
                      ('Vomit','','Flu',{True:(0.8,0.2), False:(0.1,0.9)}),
                      ('Fatigue','','Lyme Flu',{(True,True):(0.99,0.01),
                                                (True,False):(0.8,0.2),
                                                (False,True):(0.9,0.1),
                                                (False,False):(0.4 , 0.6)})])        
        
'''Please Build the Bayes net from class'''
testNode123=BayesNode('Node','val1 val2 val3', #for reference fro,m below_
                       'A/B-Parent C/D-Parent', 
                       {('A','C'):(0.1, 0.2, 0.7),
                        ('A','D'):(0.3, 0.5, 0.2),
                        ('B','C'):(0.0, 0.2, 0.8),
                        ('B','D'):(0.998, 0.001, 0.001)})

awakeNet= BayesNet([('T','<6, <7, <8, <9, >9', '', (0.3,0.1,0.1, 0.1, 0.4)),
                    ('A', '', 'T', {'<6':(0.05, 0.95),'<7':(0.3, 0.7), '<8':(0.8, 0.2), '<9':(0.9,0.1),'>9':(0.95,0.05)}),('L', '', 'A',{ True:(0.7,0.3),False:(0.2,0.8)}),('N', 'quiet, snore, blanket, steps','A', {   True: (0.2,0.01,0.29,0.5),False:(0.6,0.29,0.1,0.01)}),]) #<-------- Your code goes heres               
                     
if __name__ == '__main__':
 
    '''
    Example Uses of ProbDist:
        There are two ways to initialize distributions
        * Give it dictionary where the keys are the element of the sample space 
          and the values are counte or un-normalized probablities <<-- Will use this one
        * Give a sample_space list/tuple of domain values and a list/tuple that defines
          the distibution
    '''        
    
    ''' roll virtual dice '''
    counts={}
    for i in range(1,6+1):
        counts[i]=0
    for rolls in range(100):
        roll=round((random.random()*6 -0.5))+1 #scale and shift so round will work
        counts[roll] +=1
    print('Raw counts: ' + str(counts))
    pdice=ProbDist('Dice',counts)
    print('ProbDist Object: ' + str(pdice))
    print('Probability Dsitribution: ' + str(pdice.show_approx()))    
    
    '''
    BayesNodes and BayesNets
    Each node is specified with its parent names and the neccesarey CPT
    The CPTs are a little tricky. They are a dictionary where the keys are tuples 
    of possible values from the sample space of the parent domains. The value 
    is a probability vector that has the same length as the sample space. 
    '''
    
    testNode=BayesNode('Node','val1 val2 val3', 
                       'A/B-Parent C/D-Parent', 
                       {('A','C'):(0.1, 0.2, 0.7),
                        ('A','D'):(0.3, 0.5, 0.2),
                        ('B','C'):(0.0, 0.2, 0.8),
                        ('B','D'):(0.998, 0.001, 0.001)})

    '''
    * The tuple order is the same as the order listed in the parents string
    * Both the sample space and the partents can be given a lists/tuples
    * If sample space is '' or None then the samples space defaults to (True,False)
    * When there are no parents, the CPT can jsut be given as a vector of appropriate lenght
    '''            

    '''
    Working with these Bayes nets, events and samples are given as dictionaries
    To sample from a node you need an event (aka specific assignment) that specifies 
    the parents, but the event could include more values.
    '''    
    evidence={'A/B-Parent':'A', 'C/D-Parent':'C','SomeT/F-parent':True}
    
    '''Return the probability of a specific value given the evidence'''
    testNode.p('val2',evidence)    
    
    '''
    Sample from the distribution given evidence. The values will be 
    drawn from the sample_space according to the probability vector
    '''
    
    for i in range(10):
        print("Sampling given 'A/B-Parent'='A'" + " and 'C/D-Parent'='C' --> " 
              + testNode.sample(evidence) )

    '''
    A BayesNet is made up of a bunch of nodes. 
    During the specificaion they need to be added in such an order that the 
    parents always preceed their children. This makes sampling and 
    manipulation _MUCH_ easier. When you iterate  along the list of varialbes 
    to pick events, then the later ones will have their parents picked so you 
    can use both node.p(val,e) and node.sample(e) as long as e has the previous
    nodes in it. In the example below, the parents can come in either order, but must
    be added beofre 'Node'. The 'T/F-Node' must be last:
    
                  A/B-Parent   C/D-Parent  
                        \       /
                         \     /
                          V   V
                           Node -------> T/F-Node
                           
    '''    
    
    abcdNet=BayesNet([('A/B-Parent','A B','',(0.1, 0.9)),
                      ('C/D-Parent','C D','',(0.7, .3)),
                      ('Node','val1 val2 val3', 
                       'A/B-Parent C/D-Parent', 
                       {('A','C'):(0.1, 0.2, 0.7),
                        ('A','D'):(0.3, 0.5, 0.2),
                        ('B','C'):(0.0, 0.2, 0.8),
                        ('B','D'):(0.998, 0.001, 0.001)}),
                       ('T/F-Node','','Node',{'val1':(0.1, 0.9),
                                              'val2':(0.6, 0.4),
                                              'val3':(0.4, 0.6)})
                      ])    

    '''
    
    The 'T/F-Node' uses some shortcuts: 
    
    * The '' for sample_space means (True,False)
    
    * When there is only a single parent, you can drop the tuple notation
    in the keys for the CPT
    
    '''
   
    '''
    Example Usage of the InferenceClass
    '''
   
    inferHealth=Inference(diagnoseNet)
    
    #used in rejection sampling
    randomEvent=inferHealth.sample()
    print('\n\nRandom Sample from Net' + str(randomEvent))
    
    #set evidence for inference problem and then try a few methods 
    ''' 
    These should not work/do mutch until until you implement them!!
    However, there are some test cases with the restulst given the comments
    '''
    
    
    
    ev={'FluShot':False, 'Fatigue':True, 'Healthy':False, 'Flu':False}
    inferHealth.evidence=ev
    plymeW=inferHealth.likelihood_weighting('Lyme',1000)
    plymeR=inferHealth.rejection_sampling('Lyme',1000)
    plymeExact=inferHealth.enumeration_infer('Lyme')  
    #infer == ask  
    print("\n\nCompare Inference Techniques")
    print(plymeW.show_approx())     #<-- False ~ .98
    print(plymeR.show_approx())     #<-- False ~ .98 but can evaluate to  (1,0) due to sampling error
    print(plymeExact.show_approx()) #>>False: 0.98, True: 0.0198
    #infer == ask 
    plymeExact=inferHealth.enumeration_infer('Lyme',{})
    print(plymeExact.show_approx())
    #Lyme disease 0.2% given nothing
    #infer == ask
    ev={'FluShot':True, 'Fatigue':True}   
    plymeExact=inferHealth.enumeration_infer('Lyme',ev)
    print(plymeExact.show_approx())
    #Lyme disease 0.399% given fluShot & fatigue
    
    