######################################
## Cellular Automata Map Generator  ##
## run_random.py                    ##
######################################

# Run the generator with sensible random values and dump the map to the console.

import cellular, postprocess, random

#####  ROLL SENSIBLE RANDOM VALUES  #####
G = cellular.run(100, 50, random.randint(43, 47), True, 4, random.randint(15000, 35000))
pp_passes = random.randint(0, 10)
neighbor_threshold = random.randint(1, 3)
##### END RANDOM VALUE ROLL SECTION #####

#####   CONFIG SECTION   #####
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

