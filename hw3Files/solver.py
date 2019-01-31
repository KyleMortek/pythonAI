import sudoku
from sudoku import mac
import time
import queue
from queue import *
from queue import Queue
from queue import deque

class Solver:
	def AC3(self,csp, arcQ=None, removals=[]):
		# input: binary csp with (X,D,C) x= variables D = domains, C= constraints 
		# initialize arcQ with all the arcs in csp graph
		# its asking to make xi,xj tuples list of arcs 
			# place in arc q
		# return False iff theres an inconsisency 
		arcQ = []
		for xi in csp.variables:
			# iterate through variables ranging 0-80
			for xj in csp.neighbors[xi]:
				# iterate through to create tuple (xi,xj)
				# arcQ.put((xi,xj))
				arcQ.append((xi,xj))
		# for xk in csp.neighbors[arcQ.queue[0][1]]:

		# #$%print(arcQ)
		while arcQ != []:
			# remove first xi,xj
			# first = arcQ.get()
			first = arcQ.pop(0)
			xi = first[0]
			xj = first[1]
			if self.revise(csp,xi,xj, removals):
				if(len(csp.curr_domains[xi])==0): #length of curr domains is size 0 
				# if (csp.curr_domains[xi] == []):
					# #$%print("im hereewrerere")
					return False
				# #$%print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
				for xk in csp.neighbors[xi] - {xj}: # not sure if this is necessary 
					# #$%print(csp.neighbors[xi] - {xj})
					# #$%print({xj})

					# arcQ.put((xk,xi))
					arcQ.append((xk,xi))

			pass
		# #$%print(arcQ)
		
		# #$%print("removals::::::::::::::::::				",removals)
		# #$%print("currdoms", csp.curr_domains)
		return True
		# #$%print(arcQ)
		# #$%print("ARCq")
		# #$%print('currdom')
		'''
		removing the domains of what we know !!!

		check first index. in csp.neighbors 
		===csp.neighbors[0]
		neighbors of 0
		{box[1, 2, 3, 4, 5, 6, 7, 8], left-right[9, 10, 11, 18, 19, 20], up-down[27, 30, 33, 54, 57, 60]}
		but what is Zeros value? 
		and what are its neighbors values? 
		check zeros domains. if domain list is larger than 1 , then find neighbors with 1 domains value. 
		if neighbor has one domain value remove from zeros domain list ==using prune('singledomainvar', 'itsDomain',removals) 
		'''
		
		'''
		your code here
		'''
		# return true
	def revise(self,csp, Xi, Xj, removals): 
		revised = False
		Di= csp.curr_domains[Xi]
		Dj= csp.curr_domains[Xj]
		if(len(Di)!=0):
			for x in Di:
				if len(Dj)==1:
					# this then would be a value i need to delete from a domain greater than1
					#now we know that y is only going to be one value. 
					y = Dj[0]
					if y:
						# #$%print(y)
						con = csp.constraints(Xi, x, Xj, y) # if false then x == y
						# #$%print("constraint bool:" ,con,"Xi:", Xi,"x:", x,"Xj:",Xj, "y:",y)

						# #$%print(con)
						# if len(Dj)==1 and y in Dj 
						if not csp.constraints(Xi, x, Xj,y):# i think this needs 
							csp.prune(Xi,x,removals)
							revised = True
						# #$%print(board.constraints(0,'0',1,'0')) #should be False, shares the same domain. 
						# #$%print(board.constraints(0,'0',1,'1')) #should be true, different. 
						# #$%print(Di, "XI")
						# #$%print(Dj ,"XJ")
		"""Return true if we remove a value."""
		'''
		your code here
		'''
		return revised
	
	
	def backtracking_search(self,csp):
		# print(csp.curr_domains)
		# time.sleep(10)
		return self.backTrack({}, csp)	# return backTrack(self,{}, csp)
		'''
		your code here
		'''
	
	def backTrack(self,assignments, csp):#see helper code on line 80 and below 

		'''
		add current board to assignments 
		infer_assignment(self)
		'''
		# assignments = csp.infer_assignment()
		#$%print(len(assignments), "ASSIGNMENTS")
		if(len(assignments) ==81):
			return assignments
		# INITIALIZES ASSIGNMENT WITH CURRENT BOARD
		#SHOULD BE 81 ASSIGNMENTS
		'''
		done with adding current board to asssigment
		'''
		
		'''
		get all unassign vars 
		'''
		unVals = []
		unAssignedVars = []
		for var in csp.curr_domains:#GETS UNSIGN VARIABLES 
			if(len(csp.curr_domains[var])>1):
				unVals.append(csp.curr_domains[var])
				unAssignedVars.append(var)
		'''
		done with getting unassigned vars and vals

		'''
		# print("currdoms", csp.curr_domains)

		# how do we check if assignment is complete? 
			# to check if assigment is complete 
			#make sure all durr domains are of length zero

		'''
		if length of assignemnts is boardsize 81 tthen return assigbnennt 
		'''
		# if len(assignments)==81:
		# 	return assignments
		# #else get var and 
		# for var in csp.curr_domains:# goes through each index of the board 
		# 	if len(csp.curr_domains)>1:
		# 		#add var val to assignemnt 
		# 		# assignments.update(csp.suppose(var,csp.curr_domains[0]))
		# 		#$%print(assignments)
		# 		# assignments.update((var,2))
		# 		#$%print(assignments)
		# 		pass
				

		# if assignment is complete then return assignment 
		#get unassugned varibles in a list. 
		# WHAT IS UNASIGNED VARIBLES? 
			#its the varibles that have more than one domain. 
			#loop through curr domains and makea a new list called unassunged varibels 
		# #$%print("initial",csp.initial)
		# assignments.

		# for var in csp.variables:
		# 	for x in csp.curr_domains[var]:

		# WHAT IS UNASIGNED VARIBLES? 
		#$%print(csp.infer_assignment(), "HMHMMHMHMH") # i want to subtract these from curr domains. 
		# #$%print(csp.curr_domains[0], csp.curr_domains[1])
		##$%print(unVals,"UNVALS")
		# [X for X in unAssignedVars]
		# newVarArclist = [(var,val) for var in unAssignedVars for val in csp.curr_domains[var]]
		# #$%print(queue, "queueueuueueeueu")
		# var= unAssignedVars.pop(0)
		# #$%print(csp.suppose(var,csp.curr_domains[var][0]), "ASSUMING")
		'''
		now tthat we have assumed. we need to remove the curr domains from the neighbors
		firs ttime through it #$%prints true,
		figure out how to iterate suppose until it works 
		'''
		# while unAssignedVars !=[]:
		
		if(csp.goal_test(assignments)==True):
		# if(len(assignments)==81):
			return assignments
		if(unAssignedVars !=[]):
			# val = csp.curr_domains[varPop][0]
			varPop= unAssignedVars[0]
			#$%print(unAssignedVars, "unASSUINGED VARS")
			for value in csp.curr_domains[varPop]:
				# print(varPop,csp.curr_domains[varPop])
				# (assignments,"ASSIGNMENTS")
				if(value != 0):
					csp.assign(varPop,value,assignments)#ADD TO ASSIGNMENT 
					#######################################SUPPOSE AN ASSIGNEMNT
					 
					removals = csp.suppose(varPop,value)
					# board.display(board)
					# print("afterIEAUFBEIUFBEIWUFBEWIUFBEIUWFBIEFUBEWIUFB")
					# #$%print(removals)
					# time.sleep(1)
					#keep track of all removals
					inf= self.AC3(csp,arcQ=None, removals=removals)
					# print(inf,"inf")
					# print(assignments,"ASSIGNMENTS")

					if(inf):
						# assignments[varPop]=val
						assignments.update(csp.infer_assignment())
						
						if(len(assignments)==81):
							# print("ITS DONE SLEEPPP")
							print("winner?",csp.goal_test(assignments),"GOAL_TEST" )
							# time.sleep(5)
							return csp.goal_test(assignments)
						# print("assignments:",assignments)
						result = self.backTrack(assignments, csp)
					
						if csp.goal_test(assignments)is True:####IF DOESNT FAIL 
							return csp.goal_test(assignments)
					
				csp.restore(removals)
			

		'''
		should i update curr domains again? from the first suppose neigh? 
		'''
		

	


	

		return False
		'''
		more code here 
		'''


		
if __name__ == '__main__':
	
	'''
	Some board test cases, each string is a flat enumeration of all the board positions
	where . indicates an unfilled location
	Impossible: 123456789.........123456789123456789123456789123456789123456789123456789123456789
	Easy ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
	Easy ...7.46.3..38...51.1.9.327..34...76....6.8....62...98..473.6.1.68...13..3.12.5...
	Difficult ..5...1.3....2.........176.7.49....1...8.4...3....7..8.3.5....2....9....4.6...9..
	'''
	
	# board = sudoku.Sudoku('12.456789.........12.45678912.45678912.45678912.45678912.45678912.45678912.456789') 
	# board = sudoku.Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..') 
	#  board = sudoku.Sudoku('...7.46.3..38...51.1.9.327..34...76....6.8....62...98..473.6.1.68...13..3.12.5...') 
	# board = sudoku.Sudoku('..5...1.3....2.........176.7.49....1...8.4...3....7..8.3.5....2....9....4.6...9..') 
	#EVILLLLL
	board = sudoku.Sudoku('4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
	#board = sudoku.Sudoku('3.2.6......125....5..981.7...6.....1.27...35.1.....7...4.128..6....358......9.5.7')

	# board = sudoku.Sudoku('53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79')
	#Accessing the board as a csp, i.e. display the variable and domains
	#See the extra document for exapmles of how to use the  CSP class
	

	# Display this nonsensical board
	board.display(board)

	
	#Show the "flat" variables
	# #$%print("vars")
	# #$%print(board.variables)
	
	#show the domeians (curr_domains beocmes populated by infer_assignment())
	# #$%print("domains curr")
	# #$%print(board.curr_domains)
  
	
	'''You'll need to manipulate the CSP domains and variables, so here are some exampels'''
	
	# this is a list of (variable, domain value) pairs that you can use to keep track
	# # of what has been removed from the current domains
	removals=[]

	# #show domains for variable 3
	# #$%print("Domain for 3: " + str(board.curr_domains[3]))    
	# #remove the possible value '8' form domain 3
	# #not the differences int key for the first dictionary and the string keys
   
	
	# board.prune(3,'8',removals) # This line may not work if the domain for 3 does not contain "8" 

	# #$%print("Domain for 3: " + str(board.curr_domains[3]))    
	# #$%print("Removal List: " + str(removals))
	
	#Prune some more
	# #$%print("Domain for 23: " + str(board.curr_domains[23]))     
	# board.prune(23,'1',removals)
	# board.prune(23,'2',removals)
	# board.prune(23,'3',removals)
	# #$%print("Domain for 23: " + str(board.curr_domains[23]))    
	# #$%print("Removal List: " + str(removals))
	
	#ooopes took away too muche! Restore removals
	# board.restore(removals)
	# #$%print("Domain for 23: " + str(board.curr_domains[23]))    
	  
	#For assigning vaeiables use a dictionary like
	assignment={}
	# board.assign(23,'8',assignment)
	#ocne all the variables are assigned, you can use goal_thest()
	
	#find the neighbors of a varaible
	# #$%print("Neighbors of 0: " + str(board.neighbors[0]))
	
	#check for a constraint, need to plug in a specific var,val, var val combination
	#since 0 and 1 are neighbors, they should be different values
	# #$%print(board.constraints(0,'0',1,'0')) #should be False
	# #$%print(board.constraints(0,'0',1,'1')) #should be true i.e. not a constraint
	
   
	'''to check your implementatios:''' 
	
	# AC3 should return false for impossible example above
	sol = Solver()
	# start=time.clock()
	#$%print(sol.AC3(board))
	#$%print("time: " + str(time.clock() - start))
	# board.display(board)
	# #$%print(removals)
	# #$%print("Domain for 3: " + str(board.curr_domains[3]))    
	# board.prune(3,'8',removals)
	# #$%print("Domain for 3: " + str(board.curr_domains[3]))    
	# #$%print(removals)
	# backtracking search usage example
	start=time.clock()
	sol.backtracking_search(board)
	print(":EVIL")
	print("time: " + str(time.clock() - start))
	board.display(board)
	
	