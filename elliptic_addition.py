import math

class point:
    def __init__(self, x, y, origin=False):
        self.origin = origin
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
            #might need to add y check later
            return(self.x == other.x)
    
    def __str__(self):
        if self.origin:
            return "O"
        else:
            return f"({self.x}, {self.y})"
    

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

def pointAddition(p1, p2, A, B, F):
    if p1.origin:
        return p2
    
    elif p2.origin:
        return p1
    
    elif p1 == p2:
        # add code for finding the tangent and the thrid point
        return intersectionPointTangent(p1, p2, A, F)

    elif p1.isInverse(p2):
        # if they are the inverse then return the origin
        return point(None, None, True)
    
    else:
        #if they aren't inversese or equal, this is the general case and we need the intersection point
        return intersectionPoint(p1, p2, F)

if __name__ =="__main__":

    print(pointAddition(point(9,7), point(1,8), 3, 8, 13))
    print()
    print(pointAddition(point(9,7), point(9,7), 3, 8, 13))
    print()
    print(pointAddition(point(12,11), point(12,2), 3, 8, 13))
