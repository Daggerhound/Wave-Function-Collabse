from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, Vec4
from cell import Cell

# constants
BLUE  = (0  , 0, 255, 1) # RGBA
RED   = (255, 0,   0, 1) # RGBA


class Grid(ShowBase):
    def __init__(self, res):
        ShowBase.__init__(self)
        self.res = res
        
        self.cm = CardMaker("grid")
        self.squares = self.aspect2d.attachNewNode('squares') 
        self.grid = []

    def __getitem__(self, *indexes):
        match len(indexes):
            case 1: # self[10]
                return self.grid[indexes[0]]
            case 2: # self[2][5]
                return self.grid[indexes[0] * indexes[1]]
            case length:
                if length <= 0:
                    raise IndexError("[ERROR] Amount of indexes given insufficient.")
                raise IndexError("[ERROR] Too many indexes given.")

    def add_square(self, framing, color):
        self.cm.setFrame(framing)
        square = self.squares.attachNewNode(self.cm.generate())
        square.setColor(color)
        return square

    def generate(self):
        width  = 2 # abs length from left to right
        height = 2 # abs height from up to down

        cx =  width/self.res[0] # Needs better name
        cy = height/self.res[1] # Needs better name

        toggle = False
        for resY in range(self.res[1]):
            for resX in range(self.res[0]):
                left   = -1 + cx * resX
                right  = -1 + cx * (resX + 1)
                bottom = -1 + cy * (resY + 1)
                top    = -1 + cy * resY
                
                framing = Vec4(left, right, bottom, top)

                square = self.add_square(framing, [RED, BLUE][toggle])
                cell = Cell(resX, resY, square)
                self.grid.append(cell)

                toggle = not toggle

            if self.res[0] % 2 == 0:
                toggle = not resY%2