class Square:
    def __init__(self,side):
        self.l = side
    def area(self):
        print("\nArea is:",self.l * self.l)
    
    def perimeter(self):
        print("Perimeter is:",4 * (self.l))
    
    def setDimensions(self):
        self.l = int(input("\nEnter New Side:\n"))

    def getDimensions(self):
        print("length:",self.l)
        
r1=Square(5)

r1.perimeter()
r1.area()

r1.getDimensions()

r1.setDimensions()

r1.perimeter()
r1.area()

r1.getDimensions()