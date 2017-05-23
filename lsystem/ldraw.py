# L-System package
from PIL import Image, ImageDraw

def draw_lines(lines):
    '''Draw figure'''
    black = (  0,   0,   0, 255)
    white = (255, 255, 255, 255)
    canvas = Image.new('RGBA', (1000, 1000), white)
    draw = ImageDraw.Draw(canvas)
    for line in lines:
        draw.line([tuple(line[0]), tuple(line[1])], fill=black, width=2)
    return canvas


if __name__ == "__main__":
    pass