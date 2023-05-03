import math

#parent class
class shapes:                                                                                                      
    def __init__(self,sides):                                                                        
        self.sides=sides                                                                             
    def setSides(self):                                                                                                                               
        self.sides=int(input("Enter no. of sides:\n"))                                            
    def printSides(self):
        print("No. of sides = ", self.sides)

#child-1
class circle(shapes):
    def __init__(self,radius):
        self.r=radius
    def printPerimeter(self):
        print("Perimeter = ",round(2*math.pi*self.r))
    def printArea(self):
        print("Area = ",round(math.pi*self.r*self.r))
    
    

#child-2
class square(shapes):
    def __init__(self, length):
        self.length=length
    def printPerimeter(self):
        print("Perimeter = ",4*self.length)
    def printArea(self):
        print("Area = ",round(self.length*self.length))
    def getLength(self):
        return self.length

#child-3
class triangle(shapes):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def setSides(self):
        self.sides=3
    def setLength(self):
        self.a=int(input())
        self.b=int(input())
        self.c=int(input())
    def getLength(self):
        return self.a,self.b,self.c 
    def printPerimeter(self):
        print("Perimeter = ",self.a+self.b+self.c)

#child-4
class equilateralTriangle(triangle):
    def __init__(self,a):
        self.a=a
    def setLength(self):
        self.a=int(input())
    def printPerimeter(self):
        print("Perimeter = ",self.a*3)
    def getLength(self):
        return self.a,self.a,self.a
        
        
obj1 = square(5)

#here set side and print_side are present in parent class but child can access them.
obj1.setSides()
obj1.printSides()

#these two function present in square class.
obj1.printPerimeter()
print(obj1.getLength())