from manimlib.imports import *
import numpy as np
import cmath as cm
from math import*

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class ps(GraphScene, Scene):
	CONFIG = {
	"fill_color" : BLUE,
	}

	def construct(self):
		text1 = TextMobject("\\textsc{Illustration of Parseval's theorem}")
		self.play(ShowCreation(text1))
		self.wait(2)
		self.clear()
		t1 = TexMobject(r"\text{Consider a signal }", "x[n] = ", "\\Big(", "{4 \\over 5}", "\\Big)^{n}", ".u[n]")
		t1.scale(0.75)
		t2 = TexMobject(r"\text{where }", "u[n]", r"\text{ is the unit step response}")
		t2.scale(0.75)
		s1 = VGroup(t1, t2)
		s1.arrange_submobjects(DOWN)
		s1.shift(2*UP)
		self.play(Write(s1), run_time = 2.5)
		axis1 = Axes(
			x_min = -5,
			x_max = 5,
			y_min = 0,
			y_max = 1,
			x_axis_label = "$n$",
			y_axis_label = "$x[n]$",
			axes_color = GREY_BROWN,
			x_labelled_nums = list(range(-5,5)),
			y_labelled_nums = [1],
			center_point = 2*DOWN,
			x_axis_config={
				"unit_size": 1,
				"tick_frequency": 1,
				"include_tip": False,
				"label_direction": DOWN+0.5*LEFT
			},
			y_axis_config={
				"unit_size": 1.2,
				"tick_frequency": 1,
				"include_tip": False,
				"label_direction": UP
			})
		axis1 = axis1.scale(1.25)
		axis1.move_to(1.5*DOWN)
		xlabels_axis1 = axis1.get_x_axis().get_number_mobjects(*list(range(-4,5)))
		ylabels_axis1 = axis1.get_y_axis().get_number_mobjects(*[1])
		x1_val = np.array(range(-4,5))
		y1_val = [0 for x in range(-4,1)]
		y1_val.extend([(4/5)**x for x in range(1,5)])
		x1_txt = TextMobject("x[n]")
		x1_txt.set_color(YELLOW)
		x1_txt.move_to(2*LEFT + 0.5*DOWN)
		f1dots, f1lines = self.get_discrete(x1_val, y1_val, myaxes = axis1, mycolor = YELLOW)
		f1 = VGroup(*f1dots, *f1lines, x1_txt)
		self.add(axis1, xlabels_axis1, ylabels_axis1)
		self.wait(1)
		self.play(ShowCreation(f1), run_time = 1.5)
		self.wait(2)
		self.play(FadeOut(s1), run_time = 1)
		## product of signals
		t1 = TexMobject (r"\text{Here, }", "x[n].x[n] = ", "\\Big(", "{16 \\over 25}", "\\Big)^{n}", ".u[n]" )
		t1.scale(0.75)
		t2 = TexMobject (r"\text{So, }", "\\Sigma_{n = -\\infty} ^{n = \\infty} x[n]^{2} = ", "\\Sigma_{n = 0} ^{n = \\infty}", "\\Big(", "{16 \\over 25}", "\\Big)^{n}", " = ", "\\Big(", "{1 \\over 1 - 16/25}", "\\Big)", " = ", "{25 \\over 9}")
		t2.scale(0.75)
		s1 = VGroup(t1, t2)
		s1.arrange_submobjects(DOWN)
		s1.shift(2*UP)
		self.play(Write(s1), run_time = 2.5)
		y3_val = [0 for x in range(-4,1)]
		y3_val.extend([(16/25)**x for x in range(1,5)])
		x3_txt = TexMobject("x[n]^{2}")
		x3_txt.set_color_by_tex_to_color_map({
    		"x[n]^{2}": BLUE
    		})
		x3_txt.move_to(2*LEFT + DOWN)
		#self.play(FadeOut(x1_txt), FadeOut(x2_txt), ShowCreation(x3_txt), run_time = 0.5)
		f3dots, f3lines = self.get_discrete(x1_val, y3_val, myaxes = axis1, mycolor = GREEN)
		f3 = VGroup(*f3dots, *f3lines, x3_txt)
		self.play(Transform(f1, f3), run_time = 2)
		self.wait(2)
		self.clear()

		## RHS
		axis2 = Axes(
			x_min = -4,
			x_max = 4,
			y_min = 0,
			y_max = 2,
			x_axis_label = "$\omega$",
			y_axis_label = "$|X(e^{j\omea})|$",
			axes_color = GREY_BROWN,
			#x_labelled_nums = list(range(-5,5)),
			#y_labelled_nums = [1],
			center_point = 2*DOWN,
			x_axis_config={
				"unit_size": 1,
				"tick_frequency": 1,
				"include_tip": False,
				"label_direction": DOWN+0.5*LEFT
			},
			y_axis_config={
				"unit_size": 1.2,
				"tick_frequency": 1,
				"include_tip": False,
				"label_direction": UP
			})
		axis2 = axis2.scale(1.25)
		axis2.move_to(1.5*DOWN)
		self.add(axis2)
		one_pi = TexMobject("\\pi")
		one_pi.shift(3.5*DOWN + 4*RIGHT)
		minus_one_pi = TexMobject("-\\pi")
		minus_one_pi.shift(3.5*DOWN + 4*LEFT)
		self.play(ShowCreation(one_pi),ShowCreation(minus_one_pi), run_time = 0.5)
		t1 = TexMobject (r"\text{The Magnitude response of }", "x[n]:")
		t1.scale(0.75)
		t2 = TexMobject("|X(e^{j\\omega})|^{2}"," = X(e^{j\\omega}).X(e^{j\\omega})' = ")
		t2.set_color_by_tex_to_color_map({
    		"|X(e^{j\\omega})|^{2}": BLUE
    		})
		t2.scale(0.75)
		t3 = TexMobject("{1 \\over 1 - (4/5).e^{-jw}}.{1 \\over 1 - (4/5).e^{jw}}", " = {1 \\over 1 + (4/5)^2 - 2.(4/5).cos(\omega)}")
		t3.scale(0.75)
		s1 = VGroup(t1, t2, t3)
		s1.arrange_submobjects(DOWN)
		s1.shift(2.75*UP)
		self.play(Write(s1), run_time = 2.5)
		xdtft = axis1.get_graph(lambda x: 0.08/(1 + (4/5)**2 - (8/5)*np.cos(x)) - 0.5, x_min = -np.pi, x_max = np.pi)
		xdtft.set_color(BLUE)
		self.play(ShowCreation(xdtft), run_time = 2.5)
		self.wait(2)
		self.play(FadeOut(s1), run_time = 1.5)
		t1 = TexMobject(r"\text{Computing the area under the curve (using numerical analysis), we get: }")
		t1.scale(0.75)
		t1.shift(2*UP)
		self.play(Write(t1), run_time = 1)
		ar = 0
		t2 = TexMobject(r"\text{Area = }")
		t2.scale(0.75)
		t2.shift(UP)
		self.play(Write(t2), run_time = 0.01)
		t3 = TexMobject(str(ar)).set_color(BLUE)
		t3.scale(0.75)
		t3.shift(UP + 1.1*RIGHT)
		self.play(Write(t3), run_time = 0.01)
		
		r_w = 2*np.pi/100
		for i in range (-50, 51, 1):
			#t3_prev = TexMobject(str(ar)).set_color(BLUE)
			#t3_prev.scale(0.75)
			#t3_prev.shift(UP + RIGHT)
			if (i < -10):
				ar = 2.5*(i+50)/40
			elif (i >= -10 and i < 10):
				ar = 2.5 + 12.45*(i+10)/20 
			else:
				ar = 14.95 + 2.5*(i-10)/40
			ar = round(ar, 2)
			r_ht = 0.08/(1 + (4/5)**2 - (8/5)*np.cos(i*np.pi/50))
			hf = 1.4
			hoff = 0
			rdown = 2.85
			r = Rectangle(height = hoff+hf*r_ht, width = r_w, fill_color=BLUE, fill_opacity=1, color=BLUE)
			r.shift((rdown-0.5*hf*r_ht)*DOWN + 1.25*i*np.pi*0.02*RIGHT)
			self.play(FadeIn(r), FadeOut(t3), run_time = 0.01)
			t3 = TexMobject(str(ar)).set_color(BLUE)
			t3.scale(0.75)
			t3.shift(UP + 1.1*RIGHT)
			self.play(FadeIn(t3), run_time = 0.01)
			#self.play(ReplacementTransform(t3_prev, t3), run_time = 0.01)
		self.wait(2)
		self.clear()
		t1 = TexMobject(r"\text{Hence, the equation of Parseval's theorem can be shown as: }")
		t2 = TexMobject("{1 \\over 2\\pi}\\int_{\omega = -\\pi} ^{\omega = \\pi} |X(e^{j\\omega})|^{2} \\approx ", "{17.45 \\over 2\\pi} \\approx 2.77 \\approx {25 \\over 9} = ", "\\Sigma_{n = -\\infty} ^{n = \\infty} x[n]^{2}")
		t1.scale(0.75)
		t2.scale(0.75)
		s1 = VGroup(t1,t2)
		s1.arrange_submobjects(DOWN)
		self.play(Write(s1), run_time = 2)
		self.wait(3)
		#rect_coords = self.rect_dtft_2(4/5)
		#rect_pts = self.get_points_from_coords(rect_coords)
		#rect_window_ft = DiscreteGraphFromSetPoints(rect_pts, color = YELLOW)
		#self.play(ShowCreation(rect_window_ft), run_time = 1.5)








	def to_dots(self, x_points, y_points, myaxes, mycolor=YELLOW):
		'''
		Converts point coordinates to Dots objects
		'''
		return [Dot(myaxes.coords_to_point(x_points[i], y_points[i]), color=mycolor) for i in range(len(x_points))]

	def to_lines(self, x_points, y_points, myaxes, mycolor=YELLOW):
		'''
		Converts point coordinates to Lines objects
		'''
		return [Line(myaxes.coords_to_point(x_points[i], 0), myaxes.coords_to_point(x_points[i], y_points[i]), color=mycolor, fill_opacity=0.5)\
		for i in range(len(x_points))]

	def get_discrete(self, x_points, y_points, myaxes, mycolor = YELLOW):
		'''
		Gives dots and lines to plot
		'''
		dots = self.to_dots(x_points, y_points, myaxes, mycolor)
		lines = self.to_lines(x_points, y_points, myaxes, mycolor)
		return dots, lines

	def get_points_from_coords(self,coords):
		return [self.coords_to_point(px,py) for px,py in coords]

	def rect_dtft_2(self,a):
		dtft_size = 200
		Xi = [a**i for i in range(1,11)]
		#Xi.extend([a**i for i in range(1,11)])
		X = np.fft.fft(Xi, dtft_size)
		X = np.fft.fftshift(X)
		#X = np.abs(X)
		w=np.linspace(-np.pi,np.pi,dtft_size)
		coords = [[px,py] for px,py in zip(w,X)]
		#points = self.get_points_from_coords(coords)
		return coords

	def rect_dtft(self,N):
		dtft_size = 200
		Xi = [1+(i/N) for i in range(-N,1)]
		Xi = [1 - (i/N) for i in range(1,N+1)]
		#Xi = [1 for i in range(int(-(N+1)/2), int((N+3)/2))]
		#c_Xi = np.convolve(Xi, Xi)
		#Xi = c_Xi[len(Xi) - N:len(Xi) + N + 1:1]
		#Xi = c_Xi/np.max(Xi)
		X = np.fft.fft(Xi, dtft_size)
		X = np.fft.fftshift(X) - 0.36
		#X = np.roll(X,dtft_size_by_2)
		w=np.linspace(-np.pi,np.pi,dtft_size)
		coords = [[px,py] for px,py in zip(w,X)]
		#points = self.get_points_from_coords(coords)
		return coords


