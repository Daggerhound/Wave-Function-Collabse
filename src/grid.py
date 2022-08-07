from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, Vec4
from cell import Cell
from tile import Tile
import numpy as np

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

    def __getitem__(self, indexes):
        if isinstance(indexes, int):
            return self.grid[indexes]
        elif isinstance(indexes, tuple):
            return self.grid[indexes[0] + self.dim[1] * indexes[1]]
        else:
            raise TypeError(f"[ERROR] Type {type(indexes)} not supported for indexing grid.")

    def make_tile(self, framing, texture):
        self.cm.setFrame(framing)
        tile = self.tiles.attachNewNode(self.cm.generate())
        tile.setTexture(texture)
        return tile

    def get_neighbours(self, cell):
        x = cell.x
        y = cell.y

        left = self[x-1,y]
        right = self[x+1,y]
        top = self[x,y-1]
        bot = self[x,y+1]

        return [left, right, top, bot]


    def generate(self):
        Tile.WIDTH  = 2/self.dim[0] # 2 being the absolute length of screen
        Tile.HEIGHT = 2/self.dim[1] # 2 being the absolute height of screen

        blank = self.loader.loadTexture("../tiles/blank.png")
            
        for j, y in enumerate(np.arange(1, -1, -Tile.HEIGHT)):
            for i, x in enumerate(np.arange(-1, 1, Tile.WIDTH)):
                framing = Vec4(x, x + Tile.WIDTH, y - Tile.HEIGHT, y)
                tile = self.make_tile(framing, blank)
                cell = Cell(i, j, tile)
                self.grid.append(cell)