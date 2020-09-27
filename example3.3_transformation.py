from manimlib.imports import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle()
        sq = Square()
        tr = Triangle()
        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(ReplacementTransform(circle, sq))
        self.play(ReplacementTransform(sq, tr))
        self.wait(2)
       
