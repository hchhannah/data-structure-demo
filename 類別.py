class Complex:
    i=21
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        print(123)
    
    def __del__(self):
        print("delete object")
    #def aa(self):
    #    print("aa")
       
x = Complex(3.0, -4.5)
#print(Complex.i)
#print(x.r, x.i)
x = None

