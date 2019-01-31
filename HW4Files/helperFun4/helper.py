# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 02:08:34 2017

@author: nnapp
"""

"""
This import magic is pretty terrible, please feel free to fix the import mess
or move the files to the appropirate directory. The pyperplan related imports
assume that they are run in the pyperplan/src path
If you installed pyperplan on your system,  you should not have to to this 
"""

import time
import os

os.chdir("pyperplan/src")
print(os.listdir())
import pyperplan as plan
import pddl
from search import searchspace
os.chdir("../..")

from slideproblem import *

'''
Task should be a parsed task for the 3x3 grid problem
The initial condition will be prepalced with the board
from the slide problem definition
'''
def replaceBoard(prob,state):
    
    newInit=[]
    for row in range(state.boardSize):
        for col in range(state.boardSize):
            newInit.append(toPredicate(row+1,col+1,state.board[row][col],prob))
    
       
    #add all the predicates from the original initial state        
    for pred in prob.initial_state:
        if pred.name != 'at' and pred.name != 'empty':
            newInit.append(pred)        
            
    prob.initial_state = newInit         
  
    
def toPredicate(row,col,num,prob):
    if num == 0:
        return pddl.pddl.Predicate('empty',
                                   [(str(row),prob.objects[str(row)]),
                                     (str(col),prob.objects[str(col)])])   
    else:
        return pddl.pddl.Predicate('at',
                                   [('tile'+str(num),prob.objects['tile'+str(num)] ),
                                    (str(row),prob.objects[str(row)]),
                                     (str(col),prob.objects[str(col)])])
        
        
def search_plan_mod(prob, search, heuristic_class):
    """
    Copied from Pyperplan, modified to take a parsed problem rather than 
    two filenames
    """
    
    task = plan._ground(prob)
    heuristic = None
    if not heuristic_class is None:
        heuristic = heuristic_class(task)
    search_start_time = time.clock()
    
    solution = plan._search(task, search, heuristic)
    plan.logging.info('Wall-clock search time: {0:.2}'.format(time.clock() -
                                                         search_start_time))
    return solution        
        


    
'''
Initialize slide problem and make a random state 100 moves
'''    
problem = Problem()
state = State()
apply_rnd_moves(100, state, problem)

print(state)

'''
Initialize pyperplan and parse the domain and task files
'''
par=plan.Parser('class/slide-domain-grid.pddl','class/task3x3-grid.pddl')
dom=par.parse_domain()
pddlProb=par.parse_problem(dom)


'''
Replace the board in the parsed PDDL problem with the random one and 
compute the optimal solution using BFS
'''
replaceBoard(pddlProb,state)
sol=search_plan_mod(pddlProb,plan.SEARCHES['bfs'],None)

'''
Ground the problem again and make a root node that contains the random state
This is the input for the heuristic functions
'''
task=plan._ground(pddlProb)
root = searchspace.make_root_node(task.initial_state)

'''
initialize heuristic functions
and compute them on the root node 
'''
hff=plan.HEURISTICS['hff'](task)
hmax=plan.HEURISTICS['hsa'](task)
hadd=plan.HEURISTICS['hadd'](task)
hmax=plan.HEURISTICS['hmax'](task)


init_hff = hff(root)
init_hadd = hadd(root)
init_hmax = hmax(root)

print("BFS solution is length  : " +  str(len(sol)  ))
print("Hmax heuristic is       : " +  str(init_hmax ))
print("Hff heuristic is        : " +  str(init_hff  ))
print("Hadd heuristic is       : " +  str(init_hadd ))




