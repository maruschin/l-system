# L-System package
from lsystem import draw_lines, LFigure, LSystem2D

def main():
    # Def colors
    black = (  0,   0,   0, 255)
    white = (255, 255, 255, 255)
    # Def figure
    iterations = 7
    angel = 25 # In gradus
    axiom = 'f'
    productions = {
        'f': 'F-[[f]+f]+F[+Ff]-f',
        'F': 'FF',
    }
    
    lsystem = LSystem2D(axiom, productions, iterations, angel)
    figure = LFigure(lsystem, size=(1000, 1000))
    canvas = draw_lines(figure.lines)
    canvas.show()


if __name__ == "__main__":
    main()