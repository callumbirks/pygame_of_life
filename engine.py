# This is the engine for Conway's Game of Life simulation
# No storing of state here, caller will need to provide grid size and the current list of alive cells
# A cell is simply represented by an integer which denotes its position in the grid
# Position index advances from the top left which is 0, left-to-right, until the bottom right which is (size^2 - 1)

from funcy import *


def step(size: int, alive_cells_prev: frozenset):
    def will_live(cell: int):
        my_neighbours = [cell - size - 1, cell - size, cell - size + 1,
                         cell - 1, cell + 1,
                         cell + size - 1, cell + size, cell + size + 1]
        neighbour_count = len(select(lambda p: p in alive_cells_prev, my_neighbours))
        return True if neighbour_count == 3 or cell in alive_cells_prev and neighbour_count == 2 else False

    return select(will_live, frozenset(range(0, size * size)))
