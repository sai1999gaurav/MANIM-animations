from manimlib.imports import *
class SimpleNonLinearTransform(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        self.play(ShowCreation(grid))
        self.play(FadeIn(circle))
        self.wait(2)
        nonLinear_Transform = lambda coordinate: coordinate + np.array([np.sin(coordinate[0])**2, np.sin(coordinate[1]**3),0])
        grid.prepare_for_nonlinear_transform()  #for curves
        self.play(grid.apply_function, nonLinear_Transform,
                  circle.apply_function, nonLinear_Transform, run_time=1)
        self.wait(2)
