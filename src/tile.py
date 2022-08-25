from __getpath import getPath

class Tile:
    TILESET = "pipes" # for later when we have multiple tilesets and need to chose
    def __init__(self, name, *edges):
        self.LEFT, self.RIGHT, self.BOTTOM, self.TOP = edges
        self.IMG = f"{getPath(2)}/tiles/{name}.png"