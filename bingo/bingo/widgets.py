from random import Random

content = range(30)

class BingoBoard(object):
    def __init__(self, name, state=None):
        self.random = Random(name)
        self.grid = self.random.sample(content, 25)
        self.grid[12] = 'Free Space'
        self.state = state or [(1,1), (2,2), (3,4)]

    @property
    def board(self):
        grid = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append([self.grid[i*5+j], 0])
            grid.append(row)

        for row, col in self.state:
            grid[row][col][1] = 1

        return grid

    def click(row, col):
        self.state[row][col][1] = 1
