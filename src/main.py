from grid import Grid
from json import load
from __getpath import getPath

print(__file__.split())
# constants
DIM   = (11, 11) # rows, cols
RULES = load(open(f"{getPath(2)}/tiles/rules.json", "r"))


class App:
    def __init__(self):
        
        self.grid = Grid(DIM, RULES)
        self.grid.generate()

        # self.grid.grid[1].hide()
        self.grid[1].hide()

        cell = self.grid[1,1]
        ng = self.grid.get_neighbours(cell)
        # print(ng)
        # ng[0].hide()
        

    def run(self): # Need to find a better way
        self.grid.run()

app = App()
app.run()