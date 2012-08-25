Cellular Automata Map Generator
Copyright (c) 2012 Michael D. Reiley <mreiley@omegasdg.com>

Released under the MIT/Expat License.

This is a cellular automata map generator algorithm based largely upon a 
specification found at <http://www.evilscience.co.uk/?p=53>. It is well suited 
to generating natural-looking, cavernous patterns. It may be useful for a 
random dungeon generator. The algorithm can create maps of amazing variety 
with a small number of variable starting conditions.

File List:
* grid.py : Generic Grid Class
* cellular.py : Map Generator
* postprocess.py : Map Postprocessing Functions
* run.py : Configurable Test Vector
* run_random.py : Randomized Test Vector

The included test vectors demonstrate the use of the algorithm, and dump the 
generated maps to the console in an ascii representation.

The algorithm has no dependencies except for Python 2.7.X. It may work on Python
2.6.X, but this has not been tested.

Notes:
* Higher iteration counts lower the complexity of the map, while too little 
  iterations can produce ugly, messy maps.
* The iteration count needs to be adjusted for map size.
* A neighbor threshold of "4" and an initial closed cell probability of "45" 
  seems to produce the best results for regular operation. Even slight 
  deviations can produce ugly maps.
* The cell culling postprocessor isn't very useful for inverse operation mode.
* Increasing the postprocessor neighbor threshold too far will destroy the map.

##################################################
###########   ########################        ####
##########     ######################          ###
# #######      #############   ######           ##
########      ###############   ####            ##
########  ## ############ ####   ##      ##     ##
#####     #####################         ###      #
#  #       ##  #################      #####      #
#               ###############     #######      #
#                ##############     #######      #
#    ####        ##############     #######      #
#    #####        ############     #######       #
#    ######        ##########     #######        #
#    ######        #########      ######         #
#    ######        ########      #####           #
#   ######          #######     #####            #
#######              ######      ####            #
#####                 ####        ####           #
####           ##      ##          ###           #
###            ###                  ##           #
#              ####                 ###          #
#              ####                  ###        ##
#              ####                  ####  #######
#             #####        #        ##############
##################################################

