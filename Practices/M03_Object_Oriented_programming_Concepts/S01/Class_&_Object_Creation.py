class Example:
    x=100
    def display(self):
        print("This is Example class display method")
obj=Example()
print(obj.x)
obj.display()


class Circle:
    pi=3.14
    r=5
    def display(self):
        area=Circle.pi*self.r*self.r
        print("Area of Circle is:",area)
        perimeter=2*Circle.pi*self.r
        print("Perimeter of Circle is:",perimeter)
obj=Circle()
obj.display()