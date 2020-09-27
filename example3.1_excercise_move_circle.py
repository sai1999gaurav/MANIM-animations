from manimlib.imports import *

class MoveCircleExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        circle.shift(3*UP+3*RIGHT)
        square.shift(2*LEFT+2*DOWN)
        self.play(ShowCreation(circle), ShowCreation(square))
        self.wait(2) 

