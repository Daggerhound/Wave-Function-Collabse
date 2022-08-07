from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, Vec4
from cell import Cell

# constants
BLUE  = (0  , 0, 255, 1) # RGBA
RED   = (255, 0,   0, 1) # RGBA


class Grid(ShowBase):
    def __init__(self, dim):
        ShowBase.__init__(self)
        self.dim = dim
        
        self.cm = CardMaker("grid")
        self.tiles = self.aspect2d.attachNewNode('squares') 
        self.grid = []

    def __getitem__(self, *indexes):
        match len(indexes):
            case 1: # self[10]
                return self.grid[indexes[0]]
            case 2: # self[2][5]
                return self.grid[indexes[0] + self.dim[1] * indexes[1]]
            case length:
                if length <= 0:
                    raise IndexError("[ERROR] Amount of indexes given insufficient.")
                raise IndexError("[ERROR] Too many indexes given.")

    def make_tile(self, framing, texture):
        self.cm.setFrame(framing)
        tile = self.tiles.attachNewNode(self.cm.generate())
        tile.setTexture(texture)
        return tile

    def generate(self):
        width  = 2 # abs length from left to right
        height = 2 # abs height from up to down

        cx =  width/self.dim[0] # Needs better name
        cy = height/self.dim[1] # Needs better name

        blank = self.loader.loadTexture("../tiles/blank.png")

        toggle = False
        for resY in range(self.dim[1]):
            for resX in range(self.dim[0]):
                left   = -1 + cx * resX
                right  = -1 + cx * (resX + 1)
                bottom =  1 - cy * (resY + 1)
                top    =  1 - cy * resY
                
                framing = Vec4(left, right, bottom, top)

                tile = self.make_tile(framing, blank)
                cell = Cell(resX, resY, tile)
                self.grid.append(cell)

                toggle = not toggle

            if self.dim[0] % 2 == 0:
                toggle = not resY%2