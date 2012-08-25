######################################
## Cellular Automata Map Generator  ##
## run.py                           ##
######################################

# Run the generator and dump the map to the console.

import cellular, postprocess

#####   CONFIG SECTION   #####
G = cellular.run(100, 50, 45, 4, 20000, True) # Generator values, see "cellular.py".
pp_passes = 10 # Number of cell culling postprocessor passes.
neighbor_threshold = 3 # Neighbor threshold for cell culling postprocessor.
inverse_operation = False # Perform inverse cell culling postprocessor operation.
enclose = True # Run the grid enclosing postprocessor.
##### END CONFIG SECTION #####

i = 0
while i < pp_passes:
	G = postprocess.cull(G, neighbor_threshold, not inverse_operation)
	i += 1

if enclose:
	postprocess.enclose(G)

G.dump({True: " ", False: "#"})

