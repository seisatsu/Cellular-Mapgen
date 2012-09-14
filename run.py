######################################
## Cellular Automata Map Generator  ##
## run.py                           ##
######################################

# Run the generator and dump the map to the console.

import cellular, postprocess

#####   CONFIG SECTION   #####
G = cellular.run(100, 50, 45, 4, 20000, True) # Generator values, see "cellular.py".
pp_passes = 5 # Number of cell culling postprocessor passes.
neighbor_threshold = 3 # Neighbor threshold for cell culling postprocessor.
inverse_operation = False # Perform inverse cell culling postprocessor operation.
enclose = True # Run the grid enclosing postprocessor.
fill_not_largest = False # Fill cells in all areas but the largest.
##### END CONFIG SECTION #####

i = 0
while i < pp_passes:
	postprocess.cull(G, neighbor_threshold, not inverse_operation)
	i += 1

if fill_not_largest:
	postprocess.largest_group(G, True, True)

if enclose:
	postprocess.enclose(G)

G.dump({True: " ", False: "#"})

