class Cell:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile # will be changed to self.tile later
        self.choices = 0 # entropy, should be length of tileset by default 
    
    def show(self):
        self.tile.show()

    def hide(self):
        self.tile.hide()

    def __repr__(self):
        return f"({self.x}, {self.y})"