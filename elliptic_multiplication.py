from point_class import point
from elliptic_addition import pointAddition

def pointMultiplication(p, A, B, F, scalar):
    if type(scalar) != int:
        raise ValueError("Scalar must be an integer")
    elif scalar < 0:
        raise ValueError("Scalar must be a positive integer")
    else:
        res = 0
        while scalar > 0:
            if scalar % 2 == 1:
                res = pointAddition(p, p, A, B, F) + g

            g = pointAddition(p, p, A, B, F)
            scalar = scalar // 2
        
        return res
    

print(pointMultiplication(point(9,7), 3, 8, 13, 2))