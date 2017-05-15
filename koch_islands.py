# From The Algorithmic Beauty of Plants
# Chapter 1 - Graphical modeling using L-system
# 1.3 Turtle interpretation of strings
# Edge rewriting L-system

from PIL import Image, ImageDraw, ImageFont
from math import pi, sin, cos, floor

black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)
size  = (1000, 1000)

iterations = 4
angel = pi/3
start_point = (450, 450)
width_point = 1
step_length = 1
rule = 'L'
producitons = {
    'L': 'L+R++R-L--LL-R+',
    'R': '-L+RR++R+L--L-R'
}

def rule_production(rule, producitons, iterations):
    producitons['+'] = '+'
    producitons['-'] = '-'
    for i in range(iterations):
        rule = ''.join([producitons[s] for s in rule])
    return rule

def draw_koch_islands(angel, rule, start_point, width_point, step_length):
    canvas = Image.new('RGBA', size, black)
    draw = ImageDraw.Draw(canvas)
    curr_angel = angel
    for r in rule:
        if r in 'FLR':
            end_point = (start_point[0] - step_length*cos(curr_angel),
                         start_point[1] - step_length*sin(curr_angel))
            draw.line([start_point, end_point], fill=white, width=width_point)
            start_point = end_point
        elif r == 'f':
            end_point = (start_point[0] - step_length*cos(curr_angel),
                         start_point[1] - step_length*sin(curr_angel))
            start_point = end_point
        elif r == '-':
            curr_angel -= angel
        elif r == '+':
            curr_angel += angel
        else:
            pass
    return canvas

rule = rule_production(rule, producitons, iterations)

def make_dimensions(size=(600, 600)):
    '''Функция определяет необходимую длину шага для того, чтобы наша фигура
    поместилась на полотно заданного размера'''
    start_point = (0, 0)
    x_dim, y_dim = (0, 0), (0, 0)
    curr_angel = angel
    for r in rule:
        if r in 'fFLR':
            end_point = (start_point[0] - cos(curr_angel),
                         start_point[1] - sin(curr_angel))
            start_point = end_point
            x_dim = min(x_dim[0], end_point[0]), max(x_dim[1], end_point[0])
            y_dim = min(y_dim[0], end_point[1]), max(y_dim[1], end_point[1])
        elif r == '-':
            curr_angel -= angel
        elif r == '+':
            curr_angel += angel
    
    x_width = sum([abs(x) for x in x_dim])
    y_width = sum([abs(y) for y in y_dim])
    step = floor(min(size[0]/(x_width), size[1]/(y_width)))
    step = step if step > 1 else 1
    
    center = (abs(x_dim[0])*step + (size[0] - x_width * step)/2,
              abs(y_dim[0])*step + (size[1] - y_width * step)/2)
    
    return center, step
            
start_point, step_length = make_dimensions(size)
canvas = draw_koch_islands(angel, rule, start_point, width_point, step_length)

#canvas = draw_koch_islands(angel, rule, (300, 300),  3, 5)
canvas.show()