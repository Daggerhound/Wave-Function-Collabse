from grid import Grid


# constants
DIM   = (11, 11) # rows, cols


class App:
    def __init__(self):
        self.grid = Grid(DIM)
        self.grid.generate()

        # self.grid.grid[1].hide()
        # self.grid[1].hide()

        cell = self.grid[1,1]
        ng = self.grid.get_neighbours(cell)
        # print(ng)
        # ng[0].hide()
        

    def run(self): # Need to find a better way
        self.grid.run()

app = App()
app.run()