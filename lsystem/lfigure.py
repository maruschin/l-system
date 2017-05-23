# L-System package
import numpy as np

class LFigure:
    def __init__(self, lsystem, size):
        self.lsystem = lsystem
        self.rule = self.lsystem.rule
        self.angel = self.lsystem.angel
        self.make_dimensions(size)
    
    def make_dimensions(self, size):
        lines = make_dimensions(self.angel, self.rule, size)
        self.size = size
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
            lines.append(np.array([start_point, end_point]))
            start_point = end_point
            # Find min and max border of our figure
            dimension = lambda dim, dot: (min(dim[0], dot), max(dim[1], dot))
            x_dim = dimension(x_dim, end_point[0])
            y_dim = dimension(y_dim, end_point[1])
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
    
    # Move points to beginning of coordinate
    lines = [line-[x_dim[0], y_dim[0]] for line in lines]
    # Scale figure to fit in canvas
    scale = min(size[0]/sum([abs(x) for x in x_dim]),
                size[1]/sum([abs(y) for y in y_dim]))
    lines = [line*scale for line in lines]
    
    return lines


if __name__ == "__main__":
    pass