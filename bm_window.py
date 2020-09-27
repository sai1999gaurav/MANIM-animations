from manimlib.imports import *
import numpy as np
import cmath as cm
#import matplotlib.pyplot as plt
#crude graph
e = 1e-6
shift_f = 0.5 + np.pi
down_f = 1.8
dtft_size = 800
dtft_size_by_2 = 400
out_scale = 7
t_i_up = 2.5
t_i_side = 4.5
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
    "y_min": -7,
    "y_max": 17,
    "include_ticks": False,  # this boolean controls tick generation
    "tick_size": 0.1,
    "tick_frequency": 0,
    "y_axis_label": "$y$",
    "x_axis_label": "$\omega$",
    # Defaults to value near x_min s.t. 0 is a tick
    # TODO, rename this
    "leftmost_tick": None,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN + (down_f - 0.5)*DOWN,
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
        sentence.scale(0.7)
        self.play(Write(sentence))
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
        #window_conv
        w_length = 3
        rect_coords = self.rect_dtft_2(w_length)
        rect_pts = self.get_points_from_coords(rect_coords)
        rect_window_ft = DiscreteGraphFromSetPoints(rect_pts, color = BLUE)
        img_name = './images/bm_window' + str(w_length) + '.jpg'
        img = ImageMobject(img_name)
        img.scale(1.5)  # Resize to be twice as big
        img.shift((t_i_up-0.5)*UP + 1.4*(t_i_side-1)*RIGHT)  # Move the image
        self.play(ShowCreation(img), run_time = 1)  # Display the imag
        list1 = TexMobject(r"\text{which when convolved with}")
        list2 = TexMobject(r"\text{Blackman window}",r"\text{ N = }", str(w_length))
        list3 = TexMobject(r"\text{with DTFT:}")        
        list2.set_color_by_tex_to_color_map({
            "Blackman window": BLUE
        })
        sentence=VGroup(list1,list2,list3)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift(t_i_up*UP + t_i_side*LEFT)
        sentence.scale(0.7)
        self.play(Write(sentence))
        #list1 = TexMobject("$w[k] = 0.42 + 0.5cos($", "${2k \over 2}$", ")")
        #sentence2 = VGroup(list1)
        #sentence2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        #sentence2.shift(0.5*UP + (t_i_side+0.5)*LEFT)
        #sentence2.scale(0.7)
        #self.play(Write(sentence2), run_time = 0.5)
        self.play(ShowCreation(rect_window_ft), run_time = 2.5)
        self.play(FadeOut(sentence), run_time = 1)
        self.wait(2)
        self.play(FadeOut(rect_window_ft), run_time = 2)
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
        sentence.scale(0.7)
        self.play(Write(sentence))
        #CONVOLUTION
        rect_window_ft.shift(shift_f*LEFT)
        t_length = 50
        rect_window_ft.shift(shift_f*2*RIGHT/t_length)
        for i in range(1, t_length + 1):
            self.add(rect_window_ft)
            rect_window_ft.shift(shift_f*2*RIGHT/t_length)
            c_coords = conv_coords[0:int(i*(dtft_size/t_length))]
            c_pts = self.get_points_from_coords(c_coords)
            c_graph =DiscreteGraphFromSetPoints(c_pts, color = YELLOW) 
            c_graph_prev = c_graph
            self.add(c_graph)
            self.wait(0.1)
            if(i != t_length):
                self.remove(c_graph_prev)
        #FADEOUT
        self.play(FadeOut(rect_window_ft),run_time = 1)
        self.play(FadeOut(graph), run_time = 1)
        self.play(FadeOut(img), run_time = 1)
        self.wait(2)

        #increasing w_length
        self.play(FadeOut(sentence), run_time = 0.5)
        list1 = TexMobject(r"\text{Similarly,}")    
        sentence=VGroup(list1)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift(t_i_up*UP + t_i_side*LEFT)
        sentence.scale(0.7)
        self.play(Write(sentence))
        self.play(FadeOut(c_graph), run_time = 0.5)
        self.play(ShowCreation(graph), run_time = 0.5)
        w_length = w_length + 2
        rect_coords = self.rect_dtft_2(w_length)
        rect_pts = self.get_points_from_coords(rect_coords)
        rect_window_ft = DiscreteGraphFromSetPoints(rect_pts, color = BLUE)
        rect_window_ft_prev = rect_window_ft
        img_name = './images/bm_window' + str(w_length) + '.jpg'
        img = ImageMobject(img_name)
        img.scale(1.5)  # Resize to be twice as big
        img.shift((t_i_up-0.5)*UP + 1.4*(t_i_side-1)*RIGHT)  # Move the image
        self.play(ShowCreation(img), run_time = 0.5)  # Display the imag
        list1 = TexMobject(r"\text{Ideal Filter}",r"\text{ convolved with}")
        list2 = TexMobject(r"\text{Blackman window}", r"\text{ N = }", str(w_length))
        list3 = TexMobject(r"\text{with DTFT:}")
        list1.set_color_by_tex_to_color_map({
            "Ideal Filter": ORANGE
        })        
        list2.set_color_by_tex_to_color_map({
          "Blackman window": BLUE
        })
        self.play(FadeOut(sentence), run_time = 0.5)
        sentence=VGroup(list1,list2,list3)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift(t_i_up*UP + t_i_side*LEFT)
        sentence.scale(0.7)
        self.play(Write(sentence), run_time = 1)
        self.play(ShowCreation(rect_window_ft), run_time = 0.5)
        self.play(FadeOut(sentence), run_time = 0.5)
        self.wait(0.5)
        self.play(FadeOut(rect_window_ft), run_time = 0.5)
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
        sentence.scale(0.7)
        self.play(Write(sentence), run_time = 0.5)
        #CONVOLUTION
        rect_window_ft.shift(shift_f*LEFT)
        t_length = 50
        rect_window_ft.shift(shift_f*2*RIGHT/t_length)
        for i in range(1, t_length + 1):
            self.add(rect_window_ft)
            rect_window_ft.shift(shift_f*2*RIGHT/t_length)
            c_coords = conv_coords[0:int(i*(dtft_size/t_length))]
            c_pts = self.get_points_from_coords(c_coords)
            c_graph =DiscreteGraphFromSetPoints(c_pts, color = YELLOW) 
            c_graph_prev = c_graph
            self.add(c_graph)
            self.wait(0.07)
            if(i != t_length):
                self.remove(c_graph_prev)
        conv_output = c_graph
        #FADEOUT
        #self.play(FadeOut(rect_window_ft),run_time = 0.25)
        #self.play(FadeOut(graph), run_time = 0.25)
        self.play(FadeOut(img), run_time = 0.25)
        self.wait(1)
         #increasing w_length
        self.play(FadeOut(sentence), run_time = 0.5)
        list1 = TexMobject(r"\text{As the value of N increases,}")    
        sentence1=VGroup(list1)
        sentence1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence1.shift(t_i_up*UP + t_i_side*LEFT)
        sentence1.scale(0.7)
        self.play(Write(sentence1))
        #self.play(FadeOut(c_graph), run_time = 1)
        w_max = w_length + 2*4
        w_min = w_length + 2
        for w_length in range(w_min,(w_max + 1),2):
            #self.remove(c_graph)
            list1 = TexMobject(r"\text{N = }", str(w_length))    
            sentence=VGroup(list1)
            sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
            sentence.shift((t_i_up-1)*UP + t_i_side*LEFT)
            sentence.scale(0.7)
            self.play(Write(sentence))
            img_name = './images/bm_window' + str(w_length) + '.jpg'
            img = ImageMobject(img_name)
            img.scale(1.5)  # Resize to be twice as big
            img.shift((t_i_up-0.5)*UP + 1.4*(t_i_side-1)*RIGHT)  # Move the image
            self.play(ShowCreation(img), run_time = 0.25)  # Display the imag
            rect_coords = self.rect_dtft_2(w_length)
            rect_pts = self.get_points_from_coords(rect_coords)
            rect_window_ft = DiscreteGraphFromSetPoints(rect_pts, color = BLUE)
            self.play(Transform(rect_window_ft_prev, rect_window_ft), run_time = 0.5)
            conv_coords = self.convolution(coords, rect_coords)
            conv_pts = self.get_points_from_coords(conv_coords)
            conv_output =  DiscreteGraphFromSetPoints(conv_pts, color = YELLOW)
            self.play(Transform(c_graph_prev, conv_output), run_time = 0.75)
            self.play(FadeOut(img), run_time = 0.25)
            self.play(FadeOut(sentence), run_time = 0.25)
            self.wait(0.25)

        #Final Text 
        self.play(FadeOut(sentence1), run_time = 0.5)
        list1 = TexMobject(r"\text{The filter transition width}")
        list2 = TexMobject(r"\text{decreases with increasing N,}")
        list3 = TexMobject(r"\text{as main-lobe width decreases}")
        sentence=VGroup(list1,list2, list3)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift((t_i_up)*UP + t_i_side*LEFT)
        sentence.scale(0.7)
        self.play(Write(sentence))
        list1 = TexMobject(r"\text{Band Tolerances are very}")
        list2 = TexMobject(r"\text{large owing to significant}")
        list3 = TexMobject(r"\text{relative side-lobe area}")
        list4 = TexMobject(r"\text{area is very small}")
        sentence=VGroup(list1,list2, list3)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift((t_i_up)*UP + (t_i_side)*RIGHT)
        sentence.scale(0.7)
        self.play(Write(sentence))
        list1 = TexMobject("H_{FIR}", r"\text{ approaches towards}")
        list2 = TexMobject("H_{Ideal}",r"\text{ with increasing N}")
        list1.set_color_by_tex_to_color_map({
                "H_{FIR}": YELLOW
            })
        list2.set_color_by_tex_to_color_map({
                "H_{Ideal}": ORANGE
            })
        sentence=VGroup(list1,list2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        sentence.shift((t_i_up - 2.3)*UP + t_i_side*LEFT)
        #self.play(Write(sentence))


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
        Xi = [(0.42 + 0.5*np.cos(np.pi*i/N) + 0.08*np.cos(2*np.pi*i/N)) for i in range(-N,N+1)]
        X = np.fft.fft(Xi, dtft_size)
        X = np.fft.fftshift(X) + 0.11
        #X = np.roll(X,dtft_size_by_2)
        w=np.linspace(-np.pi,np.pi,dtft_size)
        coords = [[px,py] for px,py in zip(w,X)]
        #points = self.get_points_from_coords(coords)
        return coords
