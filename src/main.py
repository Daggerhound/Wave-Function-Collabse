from grid import Grid


# constants
DIM   = (11, 11) # rows, cols


class App:
    def __init__(self):
        self.grid = Grid(DIM)
        self.grid.generate()

    def run(self): # Need to find a better way
        self.grid.run()

app = App()
app.run()