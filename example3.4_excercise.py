from manimlib.imports import *

class TwoOsculatingCircles(Scene):
    def construct(self):
        circle1 = Circle() # is-a relationship
        circle2 = Circle()
        # modify the code to transform circle2 into a square
        self.play(ShowCreation(circle1), ShowCreation(circle2))
        self.wait(2)

# try shifting the same square to the top ()

