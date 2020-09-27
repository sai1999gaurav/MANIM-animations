from manimlib.imports import *

class CreateBox(Scene):
    def construct(self):
        sq = Square() 
        self.play(ShowCreation(sq))
        self.wait(20)

