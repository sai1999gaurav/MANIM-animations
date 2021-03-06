from manimlib.imports import *
import numpy as np
import cmath as cm
#import matplotlib.pyplot as plt
#crude graph
e = 1e-6
shift_f = 0.5 + np.pi
down_f = 1.5
dtft_size = 200
dtft_size_by_2 = 100
out_scale = 16
t_i_up = 2.5
t_i_side = 3.5
class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }",r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class Scene3(GraphScene):
    CONFIG = {
    "x_min": -4,
    "x_max": 4,
    "y_min": -5,
    "y_max": 15,
    "include_ticks": False,  # this boolean controls tick generation
    "tick_size": 0.1,
    "tick_frequency": 0,
    # Defaults to value near x_min s.t. 0 is a tick
    # TODO, rename this
    "leftmost_tick": None,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN + DOWN,
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
        self.play(ShowCreation(one_pi),ShowCreation(minus_one_pi),ShowCreation(half_pi),ShowCreation(minus_half_pi), run_time = 0.5)
        list1 = TexMobject(r"\text{Consider an Ideal Filter }")
        list2 = TexMobject("H_{Ideal}", r"\text{ with }", " w_{c} = \\pi/2 ")        
        list2.set_color_by_tex_to_color_map({
            "H_{Ideal}": ORANGE
        })
        sentence=VGroup(list1,list2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift(t_i_up*UP + t_i_side*LEFT)
        self.play(Write(sentence))
        #self.play(Write(list1), color = ORANGE)
        x = np.linspace(-np.pi, np.pi, dtft_size)
        y = np.zeros(dtft_size)
        for i in range (0,dtft_size):
            if(x[i] > -np.pi/2 and x[i] < np.pi/2):
                y[i] = 5
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        graph = DiscreteGraphFromSetPoints(points, color = ORANGE)
        #label_coord = self.input_to_graph_point(TAU,graph) 
        self.play(ShowCreation(graph), run_time = 3)
        self.play(FadeOut(sentence), run_time = 1)
        self.wait(2)
        rect_coords = self.rect_dtft_2(7)
        rect_pts = self.get_points_from_coords(rect_coords)
        rect_window_ft = DiscreteGraphFromSetPoints(rect_pts, color = BLUE)
        img = ImageMobject('./images/rect_window7.jpg')
        img.scale(1.5)  # Resize to be twice as big
        img.shift(t_i_up*UP + t_i_side*RIGHT)  # Move the image
        self.play(ShowCreation(img), run_time = 1)  # Display the imag
        list1 = TexMobject(r"\text{which when convolved with}")
        list2 = TexMobject(r"\text{rectangular window, N = 7}")
        list3 = TexMobject(r"\text{with DTFT:}")        
        list2.set_color_by_tex_to_color_map({
            "rectangular window": BLUE
        })
        sentence=VGroup(list1,list2,list3)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift(t_i_up*UP + t_i_side*LEFT)
        self.play(Write(sentence))
        self.play(ShowCreation(rect_window_ft), run_time = 2.5)
        self.play(FadeOut(sentence), run_time = 1)
        self.wait(2)
        self.play(FadeOut(rect_window_ft), run_time = 1)
        conv_coords = self.convolution(coords, rect_coords)
        conv_pts = self.get_points_from_coords(conv_coords)
        conv_output =  DiscreteGraphFromSetPoints(conv_pts, color = YELLOW)
        list1 = TexMobject(r"\text{Gives the FIR filter}")
        list2 = TexMobject(r"\text{response }", "H_{FIR}")   
        list2.set_color_by_tex_to_color_map({
            "H_{FIR}": YELLOW
        })
        sentence=VGroup(list1,list2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift(t_i_up*UP + t_i_side*LEFT)
        self.play(Write(sentence))
        rect_window_ft.shift(shift_f*LEFT)
        t_length = 50
        #self.play(ShowCreation(rect_window_ft), run_time = 0.04)
        #conv_coords = np.array(conv_coords)
        rect_window_ft.shift(shift_f*2*RIGHT/t_length)
        for i in range(1, t_length + 1):
            self.add(rect_window_ft)
            rect_window_ft.shift(shift_f*2*RIGHT/t_length)
            c_coords = conv_coords[0:int(i*(dtft_size/t_length))]
            c_pts = self.get_points_from_coords(c_coords)
            c_graph =DiscreteGraphFromSetPoints(c_pts, color = YELLOW) 
            self.add(c_graph)
            self.wait(0.1)

        #    self.play(ShowCreation(rect_window_ft), run_time = 0.04)
        #    self.wait(0.04)
        #    self.play(FadeOut(rect_window_ft), run_time = 0.04)
        #self.play(ShowCreation(conv_output),FadeOut(rect_window_ft),run_time = 3)
        self.play(FadeOut(rect_window_ft),run_time = 2)
        self.play(FadeOut(graph), run_time = 1.5)
        self.wait(2)

    def convolution(self, coords, rect_coords):
        coords = np.array(coords)
        rect_coords = np.array(rect_coords)
        x = np.linspace(-np.pi, np.pi, dtft_size)
        y = np.zeros(dtft_size)
        for i in range(0,dtft_size):
            if (i < dtft_size_by_2):
                for j in range(0,dtft_size_by_2+i):
                    y[i] = y[i] + (coords[j][1]*rect_coords[dtft_size_by_2-i+j][1])
            else:
                for j in range(i-dtft_size_by_2, dtft_size):
                    y[i] = y[i] + (coords[j][1]*rect_coords[dtft_size_by_2-i+j][1])
            y[i] = y[i]/(2*np.pi)
        y =y/out_scale
        coords = [[px,py] for px,py in zip(x,y)]
        #points = self.get_points_from_coords(coords)
        return coords


    def convolution2(self, coords, rect_coords):
        coords = np.array(coords)
        rect_coords = np.array(rect_coords)
        x1 = coords[:,1]
        x2 = rect_coords[:,1]
        y = np.convolve(x1,x2)
        y_out = y[len(y) - dtft_size_by_2: len(y) + dtft_size_by_2+1:1]
        x = np.linspace(-np.pi, np.pi, dtft_size)
        coords = [[px,py] for px,py in zip(x,y_out)]
        return coords
        #return points

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
        #points = self.get_points_from_coords(coords)
        return coords

    def rect_dtft_2(self,N):
        Xi = [1 for i in range(-N,N+1)]
        X = np.fft.fft(Xi, dtft_size)
        X = np.fft.fftshift(X) - 0.5
        #X = np.roll(X,dtft_size_by_2)
        w=np.linspace(-np.pi,np.pi,dtft_size)
        coords = [[px,py] for px,py in zip(w,X)]
        #points = self.get_points_from_coords(coords)
        return coords
