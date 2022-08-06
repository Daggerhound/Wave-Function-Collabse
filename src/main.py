from grid import Grid


# constants
RES   = (11, 11) # rows, cols


class App:
    def __init__(self):
        self.grid = Grid(RES)
        self.grid.generate()

    def run(self): # Need to find a better way
        self.grid.run()

app = App()
app.run()