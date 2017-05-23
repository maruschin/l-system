from PIL import Image, ImageDraw, ImageFont
from math import pi, sin, cos

black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)
size  = (500, 500)

def draw_line_init(angel2, start=(250, 500), step=50, angel=pi/12, iterations=8):
    canvas = Image.new('RGBA', size, black)
    draw = ImageDraw.Draw(canvas)
    draw_line('A', draw, start, step, angel, 0, 0, iterations)
    return canvas

rules = {
    'A': 'ABABA',
    'B': 'A'
}

def draw_line(rule, draw, start, step, angel, curr_angel, curr_it, stop_it):
    if curr_it == stop_it:
        return "stop"
    
    for r in rule:
        curr_angel = curr_angel if r=='A' else curr_angel+angel
        end = (start[0] - step*sin(curr_angel), start[1] - step*cos(curr_angel))
        draw.line([start, end], fill=white, width=3)
        draw_line(rules[r], draw, end, step, angel, curr_angel, curr_it + 1, stop_it)  

canvas = [draw_line_init(angel2=pi/angel) for angel in range(1, 20)]
canvas[0].save('out.gif', save_all=True, duration=100, loop=100, append_images=canvas[0:])