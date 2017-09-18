#########################################
# Cellular Automata Map Generator       #
# postprocess.py                        #
# Copyright 2012-2017 Michael D. Reiley #
#########################################

# **********
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# **********

# Cellular Automata Map Postprocessing Functions
# These postprocessing functions are written for game map processing.

import cellular


def cull(g, n, o):
    """
    Cull each cell in the grid (switch states) based on the states of its 
    neighbors, using the neighbor threshold "n". Perform inverse operation if 
    "o" is False. This can remove "pepper" from the map.
    """
    wi, hi = 0, 0
    w, h = g.size()

    while wi < w:
        while hi < h:
            if o:
                if cellular.examine_neighbors(g, wi, hi) >= 8 - n:
                    g.put(wi, hi, True)
            else:
                if cellular.examine_neighbors(g, wi, hi) <= 8 - n:
                    g.put(wi, hi, True)
            hi += 1
        wi += 1
        hi = 0


def enclose(g):
    """
    Create a one-wide permimeter along the edges of the grid.
    """
    w, h = g.size()

    wi, hi = 0, 0
    while wi < w:  # Top
        g.put(wi, hi, False)
        wi += 1
    wi -= 1
    while hi < h:  # Right
        g.put(wi, hi, False)
        hi += 1

    wi, hi = 0, 0
    while hi < h:  # Left
        g.put(wi, hi, False)
        hi += 1
    hi -= 1
    while wi < w:  # Bottom
        g.put(wi, hi, False)
        wi += 1


def fill_group(g, x, y, sim):
    """
    Starting from the cell at "x" by "y", switch the states of all contiguous 
    cells with the same state as the starting cell. If "sim" is True, only 
    simulate a fill operation. Return a set containing the coordinates of cells 
    filled.
    """
    group = set()
    queue = []
    size = g.size()
    target = g.get(x, y)

    queue.append((x, y))
    while queue:
        if 0 <= queue[-1][0] < size[0] - 1 and 0 <= queue[-1][1] < size[1] - 1:
            cell = queue.pop(-1)
        else:
            queue.pop(-1)
            continue
        if g.get(*cell) == target and cell not in group:
            if not sim:
                g.put(*cell, val=(not target))
            group.add(cell)
            queue.append((cell[0] + 1, cell[1]))
            queue.append((cell[0] - 1, cell[1]))
            queue.append((cell[0], cell[1] + 1))
            queue.append((cell[0], cell[1] - 1))

    return group


def largest_group(g, closed, fill):
    """
    Return a set containing the largest contiguous group in the map of closed 
    cells if "closed" is True, open cells if False. Fill the smaller groups 
    with the opposite state if "fill" is True.
    """
    wi, hi = 0, 0
    w, h = g.size()
    cells = set()
    groups = []

    # Construct a set of the closed (or open) cells in the map.
    while wi < w - 1:
        while hi < h - 1:
            if closed:
                if g.get(wi, hi):
                    cells.add((wi, hi))
            else:
                if not g.get(wi, hi):
                    cells.add((wi, hi))
            hi += 1
        wi += 1
        hi = 0

    # Split cells into contiguous groups.
    while cells:
        groups.append(fill_group(g, *list(cells)[0], sim=True))
        for cell in groups[-1]:
            cells.remove(cell)

    # Find the largest group.
    l = set()
    for group in groups:
        if len(group) > len(l):
            l = group
    largest = l

    # Fill all smaller groups.
    if fill:
        for group in groups:
            if group != largest:
                fill_group(g, *list(group)[0], sim=False)

    return largest
