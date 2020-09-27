from manimlib.imports import *
import math

from math import pi

def chebyschev_polynomial(x, N):
    """
    Evaluates the Nth order Chebyschev polynomial at x and returns the value.
    """
    if x < 1 and x >= -1:
        return math.cos(N * math.acos(x))
    elif x < -1:
        if N % 2 == 0:
            return math.cosh(N * math.acosh(-x))
        else:
            return -math.cosh(N * math.acosh(-x))
    else:
        return math.cosh(N * math.acosh(x))

def chebyschev_lowpass(f_pass, f_stop, tol_pass, tol_stop):
    """
    Returns the Chebyschev analog lowpass filter function corresponding to
    passband and stopband frequencies and tolerances.

    Inputs:
    - f_pass: The passband boundary frequency in Hz
    - f_stop: The stopband boundary frequency in Hz
    - tol_pass: The tolerance required in the passband
    - tol_stop: The tolerance required in the stopband.

    Returns a function that takes a frequency (in Hz) as input and returns
    the filter magnitude at that frequency as the output.
    """

    if f_pass == f_stop:
        raise ValueError('The passband and stopband frequencies cannot be equal.')

    if tol_pass == 0 or tol_stop == 0:
        raise ValueError('Tolerance values cannot be zero.')

    D1 = 1 / (1 - tol_pass)**2 - 1
    D2 = 1 / tol_stop**2 - 1

    # Optimal epsilon to get minimum N possible
    # epsilon = math.sqrt(D1)
    
    # Minimum order of the filter that is required
    # (Note that D1 is the same as epsilon**2)
    N = math.acosh(math.sqrt(D2 / D1)) / math.acosh(f_stop / f_pass)
    N = math.ceil(N)

    def filter_func(f):
        # Note that D1 is the same as epsilon**2
        mag2 = 1 / (1 + D1*chebyshev_polynomial(f / f_pass, N)**2)
        return math.sqrt(mag2)

    return filter_func

class chebyschev(Scene):
    """
    Class inheriting from the Scene class, which is used to generate the animation.
    """
    
    def construct(self):
        """
        Construct method used in place of __init__ as per standard manimlib usage.

        This method includes the instructions to create the complete animation for Lecture 22.
        We first show the variation of the lower limit of N with epsilon (as defined in the lecture).
        Then we show how the Chebyschev filter magnitude function changes as we change epsilon and N.
        """

        # defining the specifications for a Chebyschev filter
        f_pass = 10e3
        f_stop = 12e3
        tol_pass = 0.05
        tol_stop = 0.05

        # defining some useful constants
        D1 = 1 / (1 - tol_pass)**2 - 1
        epsilon_max = math.sqrt(D1)
        D2 = 1 / tol_stop**2 - 1

        N_min = math.acosh(math.sqrt(D2) / epsilon_max) / math.acosh(f_stop / f_pass)
        N_min = math.ceil(N_min)

        # define a function to get minimum required filter order N (non integral value)
        def get_N(epsilon, D2, f_ratio):
            return math.acosh(math.sqrt(D2) / epsilon) / math.acosh(f_ratio)

        def get_N2(D_ratio, f_ratio):
            return math.ceil(math.acosh(math.sqrt(D_ratio)) / math.acosh(f_ratio))

        # define a function to get filter function corresponding to an epsilon and N
        def get_filter(epsilon, N):
            return lambda x: math.sqrt(1 / (1 + (epsilon * chebyschev_polynomial(x, N))**2))

        # define additional colors
        LIME = "#00FF00"
        CYAN = "#00FFFF"
        BRIGHT_GREEN = "#7cff3f"
        BRIGHT_BLUE = "#59FCFF"
        PEACH = "#FFE5B4"

        epsilon_color = BRIGHT_GREEN
        N_color = BRIGHT_BLUE
        eps_max_color = BRIGHT_GREEN
        N_min_color = BRIGHT_BLUE

        ####

        text1 = TextMobject("\\textsc{Effects of Tolerance and Band Frequencies on \\\\ the order of Chebyschev Magnitude Filter Function}")
        
        self.play(ShowCreation(text1))

        self.wait(2)
        self.clear()

        text2 = TextMobject("Consider the following filter specifications:")
        text2.scale(0.7)
        s1 = TexMobject(r"\text{Passband Edge }", "= \\Omega_P = ", r"\text{10 kHz}").set_color(PEACH)
        s2 = TexMobject(r"\text{Stopband Edge }", "= \\Omega_S = ", r"\text{12 kHz}").set_color(PEACH)
        s3 = TexMobject(r"\text{Passband Tolerance }", "= \\delta_1 = 0.05").set_color(PEACH)
        s4 = TexMobject(r"\text{Stopband Tolerance }", "= \\delta_2 = 0.05").set_color(PEACH)
        s1.scale(0.7)
        s2.scale(0.7)
        s3.scale(0.7)
        s4.scale(0.7)

        specs_group = VGroup(text2, s1, s2, s3, s4)
        specs_group.arrange_submobjects(DOWN)
        specs_group.shift(2.5*UP)
        #specs_group.arrange(DOWN)
        self.play(Write(specs_group))

        D1text = str(float(int(D1*10**2))/10**2)
        D2text = str(float(int(D2*10**2))/10**2)
        t1 = TexMobject(r"\text{Then, the parameter }", "D_1 = ", "{1 \\over (1 - \\delta_1)^2}", " - 1 = ", D1text, r"\text{ and }", "D_2 = ", "{1 \\over \\delta_2^2}", " - 1 = ", D2text)
        t1.scale(0.7)
        t1.shift(0.5*UP)
        t1.set_color(YELLOW)
        self.play(Write(t1))

        n1 = TexMobject(r"\text{The minimum order of the filter }", "N_{min}", r"\text{ is given by: }")
        n1.scale(0.7)
        n1.set_color_by_tex_to_color_map({
        	"N_{min}": N_color
        	})
        n1.shift(2.75*LEFT + DOWN)
        self.play(Write(n1))
        #filter order formula
        xoff = 1.5
        yoff = -2.25
        lstart1 = (xoff+0.5, yoff + 2.25, 0)
        lend1 = (xoff, yoff + 2.25, 0)
        lend2 = (xoff, yoff, 0)
        lceil1 = Line(lstart1, lend1)
        lceil2 = Line(lend1, lend2)
        numr = TexMobject("cosh^{-1}", "\\Big(", "\\sqrt{D_2 \\over D_1}", "\\Big)")
        numr.scale(0.7)
        numr.shift((xoff + 1.5)*RIGHT + (yoff + 1.5)*UP)
        f_left = (xoff + 0.25, yoff + 1, 0)
        f_right = (xoff + 2.75, yoff + 1, 0)
        f_line = Line(f_left, f_right);
        denr = TexMobject("cosh^{-1}", "\\Big(", "{\\Omega_S \\over \\Omega_P}", "\\Big)")
        denr.shift((xoff + 1.5)*RIGHT + (yoff + 0.5)*UP)
        denr.scale(0.7)
        rstart1 = (xoff+2.5, yoff + 2.25, 0)
        rend1 = (xoff+3, yoff + 2.25, 0)
        rend2 = (xoff+3, yoff, 0)
        rceil1 = Line(rstart1, rend1)
        rceil2 = Line(rend1, rend2)
        lceil1.set_color(PURPLE)
        lceil2.set_color(PURPLE)
        rceil1.set_color(PURPLE)
        rceil2.set_color(PURPLE)
        f_line.set_color(PURPLE)
        numr.set_color(PURPLE)
        denr.set_color(PURPLE)
        self.play(ShowCreation(lceil1), ShowCreation(lceil2), Write(numr), ShowCreation(f_line), Write(denr), ShowCreation(rceil1), ShowCreation(rceil2))

        Ntext = str(N_min)
        n2 =TexMobject(" = ", Ntext)
        n2.scale(0.7)
        n2.shift(5*RIGHT + DOWN)
        self.play(Write(n2))
        #self.wait(3)
        #self.clear()

        ####
        e_maxtext = str(float(int(epsilon_max*10**2))/10**2)
        text3 = TexMobject(r"\text{The tolerance parameter, }", "e_{max}", " = \\sqrt{D_1} = ", e_maxtext)
        text3.set_color_by_tex_to_color_map({
        	"e_{max}": eps_max_color
        	})
        text3.scale(0.7)
        text3.shift(3*DOWN)
        self.play(Write(text3))

        self.wait(4)
        self.clear()

        ####

        x_min2, x_max2 = 0, 2
        y_min2, y_max2 = 0, 1.5
        x_us2, y_us2 = 3, 3

        axes2 = Axes(
                x_min = x_min2,
                x_max = x_max2,
                y_min = y_min2,
                y_max = y_max2,
                y_axis_label = "$H(\\Omega)$",
                x_axis_label = "$\\Omega$",
                # x_labelled_nums = [1, f_stop / f_pass],
                # y_labelled_nums = [tol_stop, 1-tol_pass],
                center_point = x_us2 * (x_min2 + x_max2) / 2 * LEFT + y_us2 * (y_min2 + y_max2) / 2 * DOWN + 0.5*UP,
                x_axis_config={
                    "unit_size": x_us2,
                    # "tick_frequency": 1,
                    "include_tip": False,
                    "label_direction": DOWN+RIGHT,
                    "include_ticks": False,
                },
                y_axis_config={
                    "unit_size": y_us2,
                    # "tick_frequency": 1,
                    "include_tip": False,
                    "label_direction": UP+LEFT,
                    "include_ticks": False,
                })

        # define value trackers to track how the filter function changes as epsilon and N are changed
        epsilon = ValueTracker(epsilon_max)
        N = ValueTracker(N_min)
        D1_value = ValueTracker(D1)
        D2_value = ValueTracker(D2)
        D21_value = ValueTracker(D2/D1)
        Omg_s = ValueTracker(f_stop/10**3)
        Omg_p = ValueTracker(f_pass/10**3)
        Omg_sp = ValueTracker(f_stop/f_pass)

        # create odometers for N and epsilon
        epsilon_text = TexMobject("\\epsilon = ")
        epsilon_val = DecimalNumber(epsilon.get_value(), num_decimal_places=2, color=epsilon_color)
        epsilon_val.add_updater(lambda mob: mob.set_value(epsilon.get_value()))
        epsilon_group = VGroup(epsilon_text, epsilon_val)
        epsilon_group.arrange(RIGHT, aligned_edge=DOWN)

        N_text = TexMobject("N = ")
        N_val = DecimalNumber(N.get_value(), num_decimal_places=0, color=N_color)
        N_val.add_updater(lambda mob: mob.set_value(math.floor(N.get_value())))
        N_group = VGroup(N_text, N_val)
        N_group.arrange(RIGHT, aligned_edge=DOWN)

        odo_group = VGroup(epsilon_group, N_group)
        odo_group.arrange(RIGHT, aligned_edge=DOWN, buff=LARGE_BUFF)
        odo_group.move_to(3.25*DOWN+0.5*UP)

        D1_text = TexMobject("D_1 = ")
        D1_val = DecimalNumber(D1_value.get_value(), num_decimal_places = 2, color = ORANGE)
        D1_val.add_updater(lambda mob: mob.set_value(D1_value.get_value()))
        D1_group = VGroup(D1_text, D1_val)
        D1_group.arrange(RIGHT)
        D1_group.scale(0.7)
        #D1_group.shift(6*LEFT + 3*UP)

        D2_text = TexMobject("D_2 = ")
        D2_val = DecimalNumber(D2_value.get_value(), num_decimal_places = 2, color = ORANGE)
        D2_val.add_updater(lambda mob: mob.set_value(D2_value.get_value()))
        D2_group = VGroup(D2_text, D2_val)
        D2_group.arrange(RIGHT)
        D2_group.scale(0.7)
        #D2_group.shift(4*LEFT + 2.25*UP)

        D2by1_text = TexMobject("{D_2 \\over D_1}", " = ")
        D2by1_val = DecimalNumber(D21_value.get_value(), num_decimal_places = 2, color = ORANGE)
        D2by1_val.add_updater(lambda mob: mob.set_value(D21_value.get_value()))
        D2by1_group = VGroup(D2by1_text, D2by1_val)
        D2by1_group.arrange(RIGHT)
        D2by1_group.scale(0.7)
        #D2by1_group.shift(4*LEFT + 1.5*UP)

        os_text = TexMobject("\\Omega_S (kHz) = ")
        os_val = DecimalNumber(Omg_s.get_value(), num_decimal_places = 2, color = RED)
        os_val.add_updater(lambda mob: mob.set_value(Omg_s.get_value()))
        os_group = VGroup(os_text, os_val)
        os_group.arrange(RIGHT)
        os_group.scale(0.7)
        #os_group.shift(6*LEFT)

        op_text = TexMobject("\\Omega_P (kHz) = ")
        op_val = DecimalNumber(Omg_p.get_value(), num_decimal_places = 2, color = RED)
        op_val.add_updater(lambda mob: mob.set_value(Omg_p.get_value()))
        op_group = VGroup(op_text, op_val)
        op_group.arrange(RIGHT)
        op_group.scale(0.7)
        #op_group.shift(6*LEFT + 0.75*DOWN)

        osbyp_text = TexMobject("{\\Omega_S \\over \\Omega_P}", " = ")
        osbyp_val = DecimalNumber(Omg_sp.get_value(), num_decimal_places = 2, color = RED)
        osbyp_val.add_updater(lambda mob: mob.set_value(Omg_sp.get_value()))
        osbyp_group = VGroup(osbyp_text, osbyp_val)
        osbyp_group.arrange(RIGHT)
        osbyp_group.scale(0.7)
        #osbyp_group.shift(6*LEFT + 1.5*DOWN)

        param1_group = VGroup(D1_group, D2_group, D2by1_group)
        param1_group.arrange_submobjects(DOWN)
        param1_group.shift(5.5*LEFT + 2*UP)

        param2_group = VGroup(os_group, op_group, osbyp_group)
        param2_group.arrange_submobjects(DOWN)
        param2_group.shift(5.5*LEFT + DOWN)

        nmin_text = TexMobject("N_{min} = ")
        nmin_text.scale(0.7)
        nmin_text.shift(2.5*RIGHT + 2.5*UP)
        xoff = 3.5
        yoff = 1.5
        lstart1 = (xoff+0.5, yoff + 2.25, 0)
        lend1 = (xoff, yoff + 2.25, 0)
        lend2 = (xoff, yoff, 0)
        lceil1 = Line(lstart1, lend1)
        lceil2 = Line(lend1, lend2)
        numr = TexMobject("cosh^{-1}", "\\Big(", "\\sqrt{D_2 \\over D_1}", "\\Big)")
        numr.scale(0.7)
        numr.shift((xoff + 1.5)*RIGHT + (yoff + 1.5)*UP)
        f_left = (xoff + 0.25, yoff + 1, 0)
        f_right = (xoff + 2.75, yoff + 1, 0)
        f_line = Line(f_left, f_right);
        denr = TexMobject("cosh^{-1}", "\\Big(", "{\\Omega_S \\over \\Omega_P}", "\\Big)")
        denr.shift((xoff + 1.5)*RIGHT + (yoff + 0.5)*UP)
        denr.scale(0.7)
        rstart1 = (xoff+2.5, yoff + 2.25, 0)
        rend1 = (xoff+3, yoff + 2.25, 0)
        rend2 = (xoff+3, yoff, 0)
        rceil1 = Line(rstart1, rend1)
        rceil2 = Line(rend1, rend2)
        lceil1.set_color(PURPLE)
        lceil2.set_color(PURPLE)
        rceil1.set_color(PURPLE)
        rceil2.set_color(PURPLE)
        f_line.set_color(PURPLE)
        numr.set_color(PURPLE)
        denr.set_color(PURPLE)
        


        # start creating a scene VGroup that stores all the objects we create on the scene
        scene1 = VGroup(axes2, odo_group)

        # define axis labels
        axis_labels2 = VGroup(
            axes2.get_x_axis_label("\\Omega", direction=0.5*DR),
            axes2.get_y_axis_label("H(\\Omega)", direction=0.5*UL)
            )

        scene1.add(axis_labels2)

        # defining tick marks mobjects
        f_pass_tick = axes2.get_x_axis().get_tick(1.0)
        f_stop_tick = axes2.get_x_axis().get_tick(f_stop / f_pass)

        tol_stop_tick = axes2.get_y_axis().get_tick(tol_stop)
        tol_pass_tick = axes2.get_y_axis().get_tick(1 - tol_pass)
        unity_tick = axes2.get_y_axis().get_tick(1.0)

        ticks1 = VGroup(f_pass_tick, f_stop_tick, tol_pass_tick, tol_stop_tick, unity_tick)

        scene1.add(ticks1)

        # now get the labels for the tick marks
        f_pass_mob = TexMobject("\\Omega_P").scale(0.8)
        f_pass_mob.next_to(f_pass_tick, DOWN+0.5*LEFT, buff=SMALL_BUFF)
        f_stop_mob = TexMobject("\\Omega_S").scale(0.8)
        f_stop_mob.next_to(f_stop_tick, DOWN+0.5*RIGHT, buff=SMALL_BUFF)
        
        tol_stop_mob = TexMobject("\\delta_2").scale(0.8)
        tol_stop_mob.next_to(tol_stop_tick, LEFT, buff=SMALL_BUFF)
        tol_pass_mob = TexMobject("1 - \\delta_1").scale(0.8)
        tol_pass_mob.next_to(tol_pass_tick, 0.5*DOWN+LEFT, buff=SMALL_BUFF)
        unity_mob = TexMobject("1").scale(0.8)
        unity_mob.next_to(unity_tick, 0.5*UP+LEFT, buff=SMALL_BUFF)

        mobs1 = VGroup(f_pass_mob, f_stop_mob, tol_pass_mob, tol_stop_mob, unity_mob)

        filter_graph = axes2.get_graph(get_filter(
            epsilon=epsilon.get_value(),
            N=N.get_value()),
        stroke_width = DEFAULT_STROKE_WIDTH * 0.6,
        color=YELLOW)

        scene1.add(mobs1, filter_graph)

         # create rectangles highlighting the valid region
        passband_region = Rectangle(
            width = 1 * axes2.get_x_axis().unit_size,
            height = tol_pass * axes2.get_y_axis().unit_size,
            fill_color=GREEN,
            fill_opacity=0.5,
            background_stroke_color=GREEN,
            background_stroke_opacity = 0.5,
            stroke_opacity=0
            # stroke_width=0.0
            )
        stopband_region = Rectangle(
            width = (axes2.x_max - f_stop / f_pass) * axes2.get_x_axis().unit_size,
            height = tol_stop * axes2.get_y_axis().unit_size,
            fill_color=GREEN,
            fill_opacity=0.5,
            background_stroke_color=GREEN,
            background_stroke_opacity = 0.5,
            stroke_opacity=0
            # stroke_width=0.0
            )
        passband_region.align_to(tol_pass_tick, direction=DOWN)
        passband_region.align_to(axes2.get_x_axis(), direction=LEFT)
        stopband_region.align_to(f_stop_tick, direction=LEFT)
        stopband_region.align_to(axes2.get_y_axis(), direction=DOWN)

        scene1.add(passband_region, stopband_region)

        # plot the filter function now
        self.play(Write(nmin_text), ShowCreation(lceil1), ShowCreation(lceil2), Write(numr), ShowCreation(f_line), Write(denr), ShowCreation(rceil1), ShowCreation(rceil2), run_time = 0.5)
        self.play(ShowCreation(axes2), ShowCreation(axis_labels2))

        self.play(
            ShowCreation(ticks1),
            ShowCreation(mobs1),
            ShowCreation(odo_group),
            ShowCreation(param1_group),
            ShowCreation(param2_group)
            #ShowCreation(D1_group), ShowCreation(D2_group), ShowCreation(D2by1_group),
            #ShowCreation(os_group), ShowCreation(op_group), ShowCreation(osbyp_group)
            )

        
        self.wait(1)
        
        self.play(
            ShowCreation(passband_region),
            ShowCreation(stopband_region),
            )
        self.play(ShowCreation(filter_graph))
        


        f1text = TexMobject(r"\text{The }",  r"\text{filter magnitude function}")
        f1text.set_color_by_tex_to_color_map({
        	r"\text{filter magnitude function}": YELLOW
        	})
        f2text = TexMobject(r"\text{looks like this.}")
        ftext = VGroup(f1text, f2text)
        ftext.arrange_submobjects(DOWN)
        ftext.scale(0.6)
        ftext.shift(5*RIGHT + 0*DOWN)
        f1text1 = TexMobject(r"\text{The tolerance regions}")
        f2text1 = TexMobject(r"\text{are shaded }", r"\text{green}")
        f2text1.set_color_by_tex_to_color_map({
        	r"\text{green}": BRIGHT_GREEN
        	})
        ftext1 = VGroup(f1text1, f2text1)
        ftext1.arrange_submobjects(DOWN)
        ftext1.scale(0.6)
        ftext1.shift(5*RIGHT + 1*DOWN)
        self.play(Write(ftext), Write(ftext1))
        self.wait(3)

        # now we add updater for the graph
        filter_graph.add_updater(
            lambda mob: mob.become(axes2.get_graph( get_filter( epsilon=epsilon.get_value(), N=N.get_value() ),
                color=YELLOW, stroke_width = DEFAULT_STROKE_WIDTH * 0.6) ),
            )


        self.play(FadeOut(ftext), FadeOut(ftext1), run_time = 0.5)
        dtext1 = TexMobject(r"\text{As the ratio }", "{D_2 \\over D_1}")
        dtext2 = TexMobject(r"\text{increases, the filter order}")
        dtext3 = TexMobject(r"\text{also increases}")
        dtextgroup = VGroup(dtext1, dtext2, dtext3)
        dtextgroup.arrange_submobjects(DOWN)
        dtextgroup.scale(0.6)
        dtextgroup.shift(5*RIGHT + 0.5*DOWN)
        self.play(Write(dtextgroup), run_time = 1)
        self.wait(1)

        #epsilon = ValueTracker(epsilon_max)
        #N = ValueTracker(N_min)
        #D1_value = ValueTracker(D1)
        #D2_value = ValueTracker(D2)
        #D21_value = ValueTracker(D2/D1)

        epsilon.set_value(epsilon_max)
        N.set_value(N_min)
        filter_graph.update()
        epsilon_val.update()
        N_val.update()


        self.play(
        	D2_value.set_value, D2*10,
        	D1_value.set_value, D1/10,
        	D21_value.set_value, 100*D2/D1,
        	epsilon.set_value, epsilon_max/math.sqrt(10),
        	N.set_value, get_N2(100*D2/D1, f_stop/f_pass),
        	rate_func=linear,
        	run_time=2)
        delta = 1/math.sqrt(1 + 0.1*D1) - 1/math.sqrt(1 + D1) 
        sc = 3
        tol_pass_tick.shift(sc*delta*UP)
        tol_pass_mob.next_to(tol_pass_tick, 0.5*DOWN+LEFT, buff=SMALL_BUFF)
        delta = 1/math.sqrt(1 + 10*D2) - 1/math.sqrt(1 + D2)
        tol_stop_tick.shift(sc*delta*UP)
        tol_stop_mob.next_to(tol_stop_tick, LEFT, buff=SMALL_BUFF)
        #scene1.add(passband_region, stopband_region)
        self.wait(3)




        self.play(FadeOut(dtextgroup), run_time = 0.5)
        dtext1 = TexMobject(r"\text{As the ratio }", "{D_2 \\over D_1}")
        dtext2 = TexMobject(r"\text{decreases, the filter order}")
        dtext3 = TexMobject(r"\text{also decreases}")
        dtextgroup = VGroup(dtext1, dtext2, dtext3)
        dtextgroup.arrange_submobjects(DOWN)
        dtextgroup.scale(0.6)
        dtextgroup.shift(5*RIGHT + 0.5*DOWN)
        self.play(Write(dtextgroup), run_time = 1)
        self.wait(1)

        self.play(
        	D2_value.set_value, D2*0.1,
        	D1_value.set_value, D1/0.1,
        	D21_value.set_value, 0.01*D2/D1,
        	epsilon.set_value, epsilon_max*math.sqrt(10),
        	N.set_value, get_N2(0.01*D2/D1, f_stop/f_pass),
        	rate_func=linear,
        	run_time=2)
        delta = 1/math.sqrt(1 + 10*D1) - 1/math.sqrt(1 + 0.1*D1) 
        tol_pass_tick.shift(sc*delta*UP)
        tol_pass_mob.next_to(tol_pass_tick, 0.5*DOWN+LEFT, buff=SMALL_BUFF)
        delta = 1/math.sqrt(1 + 0.1*D2) - 1/math.sqrt(1 + 10*D2)
        tol_stop_tick.shift(sc*delta*UP)
        tol_stop_mob.next_to(tol_stop_tick, LEFT, buff=SMALL_BUFF)
        self.wait(3)

        epsilon.set_value(epsilon_max)
        N.set_value(N_min)
        filter_graph.update()
        epsilon_val.update()
        N_val.update()
        delta = 1/math.sqrt(1 + D1) - 1/math.sqrt(1 + 10*D1)
        tol_pass_tick.shift(sc*delta*UP)
        tol_pass_mob.next_to(tol_pass_tick, 0.5*DOWN+LEFT, buff=SMALL_BUFF)
        delta = 1/math.sqrt(1 + D2) - 1/math.sqrt(1 + 0.1*D2)
        tol_stop_tick.shift(sc*delta*UP)
        tol_stop_mob.next_to(tol_stop_tick, LEFT, buff=SMALL_BUFF)
        self.wait(1)

        self.play(FadeOut(dtextgroup), run_time = 0.5)
        dtext1 = TexMobject(r"\text{As the ratio }", "{\\Omega_S \\over \\Omega_P}")
        dtext2 = TexMobject(r"\text{decreases, the filter order}")
        dtext3 = TexMobject(r"\text{now increases}")
        dtextgroup = VGroup(dtext1, dtext2, dtext3)
        dtextgroup.arrange_submobjects(DOWN)
        dtextgroup.scale(0.6)
        dtextgroup.shift(5*RIGHT + 0.5*DOWN)
        self.play(Write(dtextgroup), run_time = 1)
        self.wait(1)

        

        self.play(
            Omg_s.set_value, f_stop*0.85/10**3,
            Omg_p.set_value, f_pass/(10**3),
            Omg_sp.set_value, 0.85*f_stop/f_pass,
            #epsilon.set_value, epsilon_max*math.sqrt(10),
            N.set_value, get_N2(D2/D1, 0.85*f_stop/f_pass),
            rate_func=linear,
            run_time=2)
        delta = 0.85 - 1
        sc = 3
        f_stop_tick.shift(sc*delta*RIGHT)
        f_stop_mob.next_to(f_stop_tick, DOWN+0.5*RIGHT, buff=SMALL_BUFF)
        self.wait(3)

        


        self.play(FadeOut(dtextgroup), run_time = 0.5)
        dtext1 = TexMobject(r"\text{As the ratio }", "{\\Omega_S \\over \\Omega_P}")
        dtext2 = TexMobject(r"\text{increases, the filter order}")
        dtext3 = TexMobject(r"\text{now decreases}")
        dtextgroup = VGroup(dtext1, dtext2, dtext3)
        dtextgroup.arrange_submobjects(DOWN)
        dtextgroup.scale(0.6)
        dtextgroup.shift(5*RIGHT + 0.5*DOWN)
        self.play(Write(dtextgroup), run_time = 1)
        self.wait(1)

        self.play(
            Omg_s.set_value, 1.25*f_stop/10**3,
            Omg_p.set_value, f_pass/(10**3),
            Omg_sp.set_value, 1.25*f_stop/f_pass,
            #epsilon.set_value, epsilon_max*math.sqrt(10),
            N.set_value, get_N2(D2/D1, 1.25*f_stop/f_pass),
            rate_func=linear,
            run_time=2)
        delta = 1.25 - 0.85
        f_stop_tick.shift(sc*delta*RIGHT)
        f_stop_mob.next_to(f_stop_tick, DOWN+0.5*RIGHT, buff=SMALL_BUFF)
        self.wait(3)  

        self.play(FadeOut(dtextgroup),FadeOut(param1_group), FadeOut(param2_group), run_time = 0.5)
        epsilon.set_value(epsilon_max)
        N.set_value(N_min)
        filter_graph.update()
        epsilon_val.update()
        N_val.update()
        delta = 1 - 1.25
        f_stop_tick.shift(sc*delta*RIGHT)
        f_stop_mob.next_to(f_stop_tick, DOWN+0.5*RIGHT, buff=SMALL_BUFF)
        

        self.wait(2)




        
        #self.play(FadeOut(formula))






        