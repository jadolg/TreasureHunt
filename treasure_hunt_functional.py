from exceptions import NoTreasureFoundException

get_cell = lambda cell, array: array[int(cell[0]) - 1][int(cell[1]) - 1]


def treasure_hunt(array, cell="11", visited=[]):
    if cell in visited:
        raise NoTreasureFoundException
    visited.append(cell)
    if cell == get_cell(cell, array):
        return visited
    return treasure_hunt(
        cell=get_cell(cell, array),
        visited=visited,
        array=array
    )
