import sys

sys.path.insert(0, '../..')

from lsystem import draw_koch_islands, LFigure, LSystem2D
black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)

iterations = 3
angel = 90 # In gradus
axiom = 'F-F-F-F'
productions = {
    'F': 'F-F+F+FF-F-F+F',
}

for i in range(1, 4):
    # Make figure example of class
    lsystem = LSystem2D(axiom, productions, i, angel)
    figure  = LFigure(lsystem, size=(1000, 1000))
    canvas  = draw_koch_islands(figure, canvas_color=white, line_width=2, line_color=black)
    canvas.save('quadratic Koch island - %s.png' % i)