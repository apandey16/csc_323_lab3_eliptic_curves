# from elliptic_addition import intersectionPointTangent

def calcSlope( p1, p2, F ):
    return (p2.y - p1.y) * pow((p2.x - p1.x), -1, F)

def intersectionPoint (p1, p2, F):
    m = pow(calcSlope(p1, p2, F), F)

    retX = pow(m, 2, F) - p2.x - p1.x
    retY = pow(m * (p1.x - retX) - p1.y, 1, F)

    return point(pow(retX, 1,  F), pow(retY, 1, F))

def tanSlope(p, A, F):
    return pow((3 *  pow(p.x, 2, F) + A), 1, F) * pow((2 * p.y), -1, F)

def intersectionPointTangent(p1, p2, A, F):
    m = pow(tanSlope(p1, A, F), 1, F)

    retX = pow(m, 2, F) - p2.x - p1.x
    retY = pow(m*(p2.x - retX) -p2.y, 1, F)

    return point(pow(retX, 1,  F), pow(retY, 1, F))

class Curve:
    def __init__(self, a: int, b: int, field: int):
        self.a = a
        self.b = b
        self.field = field
        
    def __str__(self):
        return f"Curve: Y^2 = X^3 + {self.a}X + {self.b} over field {self.field}"


class point:

    def __init__(self, x, y, curve, origin=False):
        self.origin = origin
        if self.origin is False:
            self.x = x
            self.y = y
            self.curve = curve
        else:
            self.origin = True
            self.curve = curve


    def __eq__(self, value: object) -> bool:
        if self.origin or value.origin:
            return self.origin == value.origin
        else:
            return(self.x == value.x and self.y == value.y)
    
    def isInverse(self, other) -> bool:
        if self.origin or other.origin:
            return self.origin == other.origin
        else:
            #might need to add y check later
            return(self.x == other.x)

    def __add__(self, p):
        if self.origin:
            return p
        elif p.origin:
            return self
        elif self == p:
            return intersectionPointTangent(self, p, self.curve.a, self.curve.field)
        elif self.isInverse(p):
            # if they are the inverse then return the origin
            return point(None, None, True)
        else:
            #if they aren't inversese or equal, this is the general case and we need the intersection point
            return intersectionPoint(self, p, self.curve.field)
    
    def __mul__(self, scalar):
        if type(scalar) != int:
            raise ValueError("Scalar must be an integer")
        elif scalar < 0:
            raise ValueError("Scalar must be a positive integer")
        else:
            res = 0
            while scalar > 0:
                if scalar % 2 == 1:
                    res = self + self

                self = self + self
                scalar = scalar // 2
            
            return res