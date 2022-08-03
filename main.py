from panda3d.core import CardMaker
from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cm = CardMaker("squares") # cm for card maker

        self.squares = self.aspect2d.attachNewNode('squares') 

        res = [5,5] # [x,y]
        x = 2 # abs lenght from left to right
        y = 2 # abs heigh from up to down

        cx = x/res[0]
        cy = y/res[1]
        toggle = False
        for resY in range(res[1]):
            for resX in range(res[0]):
                left = -1 + cx*resX
                right = -1 + cx*(resX+1)
                bot = -1 + cy*(resY+1)
                top = -1 + cy*resY
                
                if toggle:
                    self.blue_square(left, right, bot, top)
                else:
                    self.red_square(left, right, bot, top)
                
                toggle = not toggle
                print(toggle)

        

    def blue_square(self,left, right, bot, top):
        self.cm.setFrame(left, right, bot, top)
        self.square = self.squares.attachNewNode(self.cm.generate())
        self.square.setColor(0,0,255,1)

    def red_square(self,left, right, bot, top):
        self.cm.setFrame(left, right, bot, top)
        self.square = self.squares.attachNewNode(self.cm.generate())
        self.square.setColor(255,0,0,1)


app = App()
app.run()