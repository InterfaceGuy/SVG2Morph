from manim import *

class Morph(Scene):
	def construct(self):
		# load two svg files and morph one to the other
		svg1 = SVGMobject("svg1.svg")
		svg2 = SVGMobject("svg2.svg")
		# set svg to white outline and transparent fill
		svg1.set_stroke(WHITE, width=1)
		svg1.set_fill(opacity=0)
		svg1.set_color(WHITE)
		# set svg to white outline and transparent fill
		svg2.set_stroke(WHITE, width=1)
		svg2.set_fill(opacity=0)
		svg2.set_color(WHITE)
		self.play(Transform(svg1, svg2), run_time=3)