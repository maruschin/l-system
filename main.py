# L-System package
import numpy as np

from lsystem import draw_lines, LFigure, LSystem2D

def main():
    # Def colors
    black = (  0,   0,   0, 255)
    white = (255, 255, 255, 255)
    # Def figure
    iterations = 3
    angel = 90 # In gradus
    axiom = 'F-F-F-F'
    productions = {
        'F': 'F-F+F+FF-F-F+F',
    }
    
    lsystem = LSystem2D(axiom, productions, iterations, angel)
    figure = LFigure(lsystem, size=(1000, 1000))
    canvas = draw_lines(figure.lines)
    canvas.show()


if __name__ == "__main__":
    main()