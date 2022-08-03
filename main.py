from panda3d.core import CardMaker
from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cm = CardMaker("squares") # cm for card maker

        squares = self.aspect2d.attachNewNode('squares') 

        # Red Square on upper left quarter
        self.cm.setFrame(-1, 0, 1, 0)
        square = squares.attachNewNode(self.cm.generate())
        square.setColor(255,0,0,1)

        # Blue Square on upper right quarter
        self.cm.setFrame(0, 1, 1, 0)
        square = squares.attachNewNode(self.cm.generate())
        square.setColor(0,0,255,1)

        # Blue Square on lower left quarter
        self.cm.setFrame(-1, 0, 0, -1)
        square = squares.attachNewNode(self.cm.generate())
        square.setColor(0,0,255,1)

        # Red Square on lower right quarter
        self.cm.setFrame(0, 1, 0, -1)
        square = squares.attachNewNode(self.cm.generate())
        square.setColor(255,0,0,1)

app = App()
app.run()