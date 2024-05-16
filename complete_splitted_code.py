class TotalScene1(Scene):
    def construct(self):
        title = Tex(r"Minkowski-Weyl at the beach").scale(1.4)
        title.set_color_by_gradient(PURPLE, BLUE)
        subtitle = Tex(r"Season 2")
        subtitle.set_color_by_gradient(BLUE, GREEN)
        
        author = Tex(r"Presented by Maxime LUCET").scale(0.5)
        supervisor = Tex(r"Supervised by Prof. Roland GRAPPE").scale(0.5)

        seminar = Tex(r"Mathematical Programming Seminar").scale(0.5)
        date = Tex(r"Beginning of June 2024").scale(0.5)

        # Adjust positions
        title.next_to(subtitle, UP, buff=0.5)
        author.next_to(subtitle, DOWN, buff=1.0)
        supervisor.next_to(author, DOWN, buff=0.2)
        seminar.next_to(supervisor, DOWN, buff=1.0)
        date.next_to(seminar, DOWN, buff=0.2)

        # Add to scene
        self.play(FadeIn(title))
        self.play(FadeIn(subtitle))
        self.play(FadeIn(author))
        self.play(FadeIn(supervisor))
        self.play(FadeIn(seminar))
        self.play(FadeIn(date))

        self.wait(32)
        self.clear()

        text1 = Tex(r"First, let us do a quick reminder on my presentation.")
        
        MWtheorem1 = Tex(r"A subset $P$ of $\mathbb{R}^n$ is a ", r"polyhedron", r" iff P = Q + C for some \\", r"polytope ", r"$Q \subset \mathbb{R}^n$ and some ", r"polyhedral cone ", r"$C \subset \mathbb{R}^n$.").scale(0.8)
        MWtheorem1[1].set_color(LOGO_BLUE)
        MWtheorem1[3].set_color(LOGO_BLUE)
        MWtheorem1[5].set_color(LOGO_BLUE)
        
        interpretation1 = Tex(r"The ", r"Minkowski-Weyl theorem ", r"can be interpreted as:").scale(0.9).next_to(MWtheorem1, DOWN)
        interpretation1[1].set_color(LOGO_BLUE)
        blist = BulletedList(r"Internal description: the linear system describing the polyhedron", 
                             r"External description: the set of extreme vertices of the polytope and extreme generators of the polyhedral cone", 
                             height=8,
                             width=9,
                             buff=0.6
                            ).next_to(MWtheorem1, DOWN)

        VGroup(interpretation1, blist).arrange(DOWN)

        geometry1 = Tex("A reminder on ", r"Tropical Geometry")
        geometry1[1].set_color(LOGO_BLUE)
        geometry2 = Tex(r"In ", r"Tropical Geometry", r", we work with the triple ", r"$(\mathbb{R}_{max} = \mathbb{R} \cup \{-\infty\}, \oplus, \otimes)$ ", r"where").scale(0.8)
        geometry2[1].set_color(LOGO_BLUE)
        geometry2[3].set_color(LOGO_BLUE)
        blist2 = BulletedList(r"$a \oplus b := \max\{a, b\}$",
                              r"$a \otimes b := a + b$", 
                              height=3, 
                              width=4,
                              buff=0.6
                             ).next_to(geometry2, DOWN)
        blist2.set_color_by_tex(r"$a \oplus b := \max\{a, b\}$", LOGO_BLUE)
        blist2.set_color_by_tex(r"$a \otimes b := a + b$", LOGO_BLUE)

        VGroup(geometry2, blist2).arrange(DOWN)

        self.play(Write(text1))
        self.wait(4)
        self.play(Uncreate(text1))

        self.play(Write(MWtheorem1))
        self.wait(8)

        new_position = MWtheorem1.get_center() + UP * 2
        self.play(MWtheorem1.animate.move_to(new_position))
        self.wait()

        new_position1 = interpretation1.get_center() + DOWN
        new_position2 = blist.get_center() + DOWN
        self.play(blist.animate.move_to(new_position2))
        self.play(interpretation1.animate.move_to(new_position1))
        self.wait(10)

        self.play(Uncreate(MWtheorem1), Uncreate(interpretation1), Uncreate(blist))
        self.wait()

        self.play(Write(geometry1))
        self.wait(4)
        self.play(Uncreate(geometry1))
        self.wait()

        self.play(Write(geometry2), Write(blist2))
        self.wait(32)
        self.clear()

        text2 = Tex(r"Let us define the ", r"Tropical Minkowski sum")
        text2[1].set_color(LOGO_BLUE)
        
        text3 = Tex(r"Given two sets $V, R$ of $\mathbb{R}^n_{max}$, the ", r"Minkowski sum ", r"of $V, R$ is the set").scale(0.8)
        text3[1].set_color(LOGO_BLUE)
        set1 = MathTex(r"V + R := \{x \in \mathbb{R}^n_{max} : x = v \oplus r \text{ for } v \in V, r \in R\}").scale(0.8)

        VGroup(text3, set1).arrange(DOWN)

        text4 = Tex(r"Now, let us state the ", r"Tropical Minkowski-Weyl theorem")
        text4[1].set_color(LOGO_BLUE)

        theorem1_1 = Tex(r"A subset $P$ of $\mathbb{R}^n_{max}$ is a ", r"tropical polyhedron ", r"iff $P = Q \oplus C$ for some").scale(0.8)
        theorem1_1[1].set_color(LOGO_BLUE)
        theorem1_2 = Tex(r"tropical polytope ", r"$Q \subset \mathbb{R}^n_{max}$ and some ", r"tropical polyhedral cone ", r"$C \subset \mathbb{R}^n_{max}$.").scale(0.8)
        theorem1_2[0].set_color(LOGO_BLUE)
        theorem1_2[2].set_color(LOGO_BLUE)

        VGroup(theorem1_1, theorem1_2).arrange(DOWN)

        self.play(Write(text2))
        self.wait(5)
        self.play(Uncreate(text2))
        self.wait()

        self.play(Write(text3), Write(set1))
        self.wait(22)
        self.play(Uncreate(text3), Uncreate(set1))
        self.wait()

        self.play(Write(text4))
        self.wait(4)
        self.play(Uncreate(text4))

        self.play(Write(theorem1_1), Write(theorem1_2))
        self.wait(26)
        self.clear()
        
class TotalScene2(Scene):
    def construct(self):
        halfspace_text = Tex(r"A ", r"tropical halfspace ", r"is a set of vectors verifying an inequality constraint of the form").scale(0.8)
        halfspace_text[1].set_color(LOGO_BLUE)
        halfspace_math = MathTex(r"\bigoplus_{i} a_i \otimes x_i \leq \bigoplus_i b_i \otimes x_i").scale(0.8)
        halfspace_math[0].set_color(LOGO_BLUE)

        VGroup(halfspace_text, halfspace_math).arrange(DOWN)

        self.play(Write(halfspace_text), Write(halfspace_math))
        self.wait(5)

        new_position_halfspace = affine_halfspace_text.get_center() + UP * 2
        new_position_halfspace2 = affine_halfspace_math.get_center() + UP * 2
        self.play(halfspace_text.animate.move_to(new_position_halfspace))
        self.play(halfspace_math.animate.move_to(new_position_halfspace2))
        self.wait()

        new_position_cone = cone_text.get_center() + DOWN
        new_position_cone2 = cone_math.get_center() + DOWN
        self.play(cone_math.animate.move_to(new_position_cone2))
        self.play(cone_text.animate.move_to(new_position_cone))
        self.wait(128)

        self.play(Uncreate(halfspace_text), Uncreate(halfspace_math), Uncreate(cone_text), Uncreate(cone_math))
        self.wait(2)

        polytope_text = Tex(r"A ", r"tropical polytope ", r"is a bounded ", r"tropical polyhedron", r".")
        polytope_text[1].set_color(LOGO_BLUE)
        polytope_text[3].set_color(LOGO_BLUE)
        
        self.play(Write(polytope_text))
        self.wait(10)
        self.play(Uncreate(polytope_text))

        cone_text = Tex(r"A ", r"tropical polyhedral cone ", r"is the intersection of a finite number of ", r"tropical affine halfspaces").scale(0.8)
        cone_text[1].set_color(LOGO_BLUE)
        cone_text[3].set_color(LOGO_BLUE)
        cone_math = MathTex(r"Ax \leq Bx").scale(0.8)
        cone_math[0].set_color(LOGO_BLUE)

        VGroup(cone_text, cone_math).arrange(DOWN)
        
        affine_halfspace_text = Tex(r"A ", r"tropical affine halfspace ", r"is a set of vectors veriying an inequality constraint of the form").scale(0.8)
        affine_halfspace_text[1].set_color(LOGO_BLUE)
        affine_halfspace_math = MathTex(r"\bigoplus_{i} a_i \otimes x_i \oplus a_0 \leq \bigoplus_i b_i \otimes x_i \oplus b_0").scale(0.8)
        affine_halfspace_math[0].set_color(LOGO_BLUE)

        VGroup(affine_halfspace_text, affine_halfspace_math).arrange(DOWN)

        tropical_text = Tex(r"A ", r"tropical polyhedron ", r"is the intersection of a finite number of ", r"tropical affine halfspaces").scale(0.8)
        tropical_text[1].set_color(LOGO_BLUE)
        tropical_text[3].set_color(LOGO_BLUE)
        tropical_math = MathTex(r"Ax \oplus a_0 \leq Bx \oplus b_0")
        tropical_math[0].set_color(LOGO_BLUE)

        VGroup(tropical_text, tropical_math).arrange(DOWN)
        
        self.play(Write(affine_halfspace_text), Write(affine_halfspace_math))
        self.wait(5)

        new_position_affine_halfspace = affine_halfspace_text.get_center() + UP * 2
        new_position_affine_halfspace2 = affine_halfspace_math.get_center() + UP * 2
        self.play(affine_halfspace_text.animate.move_to(new_position_affine_halfspace))
        self.play(affine_halfspace_math.animate.move_to(new_position_affine_halfspace2))
        self.wait()

        new_position_tropical = tropical_text.get_center() + DOWN
        new_position_tropical2 = tropical_math.get_center() + DOWN
        self.play(tropical_math.animate.move_to(new_position_tropical2))
        self.play(tropical_text.animate.move_to(new_position_tropical))
        self.wait(80)
        self.clear()

        # First, Euclidean geometry
        title1 = Tex(r"Let's take the following ", r"affine halfspace")
        title1[1].set_color(LOGO_BLUE)
        basel1 = MathTex(r"y \geq x + 1")
        VGroup(title1, basel1).arrange(DOWN)
        
        transform_title1 = MathTex(r"y \geq x + 1")
        transform_title1.to_corner(UP + RIGHT)
        
        grid = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-6, 6, 1),
            axis_config={
            "color": WHITE,  # color of the axes lines
            "stroke_width": 2,  # thickness of the axes lines
            "include_ticks": True,  # whether to include tick marks on the axes
            "include_numbers": True,  # whether to include numbers on the axes
            "label_direction": DOWN*2,  # direction of the axis labels
            "font_size": 20,  # font size of the axis labels
            },
            background_line_style = {
                "stroke_opacity": 0.4
            }
        )
        
        linear_function = grid.plot(lambda x: x + 1, color = PURPLE)
        
        halfspace1 = Polygon(
            grid.coords_to_point(-10, -9),
            grid.coords_to_point(-10, 9),
            grid.coords_to_point(9, 10),
            fill_color=PURPLE,
            fill_opacity=0.5,
            stroke_width=0
        )
        
        # Now, onto the tropical stuff
        title2 = Tex(r"Now, let's look at the equivalent ", r"tropical affine halfspace")
        title2[1].set_color(LOGO_BLUE)
        basel2 = MathTex(r"y \geq x \oplus 1")
        VGroup(title2, basel2).arrange(DOWN)
        
        transform_title2 = MathTex(r"y \geq x \oplus 1")
        transform_title2.to_corner(UP + RIGHT)
        
        linear_function1 = grid.plot(lambda x: x, color = BLUE)
        linear_function2 = Line([-10, 1, 1], [10, 1, 1])
        linear_function2.set_color(GREEN)
        
        line1 = Line([-10, 1, 1], [1, 1, 1])
        line1.set_color(YELLOW)
        line2 = Line([1, 1, 1], [10, 10, 1])
        line2.set_color(YELLOW)
        
        halfspace2 = Polygon(
            grid.coords_to_point(-10, 1),
            grid.coords_to_point(1, 1),
            grid.coords_to_point(10, 10),
            grid.coords_to_point(-10, 10),
            fill_color=YELLOW,
            fill_opacity=0.22,
            stroke_width=0
        )
        
        #Now, animating
        # First frame on halfspace
        self.play(
            Write(title1),
            FadeIn(basel1, shift=UP),
        )
        self.wait(8)
        
        # Moving the halfspace on the top left corner
        self.play(
            Transform(title1, transform_title1),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel1]),
        )
        self.wait()
        
        # Drawing the grid
        self.play(FadeIn(grid))
        self.wait(2)
        
        # Drawing the first linear function
        self.play(Write(linear_function))
        self.wait(5)
        
        # Drawing the first halfspace
        self.play(FadeIn(halfspace1))
        self.wait(16)
        
        # Removing the drawing
        self.play(FadeOut(title1), FadeOut(linear_function), FadeOut(halfspace1))
        self.play(FadeOut(grid))
        self.wait()
        
        # Now, onto tropical stuff
        self.play(
            Write(title2),
            FadeIn(basel2, shift=UP)
        )
        self.wait(8)
        
        self.play(
            Transform(title2, transform_title2),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel2])
        )
        self.wait()
        
        # Redrawing the grid
        self.play(FadeIn(grid))
        self.wait()
        
        # Drawing the tropical functions
        self.play(Write(linear_function2))
        self.wait(5)
        
        self.play(Write(linear_function1))
        self.wait(10)
        
        # Drawing the tropical halfspace
        self.play(Write(line1), Write(line2))
        self.wait(8)
        
        self.play(Uncreate(linear_function1), Uncreate(linear_function2))
        self.wait()
        
        self.play(FadeIn(halfspace2))
        self.wait(25)
        self.clear()
        
class TotalScene3(Scene):
    def construct(self):
        # First, the linear system
        title3 = Tex(r"We have the following linear system")
        basel2 = MathTex(
            r"0 \leq x_1 + 2\\",
            r"x_1 \leq \max\{x_2, 0\}\\",
            r"x_1 \leq 2\\",
            r"0 \leq \max\{x_1, x_2 - 1\}"
        )
        VGroup(title3, basel2).arrange(DOWN)
        
        equation1 = MathTex(r"0 \leq x_1 + 2\\", color=BLUE, font_size = 30)
        equation2 = MathTex(r"x_1 \leq \max\{x_2, 0\}\\", color=PURPLE, font_size = 30)
        equation3 = MathTex(r"x_1 \leq 2\\", color=YELLOW, font_size = 30)
        equation4 = MathTex(r"0 \leq \max\{x_1, x_2 - 1\}", color=GREEN, font_size = 30)
        
        transform_title2 = VGroup(equation1, equation2, equation3, equation4).arrange(DOWN, buff=0.5)
        transform_title2.to_corner(UP + RIGHT)
        
        grid1 = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-6, 6, 1),
            axis_config={
            "color": WHITE,  # color of the axes lines
            "stroke_width": 2,  # thickness of the axes lines
            "include_ticks": True,  # whether to include tick marks on the axes
            "include_numbers": True,  # whether to include numbers on the axes
            "label_direction": DOWN*2,  # direction of the axis labels
            "font_size": 20,  # font size of the axis labels
            },
            background_line_style = {
                "stroke_opacity": 0.4
            }
        )
        
        inequality1 = Line([-2, -10, 1], [-2, 10, 1])
        inequality1.set_color(BLUE)
        halfspace3 = Polygon(
            grid1.coords_to_point(-2, -10),
            grid1.coords_to_point(10, -10),
            grid1.coords_to_point(10, 10),
            grid1.coords_to_point(-2, 10),
            fill_color=BLUE,
            fill_opacity=0.35,
            stroke_width=0
        )
        
        inequality2_1 = Line([-10, -10, 1], [10, 10, 1])
        inequality2_2 = Line([0, -10, 1], [0, 10, 1], stroke_width=6)
        inequality2_1.set_color(PURPLE)
        inequality2_2.set_color(PURPLE)
        inequality2_2.set_z_index(1)
        halfspace4 = Polygon(
            grid1.coords_to_point(-10, -10),
            grid1.coords_to_point(0, -10),
            grid1.coords_to_point(0, 0),
            grid1.coords_to_point(10, 10),
            grid1.coords_to_point(-10, 10),
            fill_color=PURPLE,
            fill_opacity=0.35,
            stroke_width=0
        )
        
        inequality3 = Line([2, -10, 1], [2, 10, 1])
        inequality3.set_color(YELLOW)
        halfspace5 = Polygon(
            grid1.coords_to_point(-10, -10),
            grid1.coords_to_point(2, -10),
            grid1.coords_to_point(2, 10),
            grid1.coords_to_point(-10, 10),
            fill_color=YELLOW,
            fill_opacity=0.35,
            stroke_width=0
        )
        
        inequality4_1 = Line([0, -10, 1], [0, 10, 1], stroke_width=1)
        inequality4_2 = Line([-10, 1, 1], [10, 1, 1])
        inequality4_1.set_color(GREEN)
        inequality4_1.set_z_index(1)
        inequality4_2.set_color(GREEN)
        halfspace6 = Polygon(
            grid1.coords_to_point(-10, 10),
            grid1.coords_to_point(-10, 1),
            grid1.coords_to_point(0, 1),
            grid1.coords_to_point(0, -10),
            grid1.coords_to_point(10, -10),
            grid1.coords_to_point(10, 10),
            fill_color=GREEN,
            fill_opacity=0.35,
            stroke_width=0
        )
        
        polyhedron = Polygon(
            grid1.coords_to_point(-2, 1),
            grid1.coords_to_point(0, 1),
            grid1.coords_to_point(0, 0),
            grid1.coords_to_point(2, 2),
            grid1.coords_to_point(2, 8),
            grid1.coords_to_point(-2, 8),
            fill_color=RED,
            fill_opacity=0.30,
            stroke_width=0
        )
        
        border_polyhedron1 = Line([-2, 10, 1], [-2, 1, 1])
        border_polyhedron1.set_color(RED)
        border_polyhedron2 = Line([-2, 1, 1], [0, 1, 1])
        border_polyhedron2.set_color(RED)
        border_polyhedron3 = Line([0, 1, 1], [0, -8, 1])
        border_polyhedron3.set_color(RED)
        border_polyhedron4 = Line([0, 0, 1], [2, 2, 1])
        border_polyhedron4.set_color(RED)
        border_polyhedron5 = Line([2, 2, 1], [2, 8, 1])
        border_polyhedron5.set_color(RED)
        
        #Now, animating
        # First frame on halfspace
        self.play(
            Write(title3),
            FadeIn(basel2, shift=UP),
        )
        self.wait(18)
        
        # Moving the halfspace on the top left corner
        self.play(
            Transform(basel2, transform_title2),
            LaggedStart(*[FadeOut(obj, shift=UP) for obj in title3]),
        )
        self.wait()
        
        # Drawing the grid
        self.play(FadeIn(grid1))
        self.wait()
        
        # Drawing the different halfspaces
        self.play(Write(inequality1))
        self.play(FadeIn(halfspace3))
        self.wait(8)
        self.play(FadeOut(halfspace3))
        self.wait()
        
        self.play(Write(inequality2_1), Write(inequality2_2))
        self.play(FadeIn(halfspace4))
        self.wait(16)
        self.play(FadeOut(halfspace4))
        self.wait()
        
        self.play(Write(inequality3))
        self.play(FadeIn(halfspace5))
        self.wait(8)
        self.play(FadeOut(halfspace5))
        self.wait()
        
        self.play(Write(inequality4_1), Write(inequality4_2))
        self.play(FadeIn(halfspace6))
        self.wait(16)
        self.play(FadeOut(halfspace6))
        
        self.play(
            Write(border_polyhedron1),
            Write(border_polyhedron2),
            Write(border_polyhedron3),
            Write(border_polyhedron4),
            Write(border_polyhedron5)
        )
        self.play(
            FadeOut(inequality1),
            FadeOut(inequality2_1),
            FadeOut(inequality2_2),
            FadeOut(inequality3),
            FadeOut(inequality4_1),
            FadeOut(inequality4_2)
        )
        self.play(FadeIn(polyhedron))
        self.wait(11)
        self.clear()

        grid2 = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-6, 6, 1),
            axis_config={
            "color": WHITE,  # color of the axes lines
            "stroke_width": 2,  # thickness of the axes lines
            "include_ticks": True,  # whether to include tick marks on the axes
            "include_numbers": True,  # whether to include numbers on the axes
            "label_direction": DOWN*2,  # direction of the axis labels
            "font_size": 20,  # font size of the axis labels
            },
            background_line_style = {
                "stroke_opacity": 0.4
            }
        )

        polyhedron1 = Polygon(
            grid2.coords_to_point(-2, 1),
            grid2.coords_to_point(0, 1),
            grid2.coords_to_point(0, 0),
            grid2.coords_to_point(2, 2),
            grid2.coords_to_point(2, 8),
            grid2.coords_to_point(-2, 8),
            fill_color=RED,
            fill_opacity=0.30,
            stroke_width=0
        )
        
        border_polyhedron6 = Line([-2, 10, 1], [-2, 1, 1])
        border_polyhedron6.set_color(RED)
        border_polyhedron7 = Line([-2, 1, 1], [0, 1, 1])
        border_polyhedron7.set_color(RED)
        border_polyhedron8 = Line([0, 1, 1], [0, -8, 1])
        border_polyhedron8.set_color(RED)
        border_polyhedron9 = Line([0, 0, 1], [2, 2, 1])
        border_polyhedron9.set_color(RED)
        border_polyhedron10 = Line([2, 2, 1], [2, 8, 1])
        border_polyhedron10.set_color(RED)

        # Pairs of inequalities to get the extreme points
        inequality5 = Line([-2, -10, 1], [-2, 10, 1])
        inequality5.set_color(BLUE)

        inequality6_1 = Line([0, 0, 1], [10, 10, 1])
        inequality6_2 = Line([0, -10, 1], [0, 0, 1])
        inequality6_1.set_color(PURPLE)
        inequality6_2.set_color(PURPLE)

        inequality7 = Line([2, -10, 1], [2, 10, 1])
        inequality7.set_color(YELLOW)

        inequality8_1 = Line([0, -10, 1], [0, 1, 1])
        inequality8_2 = Line([-10, 1, 1], [0, 1, 1])
        inequality8_1.set_color(GREEN)
        inequality8_2.set_color(GREEN)
        
        # Define the coordinates for the dot
        dot_coords1 = [-2, 1]
        dot_coords2 = [0, -3.9]
        dot_coords3 = [2, 2]

        # Create a Dot at the specified coordinates
        dot1 = Dot(grid2.coords_to_point(*dot_coords1), color=LOGO_GREEN)
        dot2 = Dot(grid2.coords_to_point(*dot_coords2), color=LOGO_GREEN)
        dot3 = Dot(grid2.coords_to_point(*dot_coords3), color=LOGO_GREEN)

        # Drawing the grid
        self.play(FadeIn(grid2))

        self.play(
            Write(border_polyhedron6),
            Write(border_polyhedron7),
            Write(border_polyhedron8),
            Write(border_polyhedron9),
            Write(border_polyhedron10)
        )

        self.play(FadeIn(polyhedron1))
        self.wait(28)
        
        self.play(FadeIn(inequality5), FadeIn(inequality6_1), FadeIn(inequality6_2))
        self.wait(3)
        self.play(FadeOut(inequality5), FadeOut(inequality6_1), FadeOut(inequality6_2))
        self.wait(2)
        
        self.play(FadeIn(inequality5), FadeIn(inequality7))
        self.wait(3)
        self.play(FadeOut(inequality5), FadeOut(inequality7))
        self.wait(2)

        self.play(FadeIn(inequality5), FadeIn(inequality8_1), FadeIn(inequality8_2))
        self.wait(3)
        self.play(FadeIn(dot1))
        self.wait(2)
        self.play(FadeOut(inequality5), FadeOut(inequality8_1), FadeOut(inequality8_2))
        self.wait(2)

        self.play(FadeIn(inequality6_1), FadeIn(inequality6_2), FadeIn(inequality7))
        self.wait(3)
        self.play(FadeIn(dot3))
        self.wait(2)
        self.play(FadeOut(inequality6_1), FadeOut(inequality6_2), FadeOut(inequality7))
        self.wait(2)

        self.play(FadeIn(inequality6_1), FadeIn(inequality6_2), FadeIn(inequality8_1), FadeIn(inequality8_2))
        self.wait(3)
        self.play(FadeIn(dot2))
        self.wait(2)
        self.play(FadeOut(inequality6_1), FadeOut(inequality6_2), FadeOut(inequality8_1), FadeOut(inequality8_2))
        self.wait(2)

        self.play(FadeIn(inequality7), FadeIn(inequality8_1), FadeIn(inequality8_2))
        self.wait(3)
        self.play(FadeOut(inequality7), FadeOut(inequality8_1), FadeOut(inequality8_2))
        self.wait(11)
        self.clear()

        end = Tex(r"Thank you for attention")
        end.set_color(LOGO_BLUE)

        self.play(FadeIn(end))
        self.wait(25)
