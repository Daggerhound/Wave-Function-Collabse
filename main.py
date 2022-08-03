from panda3d.core import CardMaker, NodePath
from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cm = CardMaker("squares") # cm for card maker
        self.cm.setFrame(-0.5,0.5,-0.5,0.5) # sets size

        squares = self.aspect2d.attachNewNode('squares') 

        square = squares.attachNewNode(self.cm.generate())
        square.setColor(255,0,0,1)


app = App()
app.run()