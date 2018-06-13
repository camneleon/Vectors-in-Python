from math import sqrt, acos, degrees


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise TypeError
            self.coordinates = tuple([i for i in coordinates])
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError
        except TypeError:
            raise TypeError

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, vec):
        return self.coordinates == vec.coordinates

    def __add__(self, vec):
        return [a + b for a, b in zip(self.coordinates, vec.coordinates)]

    def __sub__(self, vec):
        return [a - b for a, b in zip(self.coordinates, vec.coordinates)]

    def __mul__(self, num):
        return [num * i for i in self.coordinates]

    # ------------------------------------------------------------------
    # Function based add, sub, and scalar returns a new Vector
    # ------------------------------------------------------------------
    def add(self, vec):
        cords = [a + b for a, b in zip(self.coordinates, vec.coordinates)]
        return Vector(cords)

    def sub(self, vec):
        cords = [a - b for a, b in zip(self.coordinates, vec.coordinates)]
        return Vector(cords)

    def scalar(self, num):
        cords = [num * i for i in self.coordinates]
        return Vector(cords)

    def magnitude(self):
        """Returns Magnitude ||v||
        (sq-root of the sumed sq vector components)"""

        sq_cords = [i**2 for i in self.coordinates]
        return sqrt(sum(sq_cords))

    def normalize(self):
        """Returns unit vector (vector of length 1) =
        norm of vector v / ||v||"""

        try:
            magnitude = self.magnitude()
            return self.scalar(1.0/magnitude)
        except ZeroDivisionError:
            raise Exception("CANNOT NORMALIZE VECTOR WITH ZERO")

    def dot(self, vec):
        """Returns DOT Product a . b = ax * bx + ay * by"""

        return sum([a * b for a, b in zip(self.coordinates, vec.coordinates)])

    def deg_angle_of(self, vec):
        """Returns Angle between two vectors. deg = acos(a . b / (||a|| ||b||))
        NOTE: python's acos returns radian convert with degrees function"""

        return degrees(acos(self.dot(vec) /
                            (self.magnitude() *
                            vec.magnitude())))

    def cross_product(self, vec):
        """Returns Cross Product of two vectors (a, b) with 3 or more coordinates
        a X b =
        Cx = ay * bz - az * by
        Cy = az * bx - ax * bz
        Cz = ax * by - ay * bx """

        ax, ay, az = self.coordinates
        bx, by, bz = vec.coordinates
        c = [(ay * bz - az * by),
             (az * bx - ax * bz),
             (ax * by - ay * bx)]
        return c

    def is_orthogonal(self, vec, tolerance=1e-10):
        """Returns Boolean if orthogonal or not"""

        return abs(self.dot(vec)) < tolerance

    def is_zero(self, tolerance=1e-10):
        """Returns Boolean if zero or not"""

        return self.magnitude() < tolerance

    def is_parallel(self, vec):
        """Returns Boolean if parallel or not"""

        return (self.is_zero or
                vec.is_zero or
                self.deg_angle_of(vec) == 0)
