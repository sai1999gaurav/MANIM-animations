from manimlib.imports import *
from math import *
import numpy as np
#from topics import functions

class inp(Scene):
	def construct(self):
		text1 = TextMobject("\\textsc{Illustration of inner products \\\\ being independent of basis}")
		self.play(ShowCreation(text1))
		self.wait(2)
		self.clear()
		s1 = TextMobject("Consider two vectors v1 and v2", "{1 \\over 2}")
		s1.scale(0.7)
		s2 = TextMobject("lying in orthogonal space with unit vectors u1 and u2")
		s2.scale(0.7)
		sent1 = VGroup(s1, s2)
		sent1.arrange_submobjects(DOWN)
		sent1.shift(3*UP)
		#specs_group.arrange(DOWN)
		self.play(Write(sent1))
		#self.setup_axes(animate = False)
