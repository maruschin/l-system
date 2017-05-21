# From The Algorithmic Beauty of Plants
# Chapter 1 - Graphical modeling using L-system
# 1.3 Turtle interpretation of strings
# Edge rewriting L-system

from PIL import Image, ImageDraw

import numpy as np

black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)
size  = (1000, 1000)

iterations = 4
angel = 22.5 # In gradus
start_point = (500, 1000)
width_point = 2
step_length = 1
axiom = 'F'
productions = {
    'F': 'F[FF+F][F]+F-F'
}

class LSystem2D:
    def __init__(self, axiom, productions, iterations, angel):
        self.axiom = axiom
        self.productions = productions
        self.iterations = iterations
        self.angel = self.ang_to_rad(angel)
    
    def ang_to_rad(self, deg):
        return np.pi/180*deg
    
    def make_rule(self):
        rule = self.axiom
        productions = self.productions
        productions['+'] = '+'
        productions['-'] = '-'
        productions['['] = '['
        productions[']'] = ']'
        for i in range(self.iterations):
            rule = ''.join([productions[s] for s in rule])
        self.rule = rule


def rotate(point, phi):
    rotation_matrix = [
        [ np.cos(phi), np.sin(phi)],
        [-np.sin(phi), np.cos(phi)]
    ]
    return point.dot(rotation_matrix)

def rad_to_euc(r, phi):
    x, y = rotate(np.array([r, r]), phi)
    return x, y

def draw_koch_islands(angel, rule, start_point, width_point, step_length):
    '''Draw figure'''
    canvas = Image.new('RGBA', size, white)
    draw = ImageDraw.Draw(canvas)
    xy_angel = np.pi
    save_angel = []
    for r in rule:
        if r == 'F':
            end_point = start_point + np.array(rad_to_euc(step_length, xy_angel))
            draw.line([tuple(start_point), tuple(end_point)], fill=black, width=width_point)
            start_point = end_point
        elif r == 'f':
            start_point += np.array(rad_to_euc(step_length, curr_angel))
        elif r == '-':
            xy_angel -= angel
        elif r == '+':
            xy_angel += angel
        elif r == '[':
            save_angel.append((xy_angel, start_point.copy()))
        elif r == ']':
            xy_angel, start_point = save_angel.pop()
        else:
            pass
    return canvas

def make_dimensions(angel, rule, size):
    '''Count step length and start point to fit in canvas size'''
    x_dim = y_dim = np.array((0, 0))
    xy_point = np.array((0,0), dtype='float64')
    curr_angel = np.pi
    save_angel = []
    for r in rule:
        if r in 'fF':
            xy_point += np.array(rad_to_euc(step_length, curr_angel))
            x_dim = min(x_dim[0], xy_point[0]), max(x_dim[1], xy_point[0])
            y_dim = min(y_dim[0], xy_point[1]), max(y_dim[1], xy_point[1])
        elif r == '-':
            curr_angel -= angel
        elif r == '+':
            curr_angel += angel
        elif r == '[':
            save_angel.append((curr_angel, xy_point.copy()))
        elif r == ']':
            curr_angel, xy_point = save_angel.pop()
        else:
            pass
    
    x_width = sum([abs(x) for x in x_dim])
    y_width = sum([abs(y) for y in y_dim])
    step = np.floor(min(size[0]/(x_width), size[1]/(y_width)))
    step = step if step > 1 else 1
    
    center = np.array((abs(x_dim[0])*step + (size[0] - x_width * step)/2,
                       abs(y_dim[0])*step + (size[1] - y_width * step)/2))
    
    return center, step

figure = LSystem2D(axiom, productions, iterations, angel)
figure.make_rule()

# Count step length and start point to fit in canvas size
start_point, step_length = make_dimensions(figure.angel, figure.rule, size)

# Draw image
canvas = draw_koch_islands(figure.angel, figure.rule, start_point, width_point, step_length)
canvas.show()