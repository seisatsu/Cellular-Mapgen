####################################
# Cellular Automata Map Generator  #
# run_random.py                    #
####################################

# Run the generator with sensible random values and dump the map to the console.

import cellular
import postprocess
import random

# Config Section
g = cellular.run(100, 50, random.randint(43, 47), 4, random.randint(15000, 35000), True)
pp_passes = random.randint(0, 5)
neighbor_threshold = random.randint(1, 3)
inverse_operation = False  # Perform inverse cell culling postprocessor operation.
enclose = True  # Run the grid enclosing postprocessor.
fill_not_largest = False  # Fill cells in all areas but the largest.

# Code Section
i = 0
while i < pp_passes:
    postprocess.cull(g, neighbor_threshold, not inverse_operation)
    i += 1

if fill_not_largest:
    postprocess.largest_group(g, True, True)

if enclose:
    postprocess.enclose(g)

g.dump({True: " ", False: "#"})
