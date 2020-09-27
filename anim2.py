from manimlib.imports import *
import numpy as np
import cmath as cm
#import matplotlib.pyplot as plt
#crude graph
e = 1e-6
shift_f = 0.5 + np.pi
down_f = 0.5
dtft_size = 100
dtft_size_by_2 = 50
class Scene1(GraphScene):
    CONFIG = {
    "x_min": -4,
    "x_max": 4,
    "y_min": -1,
    "y_max": 1,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate = False)
        func_graph = self.get_graph(self.mygraph2, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        func_graph1 = self.get_graph(self.mygraph1, RED_E) 
        self.play(ShowCreation(func_graph), run_time = 4)
        self.wait(2)
        #self.play(ShowCreation(func_graph1), FadeOut(func_graph), run_time = 4)
        #self.wait(2)
    def mygraph(self,x):
        if (abs(x) <= 0.5*np.pi):
            y = 1
        else:
            y = 0
        return y
    def mygraph1(self,x):
        return np.heaviside(x + np.pi/2, 1) - np.heaviside(x - np.pi/2, 1)

class Scene2(GraphScene):
    CONFIG = {
    "x_min": -4,
    "x_max": 4,
    "y_min": -2,
    "y_max": 2,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate = False)
        one_pi = TexMobject("\\pi")
        one_pi.shift(shift_f*RIGHT+down_f*DOWN)
        minus_one_pi = TexMobject("-\\pi")
        minus_one_pi.shift(shift_f*LEFT+down_f*DOWN)
        half_pi = TexMobject("\\pi/2")
        half_pi.shift(0.5*shift_f*RIGHT+down_f*DOWN)
        minus_half_pi = TexMobject("-\\pi/2")
        minus_half_pi.shift(0.5*shift_f*LEFT+down_f*DOWN)
        self.play(ShowCreation(one_pi),ShowCreation(minus_one_pi),ShowCreation(half_pi),ShowCreation(minus_half_pi))
        x = [-np.pi,-np.pi/2 - e, -np.pi/2,0,np.pi/2, np.pi/2+e, np.pi]
        y = [0,0, 1, 1, 1,0, 0]
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        graph = DiscreteGraphFromSetPoints(points, color = ORANGE)
        #label_coord = self.input_to_graph_point(TAU,graph)
        self.play(ShowCreation(graph), run_time = 3)
        self.wait(2)
    def get_points_from_coords(self,coords):
        return [self.coords_to_point(px,py)
            for px,py in coords
            ]
class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)


class Scene3(GraphScene):
    CONFIG = {
    "x_min": -4,
    "x_max": 4,
    "y_min": -5,
    "y_max": 5,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate = False)
        one_pi = TexMobject("\\pi")
        one_pi.shift(shift_f*RIGHT+down_f*DOWN)
        minus_one_pi = TexMobject("-\\pi")
        minus_one_pi.shift(shift_f*LEFT+down_f*DOWN)
        half_pi = TexMobject("\\pi/2")
        half_pi.shift(0.5*shift_f*RIGHT+down_f*DOWN)
        minus_half_pi = TexMobject("-\\pi/2")
        minus_half_pi.shift(0.5*shift_f*LEFT+down_f*DOWN)
        self.play(ShowCreation(one_pi),ShowCreation(minus_one_pi),ShowCreation(half_pi),ShowCreation(minus_half_pi))
        x = [-np.pi,-np.pi/2 - e, -np.pi/2,0,np.pi/2, np.pi/2+e, np.pi]
        y = [0,0, 3, 3, 3,0, 0]
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        graph = DiscreteGraphFromSetPoints(points, color = ORANGE)
        #label_coord = self.input_to_graph_point(TAU,graph) 
        self.play(ShowCreation(graph), run_time = 3)
        self.wait(2)
        rect_pts = self.rect_dtft_2(3)
        rect_window_ft = DiscreteGraphFromSetPoints(rect_pts, color = YELLOW)
        self.play(ShowCreation(rect_window_ft), run_time = 3)
        self.wait(2)

    def get_points_from_coords(self,coords):
        return [self.coords_to_point(px,py)
            for px,py in coords
            ]

    def rect_dtft(self,N): #Magnitude Spectrum
        j=cm.sqrt(-1)
        X=[]
        n = np.linspace(-N, N, 1)
        w=np.linspace(-np.pi,np.pi,100)
        for i in range(0,100):
            w_tmp=w[i]
            X_tmp=0
            for k in range(0,len(n)):
                X_tmp+=(1*np.exp(-n[k]*w_tmp*j))       
            X.append((X_tmp))
        coords = [[px,py] for px,py in zip(w,X)]
        points = self.get_points_from_coords(coords)
        return points

    def rect_dtft_2(self,N):
        Xi = [1 for i in range(-N,N+1)]
        X = np.fft.fft(Xi, dtft_size)
        X = np.fft.fftshift(X) - 0.5
        #X = np.roll(X,dtft_size_by_2)
        w=np.linspace(-np.pi,np.pi,dtft_size)
        coords = [[px,py] for px,py in zip(w,X)]
        points = self.get_points_from_coords(coords)
        return points


