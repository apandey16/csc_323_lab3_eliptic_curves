import random
from point_class import ellipticCurve, regularPoint

def find_random_point(curve):
    p = curve.field
    A = curve.A
    B = curve.B

    while True:
        x = random.randint(0, p-1)
        n = pow(x, 3, p) + A * x + B

        if eulerCriterion(n, p):
            y = tonelliShanks(n, p)
            return regularPoint(curve, x, y)

def eulerCriterion(n, p):
    return pow(n, (p-1)//2, p) == 1

def tonelliShanks(n, p):
    Q = p - 1
    S = 0

    while Q % 2 == 0:
        Q = Q // 2
        S += 1

    if S == 1:
        return pow(n, (p + 1) // 2, p)


    M = S
    R = pow(n, (Q + 1) // 2, p)
    t = pow(n, Q, p)


    for z in range(2, p):
        if p - 1 == pow(z, (p-1)//2, p):
            break
    
    c = pow(z, Q, p)

    while True:
        if t == 0:
            return 0
        elif t == 1:
            return R

        i = 0
        for i in range(1, M):
            if pow(t, pow(2, i), p) == 1:
                break

        b = pow(c, pow(2, M-i-1), p)
        M = i
        t = pow((t * pow(b, 2, p)), 1, p)
        c = pow(b, 2, p)
        R = pow((R * b), 1, p)
        

print(find_random_point(ellipticCurve(1, 1, 17)) )