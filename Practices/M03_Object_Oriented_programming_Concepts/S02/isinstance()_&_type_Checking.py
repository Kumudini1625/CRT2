'''Type checking is a way to determine the type of an object in Python. It allows you to check if an object is an instance of a specific class or a subclass thereof. This can be useful for ensuring that your code behaves as expected when working with different types of objects.'''
a=10
b=5.6
c="Kumudini"
d=[1,2,3,4]
e=(1,2,3,4)
f={1,2,3,4}
g={"name":"Kumudini"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


'''
isinstance():to check the value/object is belongs to particular class or datatype
syntax:
isinstance(obj, type)
'''
a=10
b=5.6
c="Kumudini"
d=[1,2,3,4]
e=(1,2,3,4)
f={1,2,3,4}
g={"name":"Kumudini"}
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))
print(isinstance(e, tuple))
print(isinstance(f, set))
print(isinstance(g, dict))


#checking multiple values:
x="ram"
if isinstance(x, (int,float)):
    print("Given x is int or float")
else:
    print("Given x is a String")


#checking with classes:
class Animal:
    pass
class Dog(Animal):
    pass
class Cat:
    pass
d=Dog()
c=Cat()
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(c, Dog))



#Ducking typing: Duck typing is a programming concept that allows you to use an object based on its behavior rather than its specific type. In Python, this means that if an object behaves like a certain type (i.e., it has the necessary methods and attributes), it can be used as if it were of that type, regardless of its actual class.
class Dog:
    def sound(self):
        print("Bow-Bow")
class Cat:
    def sound(self):
        print("Meow-Meow")
def make_sound(animal):
    animal.sound()
d=Dog()
c=Cat()
make_sound(d)
make_sound(c)

def process(data):
    if isinstance(data, int):
        return data*2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, float):
        return data * 10.5
print(process(10))
print(process("kumudini"))
print(process(5.6))



#interviemw questions:
class A:
    pass
class B:
    pass
obj=B()
print(type(obj)==B)
print(type(obj)==A)
print(isinstance(obj,B))
print(isinstance(obj,A))