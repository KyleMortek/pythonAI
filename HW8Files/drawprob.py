import numpy as np
import matplotlib.pyplot as plt
# import prettyplotlib as ppl


def plotQQual(q, name : str = ''):
    
    plt.ylabel('Fraction of Optimal Actions')
    plt.xlabel('Training Episode')
    
    plt.plot(q, label=name)
    
    
def pList(p,maze):

	# print probability distribution
	
	 m=np.max([p, maze.world.reshape(maze.stateSize)],axis=0)
	 print(np.array2string(m.reshape(maze.worldShape), precision=4))
	 return m.reshape(maze.worldShape)

def robotShow(r):
	pShow(r.prob,r.maze)    
	 
def pShow(p,maze):

	# visualize probability distribution

	# ==================================
	# p: probability distribution with shape (80,1)
	# input should be raw probability distribution [pn] (sum of all terms equals to 1), instead of [-np.log(pn)]
	# purple color represents walls, yellow/cyan squares are valid position, the larger value on yellow, the larger probability it has
	# ==================================

	iW = 1 - maze.world
	colormap = np.zeros((maze.worldShape))
	p_reshape = np.reshape(p,maze.worldShape)
	valid = np.multiply(p_reshape,iW)
	max_p = np.max(valid)
	if max_p > 0:
		nonzero = np.nonzero(p_reshape>0)
		for i in range(nonzero[0].shape[0]):
			colormap[7-nonzero[0][i]][nonzero[1][i]] = p_reshape[nonzero[0][i]][nonzero[1][i]]*(1.0/max_p) # map largest p to 1, make sure empty space is white
	nonzero = np.nonzero(maze.world==1)
	for i in range(nonzero[0].shape[0]):
		colormap[7-nonzero[0][i]][nonzero[1][i]] = -1

	fig, ax0 = plt.subplots(1)
	c = ax0.pcolor(colormap)
	fig.tight_layout()
	plt.show()