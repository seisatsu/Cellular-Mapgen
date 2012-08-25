######################################
## Cellular Automata Map Generator  ##
## postprocess.py                   ##
## Copyright 2012 Michael D. Reiley ##
######################################

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

# Cellular Automata Map Postprocessor Functions
# These postprocessor functions are written for game map processing.

import cellular
import copy

def cull(G, n, o):
	"""
	Cull each cell in the grid (switch states) based on the states of its 
	neighbors, using the neighbor threshold "n". Perform inverse operation if 
	"o" is False.
	"""
	wi, hi = 0, 0
	w, h = G.size()
	G2 = copy.deepcopy(G)
	
	while wi < w:
		while hi < h:
			if o:
				if cellular.examine_neighbors(G, wi, hi) >= 8-n:
					G2.put(wi, hi, True)
			else:
				if cellular.examine_neighbors(G, wi, hi) <= 8-n:
					G2.put(wi, hi, True)
			hi += 1
		wi += 1
		hi = 0
	
	del G
	return G2

def enclose(G):
	"""
	Create a one-wide permimeter on the sides of the grid.
	"""
	w, h = G.size()
	
	wi, hi = 0, 0
	while wi < w: # Top
		G.put(wi, hi, False)
		wi += 1
	wi -= 1
	while hi < h: # Right
		G.put(wi, hi, False)
		hi += 1
	
	wi, hi = 0, 0
	while hi < h: # Left
		G.put(wi, hi, False)
		hi += 1
	hi -= 1
	while wi < w: # Bottom
		G.put(wi, hi, False)
		wi += 1

