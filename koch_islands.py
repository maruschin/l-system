from PIL import Image, ImageDraw, ImageFont
from math import pi, sin, cos

black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)
size  = (500, 500)

n = 2
beta = pi/2
rules = {
    'F': 'F-F+F+FF-F-F+F',
}

def return_rule(start, rule):
    end = ''
    for s in start:
        if s=='F':
            end += rule['F']
        else:
            end += s
    return end

def make_rule(start, rule, iterations):
    for i in range(iterations):
        start = return_rule(start, rule)
    return start

assert return_rule(return_rule('F-F-F-F', rules), rules) == \
       make_rule('F-F-F-F', rules, 2)


rule = make_rule('F-F-F-F', rules, 2)

def draw_koch_islands(start, rule, step, angel):
    canvas = Image.new('RGBA', size, black)
    draw = ImageDraw.Draw(canvas)
    curr_angel = angel
    for r in rule:
        if r == 'F':
            end = (start[0] - step*sin(curr_angel), start[1] - step*cos(curr_angel))
            draw.line([start, end], fill=white, width=3)
            start = end
        elif r == 'f':
            end = (start[0] - step*sin(curr_angel), start[1] - step*cos(curr_angel))
            start = end
        elif r == '-':
            curr_angel -= angel
        elif r == '+':
            curr_angel += angel
    return canvas

canvas = draw_koch_islands((250, 250), rule, 10, pi/2)
canvas.show()