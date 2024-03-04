from elliptic_addition import pointAddition

class Curve:
    def __init__(self, a: int, b: int, field: int):
        self.a = a
        self.b = b
        self.field = field
        
    def __str__(self):
        return f"Curve: Y^2 = X^3 + {self.a}X + {self.b} over field {self.field}"


class point:
    curve: Curve

    def __init__(self, x, y, origin=False):
        self.origin = origin
        if self.origin is False:
            self.x = x
            self.y = y
        else:
            self.origin = True
            
    def __str__(self):
        return f"({self.x}, {self.y})"

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
    
    def __str__(self):
        if self.origin:
            return "O"
        else:
            return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return pointAddition(self, other, self.curve.a, self.curve.b, self.curve.field)