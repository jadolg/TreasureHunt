class TreasureHuntOO(object):

    def __init__(self, array):
        self.current = None
        self.array = array

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            self.current = "11"
        else:
            if self.array[int(self.current[0]) - 1][int(self.current[1]) - 1] == self.current:
                raise StopIteration

            self.current = self.array[int(self.current[0]) - 1][int(self.current[1]) - 1]

        return self.current
