class Cell:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile # will be changed to self.tile later
        self.choices = 0 # entropy, should be length of tileset by default 
    
    def show(self):
        self.square.show()

    def hide(self):
        self.square.hide()