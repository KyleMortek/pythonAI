# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:47:44 2017

@author: nnapp
"""

import numpy as np
import matplotlib.pyplot as plt
# import prettyplotlib as ppl

def close_all():
	plt.close('all')

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
	# fig, ax = plt.subplots(1)
	# ppl.pcolormesh(fig, ax, colormap)
	# plt.show()

	fig, ax0 = plt.subplots(1)
	c = ax0.pcolor(colormap)
	fig.tight_layout()
	plt.show()

# each column has to addd up to 1 