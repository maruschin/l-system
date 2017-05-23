from lsystem import LDrawPillow, LFigure, LSystem2D
black = (  0,   0,   0, 255)
white = (255, 255, 255, 255)

iterations = 3
angel = 90 # In gradus
axiom = 'F-F-F-F'
productions = {
    'F': 'F-F+F+FF-F-F+F',
}

# Make figure example of class
lsystem = LSystem2D(axiom, productions, iterations, angel)
figure  = LFigure(lsystem, size=(1000, 1000))
canvas  = (LDrawPillow(figure, canvas_color=white, line_width=2, line_color=black)).canvas
#canvas = draw_lines(figure, canvas_color=white, line_width=2, line_color=black)
canvas.show()