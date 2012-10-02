######################################
## Cellular Automata Map Generator  ##
## grid.py                          ##
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

# Generic Grid Class

class Grid:
	def __init__(self, width, height, initval):
		"""
		Make a new grid of "width"x"height", where the value of each cell is 
		"initval".
		"""
		self.__grid = [] # Internal Grid Data
		c = [] # Temporary Column
		wi, hi = 0, 0 # Counters
		
		while hi < height: # Build a column.
			c.append(initval) # Set the initial value for each cell.
			hi += 1
		
		while wi < width: # Build a grid from copies of the column.
			self.__grid.append(list(c)) # Copy the column instead of referencing it.
			wi += 1
	
	def size(self):
		"""
		Return the dimensions of the grid as a tuple.
		"""
		return (len(self.__grid), len(self.__grid[0]))
	
	def get(self, x, y):
		"""
		Get the contents of a cell by its "x","y" coordinates.
		"""
		return self.__grid[x][y]
	
	def put(self, x, y, val):
		"""
		Set the contents of a cell to "val" by its "x","y" coordinates.
		"""
		self.__grid[x][y] = val
	
	def append(self, x, y, val):
		"""
		Append "val" to the contents of a cell by its "x","y" coordinates.
		"""
		self.__grid[x][y] += val
	
	def data(self):
		"""
		Return a reference to the 2d grid array.
		"""
		return self.__grid
	
	def copy(self):
		"""
		Get a copy of the grid.
		"""
		return list(self.__grid)
	
	def fcopy(self):
		"""
		Get a copy of the grid with x and y axes exchanged. (Flipped copy.)
		"""
		g = [] # Temporary Grid
		r = [] # Temporary Row
		wi, hi = 0, 0 # Counters
		
		while hi < len(self.__grid[0]): # Build each row.
			r.append(self.__grid[wi][hi])
		
			if wi < len(self.__grid)-1: # Next cell.
				wi += 1
			else: # Next row.
				wi = 0
				hi += 1
				g.append(list(r)) # Copy the row into the grid.
				r = []
	
		return g
	
	def dump(self, tr):
		"""
		Dump the grid to stdout, with cell translations from dictionary "tr".
		"""
		r = "" # Temporary Row
		wi, hi = 0, 0 # Counters
	
		while hi < len(self.__grid[0]): # Build each row.
			if self.__grid[wi][hi] in tr: # Translate the cell if applicable.
				r += str(tr[self.__grid[wi][hi]])
			else:
				r += str(self.__grid[wi][hi])
		
			if wi < len(self.__grid)-1: # Next cell.
				wi += 1
			else: # Next row.
				wi = 0
				hi += 1
				print(r)
				r = ""
	
	def fdump(self, tr):
		"""
		Dump the grid to stdout, with cell translations from dictionary "tr", 
		and with x and y axes exchanged. (Flipped dump.)
		"""
		g = self.fcopy() # Temporary Grid
		r = "" # Temporary Row
		wi, hi = 0, 0 # Counters
	
		while hi < len(g[0]): # Build each row.
			if g[wi][hi] in tr: # Translate the cell if applicable.
				r += str(tr[g[wi][hi]])
			else:
				r += str(g[wi][hi])
		
			if wi < len(g)-1: # Next cell.
				wi += 1
			else: # Next row.
				wi = 0
				hi += 1
				print(r)
				r = ""
	
	def pbmdump(self, rbw):
		"""
		Dump a PBM image of the grid data (True/False) to stdout, reversing the 
		black and white values if "rbw" is True. (PBM dump.)
		"""
		print("P1") # Magic Header
		print(str(len(self.__grid))+" "+str(len(self.__grid[0]))) # Size Header
		if rbw:
			self.dump({True: "0", False: "1"})
		else:
			self.dump({True: "1", False: "0"})
	
	def fpbmdump(self, rbw):
		"""
		Dump a PBM image of the grid data (True/False) to stdout, reversing the 
		black and white values if "rbw" is True, and with x and y axes 
		exchanged. (Flipped PBM dump.)
		"""
		print("P1") # Magic Header
		print(str(len(self.__grid))+" "+str(len(self.__grid[0]))) # Size Header
		if rbw:
			self.fdump({True: "0", False: "1"})
		else:
			self.fdump({True: "1", False: "0"})

