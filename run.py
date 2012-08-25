######################################
## Cellular Automata Map Generator  ##
## run.py                           ##
######################################

# Run the generator and dump the map to the console.

import cellular, postprocess

#####   CONFIG SECTION   #####
G = cellular.run(100, 50, 45, True, 4, 20000) # Generator values, see "cellular.py".
pp_passes = 10 # Number of postprocessor cell culling passes.
neighbor_threshold = 3 # Neighbor threshold for postprocessor cell culling.
inverse_operation = False # Perform inverse postprocessor cell culling operation.
enclose = True # Run the grid enclosing postprocessor.
##### END CONFIG SECTION #####

i = 0
while i < pp_passes:
	G = postprocess.cull(G, neighbor_threshold, not inverse_operation)
	i += 1

if enclose:
	postprocess.enclose(G)

G.dump({True: " ", False: "#"})

