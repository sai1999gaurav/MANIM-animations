from manimlib.imports import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.play(ShowCreation(circle))
        self.wait(2)
