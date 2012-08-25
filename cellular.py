######################################
## Cellular Automata Map Generator  ##
## cellular.py                      ##
## Copyright 2012 Michael D. Reiley ##
######################################

## *****
## Thanks to http://www.evilscience.co.uk/?p=53
## *****

## **********
## Permission is hereby granted, free of charge, to any person obtaining a copy 
## of this software and associated documentation files (the "Software"), to 
## deal in the Software without restriction, including without limitation the 
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
## sell copies of the Software, and to permit persons to whom the Software is 
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in 
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
## IN THE SOFTWARE.
## **********

# Cellular Automata Map Generator

from grid import Grid
import random

def initialize(G, p):
	"""
	For each cell in the grid, randomly set it closed based on probability "p".
	"""
	wi, hi = 0, 0
	w, h = G.size()
	
	while wi < w:
		while hi < h:
			roll = random.randint(0, 99)
			if roll < p:
				G.put(wi, hi, True)
			hi += 1
		wi += 1
		hi = 0

def examine_neighbors(G, x, y):
	"""
	Examine the 8 neighbors of the cell at coordinates "x" by "y", and return 
	the number of neighbor cells which are closed.
	"""
	c = 0
	w, h = G.size()
	
	if x-1 >= 0:
		if G.get(x-1, y):
			c += 1
	if x+1 < w:
		if G.get(x+1, y):
			c += 1
	if y-1 >= 0:
		if G.get(x, y-1):
			c += 1
	if y+1 < h:
		if G.get(x, y+1):
			c += 1
	if x-1 >= 0 and y-1 >= 0:
		if G.get(x-1, y-1):
			c += 1
	if x-1 >= 0 and y+1 < h:
		if G.get(x-1, y+1):
			c += 1
	if x+1 < w and y-1 >= 0:
		if G.get(x+1, y-1):
			c += 1
	if x+1 < w and y+1 < h:
		if G.get(x+1, y+1):
			c += 1

	return c

def evolve(G, n, i, o):
	"""
	Choose a cell at random, and modify its state based on the states of its 
	neighbors, using the neighbor threshold "n". Continue for "i" iterations. 
	Perform inverse operation if "o" is False.
	"""
	w, h = G.size()
	gen = 0
	
	while gen < i:
		x, y = random.randint(0, w-1), random.randint(0, h-1)
		
		if o:
			if examine_neighbors(G, x, y) >= n:
				G.put(x, y, True)
			else:
				G.put(x, y, False)
		else:
			if examine_neighbors(G, x, y) >= n:
				G.put(x, y, False)
			else:
				G.put(x, y, True)
		gen += 1

def run(w, h, p, n, i, o):
	"""
	Create a new map using the cellular automata algorithm.
	
	* "w" is the map width.
	* "h" is the map height.
	* "p" is the probability of each cell being closed at start. (0 - 100)
	* "n" is the neighbor threshold. (0 - 8)
	* "i" is the number of iterations. (0 - infinity)
	* "o" is the operation switch. (Regular operation if True, inverse if False)
	"""
	G = Grid(w, h, False)
	
	initialize(G, p)
	
	evolve(G, n, i, o)
	
	return G

