class NoTreasureFoundException(Exception):
    pass


class TreasureHuntOO(object):

    def __init__(self, array):
        self.current = None
        self.array = array
        self.visited = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            self.current = "11"
        else:
            if self.array[int(self.current[0]) - 1][int(self.current[1]) - 1] == self.current:
                raise StopIteration

            self.current = self.array[int(self.current[0]) - 1][int(self.current[1]) - 1]

        if self.current not in self.visited:
            self.visited.append(self.current)
        else:
            raise NoTreasureFoundException

        return self.current
