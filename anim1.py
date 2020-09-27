from manimlib.imports import *
import numpy as np
#crude graph
class Scene1(GraphScene):
    CONFIG = {
    "x_min": -np.pi,
    "x_max": np.pi,
    "y_min": -1,
    "y_max": 1,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate = False)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        func_graph2 = self.get_graph(self.mygraph2, RED_E) 
        self.play(ShowCreation(func_graph))
        self.wait(2)
        self.play(ShowCreation(func_graph2), FadeOut(func_graph), run_time = 4)
        self.wait(2)
    def mygraph(self,x):
        return x
    def mygraph2(self,x):
        return x + 0.5*np.sin(8*x)
