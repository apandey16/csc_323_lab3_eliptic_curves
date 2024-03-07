from findPoints import findRandomPoint
from point_class import ellipticCurve, regularPoint, originPoint, Point


def findPointWithOrder(curve, q, a):
    while True:
        point = findRandomPoint(curve) 
        m = point * (q // a)
        
        if m.is_origin() is not True:
            return m

curve = ellipticCurve(-95051, 118, 233970423115425145524320034830162017933)
curve_order = 233970423115425145528637034783781621127
desired_order = 4
point_with_order = findPointWithOrder(curve, curve_order, desired_order)
print(point_with_order)
