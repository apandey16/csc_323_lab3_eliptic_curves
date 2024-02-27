import math

class point:
    def __init__(self, x, y, origin=False):
        if self.origin is False:
            self.x = x
            self.y = y
        else:
            self.origin = True

    def __eq__(self, value: object) -> bool:
        if self.origin or value.origin:
            return self.origin == value.origin
        else:
            return(self.x == value.x and self.y == value.y)
    
    def isInverse(self, other) -> bool:
        if self.origin or other.origin:
            return self.origin == other.origin
        else:
            return(self.x == other.x and self.y == -1 * other.y)
    

def calcSlope( p1, p2 ):
    return (p2.y - p1.y)/(p2.x - p1.x)

def intersectionPoint (p1, p2, F):
    m = calcSlope(p1, p2)

    retX = m^2 - p2.x - p1.x
    retY = p2.y + m(retX - p2.x)

    return point(pow(retX, 1,  F), pow(retY, 1, F))

def tanSlope(p, A):
    return (3 * p.x^2 + A) / (2 * p.y)

def intersectionPointTangent(p1, p2, A, F):
    m = tanSlope(p1, A)

    retX = m^2 - p2.x - p1.x
    retY = p2.y + m(retX - p2.x)

    return point(pow(retX, 1,  F), pow(retY, 1, F))

def pointAddition(p1, p2, A, F):
    if p1.origin:
        return p2
    
    elif p2.origin:
        return p1
    
    elif p1 == p2:
        # add code for finding the tangent and the thrid point
        print("equal")
        return intersectionPointTangent(p1, p2, A, F)

    elif p1.isInverse(p2):
        # if they are the inverse then return the origin
        return point(0, 0, True)
    
    else:
        #if they aren't inversese or equal, this is the general case and we need the intersection point
        print("gen case")
        return intersectionPoint(p1, p2, F)
    