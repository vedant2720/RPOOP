class animal:
    def speaks(self):
        print("...")
    
#child-1
class Dog(animal):

    def eats(self):
        print("Eats Non-veg")

    def speaks(self):
        print("Barks")

#child-2
class Panda(animal):

    def eats(self):
        print("Eats Bamboo")

    def speaks(self):
        print("squeak")

#created a list with objects
animals=[Dog(),Panda()]


for animal in animals:
    animal.speaks()