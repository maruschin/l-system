# From The Algorithmic Beauty of Plants
# Chapter 1 - Graphical modeling using L-system
# 1.3 Turtle interpretation of strings
# Edge rewriting L-system

from PIL import Image, ImageDraw

import numpy as np

black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)
size  = (1000, 1000)

def deg_to_rad(deg):
    return np.pi/180*deg

iterations = 4
angel = deg_to_rad(22.5)
start_point = (500, 1000)
width_point = 2
step_length = 1
axiom = 'F'
producitons = {
    'F': 'F[FF+F][F]+F-F'
}

def rule_production(axiom, producitons, iterations):
    producitons['+'] = '+'
    producitons['-'] = '-'
    producitons['['] = '['
    producitons[']'] = ']'
    rule = axiom
    for i in range(iterations):
        rule = ''.join([producitons[s] for s in rule])
    return rule



def rad_to_euc(r, phi):
    x = r * np.sin(phi)
    y = r * np.cos(phi)
    return x, y

def draw_koch_islands(angel, rule, start_point, width_point, step_length):
    canvas = Image.new('RGBA', size, black)
    draw = ImageDraw.Draw(canvas)
    xy_angel = np.pi
    save_angel = []
    for r in rule:
        if r == 'F':
            end_point = start_point + np.array(rad_to_euc(step_length, xy_angel))
            draw.line([tuple(start_point), tuple(end_point)], fill=white, width=width_point)
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

rule = rule_production(axiom, producitons, iterations)

def make_dimensions(rule, size):
    '''Функция определяет необходимую длину шага для того, чтобы наша фигура
    поместилась на полотно заданного размера'''
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
            
start_point, step_length = make_dimensions(rule, size)
canvas = draw_koch_islands(angel, rule, start_point, width_point, step_length)

#canvas = draw_koch_islands(angel, rule, start_point,  3, 5)
canvas.show()