from PIL import Image, ImageDraw
import numpy as np

def rotate(point, phi):
    rotation_matrix = np.array([
        [ np.cos(phi), np.sin(phi)],
        [-np.sin(phi), np.cos(phi)]
    ])
    return point.dot(rotation_matrix)

def rad_to_euc(r, phi):
    x, y = rotate(np.array([r, r]), phi)
    return x, y

class LDrawPillow:
    def __init__(self, figure, canvas_color, line_width, line_color):
        self.figure = figure
        self.canvas_size = figure.size
        self.canvas_color = canvas_color
        self.line_width = line_width
        self.line_color = line_color
        self.canvas = self.draw_with_pill()

    def draw_with_pill(self):
        '''Draw figure'''
        canvas = Image.new('RGBA', self.canvas_size, self.canvas_color)
        draw = ImageDraw.Draw(canvas)
        start_point = self.figure.start_point
        step_length = self.figure.step_length
        line_width = self.line_width
        line_color = self.line_color
        angel = self.figure.angel
        xy_angel = np.pi
        save_angel = []
        for r in self.figure.rule:
            if r == 'F':
                end_point = start_point + np.array(rad_to_euc(step_length, xy_angel))
                draw.line([tuple(start_point), tuple(end_point)], fill=line_color, width=line_width)
                start_point = end_point
            elif r == 'f':
                start_point += np.array(rad_to_euc(figure.step_length, curr_angel))
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