from manimlib.imports import *
def pendulum_vector_field_func(coordinate):
    x,y = coordinate[:2]
    return np.array([
        x**3,
        y**2,
        0,
    ])
class InvertedPendulumEquation(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        vector_field = VectorField( pendulum_vector_field_func )
        self.add(vector_field)
        self.wait(2)