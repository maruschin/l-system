# From The Algorithmic Beauty of Plants
# Chapter 1 - Graphical modeling using L-system
# 1.3 Turtle interpretation of strings
# Edge rewriting L-system

from PIL import Image, ImageDraw

import numpy as np

class LSystem2D:
    def __init__(self, axiom, productions, iterations, angel):
        self.axiom = axiom
        self.productions = productions
        self.iterations = iterations
        self.grad = angel
        self.angel = self.__ang_to_rad(angel)
        self.__make_rule()
    
    def __repr__(self):
        string = "axiom: " + str(self.axiom) + '\n' +\
        "productions: " + str(self.productions) + '\n' +\
        "iterations: " + str(self.iterations) + '\n' +\
        "angel: " + str(self.grad) + '°'
        return string
        
    def __ang_to_rad(self, deg):
        return np.pi/180*deg
    
    def __make_rule(self):
        rule = self.axiom
        productions = self.productions.copy()
        productions['+'] = '+'
        productions['-'] = '-'
        productions['['] = '['
        productions[']'] = ']'
        for i in range(self.iterations):
            rule = ''.join([productions[s] for s in rule])
        self.rule = rule


class LFigure:
    def __init__(self, lsystem, size):
        self.lsystem = lsystem
        self.rule = self.lsystem.rule
        self.angel = self.lsystem.angel
        self.make_dimensions(size)
    
    def make_dimensions(self, size):
        lines, center, step = make_dimensions(self.angel, self.rule, size)
        self.size = size
        self.start_point = center
        self.step_length = step
        self.lines = lines

def rotate(point, phi):
    rotation_matrix = np.array([
        [ np.cos(phi), np.sin(phi)],
        [-np.sin(phi), np.cos(phi)]
    ])
    return point.dot(rotation_matrix)

def rad_to_euc(r, phi):
    x, y = rotate(np.array([r, r]), phi)
    return x, y

def draw_koch_islands(figure, canvas_color, line_width, line_color):
    '''Draw figure'''
    canvas = Image.new('RGBA', figure.size, canvas_color)
    draw = ImageDraw.Draw(canvas)
    start_point = figure.start_point
    xy_angel = np.pi
    save_angel = []
    for r in figure.rule:
        if r == 'F':
            end_point = start_point + np.array(rad_to_euc(figure.step_length, xy_angel))
            draw.line([tuple(start_point), tuple(end_point)], fill=line_color, width=line_width)
            start_point = end_point
        elif r == 'f':
            start_point += np.array(rad_to_euc(figure.step_length, curr_angel))
        elif r == '-':
            xy_angel -= figure.angel
        elif r == '+':
            xy_angel += figure.angel
        elif r == '[':
            save_angel.append((xy_angel, start_point.copy()))
        elif r == ']':
            xy_angel, start_point = save_angel.pop()
        else:
            pass
    return canvas

def draw_lines(figure, canvas_color, line_width, line_color):
    '''Draw figure'''
    canvas = Image.new('RGBA', figure.size, canvas_color)
    draw = ImageDraw.Draw(canvas)
    for line in figure.lines:
        draw.line([tuple(line[0]), tuple(line[1])], fill=line_color, width=line_width)
    return canvas

def make_dimensions(angel, rule, size):
    '''Count step length and start point to fit in canvas size'''
    x_dim = y_dim = np.array((0, 0))
    start_point = np.array((0,0), dtype='float64')
    curr_angel = np.pi
    save_angel = []
    step_length = 1
    lines = []
    for r in rule:
        if r in 'fF':
            end_point = start_point + np.array(rad_to_euc(step_length, curr_angel))
            lines.append([start_point, end_point])
            start_point = end_point
            # Find min and max border of our figure
            dimension = lambda dim, dot: (min(dim[0], dot), max(dim[1], dot))
            x_dim = dimension(x_dim, end_point[0])
            y_dim = dimension(y_dim, end_point[1])
            #x_dim = min(x_dim[0], end_point[0]), max(x_dim[1], end_point[0])
            #y_dim = min(y_dim[0], end_point[1]), max(y_dim[1], end_point[1])
        elif r == '-':
            curr_angel -= angel
        elif r == '+':
            curr_angel += angel
        elif r == '[':
            save_angel.append((curr_angel, start_point.copy()))
        elif r == ']':
            curr_angel, start_point = save_angel.pop()
        else:
            pass
    
    x_width = sum([abs(x) for x in x_dim])
    y_width = sum([abs(y) for y in y_dim])
    
    step = np.floor(min(size[0]/(x_width), size[1]/(y_width)))
    step = step if step > 1 else 1
    
    center = np.array((abs(x_dim[0])*step + (size[0] - x_width * step)/2,
                       abs(y_dim[0])*step + (size[1] - y_width * step)/2))
    lines = [line+center for line in lines]
    return lines, center, step


if __name__ == "__main__":
    black = (  0,   0,   0, 255)
    white = (255, 255, 255, 255)
    
    iterations = 3
    angel = 90 # In gradus
    start_point = (500, 1000)
    axiom = 'F-F-F-F'
    productions = {
        'F': 'F-F+F+FF-F-F+F',
    }
    
    # Make figure example of class
    lsystem = LSystem2D(axiom, productions, iterations, angel)
    figure = LFigure(lsystem, size=(1000, 1000))
    canvas = draw_koch_islands(figure, canvas_color=white, line_width=2, line_color=black)
    #canvas = draw_lines(figure, canvas_color=white, line_width=2, line_color=black)
    canvas.show()