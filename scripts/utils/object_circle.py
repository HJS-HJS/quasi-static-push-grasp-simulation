from sympy import MatrixSymbol, symbols, ones, Matrix, cos, sin
import numpy as np

class ObjectCircle(object):
    '''
    2d object
    '''
    def __init__(self, q, v, radius, is_slider = False):
        self.radius = radius
        self.q = q
        self.v = v

        if is_slider: q = MatrixSymbol('qp_', 1, 3)

        self.r = ones(1)[0] * radius

        self.sym_t = symbols('t', real=True)

        self.m_fun = Matrix([
            q[0] + self.r*cos(self.sym_t),
            q[1] + self.r*sin(self.sym_t)
        ])

    def point_velocity(self, norm):
        _arr = np.array([[0, -1], [1, 0]])
        return self.v[2] * self.radius * _arr @ norm + self.v[:2]

    def points(self, q):
        t = np.linspace(0, np.pi * 2, 30)
        return np.array([self.m_fun.subs({self.sym_t: t_i, MatrixSymbol('qp_', 1, 3):Matrix(q.reshape(1,3))}) for t_i in t]).astype(np.float64).T.reshape(2, -1)
    
    