from panda3d.core import CardMaker, NodePath
from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cm = CardMaker("squares") # cm for card maker
        self.cm.setFrame(-0.5,0.5,-0.5,0.5)

        myFrames = self.aspect2d.attachNewNode('frames')

        myFrame = myFrames.attachNewNode(self.cm.generate())
        myFrame.setColor(255,0,0,1)


app = App()
app.run()