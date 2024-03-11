from point_class import regularPoint, ellipticCurve, calculate_hmac
import requests
from bs4 import BeautifulSoup
import re

# Public Key 
# x = 16349894185180983439102154383611486412
# y = 224942997200586455214256137069604954919
curve = ellipticCurve(-95051, 11279326, 233970423115425145524320034830162017933)
basePoint = regularPoint(curve, 182, 85518893674295321206118380980485522083)
basePointOrder = 29246302889428143187362802287225875743

def func(x, y, curve, order):
    
    session = requests.Session()

    usersPage = session.get('http://localhost:8080/users')
    soup = BeautifulSoup(usersPage.text, 'html.parser')
    soupLst = soup.findAll('td')
    # print(soupLst)

    publicKey = regularPoint(curve, x, y)

    pattern = r'\((.*?)\)'
    adminKey = re.search(pattern, str(soupLst[1])).group(0)
    userKey = re.search(pattern, str(soupLst[3])).group(0)

    # print(adminKey)
    # print(userKey) 

    sumbitURL = "http://localhost:8080/submit"
    sumbitPayload = {"recipient" : "Admin", "message" : "test", "hmac": "test", "pkey_x" : x, "pkey_y" : y}
    submitPage = session.post(sumbitURL, data=sumbitPayload)

    soup = BeautifulSoup(submitPage.text, 'html.parser')
    strHMAC = soup.findAll("font")
    # print(strHMAC)

    pattern = r'>(.*?)<'
    stringValue = re.search(pattern, str(strHMAC[0])).group(0)[2:-2]
    hmacValue = re.search(pattern, str(strHMAC[1])).group(0)[8:-2]

    # print(stringValue)
    # print(hmacValue)

    newHMAC = calculate_hmac(stringValue, publicKey)


    for i in range(1, order + 1):
        # print()
        newHMAC = calculate_hmac(stringValue, publicKey * i)
        # print(newHMAC.hexdigest())
        if newHMAC.hexdigest() == hmacValue:
            # print(newHMAC.hexdigest())
            # print(i)
            return i

def main():
    # Public Key 
    x = 16349894185180983439102154383611486412
    y = 224942997200586455214256137069604954919

    curve = ellipticCurve(-95051, 11279326, 233970423115425145524320034830162017933)
    basePoint = regularPoint(curve, 182, 85518893674295321206118380980485522083)
    basePointOrder = 29246302889428143187362802287225875743
    order = 8 

    print(func(x, y, curve, order))

if __name__ == "__main__":
    main()