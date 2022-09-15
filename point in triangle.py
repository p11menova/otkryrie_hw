from math import sqrt


class Point:
    def __init__(self, x, y, name=''):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return f'{self.name}', self.x, self.y


class Triangle:
    def __init__(self, A: Point, B: Point, C: Point):
        self.A = A
        self.B = B
        self.C = C
        self.bc = length(B, C)
        self.ac = length(A, C)
        self.ab = length(A, B)

    def get_coords(self):
        return self.A.get_coords(), self.B.get_coords(), self.C.get_coords()

    def get_halfperimetr(self):
        return (self.ab+self.bc+self.ac)/2

    def get_square(self):
        p = self.get_halfperimetr()
        return sqrt(p*(p-self.ab)*(p-self.bc)*(p-self.ac))


def length(start: Point, finish: Point):
    return sqrt((start.get_x() - finish.get_x()) ** 2 + (start.get_y() - finish.get_y()) ** 2)


A = Point(1, 1, 'A')
B = Point(1, 5, 'B')
C = Point(6, 1, 'C')

tr = Triangle(A, B, C)

M = Point(3, 3, 'M')

tr1 = Triangle(A, B, M)
tr2 = Triangle(A, C, M)
tr3 = Triangle(B, C, M)
# print(tr1.get_square(),  tr2.get_square(),  tr3.get_square(), tr.get_square(), 'сумма', tr1.get_square() + tr2.get_square() + tr3.get_square(), sep='\n')
if int(tr.get_square()) - int(tr1.get_square() + tr2.get_square() + tr3.get_square()) <= 1:
    print('yes!')
else:
    print('no')


