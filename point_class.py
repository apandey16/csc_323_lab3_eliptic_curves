def bits(n):
    while n:
        yield n & 1
        n >>= 1

class ellipticCurve:
    def __init__(self, A, B, field):
        self.A = A
        self.B = B
        self.field = field
    
        def __str__(self) -> str:
            return f"Curve: Y^2 = X^3 + {self.A}X + {self.B} over field {self.field}"
        

class Point:
    def __init__(self, curve: ellipticCurve):
        self.curve = curve

    def __add__(self, p):
        match self:
            case originPoint():
                return p
            case regularPoint():
                pass
            case _:
                raise TypeError(f"Attempting to add a non-point: {p}")
        # If we're here, self must be an regularPoint
        match p:
            case originPoint():
                return self
            case regularPoint():
                f = self.curve.field
                if self.x == p.x and pow(self.y + p.y, 1, f) == 0:
                    return originPoint(self.curve)
                if self.x == p.x and self.y == p.y:
                    m = (3 * pow(self.x, 2, f) + self.curve.A) * pow(2 * self.y, -1, f)
                else:
                    m = (p.y - self.y) * pow(p.x - self.x, -1, f)
                m = pow(m, 1, f)
                nx = pow((pow(m, 2, f) - self.x - p.x), 1, f)
                ny = pow(m * (self.x - nx) - self.y, 1, f)
                return regularPoint(self.curve, x=nx, y=ny)
            case _:
                raise TypeError(f"Attempting to add a non-point: {p}")

    def __mul__(self, scalar: int):
        if not isinstance(scalar, int):
            raise TypeError(f"Attempting to multiply a point by a non-int: {scalar = }")
        if scalar < 0:
            raise ValueError(f"Attempting to multiply point by a negative value: {scalar = }")
        res = originPoint(self.curve)
        p = self
        for b in bits(scalar):
            if b:  # odd
                res += p
            p = p + p
        return res

    def __rmul__(self, scalar: int):
        return self.__mul__(scalar)


class originPoint(Point):
    def __str__(self):
        return "Origin"

    def is_origin(self):
        return True


class regularPoint(Point):
    def __init__(self, curve: ellipticCurve, x: int, y: int):
        super().__init__(curve)
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def is_origin(self):
        return False
    
# print(regularPoint(ellipticCurve(3,8,13),12,11) + regularPoint(ellipticCurve(3,8,13),12,2))