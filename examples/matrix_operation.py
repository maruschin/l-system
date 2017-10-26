import numpy as np

def rotation_gen(phi, axis):
    cos = np.cos(phi)
    sin = np.sin(phi)
    rotation_matrix_xyz ={
    'x': np.array([
        [    1,    0,    0],
        [    0,  cos, -sin],
        [    0,  sin,  cos],
        ]),
    'y': np.array([
        [  cos,    0, sin],
        [    0,    1,   0],
        [ -sin,    0, cos],
        ]),
    'z': np.array([
        [  cos, -sin,   0],
        [  sin,  cos,   0],
        [    0,    0,   1],
        ]),
    }
    def rotation_axis(point):
        rotation_matrix_axis = rotation_matrix_xyz[axis]
        return point.dot(rotation_matrix_axis)
    return rotation_axis

rotation_zzz = rotation_gen(np.pi/2, 'x')
foo = rotation_zzz(np.array([1, 1, 1]))

print(foo)