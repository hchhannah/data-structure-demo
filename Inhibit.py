class RealNum:
    def __init__(self, r):
        self.__r = r
    def getReal(self):
        return self.__r
    def setReal (self, r):
        self.__r = r

class ImagNum:
    def __init__(self, i):
        self.__i = i
    def getImag(self):
        return self.__i
    def setImag (self, i):
        self.__i = i
        
class Complex(RealNum, ImagNum):
    i=21
    def __init__(self, realpart, imagpart):       
        super().__init__(realpart)
        self.setImag(imagpart)
    def __del__(self):
        print("delete object")

x = Complex(3.0, -4.5)
print(Complex.i)
print(x.getReal(), x.getImag())
x = None