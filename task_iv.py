import math
from point_class import ellipticCurve, regularPoint, originPoint, Point
from findOrder import findPointWithOrder
from task_III import func, basePointOrder, basePoint, calculate_hmac

def find_prime_factors(n, curveOrder):
    factors = []
    i = 2
    while i * i <= n and i < 2**16:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append((i, curveOrder))
    if n > 1 and n < 2**16:
        factors.append((n, curveOrder))
    return factors

# prime_number = 233970423115425145528637034783781621127
# factors = find_prime_factors(prime_number)
# print(factors)

curve0 = ellipticCurve(-95051, 118, 233970423115425145524320034830162017933) #order: 233970423115425145528637034783781621127

curve1 = ellipticCurve(-95051, 727, 233970423115425145524320034830162017933) #order: 233970423115425145545378039958152057148 [USE THIS]

curve2 = ellipticCurve(-95051, 210, 233970423115425145524320034830162017933) #order: 233970423115425145550826547352470124412 [USE THIS]

curve5 = ellipticCurve(-95051, 79, 233970423115425145524320034830162017933) #order: 233970423115425145538546862144009931013

curve7 = ellipticCurve(-95051, 504, 233970423115425145524320034830162017933) #order: 233970423115425145544350131142039591210 [USE THIS]

curves = [curve0, curve1, curve2, curve5, curve7]
curveOrdersDict = {233970423115425145528637034783781621127 : curve0, 233970423115425145545378039958152057148 : curve1, 233970423115425145550826547352470124412 : curve2, 233970423115425145538546862144009931013: curve5, 233970423115425145544350131142039591210: curve7}
curveOrders = [233970423115425145528637034783781621127, 233970423115425145545378039958152057148, 233970423115425145550826547352470124412 , 233970423115425145538546862144009931013, 233970423115425145544350131142039591210]

curveWithOrders = []
curveIdx = []
curveFactors = []

for i in range(0, len(curveOrders)):
    curFactors = find_prime_factors(curveOrders[i], curveOrders[i])
    print(curFactors)

    if len(curFactors) == 0:
        continue
    else:
        print(i)
        curveWithOrders.append((curves[i], curveOrders[i]))
        curFactors.reverse()
        curveFactors.append((curFactors))
        curveIdx.append(i)

curveFactorsCombined = []
for element in curveFactors:
    for val in element:
        curveFactorsCombined.append(val)

curveFactorsCombined.sort(reverse=True)
# print((curveFactorsCombined))

neededFactors = []

runningTotal = 1

for pair in curveFactorsCombined:
    if runningTotal * pair[0] <= basePointOrder:
        runningTotal *= pair[0]
        neededFactors.append(pair)
    else:
        neededFactors.append(pair)
        break

print(len(neededFactors))

generatedHMACKeys = []
for element in neededFactors:
    curOrder = element[1]
    curFactor = element[0]
    curCurve = curveOrdersDict[curOrder]
    newPoint = findPointWithOrder(curCurve, curOrder, curFactor)
    print(newPoint)
    secret_point = func(newPoint.x, newPoint.y, curCurve, curOrder)
    print(secret_point)
    generatedHMACKeys.append((secret_point, element[0]))

print(generatedHMACKeys)
    
facrtorsProduct = 1
for factor in generatedHMACKeys:
    facrtorsProduct *= factor[1]

adminKey = 0
for reminder, key in generatedHMACKeys:
    m = facrtorsProduct // key
    m_inv = pow(m, -1, key)
    adminKey += reminder * m * m_inv
adminKey = adminKey % facrtorsProduct
print(adminKey)

adminPK = basePoint * adminKey
print(adminPK)
print(adminPK.x, adminPK.y)
bobPk = regularPoint(ellipticCurve(-95051, 11279326, 233970423115425145524320034830162017933), 71654914371588382575325480982820604222, 177614151357791846076138011377300626224)
sharedKey = bobPk * adminKey
print(calculate_hmac("test", sharedKey).hexdigest())


# for group in range(len(curveFactors)):
#     tempFactors =[]
#     runningTotal = 1
#     curOrder = curveOrders[curveIdx[group]]
#     print(curOrder)
    
#     for factor in curveFactors[group]:
#         if runningTotal * factor < curOrder:
#             runningTotal *= factor
#             tempFactors.append(factor)
#             print(factor)
#         else:
#             strippedFactors.append(tempFactors)
#             break

# print(strippedFactors)


# print(curveWithOrders)
# print(curveFactors)
# print(curveIdx)
# newPoints=[]
# hmacKeys = []

# for group in range(len(curveFactors)):
#     print(group)
#     print(curveFactors[group])

#     for factor in curveFactors[group]:
#         curCurve = curveWithOrders[group]
#         curCurveOrder = curveOrders[curveIdx[group]]
#         curFactors = curveFactors[group]
        
#         if factor != 2:

#             newPoint = findPointWithOrder(curCurve, curCurveOrder, factor)
#             newPoints.append(newPoint)
#             print(newPoint)

#             secret_point = func(newPoint.x, newPoint.y, curCurve, factor)
#             print(secret_point)
#             hmacKeys.append(secret_point)
#             print()

# print(newPoints)
# print(hmacKeys)