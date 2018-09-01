from exceptions import NoTreasureFoundException

get_cell = lambda cell, array: array[int(cell[0]) - 1][int(cell[1]) - 1]


def treasure_hunt_with_lambda(array, cell="11", visited=None):
    if not visited:
        visited = []
    if cell in visited:
        raise NoTreasureFoundException
    visited.append(cell)
    if cell == get_cell(cell, array):
        return visited
    return treasure_hunt_with_lambda(
        cell=get_cell(cell, array),
        visited=visited,
        array=array
    )


def make_cell_getter(array):
    def next_cell(cell):
        if cell == array[int(cell[0]) - 1][int(cell[1]) - 1]:
            return None
        else:
            return array[int(cell[0]) - 1][int(cell[1]) - 1]

    return next_cell


def treasure_hunt_with_closure(array, cell='11', visited=None):
    if not visited:
        visited = []
    get_cell_f = make_cell_getter(array)
    if cell not in visited:
        visited.append(cell)
        cell = get_cell_f(cell)
        if not cell:
            return visited
        else:
            return treasure_hunt_with_closure(array, cell, visited)
    else:
        raise NoTreasureFoundException
