from manimlib.imports import *
import numpy as np
import cmath as cm
from math import*

x_lim = 5
y_lim = 5
x_wid = (2*x_lim + 1)/2
y_wid = (2*y_lim + 1)/2
t_i_up = 3
t_i_side = 3
class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)



class Scene3(GraphScene):
    CONFIG = {
    "x_min": -1*x_lim,
    "x_max": x_lim,
    "y_min": -1*y_lim,
    "y_max": y_lim,
    "x_axis_width": x_wid,
    "y_axis_height": y_wid,
    "include_ticks": False,  # this boolean controls tick generation
    #"tick_size": 0.1,
    "tick_frequency": 0,
    "y_axis_label": "$\Omega$",
    "x_axis_label": "$\Sigma$",
    # Defaults to value near x_min s.t. 0 is a tick
    # TODO, rename this
    #"leftmost_tick": None,
    #"x_labeled_nums": range(-4, 4),
    #"y_labeled_nums": range(-5,6),
    "graph_origin": ORIGIN,
    }
    def construct(self):
    	#Initial text
    	list1 = TexMobject(r"\text{Locating the poles of}")
    	list1.scale(0.75)
    	list2 = TexMobject("N^{th}", r"\text{-Order, magnitude squared response}")
    	list2.scale(0.75)
    	list3 = TexMobject(r"\text{of }", r"\text{Chebyschev}", r"\text{ filter}")   
    	list3.scale(0.75)     
    	list3.set_color_by_tex_to_color_map({
        	"Chebyschev": ORANGE
    	})
    	sentence=VGroup(list1,list2, list3)
    	sentence.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence.shift(t_i_up*UP)
    	self.play(Write(sentence), run_time = 1.5)
    	self.wait(1)

    	list1 = TexMobject(r"\text{Poles, }", "s_{k} = \\Omega_p.sin(A_k)sinh(B) + j\\Omega_p.cos(A_k)cosh(B)")
    	list1.scale(0.65)
    	list1.set_color_by_tex_to_color_map({
    		"s_{k} = \\Omega_p.sin(A_k)sinh(B) + j\\Omega_p.cos(A_k)cosh(B)": YELLOW
    		})
    	list2 = TexMobject(r"\text{where }", "A_k = (2k+1)", "{\\pi\\over2N}", " , B = ", "{1 \\over N}", "sinh^{-1}", "\\Big(", "{1 \\over \\epsilon}", "\\Big)")
    	list2.scale(0.65)
    	list3 = TexMobject(r"\text{ and k spans over 2N consecutive integers}")
    	list3.scale(0.65)
    	sentence1=VGroup(list1,list2, list3)
    	sentence1.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence1.shift(0.5*UP)
    	self.play(Write(sentence1), run_time = 1.5)
    	self.wait(1)

    	list1 = TexMobject(r"\text{With }", "s_{k} = \\Sigma_k + j\\Omega_k", r"\text{, the poles lie on an ellipse, given by:}")
    	list1.scale(0.65)
    	list1.set_color_by_tex_to_color_map({
    		"s_{k} = \\Sigma_k + j\\Omega_k": YELLOW
    		})
    	eq1 = TexMobject("\\Big(", "{\\Sigma_k \\over \\Omega_psinh(B)}", "\\Big)^2", " + ", "\\Big(", "{\\Omega_k \\over \\Omega_pcosh(B)}", "\\Big)^2", " = 1").set_color(GREEN)
    	eq1.scale(0.65)
    	sentence2=VGroup(list1,eq1)
    	sentence2.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence2.shift(-2.5*UP)
    	self.play(Write(sentence2), run_time = 1.5)
    	self.wait(2)
    	self.play(FadeOut(sentence),FadeOut(sentence1), FadeOut(sentence2), run_time = 1)
    	
    	eq1.shift(6*UP + 4*LEFT)
    	self.play(FadeIn(eq1), run_time = 0.1)
    	self.setup_axes(animate = False)
    	#Circle
    	list1 = TexMobject(r"\text{Consider a circle of}")
    	list1.scale(0.6)
    	list2 = TexMobject(r"\text{radius }", "\\Omega_psinh(B)")
    	list2.scale(0.6)
    	list2.set_color_by_tex_to_color_map({
    		"\\Omega_psinh(B)": BLUE
    		})
    	sentence = VGroup(list1, list2)
    	sentence.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence.shift(2.5*UP + 4.5*RIGHT)
    	self.play(Write(sentence), run_time = 1)
    	circle_i = Circle(color = BLUE, radius = 0.55)
    	self.play(ShowCreation(circle_i), run_time = 1)
    	self.play(FadeOut(sentence), run_time = 0.5)

    	list1 = TexMobject(r"\text{Consider another circle of}")
    	list1.scale(0.6)
    	list2 = TexMobject(r"\text{radius }", "\\Omega_pcosh(B)")
    	list2.scale(0.6)
    	list2.set_color_by_tex_to_color_map({
    		"\\Omega_pcosh(B)": ORANGE
    		})
    	sentence = VGroup(list1, list2)
    	sentence.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence.shift(2.5*UP + 4.5*RIGHT)
    	self.play(Write(sentence), run_time = 1)
    	circle_o = Circle(color = ORANGE, radius = 1.65)
    	self.play(ShowCreation(circle_o), run_time = 1)
    	self.play(FadeOut(sentence), run_time = 0.5)
    	self.wait(0.5)

    	list1 = TexMobject(r"\text{The}", r"\text{ ellipse }", r"\text{is then constructed}")
    	list1.set_color_by_tex_to_color_map({
    		r"\text{ ellipse }": GREEN
    		})
    	list1.scale(0.6)
    	sentence = VGroup(list1)
    	sentence.shift(2.5*UP + 4.5*RIGHT)
    	self.play(Write(sentence), run_time = 1)

    	list1 = TexMobject(r"\text{The y-axis is the major axis}")
    	list1.scale(0.6)
    	list2 = TexMobject(r"\text{because for real B, }", "cosh(B) > sinh(B)")
    	list2.scale(0.6)
    	list3 = TexMobject(r"\text{and }", "cosh^2(B) = 1 + sinh^2(B)")
    	list3.scale(0.6)
    	sentence1 = VGroup(list1, list2, list3)
    	sentence1.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence1.shift(2.5*DOWN + 4*LEFT)
    	self.play(Write(sentence1), run_time = 1.5)
    	#self.wait(1)
    	
    	dtft_size = 100
    	e_min = 1
    	e_max = 3
    	x = np.linspace(-1*e_min, e_min, dtft_size)
    	y_p = np.zeros(dtft_size)
    	y_n = np.zeros(dtft_size)
    	for i in range (0,dtft_size):
    		y_p[i] = e_max*sqrt(1 - (x[i]/e_min)**2)
    		y_n[i] = -1*e_max*sqrt(1 - (x[i]/e_min)**2)
    	coords_p = [[px,py] for px,py in zip(x,y_p)]
    	coords_n = [[px,py] for px,py in zip(x,y_n)]
    	points_p = self.get_points_from_coords(coords_p)
    	graph_p = DiscreteGraphFromSetPoints(points_p, color = GREEN)
    	points_n = self.get_points_from_coords(coords_n)
    	graph_n = DiscreteGraphFromSetPoints(points_n, color = GREEN)
    	#label_coord = self.input_to_graph_point(TAU,graph) 
    	self.play(ShowCreation(graph_p), ShowCreation(graph_n), run_time = 2)
    	self.wait(1)
    	self.play(FadeOut(sentence), FadeOut(sentence1), run_time = 1)


    	txt1 = TexMobject(r"\text {Consider a }", "4^{th}", r"\text{ order filter}")
    	txt1.scale(0.6)
    	txt1.shift(2*UP + 4*LEFT)
    	self.play(Write(txt1), run_time = 0.5)
    	self.wait(1)
    	self.play(FadeOut(txt1), run_time = 0.5)

    	#poles
    	#Pole 0
    	list1 = TexMobject(r"\text{The }", r"\text{inner circle}", r"\text{ is used to mark}" )
    	list1.scale(0.6)
    	list1.set_color_by_tex_to_color_map({
    		r"\text{inner circle}": BLUE
    		})
    	list2 = TexMobject(r"\text{the real part }", "\\Sigma_k", " = -sin(A_k)\\Omega_psinh(B)")
    	list2.scale(0.6)
    	list2.set_color_by_tex_to_color_map({
    		"\\Sigma_k": RED
    		})
    	sentence = VGroup(list1, list2)
    	sentence.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence.shift(3*UP + 4.5*RIGHT)
    	self.play(Write(sentence), run_time = 2.5)
    	list1 = TexMobject(r"\text{The }", r"\text{outer circle}", r"\text{ is used to mark}" )
    	list1.scale(0.6)
    	list1.set_color_by_tex_to_color_map({
    		r"\text{outer circle}": ORANGE
    		})
    	list2 = TexMobject(r"\text{the imag. part }", "\\Omega_k", " = cos(A_k)\\Omega_pcosh(B)")
    	list2.scale(0.6)
    	list2.set_color_by_tex_to_color_map({
    		"\\Omega_k": PURPLE
    		})
    	sentence1 = VGroup(list1, list2)
    	sentence1.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence1.shift(1.5*UP + 4.5*RIGHT)
    	self.play(Write(sentence1), run_time = 2.5)

    	list1 = TexMobject(r"\text{Consider the pole with k = 0}")
    	list1.scale(0.6)
    	list2 = TexMobject("\\Sigma_0", " = -sin(A_0)", "\\Omega_psinh(B)")
    	list2.scale(0.6)
    	list2.set_color_by_tex_to_color_map({
    		"\\Sigma_0": RED
    		})
    	list3 = TexMobject("\\Omega_0", " = cos(A_0)", "\\Omega_pcosh(B)")
    	list3.scale(0.6)
    	list3.set_color_by_tex_to_color_map({
    		"\\Omega_0": PURPLE
    		})
    	list4 = TexMobject(r"\text{where}", "A_0 = (2*(0) + 1)", "{\\pi \\over 2*4}", " = ", "{\\pi \\over 8}")
    	list4.scale(0.6)
    	sentence2 = VGroup(list1, list2, list3, list4)
    	sentence2.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence2.shift(1.5*DOWN + 4.5*RIGHT)
    	self.play(Write(sentence2), run_time = 3)


    	#Draw line
    	dtft_size = 100
    	x_max = e_max*cos(pi/2 + pi/8)
    	x = np.linspace(0, x_max, dtft_size)
    	y_max = e_max*sin(pi/2 + pi/8)
    	y = np.linspace(0, y_max, dtft_size)
    	coords = [[px,py] for px,py in zip(x,y)]
    	points = self.get_points_from_coords(coords)
    	lin_0 = DiscreteGraphFromSetPoints(points)
    	self.play(ShowCreation(lin_0), run_time = 2)

    	#ARC
    	#poly = CurvedDoubleArrow(np.array([1,0,0]),np.array([1,2,0]),color="#33FF33",fill_color="#FFFF00",fill_opacity=1)
    	sc = 1.5
    	poly  = CurvedArrow(start_point=np.array([0,e_max/sc,0]),end_point=np.array([x_max/sc,y_max/sc,0]),angle=pi/8)
    	self.play(ShowCreation(poly), run_time = 1)
    	self.wait(1)

    	list1 = TexMobject(r"\text{Since, y-axis is the major axis,}")
    	list1.scale(0.6)
    	list2 = TexMobject(r"\text{angle is measured from y-axis}")
    	list2.scale(0.6)
    	sentence3 = VGroup(list1, list2)
    	sentence3.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence3.shift(1.5*DOWN + 4*LEFT)
    	self.play(Write(sentence3), run_time = 1.5)

    	#poles
    	sc = 1.8
    	x = e_min*cos(pi/2 + pi/8)/sc
    	y = e_min*sin(pi/2 + pi/8)/sc#*np.linspace(1,2,1)
    	circle_rp0 = Circle(color = RED, radius = 0.02)
    	circle_rp0.shift(y*UP + x*RIGHT)
    	self.play(ShowCreation(circle_rp0), run_time = 0.5)
    	#self.play(FadeOut(rl_0), run_time = 0.5)
    	#self.wait(1)
    	#self.play(FadeOut(sentence), FadeOut(sentence1), run_time = 0.5)


    	sc = 1.81
    	x = e_max*cos(pi/2 + pi/8)/sc
    	y = e_max*sin(pi/2 + pi/8)/sc#*np.linspace(1,2,1)
    	circle_ip0 = Circle(color = PURPLE, radius = 0.02)
    	circle_ip0.shift(y*UP + x*RIGHT)
    	self.play(ShowCreation(circle_ip0), run_time = 0.5)
    	self.play(FadeOut(lin_0), FadeOut(poly), run_time = 0.5)
    	self.wait(1)
    	self.play(FadeOut(sentence), FadeOut(sentence1), FadeOut(sentence2), FadeOut(sentence3), run_time = 2)

    	#ellipse point
    	list1 = TexMobject("\\Sigma_0", r"\text{ is then extended}")
    	list1.scale(0.6)
    	list1.set_color_by_tex_to_color_map({
    		"\\Sigma_0": RED
    		})
    	sentence = VGroup(list1)
    	sentence.shift(2*UP + 4.5*RIGHT)
    	self.play(Write(sentence), run_time = 0.5)

    	dtft_size = 100
    	x = e_min*cos(pi/2 + pi/8)*np.ones(dtft_size)
    	y_min = e_min*sin(pi/2 + pi/8)
    	y_max = e_max*sin(pi/2 + pi/8)
    	y = np.linspace(y_min, y_max, dtft_size)
    	coords = [[px,py] for px,py in zip(x,y)]
    	points = self.get_points_from_coords(coords)
    	rl_0 = DiscreteGraphFromSetPoints(points, color = YELLOW)
    	self.play(ShowCreation(rl_0), run_time = 2)

    	list1 = TexMobject("\\Omega_0", r"\text{ is then extended}")
    	list1.scale(0.6)
    	list1.set_color_by_tex_to_color_map({
    		"\\Omega_0": PURPLE
    		})
    	sentence1 = VGroup(list1)
    	sentence1.shift(1.5*UP + 4.5*RIGHT)
    	self.play(Write(sentence1), run_time = 0.5)

    	dtft_size = 100
    	y = e_max*sin(pi/2 + pi/8)*np.ones(dtft_size)
    	x_min = e_max*cos(pi/2 + pi/8)
    	x_max = e_min*cos(pi/2 + pi/8)
    	x = np.linspace(x_min, x_max, dtft_size)
    	coords = [[px,py] for px,py in zip(x,y)]
    	points = self.get_points_from_coords(coords)
    	im_0 = DiscreteGraphFromSetPoints(points, color = YELLOW)
    	self.play(ShowCreation(im_0), run_time = 2)

    	sc = 1.81
    	x = e_min*cos(pi/2 + pi/8)/sc
    	y = e_max*sin(pi/2 + pi/8)/sc#*np.linspace(1,2,1)
    	circle_p0 = Circle(color = WHITE, radius = 0.02)
    	circle_p0.shift(y*UP + x*RIGHT)
    	self.play(ShowCreation(circle_p0), run_time = 0.5)

    	list1 = TexMobject(r"\text{The pole for k = 0 is marked}")
    	list1.scale(0.6)
    	list2 = TexMobject(r"\text{at the intersection point}")
    	list2.scale(0.6)
    	sentence2 = VGroup(list1, list2)
    	sentence2.arrange_submobjects(DOWN) #, buff=MED_LARGE_BUFF)
    	sentence2.shift(1*UP + 4*LEFT)
    	self.play(Write(sentence2), run_time = 1)
    	self.wait(1)
    	self.play(FadeOut(sentence), FadeOut(sentence1), FadeOut(rl_0), FadeOut(im_0), FadeOut(sentence2), FadeOut(circle_rp0), FadeOut(circle_ip0), run_time = 3.5)
    	self.wait(1)

    	for i in range(1, 8):
    		list1 = TexMobject(r"\text{For the pole with k}", " = ", str(i))
    		list1.scale(0.6)
    		list2 = TexMobject("A_", str(i), " = ", "(2*", str(i), " + 1)", "{\\pi \\over 8}", " = ", str(2*i + 1), "{\\pi \\over 8}")
    		list2.scale(0.6)
    		sentence = VGroup(list1, list2)
    		sentence.arrange_submobjects(DOWN)
    		sentence.shift(2*UP + 4.5*RIGHT)
    		self.play(Write(sentence), run_time = 0.5)

    		ang = (2*i+1)*pi/8
    		#Draw line
    		dtft_size = 100
    		x_max = e_max*cos(pi/2 + ang)
    		x = np.linspace(0, x_max, dtft_size)
    		y_max = e_max*sin(pi/2 + ang)
    		y = np.linspace(0, y_max, dtft_size)
    		coords = [[px,py] for px,py in zip(x,y)]
    		points = self.get_points_from_coords(coords)
    		lin_0 = DiscreteGraphFromSetPoints(points)
    		self.play(ShowCreation(lin_0), run_time = 0.5)

    		#poles
    		sc = 1.8
    		x = e_min*cos(pi/2 + ang)/sc
    		y = e_min*sin(pi/2 + ang)/sc#*np.linspace(1,2,1)
    		circle_rp0 = Circle(color = RED, radius = 0.02)
    		circle_rp0.shift(y*UP + x*RIGHT)
    		self.play(ShowCreation(circle_rp0), run_time = 0.25)

    		sc = 1.81
    		x = e_max*cos(pi/2 + ang)/sc
    		y = e_max*sin(pi/2 + ang)/sc#*np.linspace(1,2,1)
    		circle_ip0 = Circle(color = PURPLE, radius = 0.02)
    		circle_ip0.shift(y*UP + x*RIGHT)
    		self.play(ShowCreation(circle_ip0), FadeOut(lin_0), run_time = 0.25)

    		dtft_size = 100
    		x = e_min*cos(pi/2 + ang)*np.ones(dtft_size)
    		y_min = e_min*sin(pi/2 + ang)
    		y_max = e_max*sin(pi/2 + ang)
    		y = np.linspace(y_min, y_max, dtft_size)
    		coords = [[px,py] for px,py in zip(x,y)]
    		points = self.get_points_from_coords(coords)
    		rl_0 = DiscreteGraphFromSetPoints(points, color = YELLOW)
    		self.play(ShowCreation(rl_0), run_time = 0.5)

    		dtft_size = 100
    		y = e_max*sin(pi/2 + ang)*np.ones(dtft_size)
    		x_min = e_max*cos(pi/2 + ang)
    		x_max = e_min*cos(pi/2 + ang)
    		x = np.linspace(x_min, x_max, dtft_size)
    		coords = [[px,py] for px,py in zip(x,y)]
    		points = self.get_points_from_coords(coords)
    		im_0 = DiscreteGraphFromSetPoints(points, color = YELLOW)
    		self.play(ShowCreation(im_0), run_time = 0.5)

    		sc = 1.81
    		x = e_min*cos(pi/2 + ang)/sc
    		y = e_max*sin(pi/2 + ang)/sc#*np.linspace(1,2,1)
    		circle_p0 = Circle(color = WHITE, radius = 0.02)
    		circle_p0.shift(y*UP + x*RIGHT)
    		self.play(ShowCreation(circle_p0), run_time = 0.25)
    		self.play(FadeOut(rl_0), FadeOut(im_0), FadeOut(circle_rp0), FadeOut(circle_ip0), FadeOut(sentence), run_time = 1)


    	list1 = TexMobject(r"\text{All the poles are now located!!}")
    	list1.scale(0.7)
    	sentence = VGroup(list1)
    	sentence.shift(2*UP + 4*LEFT)
    	self.play(Write(sentence), run_time = 1)
    	self.wait(3)











    def get_points_from_coords(self,coords):
        return [self.coords_to_point(px,py)
            for px,py in coords
            ]