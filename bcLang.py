DOC = '''BC-LANG ek bhenchod gandu bhasha hay isko hena python
me banaya hay matlab ek funny emvironment hay
'''
CREATOR_PROFILE = {
    "name": "Mayur Solanki",
    "age": 15,
    "language": "python, javascript, c, java"
}
INITIALIZED = False
INITIALIZE_ERROR = ">>>Gandu tune laude ko intialize hi nhi kiya"
INT_IN_ERROR = ">>>O Chutiya Hay kya Gandu Number Lene ko Bola hay na"
FLOAT_IN_ERROR = ">>>Teri Maa ki C*** Float Lene ko Bola hay na Gandu"

class lauda():
    def __init__(self):
        pass

    def chaluHoBhenchod():
        global INITIALIZED
        INITIALIZED = True


class bhenchod():
    def __init__(self):
        pass
    
    def bolBhadve(text):
        global INITIALIZED
        if (INITIALIZED == True):
            print(text)
        else:
            raise Exception(INITIALIZE_ERROR)
        
    def lineSunBhadve(text):
        global INITIALIZED
        if (INITIALIZED == True):
            a = str(input(text))
            return a
        else:
            raise Exception(INITIALIZE_ERROR)
        
    def numberSunBhadve(text):
        global INITIALIZED
        if (INITIALIZED == True):
            try:
                a = int(input(text))
                return a
            except Exception:
                raise Exception(INT_IN_ERROR)
        else:
            raise Exception(INITIALIZE_ERROR)
        
    def decimalSunBhadve(text):
        global INITIALIZED
        if (INITIALIZED == True):
            try:
                a = float(input(text))
                return a
            except Exception:
                raise Exception(FLOAT_IN_ERROR)
        else:
            raise Exception(INITIALIZE_ERROR)
        
    def malikKaNaamBataBhadve():
        print(CREATOR_PROFILE)

    def apneBareMeBataBhadve():
        print(DOC)

    def addKarBhadve(a):
        b = 0
        for i in a:
            b = b + i
        return b
    
    def minusKarBhadve(a):
        b = 0
        for i in a:
            b = i - b
        return b - (b + b)

    def multiplyKarBhadve(a):
        b = 1
        for i in a:
            b = b * i
        return b
    
    def divideKarBhadve(a, b):
        return a/b